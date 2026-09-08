"""Access-level enforcement: the gate that makes READONLY mean read-only."""

import asyncio

import httpx
import pytest

from mailchimp_mcp import generated, server
from mailchimp_mcp.access import AccessDenied, AccessLevel
from mailchimp_mcp.client import MarketingClient
from mailchimp_mcp.operations import BY_NAME, OPERATIONS


def at_level(settings, level):
    return settings.__class__(**{**settings.__dict__, "access_level": level})


def client_at(settings, level, handler=None):
    handler = handler or (lambda r: httpx.Response(200, json={"ok": True}))
    cfg = at_level(settings, level)
    return MarketingClient(
        cfg, client=httpx.Client(base_url=cfg.base_url, transport=httpx.MockTransport(handler))
    )


# --------------------------------------------------------------------------- #
# The level model
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize(
    "raw,expected",
    [
        (None, AccessLevel.READONLY),
        ("", AccessLevel.READONLY),
        ("readonly", AccessLevel.READONLY),
        ("  Basic ", AccessLevel.BASIC),
        ("ADMIN", AccessLevel.ADMIN),
    ],
)
def test_parse_is_case_and_space_insensitive(raw, expected):
    assert AccessLevel.parse(raw) is expected


def test_parse_rejects_unknown_level():
    with pytest.raises(ValueError, match="not valid"):
        AccessLevel.parse("SUPERUSER")


def test_default_is_readonly():
    assert AccessLevel.parse(None) is AccessLevel.READONLY


@pytest.mark.parametrize(
    "level,expected",
    [
        (AccessLevel.READONLY, {"GET"}),
        (AccessLevel.BASIC, {"GET", "POST"}),
        (AccessLevel.ADMIN, {"GET", "POST", "PUT", "PATCH", "DELETE"}),
    ],
)
def test_methods_per_level(level, expected):
    assert set(level.methods) == expected


def test_levels_are_ordered():
    assert AccessLevel.ADMIN.permits(AccessLevel.BASIC)
    assert AccessLevel.BASIC.permits(AccessLevel.READONLY)
    assert not AccessLevel.READONLY.permits(AccessLevel.BASIC)
    assert not AccessLevel.BASIC.permits(AccessLevel.ADMIN)


# --------------------------------------------------------------------------- #
# Gate 1: the HTTP client
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("method", ["POST", "PUT", "PATCH", "DELETE"])
def test_readonly_client_refuses_every_write_method(settings, method):
    with pytest.raises(AccessDenied, match="READONLY"):
        client_at(settings, AccessLevel.READONLY).request(method, "/lists/abc/members")


def test_readonly_client_still_allows_get(settings):
    assert client_at(settings, AccessLevel.READONLY).get("/ping") == {"ok": True}


def test_basic_allows_post_but_refuses_delete_and_patch(settings):
    client = client_at(settings, AccessLevel.BASIC)
    assert client.request("POST", "/lists/abc/members", body={"email_address": "a@e.com"}) == {"ok": True}
    for method in ("DELETE", "PATCH", "PUT"):
        with pytest.raises(AccessDenied, match="ADMIN"):
            client.request(method, "/lists/abc/members/x")


def test_admin_allows_everything(settings):
    client = client_at(settings, AccessLevel.ADMIN)
    for method in ("GET", "POST", "PUT", "PATCH", "DELETE"):
        assert client.request(method, "/lists/abc") == {"ok": True}


def test_access_denied_message_names_both_levels(settings):
    with pytest.raises(AccessDenied) as excinfo:
        client_at(settings, AccessLevel.READONLY).request("DELETE", "/lists/abc")
    message = str(excinfo.value)
    assert "ADMIN" in message and "READONLY" in message


def test_denied_request_never_reaches_the_network(settings):
    """The gate must refuse before any HTTP call is made."""
    calls = {"n": 0}

    def handler(request):
        calls["n"] += 1
        return httpx.Response(200, json={})

    with pytest.raises(AccessDenied):
        client_at(settings, AccessLevel.READONLY, handler).request("DELETE", "/lists/abc")
    assert calls["n"] == 0


def test_body_is_sent_as_json(settings):
    seen = {}

    def handler(request):
        import json

        seen.update(json.loads(request.content))
        return httpx.Response(200, json={"id": "1"})

    client_at(settings, AccessLevel.BASIC, handler).request(
        "POST", "/lists/abc/members", body={"email_address": "a@e.com", "status": "subscribed"}
    )
    assert seen["email_address"] == "a@e.com"


def test_writes_are_never_retried(settings, monkeypatch):
    """Replaying a POST could duplicate a write whose first attempt landed."""
    monkeypatch.setattr("mailchimp_mcp.client.time.sleep", lambda _: None)
    calls = {"n": 0}

    def handler(request):
        calls["n"] += 1
        return httpx.Response(429, json={"title": "Too Many Requests"})

    from mailchimp_mcp.client import MailchimpError

    with pytest.raises(MailchimpError):
        client_at(settings, AccessLevel.BASIC, handler).request("POST", "/lists/abc/members", body={})
    assert calls["n"] == 1, "a write must not be replayed"


def test_gets_are_still_retried(settings, monkeypatch):
    monkeypatch.setattr("mailchimp_mcp.client.time.sleep", lambda _: None)
    calls = {"n": 0}

    def handler(request):
        calls["n"] += 1
        if calls["n"] < 3:
            return httpx.Response(429, json={"title": "Too Many Requests"})
        return httpx.Response(200, json={"ok": True})

    assert client_at(settings, AccessLevel.READONLY, handler).get("/ping") == {"ok": True}
    assert calls["n"] == 3


# --------------------------------------------------------------------------- #
# Gate 2: registration
# --------------------------------------------------------------------------- #


class FakeServer:
    def __init__(self):
        self.tools = {}

    def add_tool(self, fn, name=None, description=None, annotations=None, **kwargs):
        self.tools[name] = (fn, annotations)


@pytest.mark.parametrize(
    "level,expected_generated",
    [(AccessLevel.READONLY, 149), (AccessLevel.BASIC, 224), (AccessLevel.ADMIN, 298)],
)
def test_registration_count_matches_access_level(settings, level, expected_generated):
    fake = FakeServer()
    summary = generated.register(fake, at_level(settings, level), lambda: None)
    assert summary["registered"] == expected_generated
    assert len(fake.tools) == expected_generated


def test_readonly_registers_no_write_tool(settings):
    fake = FakeServer()
    generated.register(fake, at_level(settings, AccessLevel.READONLY), lambda: None)
    for name in fake.tools:
        assert BY_NAME[name]["method"] == "GET", f"{name} is not a GET but was registered at READONLY"


def test_basic_registers_no_delete_or_update_tool(settings):
    fake = FakeServer()
    generated.register(fake, at_level(settings, AccessLevel.BASIC), lambda: None)
    methods = {BY_NAME[n]["method"] for n in fake.tools}
    assert methods == {"GET", "POST"}


def test_delete_tools_are_flagged_destructive(settings):
    fake = FakeServer()
    generated.register(fake, at_level(settings, AccessLevel.ADMIN), lambda: None)
    for name, (_, annotations) in fake.tools.items():
        if BY_NAME[name]["method"] == "DELETE":
            assert annotations.destructive_hint is True
            assert annotations.read_only_hint is False


def test_group_filter_narrows_registration(settings):
    cfg = settings.__class__(
        **{**settings.__dict__, "access_level": AccessLevel.ADMIN, "tool_groups": frozenset({"lists"})}
    )
    fake = FakeServer()
    summary = generated.register(fake, cfg, lambda: None)
    assert summary["skipped_by_group_filter"] > 0
    assert {BY_NAME[n]["group"] for n in fake.tools} == {"lists"}


def test_curated_names_are_reserved_against_generated(settings):
    fake = FakeServer()
    generated.register(
        fake, at_level(settings, AccessLevel.ADMIN), lambda: None, reserved={"get_lists"}
    )
    assert "get_lists" not in fake.tools


# --------------------------------------------------------------------------- #
# The operations table itself
# --------------------------------------------------------------------------- #


def test_every_operation_name_is_unique_and_importable():
    names = [op["name"] for op in OPERATIONS]
    assert len(names) == len(set(names))
    assert all(name.isidentifier() for name in names)


def test_levels_match_http_methods():
    expected = {
        "GET": "READONLY",
        "POST": "BASIC",
        "PUT": "ADMIN",
        "PATCH": "ADMIN",
        "DELETE": "ADMIN",
    }
    for op in OPERATIONS:
        assert op["level"] == expected[op["method"]], op["name"]


def test_curated_tool_names_do_not_collide_with_generated():
    assert not (server.CURATED_TOOL_NAMES & set(BY_NAME))


def test_curated_tool_names_constant_matches_the_server(monkeypatch):
    """The declared list must stay in step with the decorators above it."""
    registered = {t.name for t in asyncio.run(server.mcp.list_tools())}
    assert server.CURATED_TOOL_NAMES <= registered


# --------------------------------------------------------------------------- #
# Generated tool dispatch
# --------------------------------------------------------------------------- #


def test_generated_tool_builds_path_query_and_body(settings):
    seen = {}

    def handler(request):
        import json

        seen["method"] = request.method
        seen["path"] = request.url.path
        seen["query"] = dict(request.url.params)
        seen["body"] = json.loads(request.content) if request.content else None
        return httpx.Response(200, json={"id": "new"})

    client = client_at(settings, AccessLevel.BASIC, handler)
    fn = generated._build(BY_NAME["post_lists_id_members"], lambda: client)
    fn(list_id="abc123", body={"email_address": "a@e.com", "status": "subscribed"}, skip_merge_validation=True)

    assert seen["method"] == "POST"
    assert seen["path"] == "/3.0/lists/abc123/members"
    assert seen["query"] == {"skip_merge_validation": "true"}
    assert seen["body"]["email_address"] == "a@e.com"


def test_generated_tool_omits_unset_query_params(settings):
    seen = {}

    def handler(request):
        seen["query"] = dict(request.url.params)
        return httpx.Response(200, json={})

    client = client_at(settings, AccessLevel.READONLY, handler)
    generated._build(BY_NAME["get_lists_id_members"], lambda: client)(list_id="abc", status="subscribed")
    assert seen["query"] == {"status": "subscribed"}


def test_generated_tool_quotes_path_parameters(settings):
    """A path parameter must not be able to inject extra path segments.

    Assert on raw_path, which is what is actually sent. httpx's ``url.path`` is a
    decoded convenience view and shows the traversal as if it had survived.
    """
    seen = {}

    def handler(request):
        seen["raw_path"] = request.url.raw_path
        return httpx.Response(200, json={})

    client = client_at(settings, AccessLevel.READONLY, handler)
    generated._build(BY_NAME["get_lists_id"], lambda: client)(list_id="../../ping")
    assert seen["raw_path"] == b"/3.0/lists/..%2F..%2Fping"


def test_generated_tool_rejects_blank_path_parameter(settings):
    fn = generated._build(BY_NAME["get_lists_id"], lambda: client_at(settings, AccessLevel.READONLY))
    with pytest.raises(ValueError, match="required"):
        fn(list_id="  ")


def test_generated_write_tool_is_still_refused_by_the_client(settings):
    """Gate 2 holds even if a write tool is somehow invoked at READONLY."""
    client = client_at(settings, AccessLevel.READONLY)
    fn = generated._build(BY_NAME["delete_lists_id"], lambda: client)
    with pytest.raises(AccessDenied):
        fn(list_id="abc")

"""End-to-end tool tests against a mocked Mailchimp API."""

import httpx
import pytest
from mcp.server.mcpserver.exceptions import ToolError

from mailchimp_mcp import server
from mailchimp_mcp.client import MarketingClient

LIST_ID = "abc123def4"

MEMBERS = [
    # Existed since 2024, only opted in during the window -> upgrade, high confidence.
    {
        "email_address": "upgraded@example.com",
        "status": "subscribed",
        "timestamp_signup": "2024-03-02T08:00:00+00:00",
        "timestamp_opt": "2026-08-14T11:30:00+00:00",
        "last_changed": "2026-08-14T11:30:00+00:00",
        "source": "API - Generic",
        "tags": [{"id": 1, "name": "Ecomm"}],
        "merge_fields": {"FNAME": "Dana", "LNAME": "Reyes"},
        "contact_id": "c1",
    },
    # No signup stamp at all -> upgrade, medium confidence.
    {
        "email_address": "imported@example.com",
        "status": "subscribed",
        "timestamp_signup": "",
        "timestamp_opt": "2026-08-20T09:00:00+00:00",
        "last_changed": "2026-08-20T09:00:00+00:00",
        "tags": [],
        "merge_fields": {},
        "contact_id": "c2",
    },
    # Signed up and opted in inside the window -> new subscriber.
    {
        "email_address": "brandnew@example.com",
        "status": "subscribed",
        "timestamp_signup": "2026-08-05T12:00:00+00:00",
        "timestamp_opt": "2026-08-05T12:01:00+00:00",
        "last_changed": "2026-08-05T12:01:00+00:00",
        "tags": [],
        "merge_fields": {},
        "contact_id": "c3",
    },
    # Long-standing subscriber whose record was merely touched -> other change.
    {
        "email_address": "tagged@example.com",
        "status": "subscribed",
        "timestamp_signup": "2021-01-01T00:00:00+00:00",
        "timestamp_opt": "2021-01-01T00:00:00+00:00",
        "last_changed": "2026-08-22T15:00:00+00:00",
        "tags": [{"id": 2, "name": "Blog"}],
        "merge_fields": {},
        "contact_id": "c4",
    },
]


@pytest.fixture(autouse=True)
def wired(settings, monkeypatch):
    """Point the server's module-level singletons at a mocked API."""

    def handler(request: httpx.Request) -> httpx.Response:
        path = request.url.path
        params = request.url.params
        if path == "/3.0/ping":
            return httpx.Response(200, json={"health_status": "Everything's Chimpy!"})
        if path == "/3.0/lists":
            return httpx.Response(
                200,
                json={
                    "total_items": 1,
                    "lists": [
                        {
                            "id": LIST_ID,
                            "name": "Main Audience",
                            "date_created": "2019-04-01T00:00:00+00:00",
                            "stats": {"member_count": 4, "unsubscribe_count": 1},
                        }
                    ],
                },
            )
        if path == f"/3.0/lists/{LIST_ID}/members":
            offset = int(params.get("offset", 0))
            count = int(params.get("count", 10))
            rows = MEMBERS
            if params.get("status"):
                rows = [m for m in rows if m["status"] == params["status"]]
            page = rows[offset : offset + count]
            return httpx.Response(200, json={"members": page, "total_items": len(rows)})
        if path == f"/3.0/lists/{LIST_ID}/growth-history":
            return httpx.Response(
                200,
                json={
                    "total_items": 1,
                    "history": [{"month": "2026-08", "subscribed": 4, "transactional": 2}],
                },
            )
        raise AssertionError(f"unexpected request: {path}")

    client = MarketingClient(
        settings,
        client=httpx.Client(base_url=settings.base_url, transport=httpx.MockTransport(handler)),
    )
    monkeypatch.setattr(server, "_settings", settings)
    monkeypatch.setattr(server, "_marketing", client)
    monkeypatch.setattr(server, "_transactional", None)
    return client


def test_ping_reports_datacenter():
    assert server.ping() == {"ok": True, "health_status": "Everything's Chimpy!", "datacenter": "us13"}


def test_list_audiences_flattens_response():
    result = server.list_audiences()
    assert result["audiences"][0]["list_id"] == LIST_ID
    assert result["audiences"][0]["stats"]["member_count"] == 4


def test_missing_list_id_raises_a_helpful_error():
    """Anticipated failures reach the MCP client as readable ToolErrors, not crashes."""
    with pytest.raises(ToolError, match="list_audiences"):
        server.get_audience()


def test_list_members_summarises_and_labels_status():
    result = server.list_members(list_id=LIST_ID, status="subscribed")
    assert result["returned"] == 4
    first = result["members"][0]
    assert first["email"] == "upgraded@example.com"
    assert first["status_label"] == "Subscribed"
    assert first["name"] == "Dana Reyes"
    assert first["tags"] == ["Ecomm"]


def test_list_members_rejects_unknown_status():
    with pytest.raises(ToolError, match="status must be one of"):
        server.list_members(list_id=LIST_ID, status="non-subscribed")


def test_list_members_rejects_bad_date():
    with pytest.raises(ToolError, match="valid date"):
        server.list_members(list_id=LIST_ID, since_last_changed="yesterday")


def test_find_newly_subscribed_separates_upgrades_from_new_signups():
    result = server.find_newly_subscribed(since="2026-08-01", before="2026-09-01", list_id=LIST_ID)

    assert result["counts_by_verdict"] == {
        "upgraded_to_subscribed": 2,
        "new_subscriber": 1,
        "other_change": 1,
    }
    assert result["matched"] == 2
    emails = {c["email"] for c in result["contacts"]}
    assert emails == {"upgraded@example.com", "imported@example.com"}

    by_email = {c["email"]: c for c in result["contacts"]}
    assert by_email["upgraded@example.com"]["confidence"] == "high"
    assert by_email["imported@example.com"]["confidence"] == "medium"
    assert "no status-transition history" in result["method"] or "status-transition history" in result["method"]


def test_find_newly_subscribed_all_verdicts():
    result = server.find_newly_subscribed(since="2026-08-01", list_id=LIST_ID, verdict="all")
    assert result["matched"] == 4


def test_find_newly_subscribed_validates_window():
    with pytest.raises(ToolError, match="before must be later"):
        server.find_newly_subscribed(since="2026-09-01", before="2026-08-01", list_id=LIST_ID)
    with pytest.raises(ToolError, match="verdict must be one of"):
        server.find_newly_subscribed(since="2026-08-01", list_id=LIST_ID, verdict="nope")


def test_snapshot_then_diff_reports_exact_transitions(settings, monkeypatch):
    first = server.snapshot_member_statuses(list_id=LIST_ID, name="before")
    assert first["member_count"] == 4
    assert first["truncated"] is False

    # Simulate one contact moving Non-subscribed -> Subscribed between snapshots.
    from mailchimp_mcp import analysis

    changed = [dict(m) for m in MEMBERS]
    changed[0]["status"] = "transactional"
    analysis.snapshot_members(settings.snapshot_dir, LIST_ID, changed, name="earlier")

    result = server.diff_member_status_snapshots(
        from_snapshot="earlier", to_snapshot="before", list_id=LIST_ID
    )
    assert result["transition_count"] == 1
    row = result["transitions"][0]
    assert row["email"] == "upgraded@example.com"
    assert row["from_status_label"] == "Non-subscribed"
    assert row["to_status_label"] == "Subscribed"


def test_list_status_snapshots_after_snapshot():
    server.snapshot_member_statuses(list_id=LIST_ID, name="snap1")
    listed = server.list_status_snapshots(list_id=LIST_ID)
    assert [s["snapshot"] for s in listed["snapshots"]] == ["snap1"]


def test_growth_history_passthrough():
    assert server.get_audience_growth_history(list_id=LIST_ID)["history"][0]["transactional"] == 2


def test_transactional_tools_disabled_without_key():
    with pytest.raises(ToolError, match="MAILCHIMP_TRANSACTIONAL_API_KEY"):
        server.transactional_account_info()


def test_mailchimp_api_errors_reach_the_client_with_detail(settings, monkeypatch):
    """A 401 must surface Mailchimp's own message, with the key stripped out."""

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            401,
            json={"title": "API Key Invalid", "detail": f"Your API key {settings.api_key} may be invalid"},
        )

    monkeypatch.setattr(
        server,
        "_marketing",
        MarketingClient(
            settings,
            client=httpx.Client(base_url=settings.base_url, transport=httpx.MockTransport(handler)),
        ),
    )
    with pytest.raises(ToolError) as excinfo:
        server.ping()
    message = str(excinfo.value)
    assert "API Key Invalid" in message
    assert settings.api_key not in message


def test_tool_signatures_survive_the_handled_decorator():
    """functools.wraps must keep the schema the MCP SDK derives from the signature."""
    import inspect

    params = inspect.signature(server.find_newly_subscribed).parameters
    assert "since" in params and "verdict" in params

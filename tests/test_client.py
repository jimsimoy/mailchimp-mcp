import httpx
import pytest

from mailchimp_mcp.client import (
    TRANSACTIONAL_ALLOWLIST,
    MailchimpError,
    MarketingClient,
    TransactionalClient,
    _clean_params,
    subscriber_hash,
)


def make_client(settings, handler) -> MarketingClient:
    transport = httpx.MockTransport(handler)
    http = httpx.Client(
        base_url=settings.base_url, transport=transport, auth=("mailchimp-mcp", settings.api_key)
    )
    return MarketingClient(settings, client=http)


def test_subscriber_hash_lowercases_email():
    # Mailchimp's documented example hash for the lowercase address.
    assert subscriber_hash("Person@Example.com") == subscriber_hash("person@example.com")
    assert len(subscriber_hash("person@example.com")) == 32


def test_subscriber_hash_passes_through_non_emails():
    assert subscriber_hash("abc123hash") == "abc123hash"


def test_clean_params_drops_empty_and_flattens_lists():
    assert _clean_params({"a": None, "b": "", "c": ["x", "y"], "d": True, "e": False, "f": 3}) == {
        "c": "x,y",
        "d": "true",
        "e": "false",
        "f": 3,
    }


def test_marketing_client_has_no_write_methods(settings):
    """The read-only guarantee: there is nothing to call that mutates data."""
    for verb in ("post", "put", "patch", "delete"):
        assert not hasattr(MarketingClient, verb)


def test_get_returns_json(settings):
    def handler(request):
        assert request.url.path == "/3.0/ping"
        return httpx.Response(200, json={"health_status": "Everything's Chimpy!"})

    assert make_client(settings, handler).get("/ping")["health_status"] == "Everything's Chimpy!"


def test_get_rejects_unsafe_path(settings):
    client = make_client(settings, lambda r: httpx.Response(200, json={}))
    with pytest.raises(ValueError, match="unsafe path"):
        client.get("//evil.example.com/steal")
    with pytest.raises(ValueError, match="unsafe path"):
        client.get("https://evil.example.com/steal")


def test_error_body_is_surfaced(settings):
    def handler(request):
        return httpx.Response(
            404, json={"title": "Resource Not Found", "detail": "The requested resource could not be found."}
        )

    with pytest.raises(MailchimpError) as excinfo:
        make_client(settings, handler).get("/lists/nope")
    assert excinfo.value.status == 404
    assert "Resource Not Found" in str(excinfo.value)


def test_api_key_is_redacted_from_errors(settings):
    def handler(request):
        return httpx.Response(401, json={"title": "API Key Invalid", "detail": f"Key {settings.api_key} rejected"})

    with pytest.raises(MailchimpError) as excinfo:
        make_client(settings, handler).get("/ping")
    assert settings.api_key not in str(excinfo.value)
    assert "REDACTED" in str(excinfo.value)


def test_retries_on_429_then_succeeds(settings, monkeypatch):
    monkeypatch.setattr("mailchimp_mcp.client.time.sleep", lambda _: None)
    calls = {"n": 0}

    def handler(request):
        calls["n"] += 1
        if calls["n"] == 1:
            return httpx.Response(429, headers={"Retry-After": "1"}, json={"title": "Too Many Requests"})
        return httpx.Response(200, json={"ok": True})

    assert make_client(settings, handler).get("/ping") == {"ok": True}
    assert calls["n"] == 2


def test_does_not_retry_on_401(settings, monkeypatch):
    monkeypatch.setattr("mailchimp_mcp.client.time.sleep", lambda _: None)
    calls = {"n": 0}

    def handler(request):
        calls["n"] += 1
        return httpx.Response(401, json={"title": "API Key Invalid"})

    with pytest.raises(MailchimpError):
        make_client(settings, handler).get("/ping")
    assert calls["n"] == 1


def test_paginate_walks_all_pages(settings):
    total = 2500

    def handler(request):
        offset = int(request.url.params.get("offset", 0))
        count = int(request.url.params.get("count", 10))
        members = [{"email_address": f"user{i}@example.com"} for i in range(offset, min(offset + count, total))]
        return httpx.Response(200, json={"members": members, "total_items": total})

    settings_big = settings.__class__(**{**settings.__dict__, "max_records": 5000})
    items, reported, truncated = make_client(settings_big, handler).paginate(
        "/lists/abc/members", item_key="members"
    )
    assert reported == total
    assert len(items) == total
    assert truncated is False


def test_paginate_respects_max_records(settings):
    def handler(request):
        offset = int(request.url.params.get("offset", 0))
        count = int(request.url.params.get("count", 10))
        members = [{"email_address": f"u{i}@example.com"} for i in range(offset, offset + count)]
        return httpx.Response(200, json={"members": members, "total_items": 9999})

    items, reported, truncated = make_client(settings, handler).paginate(
        "/lists/abc/members", item_key="members", max_records=30
    )
    assert len(items) == 30
    assert reported == 9999
    assert truncated is True


def test_paginate_is_capped_by_settings_max_records(settings):
    """max_records=100 in settings must override a larger per-call request."""

    def handler(request):
        offset = int(request.url.params.get("offset", 0))
        count = int(request.url.params.get("count", 10))
        return httpx.Response(
            200,
            json={
                "members": [{"email_address": f"u{i}@e.com"} for i in range(offset, offset + count)],
                "total_items": 9999,
            },
        )

    items, _, _ = make_client(settings, handler).paginate(
        "/lists/abc/members", item_key="members", max_records=10_000
    )
    assert len(items) == settings.max_records


def test_transactional_requires_key(settings):
    with pytest.raises(ValueError, match="MAILCHIMP_TRANSACTIONAL_API_KEY"):
        TransactionalClient(settings)


def test_transactional_allowlist_blocks_sending(settings):
    enabled = settings.__class__(**{**settings.__dict__, "transactional_api_key": "mkey"})
    http = httpx.Client(
        base_url=TransactionalClient.BASE_URL,
        transport=httpx.MockTransport(lambda r: httpx.Response(200, json={})),
    )
    client = TransactionalClient(enabled, client=http)
    with pytest.raises(ValueError, match="allowlist"):
        client.call("/messages/send.json", {"message": {}})
    assert "/messages/send.json" not in TRANSACTIONAL_ALLOWLIST


def test_transactional_injects_key_into_body(settings):
    enabled = settings.__class__(**{**settings.__dict__, "transactional_api_key": "mkey"})
    seen = {}

    def handler(request):
        import json

        seen.update(json.loads(request.content))
        return httpx.Response(200, json={"username": "acct"})

    http = httpx.Client(base_url=TransactionalClient.BASE_URL, transport=httpx.MockTransport(handler))
    TransactionalClient(enabled, client=http).call("/users/info.json")
    assert seen["key"] == "mkey"

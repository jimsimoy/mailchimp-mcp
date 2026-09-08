"""MCP server exposing read-only Mailchimp tools over stdio."""

from __future__ import annotations

import functools
import sys
from typing import Any, Callable, Mapping, Sequence, TypeVar

from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.exceptions import ToolError
from mcp.types import ToolAnnotations

from . import __version__, analysis, generated
from .access import AccessDenied, AccessLevel, DESCRIPTIONS
from .client import MailchimpError, MarketingClient, TransactionalClient, subscriber_hash
from .config import ConfigError, Settings, load_settings

_F = TypeVar("_F", bound=Callable[..., Any])


def handled(func: _F) -> _F:
    """Turn anticipated failures into messages the MCP client can actually read.

    Without this the SDK reports any exception as an opaque "Error executing tool",
    which hides the one thing a caller needs — a bad key, a missing audience, an
    unparseable date, or Mailchimp's own error text.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except (MailchimpError, AccessDenied) as exc:
            raise ToolError(str(exc)) from exc
        except (ConfigError, analysis.AnalysisError, ValueError) as exc:
            raise ToolError(settings_safe_message(exc)) from exc

    return wrapper  # type: ignore[return-value]


def settings_safe_message(exc: Exception) -> str:
    """Render an exception, with any credential stripped out."""
    text = str(exc)
    try:
        return settings().redact(text)
    except ConfigError:
        return text

mcp = MCPServer(
    "mailchimp",
    version=__version__,
    instructions=(
        "Read-only access to a Mailchimp account: audiences, contacts, segments, "
        "campaigns and reports. Call list_audiences first to get an audience list_id. "
        "Note that Mailchimp's API status 'transactional' is what the web UI labels "
        "'Non-subscribed'. Mailchimp stores no subscribe-status history, so use "
        "find_newly_subscribed to infer past status changes from opt-in timestamps, "
        "and snapshot_member_statuses + diff_member_status_snapshots to track them "
        "exactly from now on. Alongside these curated tools, one tool is exposed per "
        "Mailchimp API operation, named after its operationId (for example "
        "get_lists_id_members). Which of those exist depends on MAILCHIMP_ACCESS_LEVEL: "
        "READONLY registers only GET operations, BASIC adds POST, ADMIN adds "
        "PUT/PATCH/DELETE. Tools above the configured level are not registered at all, "
        "so if you cannot see a write tool, the operator has not granted that access — "
        "say so rather than looking for a workaround."
    ),
)

#: Every Mailchimp-facing tool here only reads. snapshot_member_statuses is the one
#: exception: it reads from Mailchimp but writes a snapshot file to local disk.
READ_ONLY = ToolAnnotations(
    read_only_hint=True, destructive_hint=False, idempotent_hint=True, open_world_hint=True
)
LOCAL_WRITE = ToolAnnotations(
    read_only_hint=False, destructive_hint=False, idempotent_hint=False, open_world_hint=True
)

_settings: Settings | None = None
_marketing: MarketingClient | None = None
_transactional: TransactionalClient | None = None


def settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = load_settings()
    return _settings


def marketing() -> MarketingClient:
    global _marketing
    if _marketing is None:
        _marketing = MarketingClient(settings())
    return _marketing


def transactional() -> TransactionalClient:
    global _transactional
    if _transactional is None:
        _transactional = TransactionalClient(settings())
    return _transactional


def _resolve_list_id(list_id: str | None) -> str:
    resolved = (list_id or "").strip() or (settings().default_list_id or "")
    if not resolved:
        raise ValueError(
            "No audience specified. Pass list_id, or set MAILCHIMP_DEFAULT_LIST_ID in .env. "
            "Use list_audiences to see the IDs available on this account."
        )
    return resolved


#: Fields worth returning for a member when the caller does not ask for everything.
_MEMBER_FIELDS = (
    "email_address,status,timestamp_opt,timestamp_signup,last_changed,source,"
    "tags,contact_id,id,merge_fields,member_rating,unsubscribe_reason"
)


def _member_summary(member: Mapping[str, Any]) -> dict[str, Any]:
    status = str(member.get("status", "") or "")
    return {
        "email": member.get("email_address"),
        "status": status,
        "status_label": analysis.STATUS_LABELS.get(status, status),
        "name": " ".join(
            part
            for part in (
                (member.get("merge_fields") or {}).get("FNAME"),
                (member.get("merge_fields") or {}).get("LNAME"),
            )
            if part
        )
        or None,
        "timestamp_opt": member.get("timestamp_opt") or None,
        "timestamp_signup": member.get("timestamp_signup") or None,
        "last_changed": member.get("last_changed") or None,
        "source": member.get("source") or None,
        "rating": member.get("member_rating"),
        "tags": [t.get("name") for t in member.get("tags") or [] if isinstance(t, Mapping)],
        "contact_id": member.get("contact_id") or member.get("id"),
    }


# =========================================================================== #
# Account
# =========================================================================== #


@mcp.tool(annotations=READ_ONLY)
@handled
def ping() -> dict[str, Any]:
    """Check that the configured Mailchimp credentials work and the API is reachable."""
    result = marketing().get("/ping")
    return {"ok": True, "health_status": result.get("health_status"), "datacenter": settings().datacenter}


@mcp.tool(annotations=READ_ONLY)
@handled
def get_account() -> dict[str, Any]:
    """Get details about the Mailchimp account this key belongs to: name, plan, contact, totals."""
    data = marketing().get(
        "/",
        {"fields": "account_id,account_name,email,first_name,last_name,username,"
                   "pricing_plan_type,total_subscribers,industry_stats,contact,member_since"},
    )
    return data


# =========================================================================== #
# Audiences (lists)
# =========================================================================== #


@mcp.tool(annotations=READ_ONLY)
@handled
def list_audiences(count: int = 25) -> dict[str, Any]:
    """List the audiences (lists) on this account with their IDs and member statistics.

    Start here — every member tool needs an audience `list_id`.
    """
    data = marketing().get(
        "/lists",
        {"count": min(max(count, 1), 1000), "fields": "lists.id,lists.name,lists.date_created,"
         "lists.stats.member_count,lists.stats.unsubscribe_count,lists.stats.cleaned_count,"
         "lists.stats.total_contacts,total_items"},
    )
    return {
        "total_items": data.get("total_items"),
        "audiences": [
            {
                "list_id": item.get("id"),
                "name": item.get("name"),
                "created": item.get("date_created"),
                "stats": item.get("stats", {}),
            }
            for item in data.get("lists", [])
        ],
    }


@mcp.tool(annotations=READ_ONLY)
@handled
def get_audience(list_id: str | None = None) -> dict[str, Any]:
    """Get one audience's settings and full statistics."""
    return marketing().get(f"/lists/{_resolve_list_id(list_id)}")


@mcp.tool(annotations=READ_ONLY)
@handled
def get_audience_growth_history(list_id: str | None = None, months: int = 12) -> dict[str, Any]:
    """Get month-by-month audience growth: subscribed, unsubscribed, cleaned, transactional, imports.

    Useful as a cross-check on status-change analysis — the `transactional` and
    `subscribed` columns show whether a shift you found is visible in aggregate.
    """
    data = marketing().get(
        f"/lists/{_resolve_list_id(list_id)}/growth-history",
        {"count": min(max(months, 1), 1000), "sort_field": "month", "sort_dir": "DESC"},
    )
    return {"total_items": data.get("total_items"), "history": data.get("history", [])}


@mcp.tool(annotations=READ_ONLY)
@handled
def get_audience_activity(list_id: str | None = None, days: int = 30) -> dict[str, Any]:
    """Get recent daily audience activity: sends, opens, clicks, bounces, subs and unsubs per day."""
    data = marketing().get(
        f"/lists/{_resolve_list_id(list_id)}/activity",
        {"count": min(max(days, 1), 1000)},
    )
    return {"total_items": data.get("total_items"), "activity": data.get("activity", [])}


# =========================================================================== #
# Members
# =========================================================================== #


@mcp.tool(annotations=READ_ONLY)
@handled
def list_members(
    list_id: str | None = None,
    status: str | None = None,
    since_last_changed: str | None = None,
    before_last_changed: str | None = None,
    since_timestamp_opt: str | None = None,
    before_timestamp_opt: str | None = None,
    unsubscribed_since: str | None = None,
    vip_only: bool = False,
    sort_field: str | None = None,
    sort_dir: str = "DESC",
    max_records: int = 200,
    full: bool = False,
) -> dict[str, Any]:
    """List members of an audience, with Mailchimp's server-side filters.

    `status` is one of: subscribed, unsubscribed, cleaned, pending, transactional,
    archived. Note that **`transactional` is what the Mailchimp UI calls
    "Non-subscribed"**.

    Date arguments take `YYYY-MM-DD` or a full ISO 8601 timestamp.
    `since_timestamp_opt` filters on when the contact opted in; `since_last_changed`
    filters on when their record last changed at all.

    `sort_field` is one of: timestamp_opt, timestamp_signup, last_changed.
    """
    valid_status = set(analysis.STATUS_LABELS)
    if status and status not in valid_status:
        raise ValueError(f"status must be one of {sorted(valid_status)}, got {status!r}")
    if sort_field and sort_field not in {"timestamp_opt", "timestamp_signup", "last_changed"}:
        raise ValueError("sort_field must be timestamp_opt, timestamp_signup or last_changed")

    params: dict[str, Any] = {
        "status": status,
        "since_last_changed": analysis.to_iso(analysis.coerce_window(since_last_changed, name="since_last_changed")),
        "before_last_changed": analysis.to_iso(analysis.coerce_window(before_last_changed, name="before_last_changed")),
        "since_timestamp_opt": analysis.to_iso(analysis.coerce_window(since_timestamp_opt, name="since_timestamp_opt")),
        "before_timestamp_opt": analysis.to_iso(analysis.coerce_window(before_timestamp_opt, name="before_timestamp_opt")),
        "unsubscribed_since": analysis.to_iso(analysis.coerce_window(unsubscribed_since, name="unsubscribed_since")),
        "sort_field": sort_field,
        "sort_dir": sort_dir if sort_field else None,
    }
    if vip_only:
        params["vip_only"] = True
    if not full:
        params["fields"] = f"total_items,members.{',members.'.join(_MEMBER_FIELDS.split(','))}"

    members, total, truncated = marketing().paginate(
        f"/lists/{_resolve_list_id(list_id)}/members",
        item_key="members",
        params=params,
        max_records=max_records,
    )
    return {
        "total_items": total,
        "returned": len(members),
        "truncated": truncated,
        "members": members if full else [_member_summary(m) for m in members],
    }


@mcp.tool(annotations=READ_ONLY)
@handled
def get_member(email: str, list_id: str | None = None) -> dict[str, Any]:
    """Get one member's full record by email address (or by subscriber hash / contact ID)."""
    return marketing().get(
        f"/lists/{_resolve_list_id(list_id)}/members/{subscriber_hash(email)}"
    )


@mcp.tool(annotations=READ_ONLY)
@handled
def get_member_activity(
    email: str,
    list_id: str | None = None,
    activity_filters: str | None = None,
    count: int = 50,
) -> dict[str, Any]:
    """Get a member's activity feed: signups, opens, clicks, unsubs, orders, notes and events.

    `activity_filters` is a comma-separated subset of: bounce, click, conversation,
    ecommerce_signup, event, generic_signup, landing_page_signup, marketing_permission,
    note, open, order, sent, signup, squatter_signup, survey_response, unsub,
    website_signup. The signup types are the best evidence of *how* a contact
    became subscribed.
    """
    params: dict[str, Any] = {"count": min(max(count, 1), 1000)}
    if activity_filters:
        params["activity_filters"] = activity_filters
    data = marketing().get(
        f"/lists/{_resolve_list_id(list_id)}/members/{subscriber_hash(email)}/activity-feed",
        params,
    )
    return {"email": email, "activity": data.get("activity", [])}


@mcp.tool(annotations=READ_ONLY)
@handled
def get_member_tags(email: str, list_id: str | None = None, count: int = 100) -> dict[str, Any]:
    """List the tags applied to one member."""
    data = marketing().get(
        f"/lists/{_resolve_list_id(list_id)}/members/{subscriber_hash(email)}/tags",
        {"count": min(max(count, 1), 1000)},
    )
    return {"email": email, "total_items": data.get("total_items"), "tags": data.get("tags", [])}


@mcp.tool(annotations=READ_ONLY)
@handled
def search_members(query: str, list_id: str | None = None) -> dict[str, Any]:
    """Search contacts across the account by email address or name.

    Returns exact matches and full-search results separately, as Mailchimp does.
    """
    params: dict[str, Any] = {"query": query}
    if list_id:
        params["list_id"] = list_id
    data = marketing().get("/search-members", params)
    return {
        "exact_matches": [
            _member_summary(m) for m in (data.get("exact_matches") or {}).get("members", [])
        ],
        "full_search": [
            _member_summary(m) for m in (data.get("full_search") or {}).get("members", [])
        ],
    }


# =========================================================================== #
# Segments, tags and merge fields
# =========================================================================== #


@mcp.tool(annotations=READ_ONLY)
@handled
def list_segments(list_id: str | None = None, count: int = 100, exclude_tags: bool = False) -> dict[str, Any]:
    """List an audience's segments and tags. Set `exclude_tags` to see saved segments only."""
    params: dict[str, Any] = {"count": min(max(count, 1), 1000)}
    if exclude_tags:
        params["exclude_type"] = "static"
    data = marketing().get(f"/lists/{_resolve_list_id(list_id)}/segments", params)
    return {
        "total_items": data.get("total_items"),
        "segments": [
            {
                "id": s.get("id"),
                "name": s.get("name"),
                "type": s.get("type"),
                "member_count": s.get("member_count"),
                "created_at": s.get("created_at"),
                "updated_at": s.get("updated_at"),
            }
            for s in data.get("segments", [])
        ],
    }


@mcp.tool(annotations=READ_ONLY)
@handled
def list_segment_members(
    segment_id: str,
    list_id: str | None = None,
    max_records: int = 200,
    include_transactional: bool = False,
    include_unsubscribed: bool = False,
) -> dict[str, Any]:
    """List the members in one segment or tag."""
    params: dict[str, Any] = {}
    if include_transactional:
        params["include_transactional"] = True
    if include_unsubscribed:
        params["include_unsubscribed"] = True
    members, total, truncated = marketing().paginate(
        f"/lists/{_resolve_list_id(list_id)}/segments/{segment_id}/members",
        item_key="members",
        params=params,
        max_records=max_records,
    )
    return {
        "total_items": total,
        "returned": len(members),
        "truncated": truncated,
        "members": [_member_summary(m) for m in members],
    }


@mcp.tool(annotations=READ_ONLY)
@handled
def list_merge_fields(list_id: str | None = None, count: int = 100) -> dict[str, Any]:
    """List an audience's merge fields (the custom contact fields and their tags)."""
    data = marketing().get(
        f"/lists/{_resolve_list_id(list_id)}/merge-fields", {"count": min(max(count, 1), 1000)}
    )
    return {
        "total_items": data.get("total_items"),
        "merge_fields": [
            {"tag": f.get("tag"), "name": f.get("name"), "type": f.get("type"), "required": f.get("required")}
            for f in data.get("merge_fields", [])
        ],
    }


# =========================================================================== #
# Campaigns and reports
# =========================================================================== #


@mcp.tool(annotations=READ_ONLY)
@handled
def list_campaigns(
    list_id: str | None = None,
    status: str | None = None,
    since_send_time: str | None = None,
    before_send_time: str | None = None,
    count: int = 25,
) -> dict[str, Any]:
    """List campaigns. `status` is one of: save, paused, schedule, sending, sent."""
    if status and status not in {"save", "paused", "schedule", "sending", "sent"}:
        raise ValueError("status must be save, paused, schedule, sending or sent")
    params: dict[str, Any] = {
        "count": min(max(count, 1), 1000),
        "status": status,
        "since_send_time": analysis.to_iso(analysis.coerce_window(since_send_time, name="since_send_time")),
        "before_send_time": analysis.to_iso(analysis.coerce_window(before_send_time, name="before_send_time")),
        "sort_field": "send_time",
        "sort_dir": "DESC",
        "fields": "total_items,campaigns.id,campaigns.web_id,campaigns.type,campaigns.status,"
                  "campaigns.send_time,campaigns.emails_sent,campaigns.settings.subject_line,"
                  "campaigns.settings.title,campaigns.recipients.list_id,campaigns.recipients.list_name,"
                  "campaigns.recipients.recipient_count",
    }
    if list_id:
        params["list_id"] = list_id
    data = marketing().get("/campaigns", params)
    return {"total_items": data.get("total_items"), "campaigns": data.get("campaigns", [])}


@mcp.tool(annotations=READ_ONLY)
@handled
def get_campaign_report(campaign_id: str) -> dict[str, Any]:
    """Get the performance report for one campaign: opens, clicks, bounces, unsubs, ecommerce."""
    return marketing().get(f"/reports/{campaign_id}")


@mcp.tool(annotations=READ_ONLY)
@handled
def list_campaign_reports(
    since_send_time: str | None = None, before_send_time: str | None = None, count: int = 25
) -> dict[str, Any]:
    """List campaign reports across the account, newest sends first."""
    data = marketing().get(
        "/reports",
        {
            "count": min(max(count, 1), 1000),
            "since_send_time": analysis.to_iso(analysis.coerce_window(since_send_time, name="since_send_time")),
            "before_send_time": analysis.to_iso(analysis.coerce_window(before_send_time, name="before_send_time")),
            "fields": "total_items,reports.id,reports.campaign_title,reports.send_time,"
                      "reports.emails_sent,reports.opens.open_rate,reports.clicks.click_rate,"
                      "reports.unsubscribed,reports.bounces",
        },
    )
    return {"total_items": data.get("total_items"), "reports": data.get("reports", [])}


@mcp.tool(annotations=READ_ONLY)
@handled
def get_campaign_unsubscribes(campaign_id: str, max_records: int = 200) -> dict[str, Any]:
    """List the members who unsubscribed from one campaign, with their stated reasons."""
    members, total, truncated = marketing().paginate(
        f"/reports/{campaign_id}/unsubscribed", item_key="unsubscribes", max_records=max_records
    )
    return {
        "total_items": total,
        "returned": len(members),
        "truncated": truncated,
        "unsubscribes": [
            {
                "email": m.get("email_address"),
                "timestamp": m.get("timestamp"),
                "reason": m.get("reason"),
                "list_id": m.get("list_id"),
            }
            for m in members
        ],
    }


# =========================================================================== #
# Subscribe-status change analysis
# =========================================================================== #


@mcp.tool(annotations=READ_ONLY)
@handled
def find_newly_subscribed(
    since: str,
    before: str | None = None,
    list_id: str | None = None,
    verdict: str = "upgraded_to_subscribed",
    max_records: int = 500,
) -> dict[str, Any]:
    """Find contacts that became Subscribed during a date window, and say which of
    them were previously Non-subscribed rather than brand-new signups.

    This is the answer to "who moved from Non-subscribed to Subscribed?" for a
    window that has already passed. Mailchimp stores no status history, so the
    verdict is **inferred** from the opt-in and signup timestamps and each row
    carries its own confidence. For a certain answer going forward, use
    `snapshot_member_statuses` now and `diff_member_status_snapshots` later.

    `verdict` filters the output: `upgraded_to_subscribed` (the default — existing
    contacts that became Subscribed), `new_subscriber`, `other_change`, or `all`.
    """
    since_dt = analysis.coerce_window(since, name="since")
    before_dt = analysis.coerce_window(before, name="before")
    if since_dt is None:
        raise ValueError("since is required, e.g. since='2026-08-01'")
    if before_dt and before_dt <= since_dt:
        raise ValueError("before must be later than since")

    allowed = {"upgraded_to_subscribed", "new_subscriber", "other_change", "all"}
    if verdict not in allowed:
        raise ValueError(f"verdict must be one of {sorted(allowed)}")

    params: dict[str, Any] = {
        "status": "subscribed",
        "since_last_changed": analysis.to_iso(since_dt),
        "before_last_changed": analysis.to_iso(before_dt),
        "sort_field": "last_changed",
        "sort_dir": "DESC",
        "fields": f"total_items,members.{',members.'.join(_MEMBER_FIELDS.split(','))}",
    }

    resolved = _resolve_list_id(list_id)
    members, total, truncated = marketing().paginate(
        f"/lists/{resolved}/members",
        item_key="members",
        params=params,
        max_records=max_records,
    )

    classified = [analysis.classify_member(m, since_dt, before_dt) for m in members]
    counts = analysis.summarize(classified)
    selected = classified if verdict == "all" else [c for c in classified if c.verdict == verdict]

    return {
        "window": {"since": analysis.to_iso(since_dt), "before": analysis.to_iso(before_dt)},
        "list_id": resolved,
        "examined": len(members),
        "total_changed_in_window": total,
        "truncated": truncated,
        "counts_by_verdict": counts,
        "verdict_filter": verdict,
        "matched": len(selected),
        "contacts": [c.as_dict() for c in selected],
        "method": (
            "Fetched members currently status=subscribed whose record changed in the window, "
            "then compared timestamp_opt against timestamp_signup. Mailchimp exposes no "
            "status-transition history, so 'upgraded_to_subscribed' is an inference: the "
            "contact existed before the window but only opted in during it. Confirm an "
            "individual contact with get_member_activity, or use the snapshot tools for "
            "exact tracking from now on."
        ),
    }


@mcp.tool(annotations=LOCAL_WRITE)
@handled
def snapshot_member_statuses(
    list_id: str | None = None, name: str | None = None, max_records: int = 5000
) -> dict[str, Any]:
    """Record every contact's current status to a local file, for exact change tracking later.

    Take one now and another after the period you care about, then compare them
    with `diff_member_status_snapshots`. This is the only method that reports
    status changes with certainty, because Mailchimp keeps no status history.

    Snapshots are written to MAILCHIMP_SNAPSHOT_DIR (default ./snapshots), which
    is gitignored — they contain subscriber email addresses.
    """
    resolved = _resolve_list_id(list_id)
    members, total, truncated = marketing().paginate(
        f"/lists/{resolved}/members",
        item_key="members",
        params={"fields": "total_items,members.email_address,members.status,members.last_changed,"
                          "members.timestamp_opt,members.contact_id,members.id"},
        max_records=max_records,
    )
    result = analysis.snapshot_members(settings().snapshot_dir, resolved, members, name)
    result["audience_total"] = total
    result["truncated"] = truncated
    if truncated:
        result["warning"] = (
            f"Only {len(members)} of {total} contacts were captured (max_records limit). "
            "A partial snapshot will report missing contacts as removed when diffed."
        )
    return result


@mcp.tool(annotations=READ_ONLY)
@handled
def list_status_snapshots(list_id: str | None = None) -> dict[str, Any]:
    """List the status snapshots stored locally, optionally for one audience."""
    return {
        "snapshot_dir": str(settings().snapshot_dir),
        "snapshots": analysis.list_snapshots(settings().snapshot_dir, list_id),
    }


@mcp.tool(annotations=READ_ONLY)
@handled
def diff_member_status_snapshots(
    from_snapshot: str,
    to_snapshot: str,
    list_id: str | None = None,
    from_status: str | None = "transactional",
    to_status: str | None = "subscribed",
) -> dict[str, Any]:
    """Compare two snapshots and list the exact status transitions between them.

    Defaults answer the common question directly: who went from Non-subscribed
    (`transactional`) to Subscribed. Pass `from_status=None` and `to_status=None`
    to see every transition of any kind.
    """
    resolved = _resolve_list_id(list_id)
    root = settings().snapshot_dir
    before = analysis.load_snapshot(root, resolved, from_snapshot)
    after = analysis.load_snapshot(root, resolved, to_snapshot)
    result = analysis.diff_snapshots(before, after, from_status, to_status)
    result["list_id"] = resolved
    return result


# =========================================================================== #
# Transactional (Mandrill) — optional, read-only, off unless a key is set
# =========================================================================== #


@mcp.tool(annotations=READ_ONLY)
@handled
def transactional_account_info() -> dict[str, Any]:
    """Get Transactional (Mandrill) account info and recent send stats.

    Requires MAILCHIMP_TRANSACTIONAL_API_KEY; disabled otherwise.
    """
    return transactional().call("/users/info.json")


@mcp.tool(annotations=READ_ONLY)
@handled
def transactional_search_messages(
    query: str = "*",
    date_from: str | None = None,
    date_to: str | None = None,
    senders: Sequence[str] | None = None,
    limit: int = 50,
) -> dict[str, Any]:
    """Search transactional messages sent in the last 30 days.

    `query` uses Mandrill search syntax (e.g. `email:someone@example.com`).
    Dates are `YYYY-MM-DD`. Requires MAILCHIMP_TRANSACTIONAL_API_KEY.
    """
    payload: dict[str, Any] = {"query": query, "limit": min(max(limit, 1), 1000)}
    if date_from:
        payload["date_from"] = date_from
    if date_to:
        payload["date_to"] = date_to
    if senders:
        payload["senders"] = list(senders)
    results = transactional().call("/messages/search.json", payload)
    return {"count": len(results) if isinstance(results, list) else 0, "messages": results}


# =========================================================================== #


#: The hand-written tools above. Declared explicitly rather than introspected so
#: that name clashes with the generated tools are caught by a test, not at runtime.
CURATED_TOOL_NAMES = frozenset(
    {
        "ping",
        "get_account",
        "list_audiences",
        "get_audience",
        "get_audience_growth_history",
        "get_audience_activity",
        "list_members",
        "get_member",
        "get_member_activity",
        "get_member_tags",
        "search_members",
        "list_segments",
        "list_segment_members",
        "list_merge_fields",
        "list_campaigns",
        "get_campaign_report",
        "list_campaign_reports",
        "get_campaign_unsubscribes",
        "find_newly_subscribed",
        "snapshot_member_statuses",
        "list_status_snapshots",
        "diff_member_status_snapshots",
        "transactional_account_info",
        "transactional_search_messages",
    }
)


def register_generated_tools() -> dict[str, Any]:
    """Expose one tool per Mailchimp API operation, filtered by access level."""
    return generated.register(mcp, settings(), marketing, reserved=set(CURATED_TOOL_NAMES))


def main() -> None:
    """Entry point for the ``mailchimp-mcp`` console script."""
    try:
        current = load_settings()
    except ConfigError as exc:
        print(f"mailchimp-mcp: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    summary = register_generated_tools()
    total = len(CURATED_TOOL_NAMES) + summary["registered"]
    print(
        f"mailchimp-mcp {__version__}: access level {current.access_level.value} "
        f"({DESCRIPTIONS[current.access_level]}); {total} tools "
        f"({len(CURATED_TOOL_NAMES)} curated + {summary['registered']} generated, "
        f"{summary['skipped_above_access_level']} withheld above access level).",
        file=sys.stderr,
    )
    if current.access_level is AccessLevel.ADMIN:
        print(
            "mailchimp-mcp: WARNING — ADMIN access is enabled. Tools that permanently "
            "update and delete Mailchimp data are exposed to the model.",
            file=sys.stderr,
        )
    mcp.run()


if __name__ == "__main__":
    main()

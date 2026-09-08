"""Subscribe-status change analysis.

Mailchimp has no endpoint that returns a member's status *history* — you can
read a member's status now, and you can read when their record last changed,
but the API will not tell you what the status used to be. This module offers
the two honest ways around that:

* :func:`classify_member` — an inference from the timestamps Mailchimp does
  expose (``timestamp_opt``, ``timestamp_signup``, ``last_changed``). Good for
  answering "who became subscribed recently?" retroactively, with an explicit
  confidence level attached to every row.
* :func:`snapshot_members` / :func:`diff_snapshots` — record the audience's
  statuses now, compare later, and get exact transitions. This is the only
  method that is certain, and it only works going forward.

Terminology note: Mailchimp's UI label **"Non-subscribed"** is the API status
``transactional``. That is the status this module is usually asked about.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

#: API status value -> the label shown in the Mailchimp web UI.
STATUS_LABELS: dict[str, str] = {
    "subscribed": "Subscribed",
    "unsubscribed": "Unsubscribed",
    "cleaned": "Cleaned",
    "pending": "Pending (double opt-in not confirmed)",
    "transactional": "Non-subscribed",
    "archived": "Archived",
}

#: Statuses that are "not subscribed" for the purposes of an upgrade question.
NON_SUBSCRIBED_STATUSES = frozenset({"transactional", "pending", "archived", "unsubscribed"})

_SNAPSHOT_NAME_RE = re.compile(r"^[A-Za-z0-9._-]{1,64}$")


class AnalysisError(RuntimeError):
    """Raised for bad snapshot names, missing snapshots, or unparseable input."""


# --------------------------------------------------------------------------- #
# Timestamps
# --------------------------------------------------------------------------- #


def parse_timestamp(value: Any) -> datetime | None:
    """Parse a Mailchimp ISO 8601 timestamp. Empty/absent values return None."""
    if not value or not isinstance(value, str):
        return None
    text = value.strip()
    if not text:
        return None
    if text.endswith(("Z", "z")):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def coerce_window(value: str | None, *, name: str) -> datetime | None:
    """Accept a date (``2026-09-01``) or a full ISO 8601 instant."""
    if value is None or not str(value).strip():
        return None
    text = str(value).strip()
    if len(text) == 10:
        text += "T00:00:00+00:00"
    parsed = parse_timestamp(text)
    if parsed is None:
        raise AnalysisError(
            f"{name}={value!r} is not a valid date. Use YYYY-MM-DD or a full "
            "ISO 8601 timestamp such as 2026-09-01T00:00:00+00:00."
        )
    return parsed


def to_iso(value: datetime | None) -> str | None:
    return value.isoformat() if value else None


# --------------------------------------------------------------------------- #
# Inference from a live member record
# --------------------------------------------------------------------------- #


@dataclass
class Classification:
    """One member's verdict, with the evidence that produced it."""

    email: str
    status: str
    status_label: str
    verdict: str
    confidence: str
    reason: str
    last_changed: str | None = None
    timestamp_opt: str | None = None
    timestamp_signup: str | None = None
    source: str | None = None
    tags: list[str] = field(default_factory=list)
    contact_id: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return {
            "email": self.email,
            "status": self.status,
            "status_label": self.status_label,
            "verdict": self.verdict,
            "confidence": self.confidence,
            "reason": self.reason,
            "last_changed": self.last_changed,
            "timestamp_opt": self.timestamp_opt,
            "timestamp_signup": self.timestamp_signup,
            "source": self.source,
            "tags": self.tags,
            "contact_id": self.contact_id,
        }


def classify_member(
    member: Mapping[str, Any],
    since: datetime,
    before: datetime | None = None,
) -> Classification:
    """Decide whether a now-subscribed member newly subscribed inside the window.

    The three verdicts:

    ``upgraded_to_subscribed``
        The contact record predates the window but the opt-in timestamp falls
        inside it — the shape a Non-subscribed (``transactional``) contact takes
        after being switched to Subscribed.
    ``new_subscriber``
        The contact first appeared during the window, so this is a fresh signup
        rather than a status change on an existing contact.
    ``other_change``
        Something about the record changed in the window, but the opt-in
        timestamp did not — a tag, a merge field, an email client update.
    """
    email = str(member.get("email_address", "") or "")
    status = str(member.get("status", "") or "")
    opt = parse_timestamp(member.get("timestamp_opt"))
    signup = parse_timestamp(member.get("timestamp_signup"))
    changed = parse_timestamp(member.get("last_changed"))

    tags = [str(t.get("name", "")) for t in member.get("tags") or [] if isinstance(t, Mapping)]

    common = {
        "email": email,
        "status": status,
        "status_label": STATUS_LABELS.get(status, status),
        "last_changed": to_iso(changed),
        "timestamp_opt": to_iso(opt),
        "timestamp_signup": to_iso(signup),
        "source": member.get("source") or None,
        "tags": tags,
        "contact_id": member.get("contact_id") or member.get("id") or None,
    }

    opt_in_window = bool(opt and opt >= since and (before is None or opt <= before))

    if not opt_in_window:
        return Classification(
            verdict="other_change",
            confidence="high",
            reason=(
                "Record changed during the window but the opt-in timestamp did not fall "
                "inside it, so the subscribe status most likely predates the window."
            ),
            **common,
        )

    if signup is None:
        return Classification(
            verdict="upgraded_to_subscribed",
            confidence="medium",
            reason=(
                "Opted in during the window with no signup timestamp on record. Contacts "
                "added as Non-subscribed (transactional) — via an order or an API import — "
                "typically have no signup timestamp, so this looks like an upgrade."
            ),
            **common,
        )

    if signup >= since:
        return Classification(
            verdict="new_subscriber",
            confidence="high",
            reason="Signed up and opted in during the window — a new contact, not a status change.",
            **common,
        )

    return Classification(
        verdict="upgraded_to_subscribed",
        confidence="high",
        reason=(
            f"Contact existed since {to_iso(signup)} but only opted in at {to_iso(opt)}, "
            "inside the window — an existing non-subscribed contact that became Subscribed."
        ),
        **common,
    )


def summarize(classifications: Sequence[Classification]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in classifications:
        counts[item.verdict] = counts.get(item.verdict, 0) + 1
    return counts


# --------------------------------------------------------------------------- #
# Snapshots — the exact method
# --------------------------------------------------------------------------- #


def _validate_name(name: str) -> str:
    cleaned = name.strip()
    if not _SNAPSHOT_NAME_RE.match(cleaned):
        raise AnalysisError(
            f"Snapshot name {name!r} is invalid. Use 1-64 characters from "
            "A-Z a-z 0-9 . _ - (no slashes)."
        )
    return cleaned


def snapshot_path(root: Path, list_id: str, name: str) -> Path:
    return root / _validate_name(list_id) / f"{_validate_name(name)}.json"


def default_snapshot_name() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")


def snapshot_members(
    root: Path,
    list_id: str,
    members: Iterable[Mapping[str, Any]],
    name: str | None = None,
) -> dict[str, Any]:
    """Write ``{email: status}`` for an audience to disk and return its metadata."""
    name = name or default_snapshot_name()
    path = snapshot_path(root, list_id, name)
    path.parent.mkdir(parents=True, exist_ok=True)

    records: dict[str, dict[str, Any]] = {}
    for member in members:
        email = str(member.get("email_address", "") or "").strip().lower()
        if not email:
            continue
        records[email] = {
            "status": member.get("status"),
            "last_changed": member.get("last_changed") or None,
            "timestamp_opt": member.get("timestamp_opt") or None,
            "contact_id": member.get("contact_id") or member.get("id") or None,
        }

    payload = {
        "list_id": list_id,
        "name": name,
        "taken_at": datetime.now(timezone.utc).isoformat(),
        "member_count": len(records),
        "members": records,
    }
    # 0o600: snapshots hold subscriber email addresses.
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    path.chmod(0o600)

    return {
        "list_id": list_id,
        "snapshot": name,
        "path": str(path),
        "member_count": len(records),
        "taken_at": payload["taken_at"],
    }


def load_snapshot(root: Path, list_id: str, name: str) -> dict[str, Any]:
    path = snapshot_path(root, list_id, name)
    if not path.is_file():
        available = [p.stem for p in sorted(path.parent.glob("*.json"))] if path.parent.is_dir() else []
        raise AnalysisError(
            f"No snapshot named {name!r} for audience {list_id}. "
            + (f"Available: {', '.join(available)}" if available else "None have been taken yet.")
        )
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AnalysisError(f"Could not read snapshot {path}: {exc}") from exc


def list_snapshots(root: Path, list_id: str | None = None) -> list[dict[str, Any]]:
    if not root.is_dir():
        return []
    dirs = [root / _validate_name(list_id)] if list_id else sorted(p for p in root.iterdir() if p.is_dir())
    found: list[dict[str, Any]] = []
    for directory in dirs:
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.json")):
            entry = {"list_id": directory.name, "snapshot": path.stem, "path": str(path)}
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                entry["taken_at"] = data.get("taken_at")
                entry["member_count"] = data.get("member_count")
            except (OSError, json.JSONDecodeError):
                entry["error"] = "unreadable"
            found.append(entry)
    return found


def diff_snapshots(
    before: Mapping[str, Any],
    after: Mapping[str, Any],
    from_status: str | Sequence[str] | None = None,
    to_status: str | Sequence[str] | None = None,
) -> dict[str, Any]:
    """Compare two snapshots and return the exact status transitions between them."""
    old = before.get("members") or {}
    new = after.get("members") or {}

    def wanted(value: str | Sequence[str] | None) -> set[str] | None:
        if value is None:
            return None
        if isinstance(value, str):
            return {value}
        return set(value)

    from_set, to_set = wanted(from_status), wanted(to_status)

    transitions: list[dict[str, Any]] = []
    for email, new_record in new.items():
        old_record = old.get(email)
        if old_record is None:
            continue
        was, now = old_record.get("status"), new_record.get("status")
        if was == now:
            continue
        if from_set and was not in from_set:
            continue
        if to_set and now not in to_set:
            continue
        transitions.append(
            {
                "email": email,
                "from_status": was,
                "from_status_label": STATUS_LABELS.get(str(was), was),
                "to_status": now,
                "to_status_label": STATUS_LABELS.get(str(now), now),
                "last_changed": new_record.get("last_changed"),
                "timestamp_opt": new_record.get("timestamp_opt"),
                "contact_id": new_record.get("contact_id"),
            }
        )

    transitions.sort(key=lambda row: (row["last_changed"] or "", row["email"]))

    added = [e for e in new if e not in old]
    removed = [e for e in old if e not in new]

    return {
        "from_snapshot": before.get("name"),
        "from_taken_at": before.get("taken_at"),
        "to_snapshot": after.get("name"),
        "to_taken_at": after.get("taken_at"),
        "filters": {"from_status": from_status, "to_status": to_status},
        "transition_count": len(transitions),
        "transitions": transitions,
        "added_contacts": added[:200],
        "added_count": len(added),
        "removed_contacts": removed[:200],
        "removed_count": len(removed),
        "note": (
            "Exact comparison of two point-in-time snapshots. A contact that changed "
            "status twice between the snapshots shows only its net movement."
        ),
    }

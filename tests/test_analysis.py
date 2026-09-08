import json
from datetime import datetime, timezone

import pytest

from mailchimp_mcp import analysis


SINCE = datetime(2026, 8, 1, tzinfo=timezone.utc)


def member(**overrides):
    base = {
        "email_address": "person@example.com",
        "status": "subscribed",
        "timestamp_opt": "",
        "timestamp_signup": "",
        "last_changed": "2026-08-15T10:00:00+00:00",
        "tags": [],
    }
    base.update(overrides)
    return base


# --------------------------------------------------------------------------- #
# Timestamps
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("value", ["", None, "   ", "not-a-date", 12345])
def test_parse_timestamp_rejects_junk(value):
    assert analysis.parse_timestamp(value) is None


def test_parse_timestamp_handles_z_suffix_and_naive():
    assert analysis.parse_timestamp("2026-08-15T10:00:00Z") == datetime(2026, 8, 15, 10, tzinfo=timezone.utc)
    assert analysis.parse_timestamp("2026-08-15T10:00:00") == datetime(2026, 8, 15, 10, tzinfo=timezone.utc)


def test_coerce_window_accepts_plain_date():
    assert analysis.coerce_window("2026-08-01", name="since") == SINCE


def test_coerce_window_rejects_bad_input():
    with pytest.raises(analysis.AnalysisError, match="valid date"):
        analysis.coerce_window("last tuesday", name="since")


# --------------------------------------------------------------------------- #
# Classification
# --------------------------------------------------------------------------- #


def test_existing_contact_that_opted_in_is_an_upgrade():
    result = analysis.classify_member(
        member(timestamp_signup="2024-01-05T09:00:00+00:00", timestamp_opt="2026-08-15T10:00:00+00:00"),
        SINCE,
    )
    assert result.verdict == "upgraded_to_subscribed"
    assert result.confidence == "high"


def test_transactional_contact_with_no_signup_stamp_is_a_probable_upgrade():
    result = analysis.classify_member(member(timestamp_opt="2026-08-15T10:00:00+00:00"), SINCE)
    assert result.verdict == "upgraded_to_subscribed"
    assert result.confidence == "medium"


def test_fresh_signup_is_not_an_upgrade():
    result = analysis.classify_member(
        member(timestamp_signup="2026-08-10T09:00:00+00:00", timestamp_opt="2026-08-10T09:05:00+00:00"),
        SINCE,
    )
    assert result.verdict == "new_subscriber"


def test_record_touched_without_opt_in_is_other_change():
    result = analysis.classify_member(
        member(timestamp_signup="2023-01-01T00:00:00+00:00", timestamp_opt="2023-01-01T00:00:00+00:00"),
        SINCE,
    )
    assert result.verdict == "other_change"


def test_opt_in_after_before_bound_is_excluded():
    result = analysis.classify_member(
        member(timestamp_signup="2020-01-01T00:00:00+00:00", timestamp_opt="2026-09-20T00:00:00+00:00"),
        SINCE,
        before=datetime(2026, 9, 1, tzinfo=timezone.utc),
    )
    assert result.verdict == "other_change"


def test_status_label_maps_transactional_to_non_subscribed():
    assert analysis.STATUS_LABELS["transactional"] == "Non-subscribed"
    result = analysis.classify_member(member(status="transactional"), SINCE)
    assert result.status_label == "Non-subscribed"


def test_summarize_counts_verdicts():
    rows = [
        analysis.classify_member(member(timestamp_opt="2026-08-15T10:00:00+00:00"), SINCE),
        analysis.classify_member(member(email_address="b@e.com"), SINCE),
    ]
    assert analysis.summarize(rows) == {"upgraded_to_subscribed": 1, "other_change": 1}


# --------------------------------------------------------------------------- #
# Snapshots
# --------------------------------------------------------------------------- #


def test_snapshot_name_validation_blocks_traversal(tmp_path):
    for bad in ("../escape", "a/b", "", "x" * 65):
        with pytest.raises(analysis.AnalysisError):
            analysis.snapshot_path(tmp_path, "list1", bad)


def test_snapshot_list_id_validation_blocks_traversal(tmp_path):
    with pytest.raises(analysis.AnalysisError):
        analysis.snapshot_path(tmp_path, "../../etc", "ok")


def test_snapshot_round_trip_and_permissions(tmp_path):
    meta = analysis.snapshot_members(
        tmp_path,
        "list1",
        [member(email_address="A@Example.com", status="transactional")],
        name="before",
    )
    assert meta["member_count"] == 1
    path = tmp_path / "list1" / "before.json"
    assert oct(path.stat().st_mode)[-3:] == "600"
    data = json.loads(path.read_text())
    # Emails are normalised to lowercase so diffs line up.
    assert "a@example.com" in data["members"]


def test_load_missing_snapshot_lists_alternatives(tmp_path):
    analysis.snapshot_members(tmp_path, "list1", [member()], name="before")
    with pytest.raises(analysis.AnalysisError, match="Available: before"):
        analysis.load_snapshot(tmp_path, "list1", "after")


def test_list_snapshots_reports_metadata(tmp_path):
    analysis.snapshot_members(tmp_path, "list1", [member()], name="before")
    found = analysis.list_snapshots(tmp_path, "list1")
    assert len(found) == 1
    assert found[0]["snapshot"] == "before"
    assert found[0]["member_count"] == 1


def test_diff_finds_non_subscribed_to_subscribed(tmp_path):
    analysis.snapshot_members(
        tmp_path,
        "list1",
        [
            member(email_address="upgraded@example.com", status="transactional"),
            member(email_address="stable@example.com", status="subscribed"),
            member(email_address="left@example.com", status="subscribed"),
        ],
        name="before",
    )
    analysis.snapshot_members(
        tmp_path,
        "list1",
        [
            member(email_address="upgraded@example.com", status="subscribed"),
            member(email_address="stable@example.com", status="subscribed"),
            member(email_address="opted-out@example.com", status="unsubscribed"),
            member(email_address="brand-new@example.com", status="subscribed"),
        ],
        name="after",
    )
    before = analysis.load_snapshot(tmp_path, "list1", "before")
    after = analysis.load_snapshot(tmp_path, "list1", "after")

    result = analysis.diff_snapshots(before, after, "transactional", "subscribed")
    assert result["transition_count"] == 1
    assert result["transitions"][0]["email"] == "upgraded@example.com"
    assert result["transitions"][0]["from_status_label"] == "Non-subscribed"

    # New and departed contacts are reported separately, never as transitions.
    assert result["added_count"] == 2
    assert result["removed_count"] == 1
    assert "brand-new@example.com" in result["added_contacts"]
    assert "left@example.com" in result["removed_contacts"]


def test_diff_without_filters_returns_every_transition(tmp_path):
    analysis.snapshot_members(
        tmp_path, "list1", [member(email_address="a@e.com", status="subscribed")], name="b1"
    )
    analysis.snapshot_members(
        tmp_path, "list1", [member(email_address="a@e.com", status="unsubscribed")], name="b2"
    )
    result = analysis.diff_snapshots(
        analysis.load_snapshot(tmp_path, "list1", "b1"),
        analysis.load_snapshot(tmp_path, "list1", "b2"),
        None,
        None,
    )
    assert result["transition_count"] == 1
    assert result["transitions"][0]["to_status"] == "unsubscribed"


def test_diff_accepts_multiple_from_statuses(tmp_path):
    analysis.snapshot_members(
        tmp_path,
        "list1",
        [member(email_address="a@e.com", status="transactional"), member(email_address="b@e.com", status="pending")],
        name="b1",
    )
    analysis.snapshot_members(
        tmp_path,
        "list1",
        [member(email_address="a@e.com", status="subscribed"), member(email_address="b@e.com", status="subscribed")],
        name="b2",
    )
    result = analysis.diff_snapshots(
        analysis.load_snapshot(tmp_path, "list1", "b1"),
        analysis.load_snapshot(tmp_path, "list1", "b2"),
        ["transactional", "pending"],
        "subscribed",
    )
    assert result["transition_count"] == 2

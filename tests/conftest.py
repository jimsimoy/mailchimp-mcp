import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from mailchimp_mcp.config import Settings  # noqa: E402


@pytest.fixture()
def settings(tmp_path) -> Settings:
    return Settings(
        api_key="secretkey-us13",
        datacenter="us13",
        snapshot_dir=tmp_path / "snapshots",
        timeout=5.0,
        max_records=100,
    )

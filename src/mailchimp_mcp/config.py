"""Credential loading and runtime settings.

Everything sensitive comes from the environment (optionally via a .env file).
Nothing is ever written back to it, and the API key is redacted from any text
this package produces.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

from .access import AccessLevel

#: Mailchimp datacenter suffixes look like "us13", "us1", "eu1".
_DATACENTER_RE = re.compile(r"^[a-z]{2}\d{1,3}$")

#: Hosts this server is ever allowed to talk to.
ALLOWED_HOSTS = ("api.mailchimp.com", "mandrillapp.com")


class ConfigError(RuntimeError):
    """Raised when credentials are missing or malformed."""


def _env_float(name: str, default: float) -> float:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return default
    try:
        value = float(raw)
    except ValueError as exc:
        raise ConfigError(f"{name} must be a number, got {raw!r}") from exc
    if value <= 0:
        raise ConfigError(f"{name} must be greater than zero, got {value}")
    return value


def _env_int(name: str, default: int) -> int:
    raw = os.environ.get(name, "").strip()
    if not raw:
        return default
    try:
        value = int(raw)
    except ValueError as exc:
        raise ConfigError(f"{name} must be an integer, got {raw!r}") from exc
    if value <= 0:
        raise ConfigError(f"{name} must be greater than zero, got {value}")
    return value


def split_api_key(api_key: str) -> tuple[str, str | None]:
    """Split ``<key>-<dc>`` into its two halves.

    OAuth tokens carry no datacenter suffix, so the second half may be None.
    """
    key = api_key.strip()
    if "-" not in key:
        return key, None
    secret, _, suffix = key.rpartition("-")
    if not _DATACENTER_RE.match(suffix):
        return key, None
    return secret, suffix


@dataclass(frozen=True)
class Settings:
    """Resolved configuration for one server process."""

    api_key: str
    datacenter: str
    transactional_api_key: str | None = None
    default_list_id: str | None = None
    snapshot_dir: Path = Path("snapshots")
    timeout: float = 30.0
    max_records: int = 5000
    access_level: AccessLevel = AccessLevel.READONLY
    tool_groups: frozenset[str] | None = None

    @property
    def base_url(self) -> str:
        return f"https://{self.datacenter}.api.mailchimp.com/3.0"

    @property
    def transactional_enabled(self) -> bool:
        return bool(self.transactional_api_key)

    @property
    def allowed_methods(self) -> frozenset[str]:
        return self.access_level.methods

    def redact(self, text: str) -> str:
        """Strip any credential that leaked into a message."""
        for secret in (self.api_key, self.transactional_api_key):
            if secret and secret in text:
                text = text.replace(secret, "***REDACTED***")
        return text


def load_settings(env_file: str | os.PathLike[str] | None = None) -> Settings:
    """Build :class:`Settings` from the environment.

    A .env file is loaded if present, but real environment variables always win
    so that an MCP client's ``env`` block can override the file.
    """
    if env_file is not None:
        load_dotenv(env_file, override=False)
    else:
        # Look next to the caller first, then at the installed project root.
        for candidate in (Path.cwd() / ".env", Path(__file__).resolve().parents[2] / ".env"):
            if candidate.is_file():
                load_dotenv(candidate, override=False)
                break

    raw_key = os.environ.get("MAILCHIMP_API_KEY", "").strip()
    if not raw_key:
        raise ConfigError(
            "MAILCHIMP_API_KEY is not set. Copy .env.example to .env and add your "
            "Marketing API key (format: <key>-<datacenter>, e.g. abc123-us13)."
        )

    _, suffix = split_api_key(raw_key)
    datacenter = (os.environ.get("MAILCHIMP_DC", "").strip() or suffix or "").lower()
    if not datacenter:
        raise ConfigError(
            "Could not determine the Mailchimp datacenter. Your key has no '-usX' "
            "suffix, so set MAILCHIMP_DC explicitly (e.g. MAILCHIMP_DC=us13)."
        )
    if not _DATACENTER_RE.match(datacenter):
        raise ConfigError(
            f"MAILCHIMP_DC={datacenter!r} does not look like a datacenter "
            "(expected something like 'us13' or 'eu1')."
        )

    snapshot_dir = Path(
        os.environ.get("MAILCHIMP_SNAPSHOT_DIR", "").strip() or "snapshots"
    ).expanduser()

    try:
        access_level = AccessLevel.parse(os.environ.get("MAILCHIMP_ACCESS_LEVEL"))
    except ValueError as exc:
        raise ConfigError(str(exc)) from exc

    groups_raw = os.environ.get("MAILCHIMP_TOOL_GROUPS", "").strip()
    tool_groups = (
        frozenset(g.strip().lower() for g in groups_raw.split(",") if g.strip()) or None
        if groups_raw
        else None
    )

    return Settings(
        api_key=raw_key,
        datacenter=datacenter,
        transactional_api_key=os.environ.get("MAILCHIMP_TRANSACTIONAL_API_KEY", "").strip() or None,
        default_list_id=os.environ.get("MAILCHIMP_DEFAULT_LIST_ID", "").strip() or None,
        snapshot_dir=snapshot_dir,
        timeout=_env_float("MAILCHIMP_TIMEOUT", 30.0),
        max_records=_env_int("MAILCHIMP_MAX_RECORDS", 5000),
        access_level=access_level,
        tool_groups=tool_groups,
    )

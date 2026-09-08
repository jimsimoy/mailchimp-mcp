"""Access levels.

One environment variable, ``MAILCHIMP_ACCESS_LEVEL``, decides how much of the
Mailchimp API this server will expose. It is enforced in two independent places:

1. **Registration** — tools above the configured level are never registered, so
   the model is not even shown that they exist.
2. **Dispatch** — :class:`~mailchimp_mcp.client.MarketingClient` refuses any HTTP
   method the level does not permit, so a tool that somehow reached the client
   anyway still cannot write.

The default is READONLY. Raising it is a deliberate act by whoever owns the
account, and ADMIN in particular grants permanent deletion.
"""

from __future__ import annotations

from enum import Enum


class AccessDenied(PermissionError):
    """Raised when an operation exceeds the configured access level."""


class AccessLevel(str, Enum):
    """How much of the API is exposed."""

    READONLY = "READONLY"
    BASIC = "BASIC"
    ADMIN = "ADMIN"

    @property
    def rank(self) -> int:
        return _RANK[self]

    @property
    def methods(self) -> frozenset[str]:
        """HTTP methods this level permits."""
        return _METHODS[self]

    def permits(self, required: "AccessLevel | str") -> bool:
        """Whether this level is sufficient for an operation requiring ``required``."""
        return self.rank >= AccessLevel(required).rank

    @classmethod
    def parse(cls, value: str | None, default: "AccessLevel | None" = None) -> "AccessLevel":
        text = (value or "").strip().upper()
        if not text:
            return default or cls.READONLY
        try:
            return cls(text)
        except ValueError as exc:
            raise ValueError(
                f"MAILCHIMP_ACCESS_LEVEL={value!r} is not valid. Use one of: "
                f"{', '.join(level.value for level in cls)}."
            ) from exc


_RANK: dict[AccessLevel, int] = {
    AccessLevel.READONLY: 0,
    AccessLevel.BASIC: 1,
    AccessLevel.ADMIN: 2,
}

_METHODS: dict[AccessLevel, frozenset[str]] = {
    AccessLevel.READONLY: frozenset({"GET"}),
    AccessLevel.BASIC: frozenset({"GET", "POST"}),
    AccessLevel.ADMIN: frozenset({"GET", "POST", "PUT", "PATCH", "DELETE"}),
}

#: What each level means, in one line — used in errors and in the server's instructions.
DESCRIPTIONS: dict[AccessLevel, str] = {
    AccessLevel.READONLY: "read only (GET) — cannot change anything in Mailchimp",
    AccessLevel.BASIC: "read and create (GET, POST) — can add contacts, campaigns and other records",
    AccessLevel.ADMIN: "full access (GET, POST, PUT, PATCH, DELETE) — can update and permanently delete data",
}


def require(current: AccessLevel, needed: AccessLevel | str, operation: str) -> None:
    """Raise :class:`AccessDenied` unless ``current`` is sufficient for ``needed``."""
    needed_level = AccessLevel(needed)
    if not current.permits(needed_level):
        raise AccessDenied(
            f"'{operation}' requires MAILCHIMP_ACCESS_LEVEL={needed_level.value} but this server "
            f"is running as {current.value} ({DESCRIPTIONS[current]}). Raising the level lets this "
            "server change your Mailchimp data; see the README's Access Levels section before you do."
        )

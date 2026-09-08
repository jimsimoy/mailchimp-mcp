"""HTTP clients for Mailchimp.

Two deliberate constraints live here, and they are the whole security story of
this project:

1. :class:`MarketingClient` exposes **only** ``get``. There is no post/put/patch
   /delete method to call, so no tool built on it can mutate your audience.
2. :class:`TransactionalClient` speaks Mandrill's POST-only protocol, so it
   guards itself with an explicit allowlist of read-only endpoints instead.
"""

from __future__ import annotations

import hashlib
import re
import time
from typing import Any, Mapping, Sequence

import httpx

from .config import Settings

#: Endpoint paths are built by this package, never by the caller, but validate
#: anyway so a malformed argument can't turn into a request to another host.
_SAFE_PATH_RE = re.compile(r"^/[A-Za-z0-9._~%/-]*$")

_RETRY_STATUSES = frozenset({429, 500, 502, 503, 504})
_MAX_ATTEMPTS = 4

#: Mandrill methods this server is permitted to call. Everything here is a read;
#: sending, template edits and rejection-list writes are absent on purpose.
TRANSACTIONAL_ALLOWLIST = frozenset(
    {
        "/users/ping2.json",
        "/users/info.json",
        "/messages/search.json",
        "/messages/info.json",
    }
)


class MailchimpError(RuntimeError):
    """A non-success response from Mailchimp, rendered for a human."""

    def __init__(
        self,
        status: int,
        title: str = "",
        detail: str = "",
        errors: Sequence[Mapping[str, Any]] | None = None,
    ) -> None:
        self.status = status
        self.title = title
        self.detail = detail
        self.errors = list(errors or [])
        message = f"Mailchimp API error {status}"
        if title:
            message += f" ({title})"
        if detail:
            message += f": {detail}"
        for err in self.errors:
            message += f"\n  - {err.get('field', '?')}: {err.get('message', '')}"
        super().__init__(message)


def subscriber_hash(email_or_hash: str) -> str:
    """Return Mailchimp's subscriber hash for an email address.

    Already-hashed values and contact IDs are passed through untouched, which
    matches what the API itself accepts on these routes.
    """
    value = email_or_hash.strip()
    if "@" not in value:
        return value
    # MD5 is Mailchimp's addressing scheme for members, not a security control.
    return hashlib.md5(value.lower().encode("utf-8"), usedforsecurity=False).hexdigest()


def _clean_params(params: Mapping[str, Any] | None) -> dict[str, Any]:
    """Drop unset values and flatten list-valued params to CSV, as the API expects."""
    cleaned: dict[str, Any] = {}
    for key, value in (params or {}).items():
        if value is None or value == "":
            continue
        if isinstance(value, bool):
            cleaned[key] = "true" if value else "false"
        elif isinstance(value, (list, tuple)):
            if not value:
                continue
            cleaned[key] = ",".join(str(item) for item in value)
        else:
            cleaned[key] = value
    return cleaned


class MarketingClient:
    """Read-only client for ``https://<dc>.api.mailchimp.com/3.0``."""

    def __init__(self, settings: Settings, client: httpx.Client | None = None) -> None:
        self._settings = settings
        self._client = client or httpx.Client(
            base_url=settings.base_url,
            # Any username works; the key goes in the password field.
            auth=("mailchimp-mcp", settings.api_key),
            timeout=settings.timeout,
            headers={"User-Agent": "mailchimp-mcp (+https://github.com/jimsimoy/mailchimp-mcp)"},
            follow_redirects=False,
        )

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "MarketingClient":
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()

    def get(self, path: str, params: Mapping[str, Any] | None = None) -> dict[str, Any]:
        """Issue one GET and return the decoded JSON body."""
        if not _SAFE_PATH_RE.match(path) or path.startswith("//"):
            raise ValueError(f"Refusing to request unsafe path: {path!r}")

        query = _clean_params(params)
        last_error: MailchimpError | None = None

        for attempt in range(1, _MAX_ATTEMPTS + 1):
            response = self._client.get(path, params=query)
            if response.status_code < 400:
                if not response.content:
                    return {}
                return response.json()

            error = self._to_error(response)
            if response.status_code not in _RETRY_STATUSES or attempt == _MAX_ATTEMPTS:
                raise error
            last_error = error
            time.sleep(self._backoff(response, attempt))

        raise last_error or MailchimpError(500, detail="Request failed with no response")

    def paginate(
        self,
        path: str,
        item_key: str,
        params: Mapping[str, Any] | None = None,
        max_records: int | None = None,
        page_size: int = 1000,
    ) -> tuple[list[dict[str, Any]], int, bool]:
        """Walk offset pagination until exhausted or ``max_records`` is reached.

        Returns ``(items, total_items_reported_by_mailchimp, truncated)``.
        """
        limit = max_records or self._settings.max_records
        limit = max(1, min(limit, self._settings.max_records))
        page_size = max(1, min(page_size, 1000))

        collected: list[dict[str, Any]] = []
        total = 0
        offset = 0

        while len(collected) < limit:
            page_params = dict(params or {})
            page_params["count"] = min(page_size, limit - len(collected))
            page_params["offset"] = offset

            payload = self.get(path, page_params)
            total = int(payload.get("total_items", total) or 0)
            batch = payload.get(item_key) or []
            if not isinstance(batch, list):
                break
            collected.extend(batch)
            if len(batch) < page_params["count"]:
                break
            offset += len(batch)
            if total and offset >= total:
                break

        truncated = bool(total and len(collected) < total)
        return collected, total, truncated

    @staticmethod
    def _backoff(response: httpx.Response, attempt: int) -> float:
        retry_after = response.headers.get("Retry-After", "")
        if retry_after.strip().isdigit():
            return min(float(retry_after), 30.0)
        return min(2.0 ** attempt, 16.0)

    def _to_error(self, response: httpx.Response) -> MailchimpError:
        title = detail = ""
        errors: list[Mapping[str, Any]] = []
        try:
            body = response.json()
        except ValueError:
            detail = response.text[:500]
        else:
            if isinstance(body, dict):
                title = str(body.get("title", ""))
                detail = str(body.get("detail", ""))
                raw_errors = body.get("errors")
                if isinstance(raw_errors, list):
                    errors = [e for e in raw_errors if isinstance(e, Mapping)]
        return MailchimpError(
            response.status_code,
            title=self._settings.redact(title),
            detail=self._settings.redact(detail),
            errors=errors,
        )


class TransactionalClient:
    """Read-only client for the Transactional (Mandrill) API.

    Mandrill routes are all POST and take the key in the JSON body, so this
    client enforces :data:`TRANSACTIONAL_ALLOWLIST` rather than an HTTP verb.
    """

    BASE_URL = "https://mandrillapp.com/api/1.0"

    def __init__(self, settings: Settings, client: httpx.Client | None = None) -> None:
        if not settings.transactional_api_key:
            raise ValueError(
                "Transactional tools are disabled. Set MAILCHIMP_TRANSACTIONAL_API_KEY "
                "in .env to enable them."
            )
        self._settings = settings
        self._key = settings.transactional_api_key
        self._client = client or httpx.Client(
            base_url=self.BASE_URL,
            timeout=settings.timeout,
            headers={"User-Agent": "mailchimp-mcp (+https://github.com/jimsimoy/mailchimp-mcp)"},
            follow_redirects=False,
        )

    def close(self) -> None:
        self._client.close()

    def call(self, path: str, payload: Mapping[str, Any] | None = None) -> Any:
        if path not in TRANSACTIONAL_ALLOWLIST:
            raise ValueError(
                f"{path} is not in this server's read-only transactional allowlist "
                f"({', '.join(sorted(TRANSACTIONAL_ALLOWLIST))})."
            )
        body = {k: v for k, v in (payload or {}).items() if v is not None}
        body["key"] = self._key
        response = self._client.post(path, json=body)
        if response.status_code >= 400:
            title = detail = ""
            try:
                data = response.json()
            except ValueError:
                detail = response.text[:500]
            else:
                if isinstance(data, dict):
                    title = str(data.get("name", ""))
                    detail = str(data.get("message", ""))
            raise MailchimpError(
                response.status_code,
                title=self._settings.redact(title),
                detail=self._settings.redact(detail),
            )
        return response.json()

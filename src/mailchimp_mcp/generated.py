"""Register one MCP tool per Mailchimp API operation.

Tools are built from the committed :mod:`mailchimp_mcp.operations` table — data,
not code — so what this module exposes can be audited by reading that table.

Only operations permitted by the configured
:class:`~mailchimp_mcp.access.AccessLevel` are registered. A tool above the
level is never advertised to the model at all; if one were reached anyway,
:class:`~mailchimp_mcp.client.MarketingClient` would still refuse the request.
"""

from __future__ import annotations

import inspect
from typing import Any, Callable, Literal, Optional

from mcp.types import ToolAnnotations

from .access import AccessLevel
from .client import MarketingClient
from .operations import OPERATIONS

_PY_TYPES: dict[str, type] = {"str": str, "int": int, "bool": bool, "float": float}

#: Verbs whose tools should be flagged to the client as destructive.
_DESTRUCTIVE = frozenset({"DELETE"})


def _annotation(param: dict[str, Any]) -> Any:
    """Build the type annotation the MCP SDK turns into a JSON schema."""
    enum = param.get("enum")
    base: Any = Literal[tuple(enum)] if enum else _PY_TYPES.get(param.get("type", "str"), str)
    return base if param.get("required") else Optional[base]


def _describe(operation: dict[str, Any]) -> str:
    """Compose the tool description shown to the model."""
    parts: list[str] = []
    summary = operation.get("summary") or ""
    description = operation.get("description") or ""
    if summary:
        parts.append(summary.rstrip(". ") + ".")
    if description and description.rstrip(".") != summary.rstrip("."):
        parts.append(description)

    parts.append(f"[{operation['method']} {operation['path']}]")

    if operation["level"] != AccessLevel.READONLY.value:
        parts.append(f"Requires MAILCHIMP_ACCESS_LEVEL={operation['level']}.")
    if operation["method"] == "DELETE":
        parts.append("This permanently deletes data in Mailchimp.")

    if operation.get("has_body"):
        body_desc = operation.get("body_description") or ""
        required = operation.get("body_required") or []
        hint = "Pass the request payload as `body`."
        if required:
            hint += f" Required: {', '.join(required)}."
        parts.append(f"{hint} {body_desc}".strip())

    for param in operation["path_params"] + operation["query_params"]:
        if param.get("description"):
            parts.append(f"- {param['name']}: {param['description']}")

    return "\n".join(parts)


def _build(operation: dict[str, Any], get_client: Callable[[], MarketingClient]) -> Callable[..., Any]:
    """Create the callable for one operation, with a real signature for the SDK."""
    path_names = [p["name"] for p in operation["path_params"]]
    query_names = [p["name"] for p in operation["query_params"]]

    parameters: list[inspect.Parameter] = []
    # Required first: path parameters, then a required body if the operation needs one.
    for param in operation["path_params"]:
        parameters.append(
            inspect.Parameter(
                param["name"], inspect.Parameter.KEYWORD_ONLY, annotation=_annotation({**param, "required": True})
            )
        )
    if operation.get("has_body"):
        parameters.append(
            inspect.Parameter("body", inspect.Parameter.KEYWORD_ONLY, annotation=dict[str, Any])
        )
    for param in operation["query_params"]:
        parameters.append(
            inspect.Parameter(
                param["name"],
                inspect.Parameter.KEYWORD_ONLY,
                default=param.get("default"),
                annotation=_annotation({**param, "required": False}),
            )
        )

    method = operation["method"]
    template = operation["path"]

    def call(**kwargs: Any) -> Any:
        path = template
        for name in path_names:
            value = kwargs.get(name)
            if value is None or str(value).strip() == "":
                raise ValueError(f"{name} is required for {operation['name']}")
            # Path segments are quoted so an ID can never inject another path segment.
            path = path.replace("{" + name + "}", _quote(str(value)))
        query = {name: kwargs.get(name) for name in query_names if kwargs.get(name) is not None}
        body = kwargs.get("body") if operation.get("has_body") else None
        return get_client().request(method, path, params=query, body=body)

    call.__name__ = operation["name"]
    call.__qualname__ = operation["name"]
    call.__doc__ = _describe(operation)
    call.__signature__ = inspect.Signature(parameters)  # type: ignore[attr-defined]
    call.__annotations__ = {p.name: p.annotation for p in parameters}
    return call


def _quote(value: str) -> str:
    from urllib.parse import quote

    return quote(value, safe="")


def register(
    server: Any,
    settings: Any,
    get_client: Callable[[], MarketingClient],
    reserved: set[str] | None = None,
) -> dict[str, Any]:
    """Register every operation the access level permits. Returns a summary."""
    level = settings.access_level
    groups = settings.tool_groups
    reserved = reserved or set()

    registered: dict[str, int] = {}
    skipped_by_level = 0
    skipped_by_group = 0
    skipped_reserved: list[str] = []

    for operation in OPERATIONS:
        if not level.permits(operation["level"]):
            skipped_by_level += 1
            continue
        if groups and operation["group"] not in groups:
            skipped_by_group += 1
            continue
        if operation["name"] in reserved:
            skipped_reserved.append(operation["name"])
            continue

        read_only = operation["method"] == "GET"
        server.add_tool(
            _build(operation, get_client),
            name=operation["name"],
            description=_describe(operation),
            annotations=ToolAnnotations(
                read_only_hint=read_only,
                destructive_hint=operation["method"] in _DESTRUCTIVE,
                idempotent_hint=operation["method"] in ("GET", "PUT", "DELETE"),
                open_world_hint=True,
            ),
        )
        registered[operation["level"]] = registered.get(operation["level"], 0) + 1

    return {
        "access_level": level.value,
        "registered": sum(registered.values()),
        "registered_by_level": registered,
        "skipped_above_access_level": skipped_by_level,
        "skipped_by_group_filter": skipped_by_group,
        "skipped_name_conflicts": skipped_reserved,
    }

#!/usr/bin/env python3
"""Generate ``src/mailchimp_mcp/operations.py`` from Mailchimp's OpenAPI spec.

The generated module is a plain data table — no code is executed from the spec.
It is committed to the repository so that what the server exposes can be read and
diffed directly, rather than being conjured at import time from a remote document.

Regenerate after a Mailchimp API release:

    python tools/generate_operations.py

Spec: https://api.mailchimp.com/schema/3.0/Swagger.json?expand  (Swagger 2.0)
Docs: https://mailchimp.com/developer/marketing/api/
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path
from typing import Any

SPEC_URL = "https://api.mailchimp.com/schema/3.0/Swagger.json?expand"
OUTPUT = Path(__file__).resolve().parents[1] / "src" / "mailchimp_mcp" / "operations.py"

#: HTTP method -> the access level a caller must hold to invoke it.
METHOD_LEVEL = {
    "get": "READONLY",
    "post": "BASIC",
    "put": "ADMIN",     # Mailchimp's PUTs are upserts: they can overwrite an existing record.
    "patch": "ADMIN",
    "delete": "ADMIN",
}

TYPE_MAP = {"string": "str", "integer": "int", "boolean": "bool", "number": "float", "array": "str"}

_CAMEL_1 = re.compile(r"(.)([A-Z][a-z]+)")
_CAMEL_2 = re.compile(r"([a-z0-9])([A-Z])")


def snake(name: str) -> str:
    out = _CAMEL_1.sub(r"\1_\2", name)
    out = _CAMEL_2.sub(r"\1_\2", out)
    return re.sub(r"_+", "_", out).lower()


def clean(text: Any, limit: int = 400) -> str:
    """Flatten a spec description into a single-line tool description."""
    if not text:
        return ""
    out = re.sub(r"\s+", " ", str(text)).strip()
    # Strip markdown links, keeping the label: they add noise to a tool description.
    out = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", out)
    if len(out) > limit:
        out = out[: limit - 1].rsplit(" ", 1)[0] + "…"
    return out


def resolve(spec: dict, node: Any) -> dict:
    seen = 0
    while isinstance(node, dict) and "$ref" in node and seen < 10:
        node = spec["definitions"][node["$ref"].split("/")[-1]]
        seen += 1
    return node if isinstance(node, dict) else {}


def body_hint(spec: dict, param: dict) -> tuple[list[str], str]:
    """Return (required_field_names, short description) for a body parameter."""
    schema = resolve(spec, param.get("schema") or {})
    required = [str(r) for r in schema.get("required", []) if isinstance(r, str)]
    props = list((schema.get("properties") or {}).keys())
    desc = clean(param.get("description") or schema.get("description") or "", 200)
    if props:
        shown = ", ".join(props[:15]) + ("…" if len(props) > 15 else "")
        desc = (desc + " " if desc else "") + f"Fields: {shown}."
    return required, desc.strip()


def build(spec: dict) -> list[dict]:
    operations: list[dict] = []
    used: dict[str, int] = {}

    for path in sorted(spec["paths"]):
        for method in ("get", "post", "put", "patch", "delete"):
            op = spec["paths"][path].get(method)
            if not op:
                continue

            op_id = op.get("operationId") or f"{method}{path}"
            name = snake(op_id)
            # Guarantee uniqueness without silently dropping an operation.
            if name in used:
                used[name] += 1
                name = f"{name}_{used[name]}"
            else:
                used[name] = 0

            path_params: list[dict] = []
            query_params: list[dict] = []
            body_required: list[str] = []
            body_desc = ""
            has_body = False

            for param in op.get("parameters", []):
                location = param.get("in")
                if location == "body":
                    has_body = True
                    body_required, body_desc = body_hint(spec, param)
                    continue
                if location not in ("path", "query"):
                    continue
                entry = {
                    "name": param["name"],
                    "type": TYPE_MAP.get(param.get("type", "string"), "str"),
                    "required": bool(param.get("required")) or location == "path",
                    "description": clean(param.get("description"), 220),
                }
                enum = param.get("enum") or (param.get("items") or {}).get("enum")
                if enum and all(isinstance(v, str) for v in enum):
                    entry["enum"] = list(enum)
                if param.get("default") is not None and location == "query":
                    entry["default"] = param["default"]
                (path_params if location == "path" else query_params).append(entry)

            summary = clean(op.get("summary"), 120)
            description = clean(op.get("description"), 400)
            tags = op.get("tags") or []

            operations.append(
                {
                    "name": name,
                    "method": method.upper(),
                    "path": path,
                    "level": METHOD_LEVEL[method],
                    "summary": summary,
                    "description": description,
                    "group": snake(tags[0]) if tags else "misc",
                    "path_params": path_params,
                    "query_params": query_params,
                    "has_body": has_body,
                    "body_required": body_required,
                    "body_description": body_desc,
                }
            )

    return operations


HEADER = '''"""Mailchimp Marketing API operation table — GENERATED, do not edit by hand.

Every operation Mailchimp publishes, transcribed from its official OpenAPI
specification. Regenerate with::

    python tools/generate_operations.py

Source spec: https://api.mailchimp.com/schema/3.0/Swagger.json?expand
API reference: https://mailchimp.com/developer/marketing/api/
Spec version: {version}
Generated: {count} operations ({by_level})

This module contains data only. `level` is the access level required to call the
operation: READONLY for GET, BASIC for POST, ADMIN for PUT/PATCH/DELETE.
"""

from __future__ import annotations

from typing import Any

SPEC_VERSION = "{version}"
SPEC_URL = "https://api.mailchimp.com/schema/3.0/Swagger.json?expand"

#: One entry per Mailchimp API operation. See module docstring for provenance.
OPERATIONS: list[dict[str, Any]] = '''


def render(operations: list[dict], version: str) -> str:
    by_level: dict[str, int] = {}
    for op in operations:
        by_level[op["level"]] = by_level.get(op["level"], 0) + 1
    summary = ", ".join(f"{k}: {v}" for k, v in sorted(by_level.items()))

    header = HEADER.format(version=version, count=len(operations), by_level=summary)
    body = json.dumps(operations, indent=4, ensure_ascii=False)
    # json.dumps emits JSON literals; make them Python literals.
    body = re.sub(r"\btrue\b", "True", body)
    body = re.sub(r"\bfalse\b", "False", body)
    body = re.sub(r"\bnull\b", "None", body)

    footer = '''

#: Operation lookup by tool name.
BY_NAME: dict[str, dict[str, Any]] = {op["name"]: op for op in OPERATIONS}

#: Distinct API groups (Mailchimp's own spec tags), for optional filtering.
GROUPS: tuple[str, ...] = tuple(sorted({op["group"] for op in OPERATIONS}))
'''
    return header + body + "\n" + footer


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", help="Path to a local copy of the spec (skips the download)")
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()

    if args.spec:
        spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    else:
        print(f"Downloading {SPEC_URL} …", file=sys.stderr)
        with urllib.request.urlopen(SPEC_URL, timeout=120) as response:  # noqa: S310 - fixed https URL
            spec = json.load(response)

    version = str((spec.get("info") or {}).get("version", "unknown"))
    operations = build(spec)
    args.output.write_text(render(operations, version), encoding="utf-8")

    counts: dict[str, int] = {}
    for op in operations:
        counts[op["level"]] = counts.get(op["level"], 0) + 1
    print(f"Wrote {args.output} — {len(operations)} operations {counts} (spec {version})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# AGENTS.md — Operating Guide for AI Agents

Instructions for an AI agent working **on** this repository or working **through**
the MCP server it provides. Humans, see [README.md](./README.md).

---

## 1. Official API references

This server is a thin, faithful wrapper over Mailchimp's published API. When a
tool's behaviour is unclear, or when extending the server, go to the source
rather than guessing.

| Resource | URL | Use it for |
|---|---|---|
| **OpenAPI spec (authoritative)** | `https://api.mailchimp.com/schema/3.0/Swagger.json?expand` | Exact parameters, enums, response schemas, required body fields. Swagger 2.0, ~10.7 MB. **This is what the code was generated from.** |
| Marketing API reference | https://mailchimp.com/developer/marketing/api/ | Human-readable endpoint docs |
| Marketing API root endpoint | https://mailchimp.com/developer/marketing/api/root/ | The `/` resource and account fields |
| API fundamentals | https://mailchimp.com/developer/marketing/docs/fundamentals/ | Auth, datacenters, rate limits, pagination, `fields`/`exclude_fields` |
| Error glossary | https://mailchimp.com/developer/marketing/docs/errors/ | Interpreting 400/401/403/429 responses |
| Transactional (Mandrill) API | https://mailchimp.com/developer/transactional/api/ | The separate transactional surface |
| Developer portal | https://mailchimp.com/developer/ | Everything else |

> **Warning — the HTML docs do not scrape well.** The parameter tables on
> `mailchimp.com/developer` are rendered client-side. Fetching those pages returns
> prose without the parameter details, and summarising them produces plausible but
> wrong parameter names. **Always use the OpenAPI spec** as the source of truth.

Local copy of the derived data: [`src/mailchimp_mcp/operations.py`](src/mailchimp_mcp/operations.py)
(spec version recorded in `SPEC_VERSION`).

---

## 2. Initializing the server

### Install

```bash
git clone git@github.com:jimsimoy/mailchimp-mcp.git
cd mailchimp-mcp
python3 -m venv .venv && ./.venv/bin/pip install -e ".[dev]"
cp .env.example .env
```

### Configure

Edit `.env`. Only `MAILCHIMP_API_KEY` is required; the datacenter is read from
the key's `-usXX` suffix.

```bash
MAILCHIMP_API_KEY=abc123...def-us13
MAILCHIMP_ACCESS_LEVEL=READONLY          # READONLY | BASIC | ADMIN — see §4
MAILCHIMP_DEFAULT_LIST_ID=abc123def4     # optional, saves passing list_id everywhere
```

### Verify before wiring up a client

```bash
./.venv/bin/python -m pytest -q          # 105 tests, no credentials or network needed
./.venv/bin/python -m mailchimp_mcp      # starts the stdio server; prints the tool count to stderr
```

The startup banner on stderr states the active access level and how many tools
were registered vs. withheld. Read it — it is the fastest way to confirm the
server is in the mode you expect.

### Register with an MCP client

```json
{
  "mcpServers": {
    "mailchimp": {
      "command": "/absolute/path/to/mailchimp-mcp/.venv/bin/python",
      "args": ["-m", "mailchimp_mcp"],
      "env": {
        "MAILCHIMP_API_KEY": "abc123...def-us13",
        "MAILCHIMP_ACCESS_LEVEL": "READONLY"
      }
    }
  }
}
```

---

## 3. Using the tools

### Start here

Call **`list_audiences`** first. Almost every other tool needs a `list_id`, and
guessing one produces a confusing 404 rather than a helpful error.

### Two families of tools

**Curated tools** (24) are hand-written, return compact summarised output, and
resolve `MAILCHIMP_DEFAULT_LIST_ID` when `list_id` is omitted. Prefer these —
they cost fewer tokens and label statuses in the UI's vocabulary.

**Generated tools** (up to 298) are one per Mailchimp API operation, named after
its `operationId` — `get_lists_id_members`, `post_lists_id_members`,
`delete_lists_id_members_id`. They return raw API responses and always require
every path parameter explicitly. Use them when no curated tool covers what you
need.

### Vocabulary you must get right

Mailchimp's UI and API disagree on names. The one that causes real mistakes:

| UI label | API `status` |
|---|---|
| Subscribed | `subscribed` |
| **Non-subscribed** | **`transactional`** |
| Unsubscribed | `unsubscribed` |
| Cleaned | `cleaned` |
| Pending | `pending` |
| Archived | `archived` |

If a user asks about "non-subscribed" contacts, they mean `status=transactional`.
Never pass `"non-subscribed"` as a status value; it is not valid.

### The thing agents most often get wrong

**Mailchimp stores no subscribe-status history.** There is no endpoint that
returns "this contact was `transactional` on 1 Aug and `subscribed` on 15 Aug."
`last_changed` tells you the record was touched — not what changed, and not what
it was before.

So when asked "who moved from non-subscribed to subscribed?":

- For a **past** window → `find_newly_subscribed`. It infers the transition from
  `timestamp_opt` vs `timestamp_signup` and returns a `confidence` per row.
  **Report that it is an inference.** Do not present it as a status log.
- For **ongoing** tracking → `snapshot_member_statuses` now, again later, then
  `diff_member_status_snapshots`. This is exact. Recommend it whenever the user
  will want to ask the question again.

To corroborate an individual contact, call `get_member_activity` and look for
signup activity types (`generic_signup`, `website_signup`, `landing_page_signup`,
`ecommerce_signup`). For an aggregate cross-check, `get_audience_growth_history`
shows `transactional` and `subscribed` counts per month.

### Working efficiently

- Use `max_records` deliberately. `list_members` defaults to 200; a large
  audience will otherwise burn tokens and time.
- Prefer server-side filters (`status`, `since_last_changed`, `since_timestamp_opt`)
  over fetching everything and filtering yourself.
- Mailchimp allows **10 simultaneous connections** and times out at 120s. This
  server paginates sequentially and retries GETs on 429 with backoff. Do not
  parallelise tool calls against one account.
- `count` maxes at 1000 per page on every paginated endpoint.

---

## 4. Access levels — read before writing anything

`MAILCHIMP_ACCESS_LEVEL` controls what exists:

| Level | HTTP methods | Tools registered |
|---|---|---|
| `READONLY` (default) | GET | 173 |
| `BASIC` | GET, POST | 248 |
| `ADMIN` | GET, POST, PUT, PATCH, DELETE | 322 |

**If you cannot see a write tool, the operator deliberately did not grant that
access.** Say so plainly and stop. Do not:

- suggest editing `.env` to raise the level as a way to complete the task,
- look for another tool that achieves the write indirectly,
- or retry hoping for a different result.

Reporting "this needs BASIC access, which is not enabled" is the correct,
complete answer.

Two independent gates enforce this: tools above the level are never registered,
and `MarketingClient.request()` refuses the method regardless. An `AccessDenied`
message names both the required and the active level.

### If you do hold write access

- **PUT is an upsert.** `put_lists_id_members_id` overwrites an existing contact,
  which is why it needs ADMIN rather than BASIC.
- **DELETE is permanent.** `delete_lists_id_members_id_actions_delete_permanent`
  cannot be undone and prevents the address from ever being re-added.
- **Confirm before writing.** State the exact operation, the audience, and the
  affected contacts, then wait. Writes are not retried on failure, so a timeout
  leaves genuinely ambiguous state — say so rather than re-running blind.
- Prefer a `snapshot_member_statuses` call before a bulk change, so the effect
  is measurable afterwards.

---

## 5. Working on this repository

### Layout

```
src/mailchimp_mcp/
  server.py       # 24 curated tools, MCP wiring, error translation
  generated.py    # builds one tool per operation, filtered by access level
  operations.py   # GENERATED data table — do not hand-edit
  client.py       # HTTP clients; access gate lives in MarketingClient.request()
  access.py       # AccessLevel model
  analysis.py     # status inference, snapshots, diffing
  config.py       # env loading, key parsing, redaction
tools/generate_operations.py   # regenerates operations.py from the spec
```

### Regenerating after a Mailchimp API release

```bash
python tools/generate_operations.py     # downloads the spec, rewrites operations.py
./.venv/bin/python -m pytest -q
git diff --stat src/mailchimp_mcp/operations.py
```

Review that diff. New ADMIN operations mean new destructive tools; they should
be a deliberate, noticed change, not a silent one.

### House rules

- **`operations.py` is generated.** Fix the generator, never the output.
- **Never weaken the access gates.** Both must stay: registration filtering in
  `generated.register()` and method checking in `MarketingClient.request()`.
- **Never log or echo the API key.** `Settings.redact()` exists because
  Mailchimp's own 401 body contains the key. Route new error paths through it.
- **Never commit `.env` or `snapshots/`.** Snapshots contain subscriber email
  addresses. Both are gitignored; keep it that way.
- **Tests must not need credentials or network.** Use `httpx.MockTransport`.
- Add curated tools to `CURATED_TOOL_NAMES` in `server.py`; a test enforces it
  and catches collisions with generated names.

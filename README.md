# Mailchimp MCP — Full Mailchimp Marketing API for AI Clients

<div align="center">

<img src="https://img.shields.io/badge/python-3.10%2B-blue.svg?style=flat-square" alt="Python 3.10+">
<a href="https://github.com/jimsimoy/mailchimp-mcp/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License: MIT"></a>
<a href="https://modelcontextprotocol.io"><img src="https://img.shields.io/badge/MCP-compatible-green.svg?style=flat-square" alt="MCP Compatible"></a>
<img src="https://img.shields.io/badge/tools-322-brightgreen.svg?style=flat-square" alt="322 Tools">
<img src="https://img.shields.io/badge/default-read--only-success.svg?style=flat-square" alt="Read-only by default">
<img src="https://img.shields.io/badge/dependencies-3-lightgrey.svg?style=flat-square" alt="3 runtime dependencies">

**Every Mailchimp Marketing API operation as an MCP tool — 322 in total, gated behind three access levels, read-only by default — plus curated tools for audience, member and campaign work and for subscribe-status change analysis.**

For Claude Desktop, Claude Code, and any MCP client.

by [Jan Ivan Simoy](https://github.com/jimsimoy)

</div>

---

> **Unofficial.** This is an independent, community-built project — not affiliated with, endorsed by, or sponsored by Mailchimp.

## What is this?

Mailchimp MCP is a [Model Context Protocol](https://modelcontextprotocol.io) server that gives AI assistants structured access to the [Mailchimp Marketing API](https://mailchimp.com/developer/marketing/api/) — audiences, contacts, segments and tags, campaigns, reports, automations, ecommerce stores, templates, landing pages and more.

Two things make it different from a generic API wrapper:

**It is read-only until you decide otherwise.** One environment variable, `MAILCHIMP_ACCESS_LEVEL`, decides whether this server can create, update or delete anything. The default is `READONLY`, and tools above the configured level are never registered — the model is not shown that they exist. See [Access Levels](#access-levels).

**It answers the question Mailchimp's own reporting cannot:** who changed subscribe status, and when? Mailchimp stores no status history. This server closes that gap two ways — an inference from the timestamps the API does expose, and exact snapshot-and-compare tracking. See [Tracking subscribe-status changes](#tracking-subscribe-status-changes).

Working with an AI agent on this? Point it at [AGENTS.md](./AGENTS.md).

**Supported platform:** any MCP client on macOS, Linux, or Windows with Python 3.10+.

---

## Access Levels

`MAILCHIMP_ACCESS_LEVEL` in `.env` controls what this server can do.

| Level | HTTP methods | Can it change your data? | Tools |
|---|---|---|---|
| **`READONLY`** *(default)* | `GET` | **No.** Nothing in Mailchimp can be modified. | 173 |
| **`BASIC`** | `GET`, `POST` | **Creates only.** Adds contacts, campaigns, segments, notes, stores and other new records. | 248 |
| **`ADMIN`** | `GET`, `POST`, `PUT`, `PATCH`, `DELETE` | **Yes, including permanent deletion.** | 322 |

`PUT` sits at `ADMIN` rather than `BASIC` on purpose: Mailchimp's `PUT` routes are upserts, so `put_lists_id_members_id` will silently overwrite an existing contact's record. That is update behaviour, so it needs update-level access.

### How it is enforced

Two independent gates, so a bug in one does not defeat the other:

1. **Registration.** `generated.register()` skips any operation above the configured level. At `READONLY` the model is never told a `delete_*` tool exists.
2. **Dispatch.** `MarketingClient.request()` checks the method against the level before building a request. A write at `READONLY` raises `AccessDenied` and **no HTTP call is made** — there is a test for exactly that.

### ⚠️ Disclaimer — read before raising the level

> **Setting `MAILCHIMP_ACCESS_LEVEL` to `BASIC` or `ADMIN` allows an AI model to change data in your live Mailchimp account.**
>
> At **`ADMIN`**, that includes updating and **permanently deleting** contacts, audiences, campaigns, templates, stores and automations. Mailchimp's permanent-delete operations **cannot be undone**, and a permanently deleted contact can never be re-added to that audience. This server provides **no undo, no staging mode, and no backup**.
>
> AI models make mistakes. They misread instructions, act on ambiguous requests, and can be influenced by content they read. A model with `ADMIN` access to your Mailchimp account is capable of destroying your audience.
>
> **If you raise this setting above `READONLY`, you do so entirely at your own risk and you are solely responsible for any resulting data loss, corruption, unintended sends, or compliance consequences.** The author and contributors accept no liability. This software is provided "as is", without warranty of any kind, as set out in the [MIT License](./LICENSE).
>
> **Recommended:** leave it at `READONLY`. If you need writes, raise it only for the session that needs them, use an API key belonging to a least-privileged Mailchimp user, and take a `snapshot_member_statuses` first.

---

## Tools

**24 curated tools** — hand-written, compact output, resolve a default audience, and label statuses in the UI's vocabulary. Prefer these.

| Category | Tools | What you can do |
|---|---|---|
| **Account** | 2 | Verify credentials, read account details and plan |
| **Audiences** | 4 | List audiences, read settings and stats, monthly growth history, daily activity |
| **Members** | 5 | List and filter contacts, read one contact, their activity feed and tags, search the account |
| **Segments & fields** | 3 | List segments and tags, list a segment's members, list merge fields |
| **Campaigns & reports** | 4 | List campaigns, read reports, list reports account-wide, list per-campaign unsubscribes |
| **Status changes** | 4 | Find who became subscribed in a window, snapshot audiences, diff for exact transitions |
| **Transactional** | 2 | Optional, off by default — transactional account info and message search |

<details>
<summary>Full curated tool reference</summary>

| Tool | Description |
|---|---|
| `ping` | Check that credentials work and the API is reachable |
| `get_account` | Account name, plan, contact details, total subscribers |
| `list_audiences` | Audiences with IDs and member statistics — **start here** |
| `get_audience` | One audience's full settings and statistics |
| `get_audience_growth_history` | Month-by-month subscribed / unsubscribed / cleaned / transactional / imports |
| `get_audience_activity` | Daily sends, opens, clicks, bounces, subs and unsubs |
| `list_members` | Contacts with server-side filters (status, opt-in window, last-changed window, VIP), auto-paginated |
| `get_member` | One contact's full record, by email, subscriber hash or contact ID |
| `get_member_activity` | Activity feed — signups, opens, clicks, unsubs, orders, notes, custom events |
| `get_member_tags` | Tags applied to one contact |
| `search_members` | Search contacts across the account by email or name |
| `list_segments` | Segments and tags with member counts |
| `list_segment_members` | Contacts in one segment or tag |
| `list_merge_fields` | Custom contact fields and their merge tags |
| `list_campaigns` | Campaigns, filterable by audience, status and send window |
| `get_campaign_report` | Opens, clicks, bounces, unsubs, ecommerce for one campaign |
| `list_campaign_reports` | Report summaries account-wide, newest first |
| `get_campaign_unsubscribes` | Who unsubscribed from a campaign, with reasons |
| `find_newly_subscribed` | Contacts that became Subscribed in a window, split into upgrades vs. new signups |
| `snapshot_member_statuses` | Record every contact's current status locally for exact tracking |
| `list_status_snapshots` | List snapshots stored locally |
| `diff_member_status_snapshots` | Exact status transitions between two snapshots |
| `transactional_account_info` | Transactional (Mandrill) account info and send stats |
| `transactional_search_messages` | Search transactional messages from the last 30 days |

</details>

**Up to 298 generated tools** — one per Mailchimp API operation, named after its `operationId`: `get_lists_id_members`, `post_lists_id_members`, `patch_lists_id_members_id`, `delete_lists_id_members_id`. These cover everything the curated tools do not, and return raw API responses.

| Level | Generated tools available |
|---|---|
| `READONLY` | 149 (all `GET`) |
| `BASIC` | 224 (`GET` + 75 `POST`) |
| `ADMIN` | 298 (`GET` + `POST` + 7 `PUT` + 32 `PATCH` + 35 `DELETE`) |

They are built from [`src/mailchimp_mcp/operations.py`](src/mailchimp_mcp/operations.py), a committed data table generated from Mailchimp's official OpenAPI specification. Read that file to see exactly what this server can reach.

> **On context size:** 173 tools is a lot of schema for an MCP client to hold. If your client struggles, set `MAILCHIMP_TOOL_GROUPS` to a comma-separated subset of API groups (`lists,campaigns,reports`) to register only those. The curated tools are always registered.

---

## Requirements

| Requirement | Version |
|---|---|
| Python | 3.10 or later |
| A Mailchimp account | any plan with API access |
| Marketing API key | created in your Mailchimp account settings |

Runtime dependencies are deliberately minimal — `mcp`, `httpx` and `python-dotenv`. This server calls the Mailchimp REST API directly rather than pulling in a vendor SDK, so the whole request path is a few hundred readable lines you can audit yourself.

---

## Authentication

Mailchimp Marketing API keys look like `abc123...def-us13`. The suffix after the last dash is your **datacenter**, and it decides which host the server talks to (`https://us13.api.mailchimp.com/3.0`). This server reads it from the key automatically.

1. In Mailchimp, go to **Account & billing → Extras → API keys** ([direct link](https://admin.mailchimp.com/account/api/)).
2. Create a key. An API key inherits the permissions of the user who created it, so **create it under the least-privileged user account you can**.
3. Copy the key into `.env`.

If you authenticate with an OAuth token instead, it carries no `-usX` suffix; set `MAILCHIMP_DC` explicitly in that case.

The Transactional (Mandrill) tools use a **separate** key and stay disabled unless `MAILCHIMP_TRANSACTIONAL_API_KEY` is set.

---

## Installation

```bash
git clone git@github.com:jimsimoy/mailchimp-mcp.git
cd mailchimp-mcp
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
cp .env.example .env    # then fill in MAILCHIMP_API_KEY
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
git clone git@github.com:jimsimoy/mailchimp-mcp.git
cd mailchimp-mcp
uv sync
cp .env.example .env
```

Verify before wiring up a client:

```bash
python -m mailchimp_mcp
```

It prints the active access level and tool count to stderr, then waits for a client on stdio. Ctrl-C to exit.

---

## Configuration

| Variable | Required | Default | Purpose |
|---|---|---|---|
| `MAILCHIMP_API_KEY` | yes | — | Marketing API key, `<key>-<dc>` |
| `MAILCHIMP_ACCESS_LEVEL` | no | `READONLY` | `READONLY` / `BASIC` / `ADMIN` — see [Access Levels](#access-levels) |
| `MAILCHIMP_TOOL_GROUPS` | no | all | Comma-separated API groups to register (e.g. `lists,campaigns`) |
| `MAILCHIMP_DC` | no | from key suffix | Datacenter override, for OAuth tokens |
| `MAILCHIMP_DEFAULT_LIST_ID` | no | — | Audience used when a curated tool's `list_id` is omitted |
| `MAILCHIMP_TRANSACTIONAL_API_KEY` | no | — | Enables the two transactional tools |
| `MAILCHIMP_SNAPSHOT_DIR` | no | `./snapshots` | Where status snapshots are written |
| `MAILCHIMP_TIMEOUT` | no | `30` | Per-request timeout in seconds |
| `MAILCHIMP_MAX_RECORDS` | no | `5000` | Hard cap on records any one tool will pull |

---

## Client Setup

```json
{
  "mcpServers": {
    "mailchimp": {
      "command": "/path/to/mailchimp-mcp/.venv/bin/python",
      "args": ["-m", "mailchimp_mcp"],
      "env": {
        "MAILCHIMP_API_KEY": "your-key-us13",
        "MAILCHIMP_ACCESS_LEVEL": "READONLY",
        "MAILCHIMP_DEFAULT_LIST_ID": "abc123def4"
      }
    }
  }
}
```

With `uv`:

```json
{
  "mcpServers": {
    "mailchimp": {
      "command": "uv",
      "args": ["--directory", "/path/to/mailchimp-mcp", "run", "mailchimp-mcp"],
      "env": {
        "MAILCHIMP_API_KEY": "your-key-us13",
        "MAILCHIMP_ACCESS_LEVEL": "READONLY"
      }
    }
  }
}
```

Restart your MCP client after saving.

---

## Tracking subscribe-status changes

### The vocabulary problem

Mailchimp's web UI and its API use different words for the same thing. The one that trips everyone up:

| UI label | API `status` |
|---|---|
| Subscribed | `subscribed` |
| **Non-subscribed** | **`transactional`** |
| Unsubscribed | `unsubscribed` |
| Cleaned | `cleaned` |
| Pending | `pending` |
| Archived | `archived` |

So "contacts that moved from Non-subscribed to Subscribed" means `transactional` → `subscribed`. Curated tools report both the raw status and its UI label so you never have to translate.

### The history problem

**Mailchimp does not store status history.** No endpoint returns "this contact was `transactional` on 1 August and `subscribed` on 15 August." You can read the current status, and `last_changed` tells you the record was touched — but not what changed, or what it was before.

This server gives you both honest answers.

### Retroactively: `find_newly_subscribed`

For a window that has already passed, this infers the transition from the timestamps Mailchimp *does* expose. It fetches contacts who are `subscribed` now and whose record changed inside your window, then compares `timestamp_opt` (when they opted in) against `timestamp_signup` (when the contact first appeared):

| Verdict | Meaning | Confidence |
|---|---|---|
| `upgraded_to_subscribed` | Contact existed before the window but only opted in during it — the shape a Non-subscribed contact takes after being switched to Subscribed | high, or medium when there is no signup timestamp at all |
| `new_subscriber` | Contact first appeared during the window — a fresh signup, not a status change | high |
| `other_change` | Record changed but the opt-in did not — a tag, a merge field, an email client update | high |

```
Find contacts in my main audience that became subscribed since 2026-08-01,
and show only the ones that were previously non-subscribed
```

Every row carries its own confidence and reasoning. To confirm an individual contact, follow up with `get_member_activity` — the signup activity types (`generic_signup`, `website_signup`, `landing_page_signup`, `ecommerce_signup`) show *how* they came in. `get_audience_growth_history` is a good aggregate cross-check.

### Going forward: snapshot and diff

The only *certain* method. Record the audience now, record it again later, compare:

```
Take a status snapshot of my main audience called "sept-start"
```

...then after the period you care about:

```
Take a snapshot called "oct-start", then diff sept-start against oct-start
```

`diff_member_status_snapshots` defaults to exactly the `transactional` → `subscribed` question, and accepts any other pair. Contacts added and removed between snapshots are reported separately, so a new contact is never miscounted as a transition.

Snapshots are plain JSON under `MAILCHIMP_SNAPSHOT_DIR`, written `0600` because they contain subscriber email addresses. The directory is gitignored.

---

## Usage Examples

**Get oriented**

```
List my Mailchimp audiences, then show the growth history for the largest one
```

**Audit non-subscribed contacts**

```
How many contacts in audience abc123def4 have status transactional, and what
tags do they carry?
```

**Find recent upgrades**

```
Which contacts became subscribed between 2026-08-01 and 2026-09-01, and which
of those were existing non-subscribed contacts rather than new signups?
```

**Investigate one contact**

```
Show me person@example.com's record and full activity feed
```

**Campaign performance**

```
List campaigns sent since 2026-07-01 with their open and click rates, then show
who unsubscribed from the worst performer
```

---

## Security

This project is meant to be read before it is run. The design notes that matter:

- **Read-only by default, enforced twice.** At `READONLY` — the default — the only HTTP method that can leave this process is `GET`. Write tools are not registered, *and* `MarketingClient.request()` refuses the method independently. Tests cover both gates, including that a denied request never reaches the network.
- **The tool surface is a data table, not magic.** Every generated tool comes from [`operations.py`](src/mailchimp_mcp/operations.py), transcribed from Mailchimp's OpenAPI spec by a committed script ([`tools/generate_operations.py`](tools/generate_operations.py)). Nothing is fetched or executed at import time. You can read the table to see the entire reachable surface.
- **The transactional surface is allowlisted.** Mandrill's protocol is POST-only, so it cannot be constrained by HTTP verb. Only four read methods are permitted (`users/ping2`, `users/info`, `messages/search`, `messages/info`); anything else — sending included — raises before a request is made. The surface stays disabled without a separate key.
- **Requests cannot leave Mailchimp.** Endpoint paths are validated against a strict pattern, path parameters are percent-encoded so an ID cannot inject extra path segments, and redirects are not followed.
- **Writes are never retried.** Only `GET` is replayed on 429/5xx. Retrying a `POST` could duplicate a write whose first attempt actually landed.
- **Credentials are environment-only.** `.env`, `.env.*` (except `.env.example`), `*.pem`, `*.key` and `token.json` are gitignored. The key is never logged, and it is stripped from every error message — including Mailchimp's own 401 body, which echoes it back.
- **Snapshots are treated as PII.** They hold subscriber email addresses, so they are written `0600` and `snapshots/` is gitignored. Snapshot and audience names are validated, so a crafted name cannot write outside the snapshot directory.
- **Three runtime dependencies, no vendor SDK.** `mcp`, `httpx`, `python-dotenv`.
- **No telemetry.** This server makes no network call other than the Mailchimp API request a tool asks for.

Your API key still carries the permissions of the Mailchimp user who created it. Create it under the least-privileged user available, and revoke it in **Account & billing → Extras → API keys** if it is ever exposed.

---

## Project Structure

```
src/mailchimp_mcp/
  server.py       # MCP wiring, the 24 curated tools, error translation
  generated.py    # builds one tool per API operation, filtered by access level
  operations.py   # GENERATED data table of all 298 operations — do not hand-edit
  client.py       # HTTP clients; the access gate lives in MarketingClient.request()
  access.py       # AccessLevel model and enforcement helper
  analysis.py     # Status-change inference, snapshots and diffing
  config.py       # Environment loading, key parsing, datacenter resolution, redaction
tools/
  generate_operations.py   # regenerates operations.py from the official spec
tests/            # 105 tests against a mocked API — no credentials, no network
```

The server communicates over stdio using JSON-RPC 2.0, the standard MCP transport.

---

## API Reference

The tool surface is generated from Mailchimp's own OpenAPI specification, not transcribed from documentation pages. Use these when debugging or extending:

| Resource | URL |
|---|---|
| **OpenAPI spec (authoritative)** | `https://api.mailchimp.com/schema/3.0/Swagger.json?expand` |
| Marketing API reference | https://mailchimp.com/developer/marketing/api/ |
| API root endpoint | https://mailchimp.com/developer/marketing/api/root/ |
| Fundamentals (auth, rate limits, pagination) | https://mailchimp.com/developer/marketing/docs/fundamentals/ |
| Error glossary | https://mailchimp.com/developer/marketing/docs/errors/ |
| Transactional (Mandrill) API | https://mailchimp.com/developer/transactional/api/ |
| Developer portal | https://mailchimp.com/developer/ |

Note that the parameter tables on `mailchimp.com/developer` are rendered client-side and do not scrape reliably — the OpenAPI spec is the source of truth.

To pick up a new Mailchimp API release:

```bash
python tools/generate_operations.py
pytest
git diff --stat src/mailchimp_mcp/operations.py
```

Review that diff before committing. New `ADMIN` operations mean new destructive tools.

---

## Development

```bash
pip install -e ".[dev]"
pytest
```

The test suite runs entirely against a mocked HTTP transport, so it needs no Mailchimp credentials and makes no network calls.

---

## A note on testing

The endpoints, query parameters, status enums and response fields were taken from Mailchimp's official OpenAPI specification (Marketing API v3.0.91, 298 operations), so parameter names and allowed values match the API exactly.

Covered by unit tests against a mocked API: credential parsing, datacenter resolution, key redaction, pagination, 429 retry and backoff, path validation and percent-encoding, the transactional allowlist, both access-level gates at every level, generated-tool dispatch, status classification and snapshot diffing.

---

## License

[MIT](./LICENSE) — free to use, modify, and distribute. Provided "as is", without warranty of any kind. See the [disclaimer](#️-disclaimer--read-before-raising-the-level) above regarding write access.

---

<div align="center">

[Report a Bug](https://github.com/jimsimoy/mailchimp-mcp/issues) · [Request a Feature](https://github.com/jimsimoy/mailchimp-mcp/issues)

</div>

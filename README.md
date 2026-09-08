# Mailchimp MCP — Read-Only Mailchimp Marketing Data for AI Clients

<div align="center">

<img src="https://img.shields.io/badge/python-3.10%2B-blue.svg?style=flat-square" alt="Python 3.10+">
<a href="https://github.com/jimsimoy/mailchimp-mcp/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License: MIT"></a>
<a href="https://modelcontextprotocol.io"><img src="https://img.shields.io/badge/MCP-compatible-green.svg?style=flat-square" alt="MCP Compatible"></a>
<img src="https://img.shields.io/badge/tools-24-brightgreen.svg?style=flat-square" alt="24 Tools">
<img src="https://img.shields.io/badge/access-read--only-success.svg?style=flat-square" alt="Read-only">
<img src="https://img.shields.io/badge/dependencies-3-lightgrey.svg?style=flat-square" alt="3 runtime dependencies">

**24 read-only tools for the Mailchimp Marketing API — audiences, members, segments, campaigns, reports, and subscribe-status change analysis — for Claude Desktop, Claude Code, and any MCP client.**

by [Jan Ivan Simoy](https://github.com/jimsimoy)

</div>

---

## What is this?

Mailchimp MCP is a [Model Context Protocol](https://modelcontextprotocol.io) server that gives AI assistants structured, read-only access to the [Mailchimp Marketing API](https://mailchimp.com/developer/marketing/api/) — your audiences, contacts and their statuses, segments and tags, campaigns, and campaign reports.

It is built for the question that Mailchimp's own reporting answers poorly: **who changed subscribe status, and when?** Mailchimp will tell you a contact's status *now* and when their record last changed, but it stores no status *history*. This server closes that gap two ways — an inference from the timestamps the API does expose, and exact snapshot-and-compare tracking. See [Tracking subscribe-status changes](#tracking-subscribe-status-changes).

**It never writes to your Mailchimp account.** There is no tool here that adds, updates, tags, unsubscribes or deletes a contact, and no tool that creates or sends a campaign. That is enforced in code, not just by convention — see [Security](#security).

**Supported platform:** any MCP client on macOS, Linux, or Windows with Python 3.10+.

---

## Tools

| Category | Tools | What you can do |
|---|---|---|
| **Account** | 2 | Verify credentials, read account details and plan |
| **Audiences** | 4 | List audiences, read one audience's settings and stats, monthly growth history, daily activity |
| **Members** | 5 | List and filter contacts, read one contact, their activity feed and tags, search across the account |
| **Segments & fields** | 3 | List segments and tags, list a segment's members, list merge fields |
| **Campaigns & reports** | 4 | List campaigns, read campaign reports, list reports across the account, list per-campaign unsubscribes |
| **Status changes** | 4 | Find who became subscribed in a window, take audience snapshots, and diff them for exact transitions |
| **Transactional** | 2 | Optional, off by default — transactional account info and message search |

<details>
<summary>Full tool reference</summary>

### Account

| Tool | Description |
|---|---|
| `ping` | Check that the configured credentials work and the API is reachable |
| `get_account` | Account name, plan, contact details and total subscribers |

### Audiences

| Tool | Description |
|---|---|
| `list_audiences` | List audiences (lists) with their IDs and member statistics — start here |
| `get_audience` | One audience's full settings and statistics |
| `get_audience_growth_history` | Month-by-month growth: subscribed, unsubscribed, cleaned, transactional, imports |
| `get_audience_activity` | Daily sends, opens, clicks, bounces, subs and unsubs |

### Members

| Tool | Description |
|---|---|
| `list_members` | List contacts with Mailchimp's server-side filters (status, opt-in window, last-changed window, VIP), auto-paginated |
| `get_member` | One contact's full record, by email address, subscriber hash or contact ID |
| `get_member_activity` | A contact's activity feed — signups, opens, clicks, unsubs, orders, notes, custom events |
| `get_member_tags` | The tags applied to one contact |
| `search_members` | Search contacts across the account by email or name |

### Segments & fields

| Tool | Description |
|---|---|
| `list_segments` | An audience's segments and tags, with member counts |
| `list_segment_members` | The contacts in one segment or tag |
| `list_merge_fields` | An audience's custom contact fields and their merge tags |

### Campaigns & reports

| Tool | Description |
|---|---|
| `list_campaigns` | Campaigns, filterable by audience, status and send window |
| `get_campaign_report` | One campaign's report — opens, clicks, bounces, unsubs, ecommerce |
| `list_campaign_reports` | Report summaries across the account, newest sends first |
| `get_campaign_unsubscribes` | Who unsubscribed from a campaign, with their stated reasons |

### Status changes

| Tool | Description |
|---|---|
| `find_newly_subscribed` | Contacts that became Subscribed in a date window, split into upgrades from Non-subscribed vs. brand-new signups |
| `snapshot_member_statuses` | Record every contact's current status to a local file for exact tracking |
| `list_status_snapshots` | List the snapshots stored locally |
| `diff_member_status_snapshots` | Exact status transitions between two snapshots |

### Transactional (optional)

| Tool | Description |
|---|---|
| `transactional_account_info` | Transactional (Mandrill) account info and recent send stats |
| `transactional_search_messages` | Search transactional messages sent in the last 30 days |

</details>

---

## Requirements

| Requirement | Version |
|---|---|
| Python | 3.10 or later |
| A Mailchimp account | any plan with API access |
| Marketing API key | created in your Mailchimp account settings |

Runtime dependencies are deliberately minimal — `mcp`, `httpx` and `python-dotenv`. This server calls the Mailchimp REST API directly over HTTP rather than pulling in a vendor SDK, so the whole request path is a few hundred readable lines you can audit yourself.

---

## Authentication

Mailchimp Marketing API keys look like `abc123...def-us13`. The suffix after the last dash is your **datacenter**, and it decides which host the server talks to (`https://us13.api.mailchimp.com/3.0`). This server reads it from the key automatically.

1. In Mailchimp, go to **Account & billing → Extras → API keys** ([direct link](https://admin.mailchimp.com/account/api/)).
2. Create a key. An API key inherits the permissions of the user who created it, so **create it under the least-privileged user account you can** — this server only ever reads.
3. Copy the key into `.env` (see [Installation](#installation)).

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

Verify the credentials before wiring up a client:

```bash
python -m mailchimp_mcp   # starts the stdio server; Ctrl-C to exit
```

---

## Configuration

Every setting is an environment variable, read from `.env` or from your MCP client's `env` block. Only the first is required.

| Variable | Required | Default | Purpose |
|---|---|---|---|
| `MAILCHIMP_API_KEY` | yes | — | Marketing API key, `<key>-<dc>` |
| `MAILCHIMP_DC` | no | from key suffix | Datacenter override, for OAuth tokens |
| `MAILCHIMP_DEFAULT_LIST_ID` | no | — | Audience used when a tool's `list_id` is omitted |
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
      "env": { "MAILCHIMP_API_KEY": "your-key-us13" }
    }
  }
}
```

Restart your MCP client after saving. The 24 tools appear automatically.

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

So "contacts that moved from Non-subscribed to Subscribed" means `transactional` → `subscribed`. Every tool here reports both the raw status and its UI label so you never have to translate.

### The history problem

**Mailchimp does not store status history.** No endpoint returns "this contact was `transactional` on 1 August and `subscribed` on 15 August." You can read the current status, and `last_changed` tells you the record was touched — but not what changed or what it was before.

This server gives you both honest answers to that.

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

Every row carries its own `confidence` and the reasoning behind it. To confirm an individual contact, follow up with `get_member_activity` — the signup activity types (`generic_signup`, `website_signup`, `landing_page_signup`, `ecommerce_signup`) show *how* they came in. `get_audience_growth_history` is a good aggregate cross-check: a real shift shows up as the `transactional` column falling while `subscribed` rises.

### Going forward: snapshot and diff

The only *certain* method. Record the audience now, record it again later, compare:

```
Take a status snapshot of my main audience called "sept-start"
```

...then after the period you care about:

```
Take a snapshot called "oct-start", then diff sept-start against oct-start
```

`diff_member_status_snapshots` defaults to exactly the `transactional` → `subscribed` question, and accepts any other pair. It reports contacts added and removed between snapshots separately, so a new contact is never miscounted as a transition.

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

- **Read-only, enforced in code.** `MarketingClient` implements exactly one HTTP method — `get`. There is no `post`, `put`, `patch` or `delete` to call, so no tool can mutate your audience even by mistake. A test asserts those methods do not exist.
- **The transactional surface is allowlisted.** Mandrill's protocol is POST-only, so it cannot be constrained by HTTP verb. Instead, only four read methods are permitted (`users/ping2`, `users/info`, `messages/search`, `messages/info`); anything else — sending included — raises before a request is made. The whole surface stays disabled unless you set a transactional key.
- **Requests cannot leave Mailchimp.** Endpoint paths are validated against a strict pattern and redirects are not followed, so a malformed argument cannot be turned into a request to another host.
- **Credentials are environment-only.** `MAILCHIMP_API_KEY` and `MAILCHIMP_TRANSACTIONAL_API_KEY` are read from the environment or `.env`. `.env`, `.env.*` (except `.env.example`), `*.pem`, `*.key` and `token.json` are gitignored. The key is never logged, and it is stripped from every error message this server produces — including Mailchimp's own error bodies, which sometimes echo it back.
- **Snapshots are treated as PII.** They hold subscriber email addresses, so they are written `0600` and `snapshots/` is gitignored. Snapshot and audience names are validated, so a crafted name cannot write outside the snapshot directory.
- **Three runtime dependencies, no vendor SDK.** `mcp`, `httpx`, `python-dotenv`. The Mailchimp integration is direct HTTP you can read in one sitting.
- **No telemetry.** This server makes no network call other than the Mailchimp API request a tool asks for.

Your API key still carries the permissions of the Mailchimp user who created it. Create it under the least-privileged user available, and revoke it in **Account & billing → Extras → API keys** if it is ever exposed.

---

## Project Structure

```
src/mailchimp_mcp/
  server.py     # MCP server entry point and the 24 tool definitions
  client.py     # Marketing API client (GET-only, pagination, retry) + allowlisted Mandrill client
  analysis.py   # Status-change inference, snapshots and diffing
  config.py     # Environment loading, key parsing, datacenter resolution, redaction
tests/          # Unit tests against a mocked API — no live account needed
```

The server communicates over stdio using JSON-RPC 2.0, the standard MCP transport.

---

## Development

```bash
pip install -e ".[dev]"
pytest
```

The test suite runs entirely against a mocked HTTP transport, so it needs no Mailchimp credentials and makes no network calls.

---

## A note on testing

The endpoints, query parameters, status enums and response fields in this server were taken from Mailchimp's own OpenAPI specification (Marketing API v3.0.91) rather than transcribed from documentation pages, so parameter names and allowed values match the API exactly.

Credential parsing, datacenter resolution, key redaction, pagination, 429 retry and backoff, path validation, the transactional allowlist, status classification and snapshot diffing are covered by unit tests against a mocked API.

---

## License

[MIT](./LICENSE) — free to use, modify, and distribute.

---

<div align="center">

[Report a Bug](https://github.com/jimsimoy/mailchimp-mcp/issues) · [Request a Feature](https://github.com/jimsimoy/mailchimp-mcp/issues)

</div>

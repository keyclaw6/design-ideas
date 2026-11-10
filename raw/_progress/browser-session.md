# Browser session (resume)

**Historical session note:** the endpoints and status below describe September
2026. The current [2026-10-15 import](import-2026-10-15/README.md) recovered Reddit
access through an authenticated read-only route and verified the live account as
`Strange_Tomatillo335`. The completed follow-up unsaved all 130 X bookmarks and
38 Reddit entries; both saved lists were independently verified empty. Use that
run's reports, inventories, and unsave ledgers for current state.

**CDP port:** `BU_CDP_URL=http://127.0.0.1:33789` (headed agent-browser — **not** Grok Bot / `127.0.0.1:9222`)

Also available: `agent-browser --session chrome-profile get cdp-url` → port `37349` (same tabs, still guest on Reddit).

**Tabs:** `agent-browser tab list` — use `agent-browser tab reddit` / `agent-browser tab t10` before site-specific commands.

## Status (2026-09-04 ~11:20)

### X — **CLEARED** (verified)

Bookmarks and likes list pages empty (`[]`). Harvest on `origin/main` at `e1c98a9`. Skill: `skills/x-harvest-clear/SKILL.md`.

### Reddit — **STOPPED** (out of scope per user)

Reddit login blocked; user directed stop Reddit work.

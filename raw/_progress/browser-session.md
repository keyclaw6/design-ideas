# Browser session (resume)

**CDP port:** `BU_CDP_URL=http://127.0.0.1:33789` (headed agent-browser — **not** Grok Bot / `127.0.0.1:9222`)

Also available: `agent-browser --session chrome-profile get cdp-url` → port `37349` (same tabs, still guest on Reddit).

**Tabs:** `agent-browser tab list` — use `agent-browser tab reddit` / `agent-browser tab t10` before site-specific commands.

## Status (2026-09-04 ~10:15)

### X — **CLEARED** (verified)

Bookmarks and likes list pages empty (`[]`). Harvest used fxtwitter + GraphQL `DeleteBookmark` (`Wlmlj2-xzyS1GN3a6cj-mQ`) when UI clicks stalled.

Re-inject cookies if session drops:
```bash
export BU_CDP_URL=http://127.0.0.1:33789
agent-browser cookies set auth_token "$X_AUTH_TOKEN" --domain .x.com
agent-browser cookies set ct0 "$X_CT0" --domain .x.com
```

### Reddit — **STOPPED** (out of scope per user)

Reddit login blocked (reCAPTCHA / Google OAuth). User directed: stop Reddit; commit X harvest only.

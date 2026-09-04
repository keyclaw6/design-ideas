---
name: x-harvest-clear
description: Harvest X bookmarks and likes into design-ideas raw/items/x-<tweet_id>/, clear platform lists, rebuild catalog. Use when draining X bookmarks/likes, resuming harvest, or verifying empty lists after capture.
---

# X bookmark/likes harvest-clear

Drain **Bookmarks** and **Likes** on X into `raw/items/x-<tweet_id>/` per [SCHEMA.md](../../SCHEMA.md), then clear both lists on X and rebuild `catalog/`.

## When to use

- User asks to harvest/clear X bookmarks or likes
- `raw/_progress/harvest-loop.md` or `browser-session.md` says resume X harvest
- Bookmarks/likes need capture + unsave/unlike in one pass

## Prerequisites

| Requirement | Notes |
|-------------|-------|
| Repo root | cwd with `raw/items/`, `SCHEMA.md` |
| Browser | **agent-browser** headed Chrome via `BU_CDP_URL` |
| Wrong CDP | **Never** Grok Bot / `127.0.0.1:9222` |
| X session | `auth_token` + `ct0` cookies |
| Tools | `agent-browser`, `curl`, `python3` |

```bash
export BU_CDP_URL="$(agent-browser get cdp-url)"
agent-browser tab x   # or tab t9 — one tab for all X work
```

## 1. Authenticate X

```bash
# Option A: env vars (from Cursor partition or manual export)
export X_AUTH_TOKEN='...'
export X_CT0='...'
python3 scripts/x_extract_cookies.py --inject   # read partition + inject

# Option B: manual inject
agent-browser cookies set auth_token "$X_AUTH_TOKEN" --domain .x.com
agent-browser cookies set ct0 "$X_CT0" --domain .x.com
```

Verify: open `https://x.com/i/bookmarks` — URL must not contain `login` or `onboarding`.

## 2. Extract tweet IDs

**Bookmarks:** `https://x.com/i/bookmarks`  
**Likes:** `https://x.com/<handle>/likes` (handle from `a[data-testid="AppTabBar_Profile_Link"]`)

```javascript
JSON.stringify([...new Set(
  [...document.querySelectorAll('a[href*="/status/"]')]
    .map(a => (a.href.match(/status\/(\d+)/) || [])[1])
    .filter(Boolean)
)])
```

Scroll until IDs stabilize. Process in batches (~5 visible cards), reload after each batch.

## 3. Capture each tweet (HTTP)

```bash
curl -s "https://api.fxtwitter.com/i/status/<tweet_id>"
```

Per folder `raw/items/x-<tweet_id>/`:

| File | Content |
|------|---------|
| `source.json` | `source_type: x`, `extra.tweet_id` |
| `post.md` | Title, author, body |
| `comments.md` | Replies stub |
| `research.md` | Synthesis or harvest note |
| `media/` | From fxtwitter media URLs |

**>100MB media:** keep locally, gitignore path, set `extra.media_omitted` in `source.json`.

**Verify before clearing on X:** `source.json` and `post.md` must exist.

## 4. Clear bookmarks — GraphQL first (critical)

UI `removeBookmark` clicks often **stall or re-sync** — bookmarks reappear after reload. Use GraphQL:

```bash
./scripts/x_delete_bookmark.sh <tweet_id>
```

Implementation: `DeleteBookmark` with `queryId=Wlmlj2-xzyS1GN3a6cj-mQ`, `auth_token` + `ct0` + `x-csrf-token`. On success, set `unsaved: true` in `source.json`.

UI fallback only for debugging single items: `button[data-testid=removeBookmark]` on post detail.

## 5. Clear likes — UI (reliable in session)

```javascript
(() => {
  const b = document.querySelector('button[data-testid=unlike]');
  if (b) { b.click(); return 'unliked'; }
  return 'none';
})()
```

Set `unliked: true` in `source.json`.

## 6. Loop until empty

```
1. Open bookmarks OR likes
2. Extract IDs (scroll)
3. Capture missing → disk verify
4. Clear on platform (GraphQL bookmarks / UI likes)
5. Reload → repeat until []
```

Orchestration:

```bash
export BU_CDP_URL='...'
export X_AUTH_TOKEN='...' X_CT0='...'
python3 scripts/x_harvest_clear.py      # full loop
./scripts/x_clear_lists.sh              # clear only (disk must exist)
```

## 7. Verify + catalog

Both list pages must return `[]`. Then:

```bash
python3 scripts/rebuild_catalog.py
graphify update .
```

## Pitfalls

| Problem | Fix |
|---------|-----|
| Bookmarks reappear after UI click | **Use GraphQL** `x_delete_bookmark.sh` |
| Wrong browser session | Check `BU_CDP_URL`, not port 9222 |
| Cookie drift | Re-run `x_extract_cookies.py --inject` |
| Scroll trap | Unsave visible batch, reload, repeat |
| Cleared before capture | Never delete until `source.json` + `post.md` exist |
| queryId 404 | Probe live X bundle; session default `Wlmlj2-xzyS1GN3a6cj-mQ` |
| Git push fails | Media >100MB — gitignore + `extra.media_omitted` |

## Reference

- [SCHEMA.md](../../SCHEMA.md)
- [raw/_progress/harvest-loop.md](../../raw/_progress/harvest-loop.md)
- [scripts/x_harvest_clear.py](../../scripts/x_harvest_clear.py)
- [scripts/x_delete_bookmark.sh](../../scripts/x_delete_bookmark.sh)

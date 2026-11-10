# Harvest loop (X + Reddit)

The default is **capture → verify locally → unsave → verify the saved list is
empty**. Follow the [current import guide](import-2026-10-15/README.md) and
`AGENTS.md`. Preserve platform save state only when the user explicitly requests
a capture-only export. Historical usernames must be checked against the current
authenticated identity. Change Likes only when the requested scope includes Likes.

## X — Bookmarks + Likes

Browser: agent-browser headed session (`BU_CDP_URL` from `agent-browser get cdp-url`). **Not** Grok Bot / `127.0.0.1:9222`.

Per batch (max 5 visible cards):

1. Open `https://x.com/i/bookmarks` or Profile → **Likes**
2. Extract status IDs from `a[href*="/status/"]`
3. For each ID not in `raw/items/x-<id>/`: HTTP capture (fxtwitter/vxtwitter/jina) → `content.md` (verbatim single file), `media/`, `source.json`
4. Verify folder complete
5. **Bookmarks:** click bookmark control until aria-label is `Bookmark` (not `Remove Bookmark`); set `unsaved: true`
6. **Likes:** click like (heart) until unliked; set `extra.unliked: true` in `source.json`
7. Reload list; repeat until both lists empty

## Reddit — Saved (`kab264set`)

Login: reddit.com → Log in with Google → **Kab264z@gmail.com**

Folder: `raw/items/reddit-<id>/` with `source_type: reddit`, `content.md` (verbatim single file), `media/`, `unsaved: true` after unsave on Reddit.

## Git

First commit on `main`: AGENTS.md, README.md, SCHEMA.md, catalog/, raw/, .gitignore (exclude `.cursor/`). Push `origin main` → https://github.com/keyclaw6/design-ideas

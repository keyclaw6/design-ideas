# Harvest loop (X + Reddit)

## X — Bookmarks + Likes

Browser: agent-browser headed session (`BU_CDP_URL` from `agent-browser get cdp-url`). **Not** Grok Bot / `127.0.0.1:9222`.

Per batch (max 5 visible cards):

1. Open `https://x.com/i/bookmarks` or Profile → **Likes**
2. Extract status IDs from `a[href*="/status/"]`
3. For each ID not in `raw/items/x-<id>/`: HTTP capture (fxtwitter/vxtwitter/jina) → `post.md`, `comments.md`, `research.md`, `media/`, `source.json`
4. Verify folder complete
5. **Bookmarks:** click bookmark control until aria-label is `Bookmark` (not `Remove Bookmark`); set `unsaved: true`
6. **Likes:** click like (heart) until unliked; set `extra.unliked: true` in `source.json`
7. Reload list; repeat until both lists empty

## Reddit — Saved (`kab264set`)

Login: reddit.com → Log in with Google → **Kab264z@gmail.com**

Folder: `raw/items/reddit-<id>/` with `source_type: reddit`, `post.md`, `comments.md`, `research.md`, `media/`, `unsaved: true` after unsave on Reddit.

## Git

First commit on `main`: AGENTS.md, README.md, SCHEMA.md, catalog/, raw/, .gitignore (exclude `.cursor/`). Push `origin main` → https://github.com/keyclaw6/design-ideas

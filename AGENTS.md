# Agent query guide

How to search this library when answering questions or continuing research.

## Query order

1. **Start at `catalog/README.md`** — taxonomy map, topic lanes, and how to navigate.
2. **Scan `catalog/index.md`** — id/title/topics/filtered table for every entry.
3. **Check `catalog/filtered.md`** — noise items excluded from topic lanes (still on disk).
4. **Open `catalog/topics/<slug>.md`** — lane brief + curated picks + full item list.
5. **Read `catalog/patterns.md`** — cross-cutting pipelines with item ids.
6. **Inside an item folder** (`raw/items/<id>/`), read in this order:
   - `source.json` — metadata, URL, topics
   - `page.md` or `post.md` — primary content (`post.md` for `x` and `reddit`)
   - `comments.md` — optional thread/replies
   - `research.md` — optional agent notes (only when post alone is insufficient)
   - `media/` — screenshots, attachments
6. **Long-form notes:** `raw/notes/<name>.md` — research not yet split into items (`*.meta.json` for topics)

## Graphify

Knowledge graph at `graphify-out/graph.json` (4200+ nodes). **Run graphify before Read/Grep/Glob** for architecture or corpus questions:

```bash
graphify query "<question>"
graphify explain "<concept>"
graphify path "<A>" "<B>"
```

After changing `catalog/`, `raw/`, or `scripts/`: `graphify update .`

Wiki index (if present): `graphify-out/wiki/index.md`. Broad review: `graphify-out/GRAPH_REPORT.md`.

## X harvest skill

When draining X bookmarks/likes into this library, read and follow **`skills/x-harvest-clear/SKILL.md`**. Prefer GraphQL `DeleteBookmark` over UI clicks for unsave.

## Conventions

- No judgment ranking — presence in the catalog does not imply recommendation.
- Topics are tags, not hierarchies.
- Do not write under `raw/items/` unless you own that harvest lane.
- Keyboard business brief content is out of scope for this library.

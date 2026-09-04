# Agent query guide

How to search this library when answering questions or continuing research.

## Query order

1. **Start at `catalog/index.md`** — scan the id/title/topics table for relevant entries.
2. **Check `catalog/topics/`** — topic files group items by theme (e.g. `bess-3d-flythrough.md`). Non-exclusive: one item may appear in several topics.
3. **Read `catalog/patterns.md`** — cross-cutting techniques discovered during harvest (stub until wave 1 completes).
4. **Open the path** listed in the index:
   - `raw/items/<id>/` — normalized captures (see SCHEMA.md)
   - `raw/notes/<name>.md` — long-form research not yet split into items
5. **Inside an item folder**, read in this order:
   - `source.json` — metadata, URL, topics
   - `page.md` or `post.md` — primary content (`post.md` for `x` and `reddit`)
   - `comments.md` — optional thread/replies
   - `research.md` — agent synthesis or follow-ups
   - `media/` — screenshots, attachments

## Graphify

Knowledge graph at `graphify-out/graph.json` (3100+ nodes). **Run graphify before Read/Grep/Glob** for architecture or corpus questions:

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

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

## Graphify (future)

When a Graphify index exists, prefer graph queries for relationship traversal (related URLs, shared topics, author clusters). Until then, use catalog + grep/file search.

## Conventions

- No judgment ranking — presence in the catalog does not imply recommendation.
- Topics are tags, not hierarchies.
- Do not write under `raw/items/` unless you own that harvest lane.
- Keyboard business brief content is out of scope for this library.

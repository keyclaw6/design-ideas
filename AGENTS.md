# Agent query guide

How to search this library when answering questions or continuing research.

## Query order

1. `analysis/README.md`
2. `analysis/subjects.json`
3. `analysis/subjects/<slug>/brief.md`
4. `analysis/index.jsonl`
5. `analysis/items/<id>/card.md`
6. `raw/` only when card.readiness != ready

## Graphify

Knowledge graph at `graphify-out/graph.json` (4200+ nodes). **Run graphify before Read/Grep/Glob** for architecture or corpus questions:

```bash
graphify query "<question>"
graphify explain "<concept>"
graphify path "<A>" "<B>"
```

The graph covers `analysis/` only. After analysis edits: `graphify update .`

Wiki index (if present): `graphify-out/wiki/index.md`. Broad review: `graphify-out/GRAPH_REPORT.md`.

## X harvest skill

When draining X bookmarks/likes into this library, read and follow **`skills/x-harvest-clear/SKILL.md`**. Prefer GraphQL `DeleteBookmark` over UI clicks for unsave.

## Conventions

- No judgment ranking — presence in the catalog does not imply recommendation.
- Topics are tags, not hierarchies.
- Do not write under `raw/items/` unless you own that harvest lane.
- Keyboard business brief content is out of scope for this library.

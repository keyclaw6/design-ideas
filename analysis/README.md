# Analysis layer

This is the only tree a later agent should read. Raw harvest stays under `raw/`. Graphify covers `analysis/**/*.md` only.

## Analyze one subject in five reads

1. Open `subjects.json` and pick a slug (`serp-ai-visibility` for SERP / “syrups” optimization; `image-to-3d-world` for “freedom modeling”; `gaussian-splatting` for 3DGS).
2. Read `subjects/<slug>/brief.md`.
3. If it exists, read `subjects/<slug>/worksheet.md` (short stack + axis scores; not a ranking).
4. Scan `subjects/<slug>/claims.jsonl`.
5. Open the technique pages listed in the brief.
6. Open `items/<id>/card.md` for ids the brief marks `must_read`.

Do not open `raw/` unless the card's `readiness` is `ready-with-gaps` or `blocked`.

## Machine access

```bash
# items in one subject
jq -c 'select(.primary_subject=="serp-ai-visibility")' analysis/index.jsonl

# tools / techniques in a subject
jq -c 'select(.primary_subject=="gaussian-splatting") | {id,title,roles,tools,techniques}' analysis/index.jsonl

# thread coverage
jq -c 'select(.source_type=="x") | {id, thread}' analysis/index.jsonl

# ready-to-judge only
jq -c 'select(.readiness=="ready" and .disposition=="analyze")' analysis/index.jsonl
```

## Files and who writes them

| Path | Who writes |
|------|------------|
| `items/<id>/card.json` | card worker |
| `items/<id>/thread.json` | thread worker (X only) |
| `items/<id>/card.md`, `thread.md` | `scripts/analysis/render.py` |
| `subjects/<slug>/brief.md`, `brief.json` | subject worker |
| `subjects/<slug>/items.jsonl`, `claims.jsonl` | `render.py` |
| `tools/*.md`, `techniques/*.md` | `render.py` (NOTES preserved) |
| `registry/tools.jsonl`, `techniques.jsonl` | `build_registry.py` |
| `registry/aliases.json` | registry worker |
| `index.jsonl`, `shelf/*` | `build_index.py` / `render.py` |
| `subjects.json` | parent (this spec) |

## Shelves

| Shelf | Meaning |
|-------|---------|
| `noise` | Engagement bait, promo with no artifact, empty capture, unrelated personal |
| `duplicate` | Same artifact, no new angle (`duplicate_of` required) |
| `out-of-scope` | Real artifact that no subject covers |
| `uncategorized` | Transitional triage (≤ 19 after audit) |

Shelved items keep a card and a reason. Nothing is deleted.

## Graph

```bash
graphify query "<question>"
graphify explain "<concept>"
graphify path "<A>" "<B>"
```

The graph covers `analysis/**/*.md` only. After analysis edits: `graphify update .`.

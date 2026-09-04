# design-ideas

Personal technique library — captured X bookmarks, URLs, and research notes for later human and agent query.

This is **not** a product or public service. It is a structured archive of interesting techniques, pipelines, and references, organized for retrieval rather than ranking or judgment.

**Agent entry point:** [analysis/README.md](./analysis/README.md) → subject briefs → claims.jsonl → item cards. Legacy harvest tables remain under [catalog/](./catalog/README.md). See [AGENTS.md](./AGENTS.md).

**Bank stats:** 388 analysis units (387 harvest folders + 1 note) · 17 subjects · 345 analyze / 43 shelf · each subject has a `worksheet.md` · Graphify covers `analysis/**/*.md` only.

## Current focus

- **Now:** SERP / “syrups” (AEO/GEO), “freedom modeling” (image→3D world), Gaussian splatting, BESS blockout→video, web 3D scenes, landing motion, design-agent skills
- **Standard / later:** remaining subjects — worksheets exist; capture gaps still open
- **Judge path:** `analysis/subjects/<slug>/brief.md` then `worksheet.md` (short stack + axis scores; not a ranking)

## Layout

| Path | Purpose |
|------|---------|
| `analysis/` | **Start here** — [README](analysis/README.md), subject briefs, cards, claims |
| `docs/ANALYSIS_STRUCTURE.md` | Binding analysis-layer contract |
| `catalog/` | Legacy harvest tables (input only) |
| `raw/notes/` | Long-form research and synthesis |
| `raw/items/<id>/` | Frozen captures (thread-raw may be appended) |
| `graphify-out/` | Knowledge graph over the analysis layer |
| `skills/` | Agent skills (e.g. `x-harvest-clear` for X bookmark drain) |

See [SCHEMA.md](./SCHEMA.md) for item folder structure and [AGENTS.md](./AGENTS.md) for query workflow.

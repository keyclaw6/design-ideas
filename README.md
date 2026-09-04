# design-ideas

Personal technique library — captured X bookmarks, URLs, and research notes for later human and agent query.

This is **not** a product or public service. It is a structured archive of interesting techniques, pipelines, and references, organized for retrieval rather than ranking or judgment.

**Agent entry point:** [analysis/README.md](./analysis/README.md) → subject briefs → claims.jsonl → item cards. Legacy harvest tables remain under [catalog/](./catalog/README.md). See [AGENTS.md](./AGENTS.md).

**Bank stats (2026-09-04):** 387 items + 1 long-form note · 12 topic lanes · 47 filtered (noise) · graphify corpus ~4.2k nodes.

## Current focus

- **Now:** BESS 3D flythrough, marketing video pipelines, SEO agents
- **Later:** Split ergonomic keyboard design and related hardware topics

## Layout

| Path | Purpose |
|------|---------|
| `catalog/` | **Start here** — [README](catalog/README.md), index, topic briefs, patterns, filtered list |
| `raw/notes/` | Long-form research and synthesis (not yet split into items) |
| `raw/items/<id>/` | Normalized captures (one folder per bookmark/URL) |
| `raw/_progress/` | Multi-agent orchestration state |
| `graphify-out/` | Knowledge graph (`graph.json`) for corpus search |
| `skills/` | Agent skills (e.g. `x-harvest-clear` for X bookmark drain) |

See [SCHEMA.md](./SCHEMA.md) for item folder structure and [AGENTS.md](./AGENTS.md) for query workflow.

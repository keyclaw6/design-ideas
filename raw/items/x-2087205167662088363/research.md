# Research

## What it is
Hamilton Ulmer (Observable/Plot/Mosaic lineage) reacting that some dataviz path “EXTREMELY works”: charts at DuckDB speed, nearly free, no JavaScript required. Parent tweet/tool was not captured.

## How it works
- Quote-style reaction; mechanism not in `post.md`.
- Author context: DuckDB + Mosaic/Plot — SQL in, viz out, often via WASM or a thin server.
- “No JS required” implies SQL/notebook/markdown charts (Evidence, Quarto, DuckDB UI, or similar) rather than a custom D3 app.
- Treat as a recommendation to prefer DuckDB-backed viz over JS chart spaghetti.

## Why saved
Infographics lane: agent-authored charts should be SQL-native and cheap. Complements Flint/AntV/diagram-design.

## Topics
- `infographics`

## Related
- `web-flint-chart` — viz language for AI
- `github-antvis-infographic` — AntV infographics
- `github-cathrynlavery-diagram-design` — diagram types for agents
- `web-iandmacomber-post-ai-data-stack` — post-AI data stack feel

## Use when
Picking a chart stack for agent-generated reports. Re-fetch the X parent if you need the exact tool name; until then assume DuckDB + Plot/Mosaic/Evidence-class.

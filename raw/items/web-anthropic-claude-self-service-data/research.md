# Research

## What it is

Anthropic engineering post (June 2026): how they automated ~95% of business analytics queries with Claude at ~95% aggregate accuracy by treating analytics as entity mapping, not SQL generation.

## How it works

- Insight: coding agents have tests; analytics has one correct source. Map question → current entities, then SQL is easy.
- Failure modes: concept↔entity ambiguity, staleness, retrieval miss.
- Stack: canonical datasets + CI; semantic layer/lineage/query corpus; skills that route to governed answers; freshness/provenance checks; evals.
- Colocate modeling, semantic layer, docs, dashboard defs in one repo so CI catches cross-layer breaks.
- Metadata treated as product (grain, lineage, owners). Frees DS for causal/forecasting work.

## Why saved

Playbook for agent-readable company context — same problem as Cerebras KB and Gasquez “context is ETL.” Relevant if marketing agents query warehouse (Graphed) without inventing metric definitions.

## Topics

`agent-skills`, `mcp`

## Related

`web-cerebras-knowledge-base`, `web-davidgasquez-context-engineering`, `web-iandmacomber-post-ai-data-stack`, `web-chatgpt-training`, `web-graphed`

## Use when

Designing a semantic layer or analytics skills; diagnosing why an agent invents metrics; connecting warehouse MCP to governed entities.

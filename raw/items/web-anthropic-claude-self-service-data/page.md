# How Anthropic enables self-service data analytics with Claude

**URL:** https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude  
**Published:** June 3, 2026 · ~5 min read

Anthropic's playbook for agentic self-service analytics — avoiding both wide denormalized table sprawl and siloed ringfenced environments.

## Headline results

- **~95%** of business analytics queries automated via Claude
- **~95%** accuracy in aggregate
- Data science team freed for causal modeling, forecasting, ML

## Core insight: data ≠ software

Coding agents have open-ended solution spaces with tests/docs as guardrails. Analytics often has **one correct answer** from **one correct source** with no deterministic proof.

Central problem: **map user question → specific, up-to-date entities in the data model** with correct usage. SQL generation is then trivial.

## Three failure modes (~majority of errors)

1. **Concept ↔ entity ambiguity** — hundreds of plausible fields (e.g. "active users": which actions, fraud inclusion, lookback window?)
2. **Data staleness** — schemas, definitions, and agent knowledge rot
3. **Retrieval failure** — right info exists and is annotated but agent doesn't find it in vast search space

## Agentic stack (layer → failure mode)

| Layer | Primary attack |
|-------|----------------|
| **Data foundations** | Ambiguity + staleness — canonical datasets, CI, colocated artifacts |
| **Sources of truth** | Ambiguity — semantic layer, lineage, query corpus distillations |
| **Skills** | Retrieval — structurally route agent to governed answers |
| **Maintenance & validation** | Staleness — freshness, provenance, online checks |
| **Evals** | All three — measure regressions |

### Data foundations (highlights)

- **Canonical datasets** — small governed logical models; deprecate near-duplicates so search returns one answer
- **Enforce via tooling + CI + mandate** — governance without enforcement decays
- **Colocate artifacts** — modeling, semantic layer, reference docs, dashboard definitions in one repo; CI catches cross-layer breaks
- **Metadata as product** — descriptions, grain, lineage, ownership maintained like code

### Sources of truth (trust order)

1. **Semantic layer** — compiled metrics; agents structurally required to use first. Auto-generating metric defs from raw tables **failed evals** (plausible but ambiguous defs)
2. **Lineage / transformation graph** — upstream models, deprecation, grain
3. **Query corpus** — raw retrieval of thousands of prior SQL moved accuracy **<1 point**; distilled per-domain reference docs work better

### Skills

Template-based skills for majority of analyses (appendix in full post). Slack ad-hoc path via Claude Tag (linked separate blog post).

## Related posts in library

- Ian Macomber: agent-readable dashboards, semantic layer as contract
- David Gasquez: context engineering as ETL/ELT for knowledge

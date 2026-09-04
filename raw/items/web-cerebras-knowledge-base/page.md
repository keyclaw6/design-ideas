# How Cerebras Built Its Enterprise Knowledge Base

**URL:** https://www.cerebras.ai/blog/how-we-built-our-knowledge-base

Engineering post on **Cerebras Knowledge** — internal KB used by humans, automations, and agents. Claim at publish: **15,000+ questions/day**, widely adopted within ~3 months of launch.

## Design principle

Don't force a single platform of record. Information lives where it's ergonomic (Slack threads, Google Docs, GitHub, Jira). System **extracts from each platform directly** with minimal behavior change.

## Three-layer product

1. Platform for collecting and storing internal data
2. Platform for querying that data
3. AuthZ/authN layer with auditing and analytics

**Core datastore:** single Postgres table — embeddings, raw summaries, metadata from many sources. Every connector writes rows to the same interface.

## Slack (primary source)

Challenges: variable information density, short messages beating long ones in cosine similarity, meaning depends on thread context.

**Hybrid retrieval** (fused at query time):

| Signal | Role |
|--------|------|
| Full-text search | Exact tokens — error strings, flag names, hostnames |
| Embedding search | Paraphrase matching across vocabulary |
| IDF | Down-rank filler ("sounds good, thanks!") |
| Age decay | Prefer recent threads when relevance ties |

**Ingestion:** Slack bot in Socket Mode → dedupe by event ID → re-fetch **entire thread** on any new message (parent + all replies as one row).

**Distillation:** LLM extracts structured fields from thread — searchable question, summary, resolution, systems, code refs — then embed normalized document (not raw transcript directly; accuracy gain in their experiments).

**Bursting:** Embed individual author "bursts" with thread topic prepended; gate by IDF ≥4.0, length ≥200 chars, or reactions.

## Code repositories

Large internal repos (some **>40 GB**). Chose **CocoIndex** (open-source) for incremental code embeddings:

- Language-aware recursive chunking (class → method → block)
- Multiple embeddings per file at different granularities
- Re-embed only changed chunks on commit via sync metadata in Postgres

## Connector model

Each source defines: what the data is, how to connect, fetch frequency. Embedding row schema is uniform regardless of origin (Slack, code, docs, custom DB).

## Cross-references

- Cited by Ian Macomber post-AI data stack essay as exemplar internal KB
- David Gasquez "context engineering is a data problem" links here for Slack normalization pattern

# Research

## What it is

David Gasquez essay arguing context engineering is a data problem: extract, filter, curate, model, and publish artifacts so agents (and orgs) decide better — not stuffing every raw source into the prompt.

## How it works

- Knowledge Build System as compiler: Extract (preserve source shape) → Transform (org-specific summaries/models, cf. Cerebras Slack distillation) → Publish (curated text files; embeddings as disposable index).
- Analogy: connecting Looker to every raw table never solved analytics; agents reading every Slack thread will not either.
- Curated files = materialized views for LLMs. Direct access beats a stale KB, but conflicting OKR defs require a process to codify truth.
- Operational: marts per team, no universal “company context” pack; cite Anthropic contextual retrieval.
- Diagrams look like 2018 Fivetran/dbt because the job is the same.

## Why saved

Conceptual backbone for Cerebras/Anthropic/Macomber cluster. Applies to this idea bank itself (catalog + research.md as published marts).

## Topics

`agent-skills`

## Related

`web-cerebras-knowledge-base`, `web-iandmacomber-post-ai-data-stack`, `web-anthropic-claude-self-service-data`, `web-chatgpt-training`, `web-blume-codes`

## Use when

Designing agent knowledge pipelines; deciding what to materialize vs retrieve raw; explaining why prompt-stuffing fails at org scale.

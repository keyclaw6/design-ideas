# Research

## What it is

Cerebras engineering post on Cerebras Knowledge: internal KB for humans, automations, and agents (~15k questions/day). Extracts from Slack, Docs, GitHub, Jira in place instead of forcing a single platform of record.

## How it works

- Three layers: collect/store, query, AuthZ/audit. Core store: one Postgres table of embeddings, summaries, metadata; every connector writes the same row shape.
- Slack: Socket Mode bot, thread re-fetch on any message, LLM distillation (question/summary/resolution/systems), hybrid retrieval (full-text + embeddings + IDF + age decay), burst embeddings gated by IDF/length/reactions.
- Code: CocoIndex incremental embeddings, language-aware chunking, re-embed changed chunks only (repos >40 GB).
- Cited by Macomber (post-AI data stack) and Gasquez (context engineering as ETL).

## Why saved

Concrete KB architecture for agent context — the implementation sibling of Gasquez’s essay. Useful if this idea bank or a company wiki must be queryable by agents without stuffing raw Slack.

## Topics

`agent-skills`

## Related

`web-davidgasquez-context-engineering`, `web-anthropic-claude-self-service-data`, `web-iandmacomber-post-ai-data-stack`, `web-chatgpt-training`, `web-blume-codes`

## Use when

Designing Slack/code connectors for an agent KB; hybrid retrieval with IDF/age decay; incremental code embeddings at repo scale.

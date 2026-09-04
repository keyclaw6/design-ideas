## What it is

Pointer to PipesHub (pipeshub-ai): an open-source governed context layer that connects org knowledge for agents, RAG, and search.

## How it works

- GitHub: github.com/pipeshub-ai/pipeshub-ai — enterprise connectors into a single retrieval/governance plane.
- Pitch is one context layer rather than per-app RAG silos (Slack/Drive/wiki/tickets).
- Governance (permissions, audit) is the differentiator vs naive embeddings dumps.
- Useful as a pattern even if the product is not adopted: ETL-style context engineering, not prompt stuffing.
- Adjacent to Cerebras KB writeup and David Gasquez's 'context is a data problem' note in this library.

## Why saved

KB's agent stack needs durable knowledge (BESS product facts, SEO topical maps, DESIGN.md sources). This is a candidate architecture, not a UI kit.

## Topics

`agent-skills`, `mcp`

## Related

`web-cerebras-knowledge-base`, `web-davidgasquez-context-engineering`, `web-anthropic-claude-self-service-data`, `github-punkpeye-awesome-mcp-servers`

## Use when

Designing a company knowledge plane for agents, comparing RAG platforms, or looking for OSS connectors + ACL-aware retrieval.

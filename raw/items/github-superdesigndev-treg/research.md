# Research

## What it is

superdesigndev/treg (~1k stars): “OpenRouter for agent tools.” One base URL and token unlock thousands of catalogued endpoints (SEO, backlinks, social, people/company enrichment, ads, scraping) priced per call, plus team-owned keys/skills/CLIs injected server-side.

## How it works

- Catalog endpoints run on treg’s keys, metered against prepaid balance ($1 free); team keys always win and are unmetered.
- Proxy relays, never models, upstream; auth injected server-side. HTTP 402 with machine-actionable top-up when broke.
- CLI: `treg login`, `catalog search`, `call`, `balance`; Claude plugin, `npx skills add`, `treg mcp install`, connector `https://treg.to/mcp/v2/`.
- Credential ladder: team tool → team secret → treg key. `treg scan` / `upload` share internal tools without leaking secrets to teammates’ laptops.
- People-search marketing claims Claude Code + treg ~78% vs ~43% alone on Lessie B2B tasks.

## Why saved

Solves the “Semrush $139/mo for one agent run” problem. Core MCP/SEO infrastructure next to iannuttall/seo (local crawl) and CrowdReply (citations).

## Topics

`mcp`, `agent-skills`, `seo-agents`

## Related

`web-treg-people-search`, `github-LessieAI-people-search-bench`, `github-iannuttall-seo`, `github-punkpeye-awesome-mcp-servers`, `web-graphed`

## Use when

An agent needs SERP, backlinks, or enrichment without N vendor signups; sharing team APIs via MCP; comparing people-search providers on the Lessie bench.

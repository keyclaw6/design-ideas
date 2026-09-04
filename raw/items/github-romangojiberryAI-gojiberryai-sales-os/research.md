# Research

## What it is

Open-source “AI outbound sales department” for Grok Bot (also Claude Code/Cursor): thirteen specialized agents coordinated through hosted GojiberryAI MCP. MIT.

## How it works

- Pipeline: Signal Hunter → ICP Analyst → Account Researcher → Lead Enricher → Copywriter → Outreach Operator → Reply Agent → Meeting Qualifier; Head of Sales / Sales Manager orchestrate; Pipeline Analyst tracks conversion.
- Install: `/plugin marketplace add romangojiberryAI/gojiberryai-sales-os` then `sales-os@gojiberryai-sales-os`. Cursor: copy `skills/sales-os/` and point MCP at `https://mcp.gojiberry.ai/mcp`.
- Hosted MCP is the coordination bus; skills encode role prompts.
- Intended for prospecting/sequencing, not technical SEO crawls — but shares enrichment APIs with treg people-search.

## Why saved

Template for multi-agent outbound that can sit on treg enrichment + CrowdReply visibility. Useful if KB products need founder-led sales automation.

## Topics

`mcp`, `agent-skills`, `seo-agents`

## Related

`github-superdesigndev-treg`, `web-treg-people-search`, `github-LessieAI-people-search-bench`, `web-graphed`, `web-crowdreply`

## Use when

Standing up outbound/ICP research agents; comparing a role-based sales OS vs a single SEO skill; wiring people-search tools into a sequence.

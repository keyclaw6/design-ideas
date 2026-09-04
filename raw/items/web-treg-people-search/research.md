# Research

## What it is

treg.to/people-search: product slice of treg — one skill/token for 1B+ contacts across Apollo, Hunter, Tomba, PDL, etc. Finds people, companies, verified work emails. Pay per answer, no seat subscription. Claims Claude Code + treg ~78.2% vs ~43% alone on Lessie B2B tasks.

## How it works

- Task table: verified email from ~$0.0089, mobile, person/company enrich, lookalikes, email verify, people-at-company, buying signals; routed endpoints pick BYO key then cheapest catalog.
- Prepaid, 0% markup on catalog rates; $1 free; BYO keys unmetered.
- Setup: dashboard, `treg login`, `treg mcp install`. Protocol in llms.txt: `GET https://treg.to/call/{endpoint-id}` + `X-Treg-Token`.
- Indexes: /use-cases, /workflows. Full catalog/tool-proxy story lives on the GitHub item.

## Why saved

Human-facing people-search pitch + bench claim. Use with Lessie bench when evaluating outbound agents.

## Topics

`mcp`, `agent-skills`, `seo-agents`

## Related

`github-superdesigndev-treg`, `github-LessieAI-people-search-bench`, `web-arxiv-2603-27476`, `github-romangojiberryAI-gojiberryai-sales-os`, `github-iannuttall-seo`

## Use when

Agents need emails/enrichment; citing the 78% vs 43% bench; onboarding via llms.txt rather than the full catalog README.

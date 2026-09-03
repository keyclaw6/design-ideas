# treg — People Search

**Primary URL:** https://treg.to/people-search  
**Product home:** https://treg.to  
**Repo:** https://github.com/superdesigndev/treg

One skill gives your agent **1B+ contacts** across Apollo, Hunter, Tomba, People Data Labs — 60 providers behind one token. Finds companies, people, and **verified work emails**. Pay per answer, no subscription.

## Capabilities (task-first)

| Task | Example providers | From |
|------|-------------------|------|
| Verified work email | Tomba, LeadMagic, Hunter | $0.0089 |
| Mobile number | routed across 3 providers | per hit |
| Person enrich | People Data Labs | $0.028 |
| Company enrich | Crustdata, Crunchbase | $0.010+ |
| Lookalike companies | company graph APIs | $0.049 |
| Email verify | Hunter | $0.003/check |
| People at company | LeadMagic, Apollo | routed |
| Buying signals | Crunchbase, Coresignal | funding & hiring |

Routed endpoints (e.g. `people.email.find`) pick provider by your keys first, then cheapest per hit.

## Benchmark claim

People Search Bench (LessieAI) — 119 real tasks. treg page cites **Claude Code alone ~43%** vs **Claude Code + treg ~78.2%** on B2B prospecting (% tasks answered correctly). Full bench: https://github.com/LessieAI/people-search-bench

## Pricing model

- No subscription; prepaid balance metered at provider rates (**0% markup**)
- Example: $0.0089 per verified email (Tomba catalog rate at capture)
- New teams: **$1.00 free**
- BYO keys always win and are unmetered

## Setup

- Dashboard: https://treg.to/app?ref=people-search
- CLI: `curl -fsSL https://treg.to/install.sh | sh` → `treg login`
- MCP: `treg mcp install`

---

## llms.txt (agent onboarding excerpt)

Source: https://treg.to/llms.txt

> **OpenRouter, but for agent tools instead of models.** Point an agent at ONE base URL with ONE token and it can do the *job*: 2,600+ catalogued endpoints across 60+ providers (SEO and SERP data, backlinks, social and trends, people and company enrichment, ads, scraping) — plus your own team's keys, skills and CLIs. Every credential is injected **server-side**.

**Base URL:** https://treg.to  
**Call protocol:** `GET https://treg.to/call/{endpoint-id}?...` with header `X-Treg-Token`

Catalog discovery indexes (append `.md` for Markdown):

- `https://treg.to/use-cases` — compare providers by job
- `https://treg.to/workflows` — chained multi-step jobs with receipts
- `https://treg.to/tools/<provider>` — per-provider endpoint prices

Routed people email example:

```
POST /call/treg.people.email.find
{ "full_name": "...", "domain": "..." }
→ { output, raw, _treg: { served_by, tried, charged_micro } }
```

Integration skill for resellers: https://treg.to/integrate.md

---

## Main site (treg.to)

Marketing positions treg as **OpenRouter for agent tools**: 2,630+ endpoints, one unified key, pay-per-result vs ~$536/mo of equivalent SaaS seats. Catalog groups: keyword/rank, backlinks, AI visibility, trending/social, publish, people/company enrichment, ads, measurement. **100% open source · AGPL.**

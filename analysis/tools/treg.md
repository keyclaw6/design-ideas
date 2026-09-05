# Treg

**Slug:** `treg` · **Kind:** repo · **URL:** https://treg.to · **Canonical item:** [github-superdesigndev-treg](../items/github-superdesigndev-treg/card.md)
**Subjects:** [mcp-and-agent-browsers](../subjects/mcp-and-agent-browsers/brief.md), [outbound-gtm-agents](../subjects/outbound-gtm-agents/brief.md), [serp-ai-visibility](../subjects/serp-ai-visibility/brief.md)
**Referenced by (2):**
- [treg: OpenRouter-style proxy for 2,896 metered agent tool endpoints](../items/github-superdesigndev-treg/card.md) — tool, claim-source — mcp-and-agent-browsers
- [treg people-search: one-token B2B enrichment across 60 providers](../items/web-treg-people-search/card.md) — tool — outbound-gtm-agents

<!-- NOTES:START -->
Fetched 2026-09-04 README + live site + `GET https://treg.to/providers.json` + `https://treg.to/llms.txt`.

First-party counts **do not agree**. Do not collapse them:

- README (raw, this pass): still **2,896 catalogued endpoints across 60 providers**.
- Homepage hero (`treg.to`): **2,630 endpoints · 47 providers**. Same page also says “Forty-two providers, one credential” and “47 providers.”
- `llms.txt`: “2,600+ … across 60+ providers” in the lead; later “2,800+ tools across 60 providers.”
- `GET https://treg.to/providers.json` (HTTP 200, `version: 12`): **104 named BYO providers** (Google Ads … OpenWeather). This is the env-door / `.env` matcher (~80 in `llms.txt`), **not** a dump of the metered catalog. `/tools/` returns 401.
- `GET https://treg.dev/providers.json` is **404** (HTML 6,888 B). `treg.dev/` homepage still 200 / **599,592** B. Do not treat `treg.dev` as the providers dump host.

Catalog dump still needs a token (`treg catalog` / `/call/…`). $1.00 free prepaid; team keys override catalog keys and are unmetered. AGPL on the homepage. Treat 2,896 as the README integer and 2,630 as the live-hero integer until someone `wc`s a catalog export.

**2026-09-05 capture — people-search page.** `https://treg.to/people-search` GET 200 / **83,902 B**. Title Claude for People Search — 1B+ Contacts for Your Agent. First-party: one skill / 1B+ contacts across Apollo, Hunter, Tomba, People Data Labs — **60** providers; pay per answer. `people.email.find` routed **from $0.0089**. `companies.search` ranked examples: Apollo **$0.026 · 98%**; TheCompaniesAPI **$0.004 · 91%**. Do not collapse $0.0089 with $0.026. Receipt `analysis/_work/captures/leftover-2026-09-05.json`.
<!-- NOTES:END -->

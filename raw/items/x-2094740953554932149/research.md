## What they are actually doing

Paul is amplifying Jason Zhou’s **treg people-search** launch: an agent-facing catalog that routes people/company enrichment across many providers (Apollo, Hunter, Tomba, PDL, etc.) behind one token, billed per successful find. The quoted line “$0.0089/lead” matches the people-search page’s cheapest **email-find** catalog rate (Tomba in the copy). “No subscriptions / 0% markup” on the tweet is prepaid metered calls at provider rates, not a free API.

**Product** — https://treg.to/people-search (also https://treg.to, `llms.txt`). Copy: 1B+ contacts, 60 providers, “Claude for people search,” pay per answer, misses free. Same token reaches SERP/SEO/ads/scrape tools. New teams: **$1.00** free balance. `treg.ai` HTTP is a GoDaddy parking lander, not the product.

**Repo** — https://github.com/superdesigndev/treg (1,020★ / 102 forks at capture, homepage treg.to, language Python, license SPDX `NOASSERTION` / “Other”). README: “OpenRouter, but for agent tools.” CLI `curl … treg.to/install.sh`; Claude plugin `/plugin marketplace add superdesigndev/treg` then `/plugin install treg@treg`; first-run walks `treg mcp install`. Catalog + BYO keys injected server-side. MCP support also listed on the README roadmap.

**Benchmark cited in the quote** — https://github.com/LessieAI/people-search-bench (MIT, 132★). arXiv:2603.27476 *PeopleSearchBench* (119 queries, four scenarios). The treg landing page compares Claude Code alone vs Claude Code + treg on B2B prospecting (page figures 43% vs 78.2% “tasks answered correctly”) against Lessie / Exa / Claude Code columns. Leaderboard in the bench README is a different table (Lessie / Exa / Claude Code / Juicebox) — not independently re-run here.

**Jason “Git Repo below”** — not in the fxtwitter quote payload; fixupx/vxtwitter on the quoted status returned 403 / truncated thread. The people-search page’s Open source control points at `superdesigndev/treg`.

## Open questions

- Exact contents of Jason’s missing “Git Repo below” self-reply (same repo vs a people-search skill path).
- How the landing-page “#1 on People Search Bench” claim lines up with LessieAI’s published leaderboard (Lessie overall 65.2 in the README table).
- Whether `treg mcp install` is live for all clients or still roadmap-adjacent.
- Devansh’s KYC Genie article (https://x.com/i/article/2091990303062593536) as a separate ingest.

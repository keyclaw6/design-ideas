# treg: OpenRouter-style proxy for 2,896 metered agent tool endpoints

`github-superdesigndev-treg` · github · repo · en · [source](https://github.com/superdesigndev/treg) · [raw](../../../raw/items/github-superdesigndev-treg/)
**Author:** superdesigndev (@superdesigndev) · **Published:** — · **Captured:** 2026-09-02T20:15:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [mcp-and-agent-browsers](../../subjects/mcp-and-agent-browsers/brief.md) · **Also:** [serp-ai-visibility](../../subjects/serp-ai-visibility/brief.md), [outbound-gtm-agents](../../subjects/outbound-gtm-agents/brief.md) · **Roles:** tool, claim-source · **Platforms:** mcp, cli

**Summary.** treg is a Python tools registry and proxy: one token routes agents to thousands of catalogued SEO, people-search, ads, and scraping APIs billed per call, while team-owned keys and skills stay server-side and unmetered.
**Question it answers.** How can agents call SEO and enrichment APIs without buying Semrush-scale subscriptions?

**Claims.**
- `github-superdesigndev-treg#c1` (capability, stated) treg catalogs 2,896 endpoints across 60 providers, priced per call from about one cent. — evidence: "2,896 catalogued endpoints across 60 providers — SEO and backlinks, social and trends, people and company enrichment, ads, scraping — priced per call, from a cent" [linked-page]
- `github-superdesigndev-treg#c2` (recipe, stated) Team-registered API keys always override treg's catalog keys and are never metered. — evidence: "Your own key always wins over treg's, and those calls are never metered." [linked-page]
- `github-superdesigndev-treg#c3` (result, demonstrated) GET treg.to/providers.json is still version 12 with 104 named BYO providers. GET treg.dev/providers.json is 404; treg.dev is not the dump host. — evidence: "treg.to/providers.json HTTP 200 size 23376 version 12 providers.length 104 (Google Ads … OpenWeather). treg.dev/providers.json HTTP 404 size 6888. treg.dev/ 200 599592 B." [note]
- `github-superdesigndev-treg#c4` (availability, demonstrated) leftover30 unused github.com/superdesigndev/treg host string is leftover24 1,190★. No new integers. — evidence: "leftover30-2026-09-05.json skip superdesigndev/treg already leftover24." [note]
**Numbers.** —
**Recipe.** —
**Techniques.** —
**Tools.** [treg](../../tools/treg.md)
**Links.** repo (https://github.com/superdesigndev/treg), product (https://treg.to), https://treg.to/mcp/v2/, https://treg.to/people-search, https://github.com/superdesigndev/treg
**Related items.** [web-treg-people-search](../web-treg-people-search/card.md), [github-LessieAI-people-search-bench](../github-LessieAI-people-search-bench/card.md), [github-iannuttall-seo](../github-iannuttall-seo/card.md)
**Media.** —
**Judge hints.** must_read: True · compare with: [github-punkpeye-awesome-mcp-servers](../github-punkpeye-awesome-mcp-servers/card.md), [web-treg-people-search](../web-treg-people-search/card.md)

# Crowdreply Mcp

**Slug:** `crowdreply-mcp` · **Kind:** product · **URL:** https://crowdreply.io · **Canonical item:** [web-crowdreply](../items/web-crowdreply/card.md)
**Subjects:** [mcp-and-agent-browsers](../subjects/mcp-and-agent-browsers/brief.md), [outbound-gtm-agents](../subjects/outbound-gtm-agents/brief.md), [serp-ai-visibility](../subjects/serp-ai-visibility/brief.md)
**Referenced by (2):**
- [CrowdReply — AI search visibility and citation-outreach platform](../items/web-crowdreply/card.md) — tool, example — serp-ai-visibility
- [CrowdReply Grok Bot setup for AI-answer citation outreach via MCP](../items/x-2094553318031024285/card.md) — technique, tool — serp-ai-visibility

<!-- NOTES:START -->
Fetched 2026-09-04 from https://crowdreply.io/mcp (landing HTML still missing in raw/).

Named tools on the public catalogue, grouped as on the page:

- Visibility & citations (READ): `get_visibility_overview`, `get_visibility_trend`, `list_llm_mentions`, `list_llm_citations`, `list_prompts`
- Brands & projects (READ): `list_brands`, `get_brand`, `list_projects`
- Agent orders (WRITE, two-step confirm, claimed idempotent): `create_task`, `refund_task`, `cancel_task`, `create_group_task`, `send_upvotes`, `add_tracked_keyword`, `add_prompts`, `delete_prompts`, `remove_tracked_keyword`
- Reddit & listening (READ): `find_reddit_threads`, `list_mentions`, `list_tracked_keywords`
- Tasks & billing (READ): `list_tasks`, `get_balance`, `get_usage_metrics`

Also named in marketing copy on the same page, not in the catalogue table: `compare_competitors`, `analyze_prompt_gaps`, `find_citation_sources`.

Count: 18 write/read names in the table + 3 extra marketing names. Endpoint `https://mcp.crowdreply.io/mcp` still 401 without a key (evening re-fetch: HTTP **401**, **24** B `{"error":"Unauthorized"}`). The 4%→40% / 11-week article (`https://x.com/i/article/2094451432208711681`) returned 403 on jina and **404** on later direct fetch.

Citation-outreach marketing page (https://crowdreply.io/features/citation-outreach, 2026-09-04): “You only pay when the mention goes live.” Claimed ops stats: 240+ brands, 1,860+ offsite mentions, 22,400+ cited pages contacted, unpublished charge $0. G2 4.9 / 5,000+ brands repeated. **4%→40% / 11 weeks is not on this page.** `/case-studies` 404’d.

**2026-09-04 capture — homepage.** `GET https://crowdreply.io` **200 / 1,136,240 B**. Title quotes **CrowdReply: The #1 AI Search Visibility Tool** (source ranking language — do not echo as a finding). Visible marketing: Engagement Engine; AI Backlinks Marketplace of **40,000+** publishers; Trusted by **5,000+** brands; 7 day free trial; AI Visibility Score. Do not treat CSS `width:90%` as a metric. **4%→40% / 11 weeks is still not on this homepage.** Receipt `crowdreply-home-2026-09-04.json`.

**2026-09-04 capture — docs/mcp + features 4% is not 4→40.** `https://crowdreply.io/docs/mcp` HTTP **200**, **53,320** B, title “CrowdReply MCP Documentation”, last updated **15 July 2026**. Endpoint `https://mcp.crowdreply.io/mcp/client` (Streamable HTTP). Auth: OAuth 2.1 + PKCE or API key. Accounts without MCP+API get **403** `E_PLAN_GATE`. HTML extract has **58** snake_case tool ids after dropping `org_id` / `public_key` / `sample_*` / `trace_id` / `summary_large_image`. Do not collapse with the **18**-row marketing table. Docs use `add_tracked_keywords` (plural); marketing table used `add_tracked_keyword`. Marketing extras `analyze_prompt_gaps` / `find_citation_sources` / `find_reddit_threads` did not appear in this extract. `/features` (1,025,519 B) has “A brand at 30% on ChatGPT can sit at **4%** on Perplexity” — not 4%→40% / 11 weeks. `/blog` is SiteGround captcha **202**. Sitemap marketing locs: `/pricing`, `/mcp`, `/demo`, `/affiliates`, `/searchmaxxing`.

**2026-09-05 capture — X article 2094451432208711681 body via fxtwitter.** Carrier `dawoodkhan254/2094451439573881015`. **165** blocks / **150** nonempty / **14,763** chars. Title *How I use Grok Bots to rank brands on AI answers that it feels illegal*. First-party copy **does** include **4%→40% visibility on buying questions in 11 weeks**, plus **847** cited domains / **~10%** closed / **85** mentions; **76→127** of 847 cited pages; **2→9** of 17 ChatGPT sources on “the one that mattered most”; **1,860+** offsite mentions; **10,000+** brands. Six named bots: Chief of Staff, Scout, Finder, Writer, Closer, Watcher. Logged-out `x.com/i/article/…` still 404. Do not collapse with `/features` “4% on Perplexity.” Receipt `analysis/_work/captures/crowdreply-x-article-2094451432208711681.json`.

**2026-09-05 leftover24.** Unused `/features/citation-outreach` **396,104 B** restates **5,000+** brands / **240+** / **1,860+** / **22,400+** / unpublished **$0**. MCP stays keyed. Receipt `leftover24-2026-09-05.json`.

**2026-09-05 leftover26.** Unused `mcp.crowdreply.io/mcp` stays keyed — do not hammer. Receipt `leftover26-2026-09-05.json`.
<!-- NOTES:END -->

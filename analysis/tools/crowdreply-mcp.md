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

Count: 18 write/read names in the table + 3 extra marketing names. Endpoint `https://mcp.crowdreply.io/mcp` still 401 without a key. The 4%→40% / 11-week article (`https://x.com/i/article/2094451432208711681`) returned 403 on jina and direct fetch.
<!-- NOTES:END -->

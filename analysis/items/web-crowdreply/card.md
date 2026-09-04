# CrowdReply — AI search visibility and citation-outreach platform

`web-crowdreply` · website · product · en · [source](https://crowdreply.io) · [raw](../../../raw/items/web-crowdreply/)
**Author:** CrowdReply (@—) · **Published:** — · **Captured:** 2026-09-02T20:56:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [serp-ai-visibility](../../subjects/serp-ai-visibility/brief.md) · **Also:** [mcp-and-agent-browsers](../../subjects/mcp-and-agent-browsers/brief.md) · **Roles:** tool, example · **Platforms:** mcp

**Summary.** SaaS for tracking and improving brand citations in assistant answers (ChatGPT, Grok, Perplexity), with citation-outreach workflows and a remote MCP exposing 18+ tools at mcp.crowdreply.io.
**Question it answers.** Which AEO platform pairs citation outreach with an agent-callable MCP?

**Claims.**
- `web-crowdreply#c1` (capability, stated) CrowdReply exposes a remote MCP with 18+ tools for agent workflows. — evidence: "Advertised tool count at ingest: 18+" [linked-page]
- `web-crowdreply#c2` (availability, demonstrated) Unauthenticated MCP probe to the endpoint returns HTTP 401 without an API key. — evidence: "Probe without key: HTTP 401" [linked-page]
- `web-crowdreply#c3` (result, demonstrated) Public /docs/mcp (53,320 B, updated 15 July 2026) names endpoint mcp.crowdreply.io/mcp/client with OAuth 2.1 PKCE. HTML extract has 58 snake_case tool ids — do not collapse with the marketing 18-row table. Features-page 4% is a ChatGPT-vs-Perplexity gap, not 4%→40% in 11 weeks. — evidence: "GET 200 crowdreply.io/docs/mcp; E_PLAN_GATE; 58 snake names after dropping org_id/public_key/sample_*/trace_id. Features: 30% ChatGPT / 4% Perplexity. See crowdreply-mcp NOTES." [note]
- `web-crowdreply#c4` (availability, demonstrated) Live GET https://crowdreply.io is 200 / 1,136,240 B. Title quotes CrowdReply: The #1 AI Search Visibility Tool (source ranking language). Visible marketing: Engagement Engine; AI Backlinks Marketplace of 40,000+ publishers; Trusted by 5,000+ brands; 7 day free trial; AI Visibility Score. 4%→40% / 11 weeks is still not on this homepage. — evidence: "analysis/_work/captures/crowdreply-home-2026-09-04.json" [note]
**Numbers.** —
**Recipe.** —
**Techniques.** [citation-outreach](../../techniques/citation-outreach.md)
**Tools.** [crowdreply-mcp](../../tools/crowdreply-mcp.md)
**Links.** product (https://crowdreply.io/mcp), https://crowdreply.io/features/citation-outreach, https://mcp.crowdreply.io/mcp, https://crowdreply.io/docs/mcp
**Related items.** [github-iannuttall-seo](../github-iannuttall-seo/card.md), [web-known-agency](../web-known-agency/card.md), [web-nqz-ai-search-prompt-generator](../web-nqz-ai-search-prompt-generator/card.md)
**Media.** —
**Judge hints.** must_read: False · compare with: —

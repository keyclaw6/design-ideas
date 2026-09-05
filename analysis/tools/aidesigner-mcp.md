# Aidesigner Mcp

**Slug:** `aidesigner-mcp` · **Kind:** product · **URL:** https://www.aidesigner.ai/ai-ui-design-mcp · **Canonical item:** [web-aidesigner-mcp](../items/web-aidesigner-mcp/card.md)
**Subjects:** [design-agent-skills](../subjects/design-agent-skills/brief.md), [mcp-and-agent-browsers](../subjects/mcp-and-agent-browsers/brief.md)
**Referenced by (2):**
- [AIDesigner remote MCP for in-repo HTML/Tailwind UI design](../items/web-aidesigner-mcp/card.md) — tool, technique — design-agent-skills
- [AIDesigner MCP clones site HTML and CSS into Claude Code projects](../items/x-2094467179320119498/card.md) — tool, example — design-agent-skills

<!-- NOTES:START -->
**2026-09-04 capture — named tools on the marketing page.**
`https://www.aidesigner.ai/ai-ui-design-mcp` heading: “Twenty-one tools. One protocol.” Endpoint in the snippet: `https://api.aidesigner.ai/api/v1/mcp`. Unauthed `initialize` → **401**.

Names listed as tool titles on that page (**22**, not 21): `generate_design`, `refine_design`, `generate_image`, `generate_website_design_image`, `generate_branding_kit_variations`, `generate_media_asset_kit`, `create_brand_kit_from_variation`, `list_brand_kits`, `set_editor_brand_kit`, `save_media_asset_to_brand_kit`, `drop_image_on_canvas`, `remove_image_background`, `vectorize_image`, `extract_image_assets`, `create_editor_session`, `link_editor_session`, `unlink_editor_session`, `list_canvases`, `get_canvas`, `extract_canvas_design`, `get_credit_status`, `whoami`. Quote the page’s “21” as marketing; the title list is 22.

**2026-09-04 evening re-fetch.** `https://www.aidesigner.ai/ai-ui-design-mcp` HTTP 200, **298,652** B, heading still **“Twenty-one tools. One protocol.”** All **22** snake_case titles still present. Unauthed `POST https://api.aidesigner.ai/api/v1/mcp` `initialize` → **401** `{"error":"OAuth access token required."}`. No `tools/list` without a token.

**2026-09-05 docs + npm.** `https://www.aidesigner.ai/docs/mcp` **200 / 202,792 B**. First-party: OAuth for MCP, API keys for REST; `npx -y @aidesigner/agent-skills init` (cursor / claude / codex). Hosts: Claude Code, Codex, Cursor, VS Code/Copilot **project** installs; Windsurf **user-scope only**. MCP Tools Reference names the same **22** snake_case tools. Rate table: `generate_design` + `refine_design` **30 / 60s** per account; concurrent remote generations **4 in flight**. Discovery calls (`initialize`, `tools/list`, `get_credit_status`, `whoami`) are excluded. npm registry `@aidesigner/agent-skills` latest **0.1.4** UNLICENSED (5 versions; homepage `AI-Diffusion-Organization/growthpedia`). npmjs.com HTML **403**. Receipt `analysis/_work/captures/leftover3-2026-09-05.json`.
<!-- NOTES:END -->

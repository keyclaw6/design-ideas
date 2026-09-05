# AIDesigner remote MCP for in-repo HTML/Tailwind UI design

`web-aidesigner-mcp` · website · product · en · [source](https://www.aidesigner.ai/ai-ui-design-mcp) · [raw](../../../raw/items/web-aidesigner-mcp/)
**Author:** AIDesigner (@aidesigner) · **Published:** — · **Captured:** 2026-09-02T20:38:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [design-agent-skills](../../subjects/design-agent-skills/brief.md) · **Also:** [mcp-and-agent-browsers](../../subjects/mcp-and-agent-browsers/brief.md) · **Roles:** tool, technique · **Platforms:** mcp, cursor, claude-code

**Summary.** Remote MCP server with 21 tools that generates, refines, and clones production HTML/Tailwind UI inside Cursor, Claude Code, Codex, and Windsurf, including URL clone/enhance/inspire modes and editor-session pairing via OAuth.
**Question it answers.** How do I wire an MCP server to generate and refine landing UI inside my repo?

**Claims.**
- `web-aidesigner-mcp#c1` (capability, stated) AIDesigner exposes 21 MCP tools for design generation, refinement, brand kits, and editor sessions. — evidence: "21 MCP tools — design generation, live canvas streaming, brand kits, image tools, editor session pairing, credits." [linked-page]
- `web-aidesigner-mcp#c2` (recipe, stated) URL modes include clone, enhance, and inspire for competitor references. — evidence: "Pass a reference URL with `mode`: clone (near 1:1), enhance (modernize), inspire (visual language only)." [linked-page]
- `web-aidesigner-mcp#c3` (result, demonstrated) AIDesigner marketing page still says Twenty-one tools and lists 22 snake_case titles. Unauthed MCP initialize returns 401 OAuth access token required. — evidence: "2026-09-04 evening: page 200 298652 B; all 22 names present; POST api.aidesigner.ai/api/v1/mcp initialize 401 {"error":"OAuth access token required."}" [note]
- `web-aidesigner-mcp#c4` (capability, demonstrated) Official /docs/mcp 200 / 202,792 B documents the same 22 tools, OAuth for MCP / API keys for REST, and rate limits: generate_design + refine_design 30 / 60s per account; 4 concurrent remote generations. Hosts: Claude Code, Codex, Cursor, VS Code/Copilot project installs; Windsurf user-scope only. Bootstrap is npx -y @aidesigner/agent-skills init. npm latest 0.1.4 UNLICENSED. — evidence: "GET 200 https://www.aidesigner.ai/docs/mcp 202792 B. Rate table 30/60s and 4 in flight. leftover3-2026-09-05.json" [note]
**Numbers.** —
**Recipe.** —
**Techniques.** [url-clone-ui](../../techniques/url-clone-ui.md), [design-md-contract](../../techniques/design-md-contract.md)
**Tools.** [aidesigner-mcp](../../tools/aidesigner-mcp.md), [aidesigner-agent-skills](../../tools/aidesigner-agent-skills.md)
**Links.** product (https://api.aidesigner.ai/api/v1/mcp), https://www.aidesigner.ai/docs/mcp, https://www.aidesigner.ai/website-cloner
**Related items.** [github-nexu-io-open-design](../github-nexu-io-open-design/card.md), [web-getlayers-ai](../web-getlayers-ai/card.md), [github-google-labs-code-design-md](../github-google-labs-code-design-md/card.md)
**Media.** —
**Judge hints.** must_read: False · compare with: —

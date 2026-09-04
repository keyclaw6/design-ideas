# AIDesigner MCP

**Landing:** https://www.aidesigner.ai/ai-ui-design-mcp  
**Docs:** https://www.aidesigner.ai/docs/mcp  
**MCP endpoint:** https://api.aidesigner.ai/api/v1/mcp  
**Website cloner:** https://www.aidesigner.ai/website-cloner  
**npm bootstrap:** `@aidesigner/agent-skills` v0.1.4

Lightweight MCP server for Claude Code, Codex, Cursor, VS Code/Copilot, and Windsurf — generate, refine, and adopt production-ready UI designs inside a repo.

## Setup

```bash
npx -y @aidesigner/agent-skills init <host>
```

Example `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "aidesigner": {
      "url": "https://api.aidesigner.ai/api/v1/mcp"
    }
  }
}
```

OAuth sign-in once per host; CLI writes host-specific config (Claude Code also gets agents, commands, and skill markdown).

## Product positioning

- **Design as compilation target** — layout, styling, preview rendering handled by MCP; agent iterates visually.
- **Production-grade output** — Tailwind CSS, typography hierarchy (not generic templates).
- **Repo-aware context** — detects framework, component library, CSS tokens, routes.
- **21 MCP tools** — design generation, live canvas streaming, brand kits, image tools, editor session pairing, credits.

## Core design tools

| Tool | Purpose |
|------|---------|
| `generate_design` | Full HTML/Tailwind UI from prompt; viewports desktop/mobile; optional `design_mode`: classic / ultradesign |
| `refine_design` | Natural-language iteration on prior run or HTML |
| `generate_image` / `generate_website_design_image` | Standalone or page-slice imagery; brand-kit steering |
| Brand kit tools | Variations board, list/set kits, save media assets |
| Editor session tools | `create_editor_session`, `link_editor_session` (6-char code), `list_canvases`, `get_canvas`, `extract_canvas_design` |
| Account | `get_credit_status`, `whoami` |

## URL-based workflows (clone / enhance / inspire)

Pass a reference URL with `mode`:

| Mode | Behavior |
|------|----------|
| **clone** | Near 1:1 recreation — layout, typography, colors, content |
| **enhance** | Modernize while keeping content |
| **inspire** | Extract visual language without copying content |

Website analysis costs 1 credit (same as web cloner). Browser cloner: paste URL → editable semantic HTML + Tailwind in ~1 min.

## Website cloner (browser product)

From https://www.aidesigner.ai/website-cloner:

1. Paste any public URL
2. AI rebuilds layout, type, colors, content as real code (not a screenshot)
3. Edit in visual editor or hand off via MCP to integrate into React/Next.js

Output: semantic HTML + Tailwind; responsive layout; export anytime; one-click publish with SSL/CDN.

## Rate limits (MCP)

- `generate_design` / `refine_design`: 30 per 60s per account
- Concurrent remote generations: 4 in flight
- Discovery calls (`whoami`, `get_credit_status`, `tools/list`) not rate-limited

## Auth

- MCP: OAuth (recommended)
- REST/backend: API keys from https://www.aidesigner.ai/settings/api-keys

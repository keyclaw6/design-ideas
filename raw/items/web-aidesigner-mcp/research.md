# Research

## What it is

AIDesigner’s remote MCP (api.aidesigner.ai) for Claude Code, Codex, Cursor, Copilot, Windsurf: generate, refine, and adopt production-ready HTML/Tailwind UI inside an existing repo, with URL clone/enhance/inspire modes.

## How it works

- Bootstrap: `npx -y @aidesigner/agent-skills init <host>` writes MCP config; OAuth once per host.
- 21 tools: `generate_design` / `refine_design`, image tools, brand kits, editor sessions (6-char pairing codes), canvases, credits/`whoami`.
- Repo-aware: detects framework, component library, CSS tokens, routes so output is not a generic template.
- URL modes: clone (near 1:1), enhance (modernize, keep content), inspire (visual language only).
- Design treated as a compilation target — layout/styling/preview happen in MCP; the agent iterates visually.

## Why saved

In-editor design MCP complementary to OpenDesign (local desktop) and DESIGN.md extractors (tokens only). Useful when the marketing site already lives in git.

## Topics

`mcp`, `design`, `agent-skills`

## Related

`github-google-labs-code-design-md`, `web-getlayers-ai`, `github-nexu-io-open-design`, `web-design-md-hyperbrowser`, `github-punkpeye-awesome-mcp-servers`

## Use when

Generating or cloning a landing inside Cursor via MCP; pairing a visual editor session to a repo; extracting a competitor’s visual language without copying copy.

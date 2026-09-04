# Research

## What it is
CopilotKit’s `@copilotkit/aimock`: mock everything an AI app talks to (LLM APIs, MCP, A2A, AG-UI, vector DBs, search) on one port, zero deps. Docs: https://aimock.copilotkit.dev — repo: https://github.com/CopilotKit/aimock

## How it works
- Single npm package, one local port, full mock stack.
- Lets you develop/test agent UIs and MCP clients without live keys or quota.
- Open source; tweet is the “go break it” launch note (thread may be truncated).

## Why saved
Needed when building MCP/design-in-editor or SEO agent tools: deterministic mocks beat hitting production APIs.

## Topics
- `agent-skills`
- `mcp`

## Related
- `github-superdesigndev-treg` — OpenRouter-for-tools
- `web-aidesigner-mcp` — design MCP
- `github-punkpeye-awesome-mcp-servers` — MCP catalog
- `web-blume-codes` — agent monitoring sidecar

## Use when
Writing tests or local demos for MCP/agent UIs. Install aimock instead of stubbing each vendor.

## What they are actually doing

robin is amplifying a Claude Code demo (Spanish: “this person gave Claude Code the ability to replicate any site’s design”). The tweet itself has **no URL**. A reply asks “Wheres the link?” and is unanswered in the visible thread.

**From the attached video** (not from a tweet link): the operator is in `C:\Users\tyler\OneDrive\Documents\GitHub\aidesigner-mcp-demo`, running Claude Code with skill `aidesigner-frontend` and MCP tool `get_credit_status`. Prompts include “CLONE browserbase.com using the aidesigner MCP”, Linear-inspired generate (`mode: "inspire"`, `url: "https://linear.app"`), and a PostHog-inspired landing. Side-by-sides compare localhost clones to cluely.com and other live sites.

That matches **AIDesigner MCP**, a hosted remote MCP (not a public GitHub app repo at capture):

- Product: https://www.aidesigner.ai/ai-ui-design-mcp (v0.1.0 “now available on npm”)
- Docs: https://www.aidesigner.ai/docs/mcp
- MCP endpoint in Cursor config: `https://api.aidesigner.ai/api/v1/mcp`
- Bootstrap CLI on npm: `@aidesigner/agent-skills` (“Multi-host AIDesigner MCP bootstrap”; `aidesigner init`). Linked GitHub path `AI-Diffusion-Organization/growthpedia` **404’d** on the GitHub API at capture.
- Claude extras the CLI writes: `.claude/skills/aidesigner-frontend/SKILL.md`, `/aidesigner` command — same names as the video.
- URL workflows on the product page: Clone / Enhance / Inspire from a reference URL (layout, typography, colors). Credits via `get_credit_status`; OAuth, not a local HTML parser.

No public `aidesigner-mcp-demo` repository showed up in GitHub search. **Name collision:** npm `aidesigner` / `bacoco/aidesigner` is a different “universal AI agent framework” (BMAD-style), not the video product.

## Open questions

- Who “esta persona” / `tyler` is (original demo author); robin does not name them.
- Whether `@aidesigner/agent-skills` is the v0.1.0 package the landing page means, given the growthpedia GitHub 404.
- How much of a clone is HTML/CSS extraction vs screenshot-to-layout generation (Dima’s reply: states, responsive, a11y).

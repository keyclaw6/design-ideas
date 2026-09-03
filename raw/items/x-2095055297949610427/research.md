## What they are actually doing

Author feedback ask, not a launch thread. The linked repo is real.

**Repo** — `https://github.com/iannuttall/seo` (Apache-2.0, 378★ / 28 forks at capture). Homepage `https://seoskill.dev`. npm unscoped `seo` **0.2.40**. Node 22+.

- Positioning: “The only SEO skill your agent needs. 70+ SEO audit tools through a local CLI and MCP server, using your own crawl, Search Console, and GA4 data.”
- Quick start: `npm i -g seo` → `seo start` → `seo report`.
- Optional research providers in-package: DataForSEO, Semrush, Ahrefs.
- MCP: `seo mcp serve`. Skill at `skills/seo` (router; report depth via `seo reports describe`). Canonical skill index: `https://seoskill.dev/.well-known/agent-skills/index.json`.
- Local-first: crawl + GSC + traffic analytics; evidence-backed reports for agents.

Ian’s tweet is him doubting the “all we need” README (exactly what [@midego1](https://x.com/midego1) called out) and leaning toward smaller single-purpose tools.

## Open questions

- Whether he splits the 70+ tool CLI after this thread.
- Full 26-reply bug/simplicity dump still login-walled.

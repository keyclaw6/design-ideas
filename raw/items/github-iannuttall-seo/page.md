# SEO Skill

**Repo:** iannuttall/seo  
**Homepage:** https://seoskill.dev  
**Stars:** 380 · **License:** Apache-2.0 · **npm:** `seo@0.2.40` · **Node:** 22+

The SEO command for AI agents. Audit sites, find search opportunities, research competitors, and verify work from one local CLI and MCP server — using your own crawl, Search Console, and GA4 data.

## Quick start

```sh
npm i -g seo
seo start
seo report
```

`seo report --url https://example.com` runs a local technical crawl with no Google sign-in.

## Core capabilities

- Technical audits: metadata, links, indexability, canonicals, structured data, performance, security, mobile, i18n, social previews
- Search Console + GA4 integration; optional DataForSEO, Semrush, Ahrefs research providers
- 70+ report types; ranked action queue with stable rule IDs
- JSON/Markdown/HTML export; CI-friendly `--json` and `--fail-on`
- **MCP server** — `seo mcp install` exposes tools to Cursor and other MCP clients
- **Packaged agent skill** — `seo skill list`

## Key commands

| Command | Purpose |
| --- | --- |
| `seo start` | Connect Google data, save project profile |
| `seo report` | Main SEO report |
| `seo quick-wins` | Ranking 4–10, low-CTR opportunities |
| `seo crawl` | Full or sitemap-health crawl |
| `seo mcp install` | Wire MCP into local agents |
| `seo indexnow submit` | Notify IndexNow after changes |

## Agent / CI use

- Deterministic JSON, evidence separated from heuristics
- Service account auth for unattended GitHub Actions
- Provider plugin API for custom research backends

## Links

- Docs: https://seoskill.dev/docs
- MCP: https://seoskill.dev/features/mcp
- npm: https://www.npmjs.com/package/seo

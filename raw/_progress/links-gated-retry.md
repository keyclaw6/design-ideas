# Links Gated Retry — Manifest

Retried: 2026-09-02T17:20Z  
Method: `r.jina.ai` (primary), `gh` (GitHub README fallback), `curl` (connectivity check)

| ID | URL | Retry | Status | Notes |
|----|-----|-------|--------|-------|
| web-meigen-ai | https://www.meigen.ai/ | jina | **recovered** | Full homepage (~10KB); prompt gallery, categories, MCP link. Prior Cloudflare block cleared. |
| web-checklist-design | https://www.checklist.design/ | jina | **recovered** | Full homepage (~35KB); 5 category indexes, 40+ checklist links, Figma/agent skill integrations. |
| web-recent-design | https://recent.design/ | jina | **recovered** | Full feed (~16KB). `www.recent.design` has no DNS — URL corrected to apex. |
| web-cult-ui | https://www.cult-ui.com/ | jina + gh | **partial** | r.jina.ai → Vercel Security Checkpoint 429. Content enriched from `nolly-studio/cult-ui` README via `gh`. |

## Metadata

All four `source.json` files updated with `extra.retry = "jina"`.

| ID | `extra.error` |
|----|---------------|
| web-meigen-ai | *(cleared — capture succeeded)* |
| web-checklist-design | *(cleared — capture succeeded)* |
| web-recent-design | `www.recent.design DNS unresolved; apex recent.design works` |
| web-cult-ui | `Vercel Security Checkpoint 429 on r.jina.ai; content from GitHub README via gh` |

## Summary

- **3/4** fully recovered via r.jina.ai
- **1/4** partial — cult-ui homepage still gated; GitHub mirror is authoritative
- **4/4** item folders updated in place (`page.md`, `research.md`, `source.json`)

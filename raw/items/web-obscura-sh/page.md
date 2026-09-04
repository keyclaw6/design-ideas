# Obscura (obscura.sh)

**URL:** https://obscura.sh  
**Docs:** https://docs.obscura.sh  
**Repo:** https://github.com/h4ckf0r0day/obscura

Marketing site for an open-source Rust headless browser aimed at AI agents and automation at scale.

## Problem framing (site)

Chrome was built for humans browsing one page at a time, not software running thousands of sessions. At scale that shows up as cost, latency, and flaky results.

| Pain | Claim |
|------|-------|
| Heavy at scale | Each Chrome instance eats memory/CPU; thousands of instances inflate bills for unused UI features |
| Slow to start | Cold starts in seconds; pipelines lose throughput |
| State bleeds | Cookies, logins, cached data carry over — data leaks and non-reproducible runs |

## Product thesis

Obscura keeps only what machines need — faster, cheaper, safer than Chrome without rewrites.

| Capability | Claim |
|------------|-------|
| Boot on demand | Sessions boot in **<50 ms** |
| Clean every time | Fresh sandbox per session; reproducible runs |
| More per machine | Fraction of Chrome's memory → more concurrent sessions |
| Keep your stack | Playwright + CDP compatible — point existing scripts at Obscura |

## Documentation (docs.obscura.sh)

Intro describes Obscura as open-source headless browser in Rust: V8 JavaScript, Chrome DevTools Protocol, Puppeteer/Playwright drop-in.

Docs sections: Quickstart (install, first fetch, extract data, connect Puppeteer/Playwright), Guides (MCP server, markdown extraction, production scale, Rust library), Reference (CLI, env vars), Contributing (architecture, CDP/Web API).

Docs index: https://docs.obscura.sh/llms.txt

## Related

- GitHub: [github-h4ckf0r0day-obscura](../github-h4ckf0r0day-obscura/page.md)
- Cloudflare ported Obscura to Workers as Kitesurf prototype: [web-cloudflare-kitesurf](../web-cloudflare-kitesurf/page.md)

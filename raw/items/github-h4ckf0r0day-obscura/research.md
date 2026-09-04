# Research

## What it is

Apache-2.0 Rust headless browser (h4ckf0r0day/obscura, ~24k stars) for agent automation and scraping: V8 JS, CDP, Puppeteer/Playwright drop-in, native screenshot/PDF without shipping Chromium.

## How it works

- Claims ~30 MB RAM / 70 MB binary / 85 ms page load vs Chrome ~200 MB / 300 MB / 500 ms; instant startup vs ~2s.
- CDP on 9222; Docker `h4ckf0r0day/obscura`; binaries for Linux/macOS/Windows; AUR and Nix packages.
- CLI: `./obscura fetch URL --eval "document.title"`; optional rendering-off and stealth-transport release variants (engine only — no anti-detect procedures recorded here).
- Docs at docs.obscura.sh include an MCP server guide and `llms.txt`.
- README states Cloudflare started Kitesurf by porting Obscura to Workers. Hosted Obscura Cloud is waitlist (proxies/support); OSS engine stays fully featured.

## Why saved

Agent browser cost and isolation are the bottleneck for SEO crawls, DESIGN.md extraction, and scroll-craft screenshot verification. This is the OSS engine behind the marketing site and the Kitesurf origin story.

## Topics

`agent-skills`, `mcp`

## Related

`web-obscura-sh`, `web-cloudflare-kitesurf`, `github-punkpeye-awesome-mcp-servers`, `web-aidesigner-mcp`, `github-nateherkai-scroll-craft`

## Use when

Choosing a headless browser for agents (vs Playwright Cloud / Browser Run); wiring MCP fetch; comparing Cloudflare Kitesurf; isolated sessions for crawl/audit skills.

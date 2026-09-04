# Research

## What it is
KERNEL (usekernel) cloud browsers now accept a custom proxy plus a CA bundle, installed into the browser trust store at proxy-create time.

## How it works
- Product is an agent-facing browser (same lane as Obscura / Kitesurf): isolated Chromium sessions for tools that need a real page.
- New API: when you create a proxy, pass a CA bundle; KERNEL installs it in the browser trust store automatically.
- Unlocks TLS interception, corporate MITM proxies, and private PKI without baking certs into a custom image.
- Capture includes a screenshot of the proxy/CA flow (media/media_0.jpg).
- Operational detail for SEO agents and design-extraction agents that must crawl staging sites behind custom TLS.

## Why saved
KB’s browser-for-agents cluster (Obscura, Kitesurf) is the crawl/screenshot substrate for DESIGN.md extraction and SEO audits. Custom CA support is the missing piece for private or MITM-proxied sites.

## Topics
`agent-skills`, `mcp`

## Related
- `github-h4ckf0r0day-obscura` — headless browser for AI agents
- `web-cloudflare-kitesurf` — agent-first browser on Workers
- `web-obscura-sh` — product site for per-agent browsers
- `github-punkpeye-awesome-mcp-servers` — MCP routing for browser tools

## Use when
An agent browser must hit sites with private PKI, a corporate proxy, or TLS inspection, or when comparing KERNEL vs Obscura/Kitesurf for crawl infrastructure.

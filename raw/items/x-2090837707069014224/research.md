## What it is

A note that some sites change payload based on well-known AI crawler User-Agent strings (examples named: OpenAI File Downloader, XaiImageApiFetch, Claude-User), including LinkedIn showing less clickbait/paywall chrome to Claude-User.

## How it works

- This is crawler-behavior intel for AEO/SEO: publishers already special-case AI agents.
- Relevant when building honest agent browsers (Obscura, Kitesurf) that must identify as agents, not as stealth clients.
- Also relevant to citation/AEO work: what an AI crawler sees may not match what a human sees.
- Do not treat this item as a bypass cookbook. Paywall circumvention and impersonation are out of scope for this library.
- Use it to document that UA-based content negotiation exists, then prefer official crawler programs and logged-in human review.

## Why saved

KB's SEO/AEO lane and agent-browser lane both need to know that AI UAs get different HTML. Saved as a warning, not a trick.

## Topics

`agent-skills`, `seo-agents`

## Related

`github-h4ckf0r0day-obscura`, `web-cloudflare-kitesurf`, `web-obscura-sh`, `web-crowdreply`

## Use when

Investigating how a site treats AI crawlers vs users, designing an agent browser's default UA policy, or debugging why an agent fetch diverges from a human screenshot.

# Research

## What it is

Cloudflare blog (2026-08-06) introducing Kitesurf: an agent-first browser running entirely on Workers, sold via Browser Run (free in beta). Built because Chromium is too heavy for per-agent sessions.

## How it works

- Origin: port of Obscura (Rust headless) to Workers with AI assistance, then a 12-week production build.
- Agents optimize for tokens, scale, cost — not tabs/60fps. Threat model: prompt injection/tool safety over pixel-perfect rendering.
- Stack: Rust→Wasm, WPT + Puppeteer visual regression vs Chromium, fail to blank frame never dead session, Workers isolation, stateless burst components.
- Architecture: Engine (CDP WS + REST, Puppeteer/Playwright compatible), PageScript, PageRenderer; SandboxOutbound is sole egress with per-page cookie jars.
- Capture truncated mid-PageRenderer; architecture/origin complete.

## Why saved

Vendor validation of Obscura’s direction and a hosted path (Browser Run) vs self-hosting the Rust binary. Relevant to SEO crawls and screenshot verification at scale.

## Topics

`agent-skills`, `mcp`

## Related

`github-h4ckf0r0day-obscura`, `web-obscura-sh`, `github-punkpeye-awesome-mcp-servers`, `github-nateherkai-scroll-craft`, `web-aidesigner-mcp`

## Use when

Choosing Browser Run vs Obscura binary vs Playwright cloud; reading the Workers isolation model; CDP-compatible agent browsers.

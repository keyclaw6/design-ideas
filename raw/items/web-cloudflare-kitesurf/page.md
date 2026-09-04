# Introducing Kitesurf

**URL:** https://blog.cloudflare.com/kitesurf/  
**Published:** 2026-08-06  
**Product:** [Browser Run](https://developers.cloudflare.com/browser-run/) — free while in beta

Agent-first browser running **entirely on Cloudflare Workers**, built for AI agents rather than human browsing.

## Motivation

Chromium was built for humans, not agents — heavy memory/compute makes per-agent browser instances prohibitively expensive.

Agents care about: token count, context windows, scalability, performance, cost — not tabs, themes, extensions, or 60fps scrolling.

**Threat model differs:** prompt injection and tool safety prioritized over pixel-perfect rendering.

## Origin: Obscura

Initial inspiration from [Obscura](https://github.com/h4ckf0r0day/obscura) — Rust headless engine with "no Chrome, no Node.js, no dependencies."

Cloudflare ported Obscura to Workers with AI assistance; after a detailed success plan, prototype worked → 12-week build.

## Design decisions

| Decision | Rationale |
|----------|-----------|
| **Tests (WPT + integration)** | Web Platform Tests for conformance; Puppeteer visual regression vs Chromium on real sites |
| **Rust → Wasm** | Native Rust via wasm-bindgen, avoid bulky Emscripten layers |
| **Exception handling** | Failures → blank frame/missing element, never dead session |
| **Isolation** | Every page load untrusted; components get minimal resources (Workers isolate model + app-level enforcement) |
| **Stateless when possible** | Disposable, parallel components; burst automation workloads |

## Architecture (high level)

Three main components: **Engine**, **PageScript**, **PageRenderer**.

**Engine** — public CDP WebSocket + HTTP REST; session state; Puppeteer/Playwright/DevTools compatible.

**SandboxOutbound worker** — sole network egress; CORS, browser-shaped headers, per-page cookie jars; Dynamic Workers enforcement.

**PageScript** — Dynamic Workers spin long-lived isolates per page/OOPIF; Blitz (HTML/CSS parse) + Stylo (CSS); V8 scripts in isolate; Boa JS for eval until native Workers eval lands.

Request lifecycle diagram in full post (fetch → parse → render pipeline).

## Platform primitives used

- WebAssembly on Workers
- Dynamic Workers
- SQLite Durable Objects
- Worker-to-worker RPC / service bindings
- Higher Node.js compatibility and limits

## Availability

Kitesurf available in **Browser Run** during beta. CDP endpoint compatible with existing Browser Run Puppeteer integration.

## Related library items

- [github-h4ckf0r0day-obscura](../github-h4ckf0r0day-obscura/page.md) — upstream open-source engine
- [web-obscura-sh](../web-obscura-sh/page.md) — Obscura marketing/docs

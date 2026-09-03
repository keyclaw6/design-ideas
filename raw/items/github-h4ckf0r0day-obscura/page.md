# Obscura (GitHub)

**Repo:** h4ckf0r0day/obscura  
**Homepage:** https://obscura.sh  
**Docs:** https://docs.obscura.sh  
**Stars:** 23,989 · **Forks:** 1,762 · **License:** Apache-2.0 · **Language:** Rust

> *The open-source headless browser for AI agents and web scraping. Lightweight, stealthy, and built in Rust.*

## Stated purpose (README)

Obscura is a headless browser engine written in Rust, built for web scraping and AI agent automation. It runs real JavaScript via V8, supports the Chrome DevTools Protocol, and acts as a drop-in replacement for headless Chrome with Puppeteer and Playwright.

**Native rendering (no Chromium required):** capture screenshots, screencast live pages, and export PDFs directly with Obscura.

## vs headless Chrome (project comparison table)

| Metric | Obscura | Headless Chrome |
|--------|---------|-----------------|
| Memory | 30 MB | 200+ MB |
| Binary size | 70 MB | 300+ MB |
| Page load | 85 ms | ~500 ms |
| Startup | Instant | ~2s |
| Puppeteer | Yes | Yes |
| Playwright | Yes | Yes |

## Cloudflare Kitesurf connection

README notes Obscura inspired Cloudflare Kitesurf's first prototype — Cloudflare began by porting Obscura to Workers while developing its agent-first browser. See [web-cloudflare-kitesurf](../web-cloudflare-kitesurf/page.md).

## Obscura Cloud (hosted)

Waitlist for managed infrastructure, residential proxies, and dedicated support. Open-source engine stays Apache-2.0, fully featured; no feature gating claimed.

## Install (summary)

- Release binaries: Linux x86_64/ARM64, macOS Apple Silicon/Intel, Windows zip — from [Releases](https://github.com/h4ckf0r0day/obscura/releases)
- No Chrome, no Node.js, no dependencies (per README)
- Docker: `docker run -d --name obscura -p 127.0.0.1:9222:9222 h4ckf0r0day/obscura`
- Package managers: AUR (`yay -S obscura-browser`), NixOS (`nix-env -iA nixpkgs.obscura`)

Release archive variants include rendering on/off and optional stealth transport builds (see release naming on GitHub).

## CLI example

```bash
./obscura fetch https://example.com --eval "document.title"
```

## Ecosystem

- Documentation: https://docs.obscura.sh (GitBook; `llms.txt` at docs root)
- MCP server guide listed in docs nav
- CDP on port 9222 (Docker default)

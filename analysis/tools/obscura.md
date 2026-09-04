# Obscura

**Slug:** `obscura` · **Kind:** repo · **URL:** https://github.com/h4ckf0r0day/obscura · **Canonical item:** [github-h4ckf0r0day-obscura](../items/github-h4ckf0r0day-obscura/card.md)
**Subjects:** [mcp-and-agent-browsers](../subjects/mcp-and-agent-browsers/brief.md)
**Referenced by (3):**
- [Obscura — Apache-2.0 Rust headless browser for agent automation](../items/github-h4ckf0r0day-obscura/card.md) — tool, reference — mcp-and-agent-browsers
- [Obscura — Rust headless browser for agent-scale automation](../items/web-obscura-sh/card.md) — tool, reference — mcp-and-agent-browsers
- [Viral Obscura tweet — Rust agent browser at 30MB RAM, Puppeteer-compatible](../items/x-2094427822064279870/card.md) — claim-source, reference — mcp-and-agent-browsers

<!-- NOTES:START -->
**2026-09-04 capture — v0.2.1 x86_64-linux binary boot.** Release tag `v0.2.1`; `obscura --version` prints `obscura 0.2.1`. Assets: `obscura` **105,616,672** B + `obscura-worker` **95,479,240** B (README “70 MB” binary is below this pair). `./obscura fetch https://example.com --eval "document.title"` → `Example Domain`. `./obscura fetch https://example.com --screenshot` → PNG **17,130** B, **1280×720** RGBA (`analysis/_work/captures/obscura-example.png`). `./obscura serve --port 19222`: idle RSS **24,480–25,068 KB** (~24.5–25.1 MB) for the serve process (no worker child in `ps`). `GET /json/version` 200: `Browser` `Chrome/145.0.0.0`, `Protocol-Version` `1.3`, `webSocketDebuggerUrl` `ws://127.0.0.1:19222/devtools/browser`. Do not collapse idle-serve RSS with the README “30 MB” marketing row or with a page-loaded session.
<!-- NOTES:END -->

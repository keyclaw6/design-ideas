# Obscura

**Slug:** `obscura` · **Kind:** repo · **URL:** https://github.com/h4ckf0r0day/obscura · **Canonical item:** [github-h4ckf0r0day-obscura](../items/github-h4ckf0r0day-obscura/card.md)
**Subjects:** [mcp-and-agent-browsers](../subjects/mcp-and-agent-browsers/brief.md)
**Referenced by (3):**
- [Obscura — Apache-2.0 Rust headless browser for agent automation](../items/github-h4ckf0r0day-obscura/card.md) — tool, reference — mcp-and-agent-browsers
- [Obscura — Rust headless browser for agent-scale automation](../items/web-obscura-sh/card.md) — tool, reference — mcp-and-agent-browsers
- [Viral Obscura tweet — Rust agent browser at 30MB RAM, Puppeteer-compatible](../items/x-2094427822064279870/card.md) — claim-source, reference — mcp-and-agent-browsers

<!-- NOTES:START -->
**2026-09-04 capture — v0.2.1 x86_64-linux binary boot.** Release tag `v0.2.1`; `obscura --version` prints `obscura 0.2.1`. Assets: `obscura` **105,616,672** B + `obscura-worker` **95,479,240** B (README “70 MB” binary is below this pair). `./obscura fetch https://example.com --eval "document.title"` → `Example Domain`. `./obscura fetch https://example.com --screenshot` → PNG **17,130** B, **1280×720** RGBA (`analysis/_work/captures/obscura-example.png`). `./obscura serve --port 19222`: idle RSS **24,480–25,068 KB** (~24.5–25.1 MB) for the serve process (no worker child in `ps`). `GET /json/version` 200: `Browser` `Chrome/145.0.0.0`, `Protocol-Version` `1.3`, `webSocketDebuggerUrl` `ws://127.0.0.1:19222/devtools/browser`. Do not collapse idle-serve RSS with the README “30 MB” marketing row or with a page-loaded session.

**2026-09-04 capture — page-loaded serve RSS via CDP.** `./obscura serve --port 19233 --workers 1`. Browser WS `Target.createTarget({url:"https://example.com"})` then `Target.attachToTarget` + `Runtime.evaluate`: `title=Example Domain`, `url=https://example.com/`. `/json/new` HTTP is empty-reply; page-1 WS without Target attach returns `-32601 No page`. Serve PID RSS while the page stayed loaded: **37,856 KB** (~37.0 MB), three samples identical; threads 9 vs idle 7. Idle on this same binary was 24.5–25.1 MB. Still one process (no worker child). Do not collapse with the README “30 MB” row.

**2026-09-04 capture — fetch CLI on tinyshelf (not serve).** `./obscura fetch https://www.tinyshelf.co/ --eval 'document.title + "|" + document.body.innerText.length' --screenshot analysis/_work/captures/obscura-tinyshelf.png` exit 0. Title **TinyShelf**; body text length **13,883**; PNG **73,559** B; captureState view **1280×720**, `scrollHeight` **3158**. This is the fetch CLI, not a CDP page-loaded serve session. Do not invent tinyshelf page-loaded RSS from this command.

**2026-09-04 capture — tinyshelf page-loaded serve RSS via CDP.** Fresh `./obscura serve --port 19255 --workers 1`. Idle VmRSS **25,108 KB** ×3. `Target.createTarget({url:"https://www.tinyshelf.co/"})` + attach + `Runtime.evaluate`: `title=TinyShelf`, `url=https://www.tinyshelf.co/`, `bodyLen=13883`, `scrollHeight=3158`, `clientHeight=720`, `ready=complete`. Loaded VmRSS **73,080 KB** ×3 (~71.4 MB); **20** threads. Bank `analysis/_work/captures/obscura-tinyshelf-cdp.json`. Heavier than example.com **37,856 KB**. Still one process. Do not collapse with README “30 MB”, idle ~25 MB, example.com 37.0 MB, or the fetch-CLI PNG.

**2026-09-05 leftover16 attach.** Publisher UA leftover ([x-2090837707069014224](../items/x-2090837707069014224/card.md)) is site×bot HTML variance (Claude-User / GPTBot), not this headless agent browser.

**2026-09-05 leftover24.** Unused `obscura.sh` **11,965 B**: Star **16.2k**; **<50ms** session start; **10×** leaner vs Chrome. `docs.obscura.sh` **926,821 B** GitBook SPA. Do not collapse 16.2k with local RSS. Receipt `leftover24-2026-09-05.json`.
<!-- NOTES:END -->

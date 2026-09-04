# Complete Shelf

**Slug:** `complete-shelf` · **Kind:** repo · **URL:** https://mengto.github.io/complete-shelf/ · **Canonical item:** [github-mengto-complete-shelf](../items/github-mengto-complete-shelf/card.md)
**Subjects:** [web-3d-scenes](../subjects/web-3d-scenes/brief.md)
**Referenced by (1):**
- [MengTo Complete Shelf — single-file Three.js interactive book demo](../items/github-mengto-complete-shelf/card.md) — example, tool — web-3d-scenes

<!-- NOTES:START -->
Fetched 2026-09-04 README + live `https://mengto.github.io/complete-shelf/` (curl, no headed FPS).

Seven clothbound volumes (Codex, Claude Code, Cursor, Antigravity, Figma, Framer, Xcode). Whole experience in `index.html` (no bundler/backend/MCP). State machine: `shelf → opening detail → closed inspection → open book → closing → shelf`. Three.js PBR + OrbitControls; cloth/foil/paper/wood textures; Pika-generated MP3s embedded as data URLs.

**Transfer (2026-09-04, this host):** `index.html` **2,233,796 bytes** uncompressed, **1,574,186 bytes** gzip on the wire. README still pulls Three.js **r165** from jsDelivr (`three.module.js` 1,284,652 + OrbitControls 32,250 + RoomEnvironment 3,623 + RoundedBoxGeometry 4,625 + RectAreaLightUniformsLib 313,854 ≈ **1.64 MB** extra) and Inter from Google Fonts. “Single file” is the app body; first paint is HTML + CDN Three + font, not 2.2 MB alone. GitHub: 664 stars, **no SPDX license** on the API payload.

**2026-09-04 capture — CPU rAF on SwiftShader (GPU unknown).** Headless Playwright Chromium, `--use-angle=swiftshader`, viewport 1440×900, live `https://mengto.github.io/complete-shelf/` HTTP 200. Document title **Working Volumes — Seven Tools for Making**. Canvas **1440×900**. `WEBGL_debug_renderer_info`: renderer `ANGLE (Google, Vulkan 1.3.0 (SwiftShader Device (Subzero) (0x0000C0DE)), SwiftShader driver)`, vendor `Google Inc. (Google)`. CPU `requestAnimationFrame` sample **n=20**, mean **102.49 ms** (~**9.76** fps), p50 **116.6**, p95 **216.7**. `consoleErrors: []`. Page screenshot timed out waiting for Google Fonts; no PNG in this bank. Receipt: `analysis/_work/captures/complete-shelf/raf-report.json`. **Do not infer GPU frame time from this CPU rAF** — the GL backend is software SwiftShader, not a laptop GPU.
<!-- NOTES:END -->

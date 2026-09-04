# Complete Shelf

**Slug:** `complete-shelf` · **Kind:** repo · **URL:** https://mengto.github.io/complete-shelf/ · **Canonical item:** [github-mengto-complete-shelf](../items/github-mengto-complete-shelf/card.md)
**Subjects:** [web-3d-scenes](../subjects/web-3d-scenes/brief.md)
**Referenced by (1):**
- [MengTo Complete Shelf — single-file Three.js interactive book demo](../items/github-mengto-complete-shelf/card.md) — example, tool — web-3d-scenes

<!-- NOTES:START -->
Fetched 2026-09-04 README + live `https://mengto.github.io/complete-shelf/` (curl, no headed FPS).

Seven clothbound volumes (Codex, Claude Code, Cursor, Antigravity, Figma, Framer, Xcode). Whole experience in `index.html` (no bundler/backend/MCP). State machine: `shelf → opening detail → closed inspection → open book → closing → shelf`. Three.js PBR + OrbitControls; cloth/foil/paper/wood textures; Pika-generated MP3s embedded as data URLs.

**Transfer (2026-09-04, this host):** `index.html` **2,233,796 bytes** uncompressed, **1,574,186 bytes** gzip on the wire. README still pulls Three.js **r165** from jsDelivr (`three.module.js` 1,284,652 + OrbitControls 32,250 + RoomEnvironment 3,623 + RoundedBoxGeometry 4,625 + RectAreaLightUniformsLib 313,854 ≈ **1.64 MB** extra) and Inter from Google Fonts. “Single file” is the app body; first paint is HTML + CDN Three + font, not 2.2 MB alone. GitHub: 664 stars, **no SPDX license** on the API payload. FPS not measured (no headed GPU pass).
<!-- NOTES:END -->

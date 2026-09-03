# The Complete Shelf

**Repo:** MengTo/complete-shelf  
**Stars:** 659 · **Live:** mengto.github.io/complete-shelf

Single-file Three.js library of seven interactive clothbound hardcovers on a continuous shelf. Browse, pull a volume into detail view, orbit binding, drag through curved pages.

## Volumes

Codex, Claude Code, Cursor, Antigravity, Figma, Framer, Xcode

## Technical

- Entire experience in `index.html` — no bundler, no backend
- Three.js PBR + OrbitControls; procedural cloth/foil/paper textures
- State machine: shelf → opening → inspection → open book → closing → shelf
- Embedded WebP atlases, generated ambient score + Foley (Pika API, embedded MP3)
- Recreation brief in `PROMPT.md`

## Run locally

```bash
python3 -m http.server 4173
```

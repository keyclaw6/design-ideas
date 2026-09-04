# Research

## What it is

MengTo’s “Complete Shelf”: a single-file Three.js demo of seven clothbound hardcovers on a continuous shelf — browse, pull a volume, orbit the binding, drag curved pages. Live at mengto.github.io/complete-shelf.

## How it works

- Entire experience in `index.html` — no bundler, no backend; serve with `python3 -m http.server`.
- Three.js PBR + OrbitControls; procedural cloth/foil/paper textures; embedded WebP atlases.
- State machine: shelf → opening → inspection → open book → closing → shelf.
- Generated ambient score + Foley (Pika API) embedded as MP3.
- Volumes themed as Codex, Claude Code, Cursor, Antigravity, Figma, Framer, Xcode. Recreation brief in `PROMPT.md`.

## Why saved

Concrete Three.js product-object interaction (not a particle hero). Useful as a promptable demo for “interactive 3D object on a marketing page” and as a companion to MengTo’s skill pack.

## Topics

`three-js`, `design`, `ui-motion`

## Related

`github-mengto-skills`, `github-scottstts-threejs-awesome-graphics-agent-skills`, `web-utsubo`, `web-oryzo-ai`, `github-oso95-scroll-world`

## Use when

Briefing an agent to recreate a tactile 3D object UI; looking for a no-bundler Three.js craft bar; pairing with graphics skills for PBR/book/paper materials.

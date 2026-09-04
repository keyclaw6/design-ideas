# Threejs Awesome Graphics Agent Skills

**Slug:** `threejs-awesome-graphics-agent-skills` · **Kind:** repo · **URL:** https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills · **Canonical item:** [github-scottstts-threejs-awesome-graphics-agent-skills](../items/github-scottstts-threejs-awesome-graphics-agent-skills/card.md)
**Subjects:** [blockout-to-video-flythrough](../subjects/blockout-to-video-flythrough/brief.md), [web-3d-scenes](../subjects/web-3d-scenes/brief.md)
**Referenced by (2):**
- [Three.js graphics agent skills: camera rigs, PBR, WebGPU validation](../items/github-scottstts-threejs-awesome-graphics-agent-skills/card.md) — tool, technique — web-3d-scenes
- [Three.js Awesome Graphics Agent Skills v0.8.0 release with new examples](../items/x-2088738850705113398/card.md) — tool — web-3d-scenes

<!-- NOTES:START -->
Fetched 2026-09-04 README from https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills

Vanilla Three.js + TSL/WebGPU **example library** attached to named skills (`threejs-camera-direction`, `threejs-spectral-ocean`, `threejs-procedural-vegetation`, …). Author says it is not an API cheat sheet: the agent is supposed to copy implementation vocabulary. No R3F / React Three Fiber mention in the README skill table. Operating model asks for deterministic inputs, named perceptual fields, diagnostic outputs, and a no-post baseline.

**2026-09-04 capture — gallery is runnable scenes, not stills.** Clone: **24** `skills/threejs-*` folders. `example-gallery/examples` has **40** `example.json` + **40** `scene.js`. Opened `threejs-procedural-vfx/filmic-lens-flare/scene.js` (4,626 bytes): `import * as THREE from "three/webgpu"` + `RenderPipeline` from `three/webgpu`, EXRLoader, local `createFilmicLensFlare`. Backend field in `example.json`: “WebGPU / TSL fullscreen compositor.” Gallery shim (`example-gallery/public/index.html`) is the inspector; README says the agent should copy the example implementation, not the gallery host. No `@react-three` in the skill/example trees (one mention in `source_materials/README.md` only).
<!-- NOTES:END -->

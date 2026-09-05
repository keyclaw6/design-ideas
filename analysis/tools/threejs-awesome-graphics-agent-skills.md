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

**2026-09-04 capture — `threejs-visual-validation` protocol (no headed FPS).** SKILL.md required evidence: fixed camera + seed manifest; final and no-post captures; field/pass mosaic; near/design/far views; stress seed; frame-time and render-target inventory; written invariants. Protocol §Performance: report CPU frame time **and** GPU frame time when available; never infer GPU cost from CPU time; warm-up before recording; separate shader compile from steady-state.

**2026-09-04 capture — official `scripts/capture-examples.mjs`.** After `npm install --legacy-peer-deps` + `npx playwright install chromium` in the clone: `node scripts/capture-examples.mjs --example filmic-lens-flare --output analysis/_work/captures/threejs-filmic`. Result: **1** example, `runtimeErrors: []`. PNG `threejs-procedural-vfx-filmic-lens-flare-final.png` **647,301** bytes at viewport **1440×900**, `debugMode=final`, backend **WebGPU / TSL fullscreen compositor**, skill `threejs-procedural-vfx`. Manifest + contact-sheet `index.html` sit beside the PNG. This is a still plate (HDR winter sun + ghost orbs visible). **GPU frame time was not measured** — do not treat the PNG as a perf receipt. Also captured the other official debug modes at 1440×900, all `runtimeErrors: []`: `no-flare` **848,177** B; `plate` **482,580** B; `flare-only` **373,499** B. Manifests sit beside the PNGs in `analysis/_work/captures/threejs-filmic/`.

**improve-threejs** (no tool file — park here): `aidenybai/react-doctor` `skills/improve-threejs/SKILL.md` (9,128 B). Skill dir is **only** that file. Scan engine: `npx react-doctor@latest --verbose`. Severity follows the render loop (`useFrame` / RAF). Visual rubric 10 rows (render sanity … resize/DPR); a row fails only with screenshot/frame evidence, or is labelled inferred-from-source if no browser. Tweet install `npx skills add … --skill improve-threejs` matches this folder name.

**2026-09-05 leftover14 — Google Antigravity (no antigravity.md).** `www.antigravity.google` **136,935 B** (apex **28,747 B**). Title Google Antigravity. Surfaces: Antigravity 2.0 / CLI / Extensions / IDE / SDK. Blog *Gemini 3.7 Flash in Google Antigravity* **105,119 B** (Aug 13, 2026). Homepage copy: available at no charge for developers. `developers.google.com/antigravity` **404**. Bugatti / W16 / Three.js / ~4 min **absent**. leftover9 `covers.step` W16 is text-to-cad, not this Three.js scene ([x-2088240171565412733](../items/x-2088240171565412733/card.md)). Receipt `leftover14-2026-09-05.json` + `leftover14b-2026-09-05.json`.

**2026-09-05 leftover29.** Unused GitHub `scottstts/Threejs-Awesome-Graphics-Agent-Skills` MIT **782★**. Receipt `leftover29-2026-09-05.json`.
<!-- NOTES:END -->

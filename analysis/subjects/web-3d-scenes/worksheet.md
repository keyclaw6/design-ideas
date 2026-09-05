# Judgment worksheet: Three.js / WebGL / WebGPU scenes (web-3d-scenes)

Owner aliases: three.js, WebGL, scroll world. Decide a *shippable landing scene*, not a DCC file and not a splat viewer.

## web-3d-scenes — short stack to try

Four jobs. A Three.js skill pack does not replace a finished page.

1. **Agent coverage for Three.js.** Must-read [scottstts/threejs-awesome-graphics-agent-skills](../../items/github-scottstts-threejs-awesome-graphics-agent-skills/card.md) (camera, PBR, TSL/WebGPU validation). Pair with [/improve-threejs](../../items/x-2089400082550620636/card.md) when the first pass is a vibe-coded mess, and MengTo’s extracted skills plus Sylva ([x-2089602918605619401](../../items/x-2089602918605619401/card.md)) when the target is an instanced nature scene.
2. **Scroll or pointer as the camera.** [oso95/scroll-world](../../items/github-oso95-scroll-world/card.md) for isometric flythrough landings. [VanhDesign WebGPU single-file page](../../items/x-2091748299975880994/card.md) when one Blender model should *be* the site. [Complete Shelf](../../items/github-mengto-complete-shelf/card.md) when the interaction is orbit + state machine, not scroll-scrub.
3. **Copy-paste layers, not a runtime.** GetLayers prompts + MCP ([web-getlayers-ai](../../items/web-getlayers-ai/card.md)). FeralUI for physics-flavored React chrome ([web-feralui-dev](../../items/web-feralui-dev/card.md)). vgpu when the agent is writing WebGPU shaders ([x-2093012548031254932](../../items/x-2093012548031254932/card.md)).
4. **Reference pages only.** ORYZO / Lusion ([web-oryzo-ai](../../items/web-oryzo-ai/card.md)) and Utsubo ([web-utsubo](../../items/web-utsubo/card.md)) are finished studio work. Do not treat them as installable kits.

Spline as “the likely disruptor” is one opinion tweet ([x-2090526692427104508](../../items/x-2090526692427104508/card.md)). Keep it as a hypothesis. Splat viewers stay in [gaussian-splatting](../gaussian-splatting/worksheet.md).

## web-3d-scenes — axis scores

| item | ships as web page | scroll/pointer camera | WebGL vs WebGPU vs Spline | agent-skill coverage | performance notes |
|---|---|---|---|---|---|
| threejs-awesome-graphics-agent-skills | n/a (skill, not a page) | teaches rigs | WebGL + TSL/WebGPU | high | validation hooks stated |
| /improve-threejs | n/a (slash skill) | unknown | WebGL implied | mid (polish pass) | “faster / less buggy” stated |
| MengTo Sylva + 3 skills | high (reference scene) | mid (interaction, not only scroll) | WebGL / Three.js r149 | high (extracted skills) | README up to 250k blades; first-load ≈1.51 MB |
| scroll-world | high (generated landing) | high (scroll-scrub flight) | WebGL (isometric stills + connectors) | high (skill interviews brand) | skill engine **31,410** bytes JS+HTML; generated-page 3 MB budget still open |
| Complete Shelf | high (one index.html) | mid (orbit + shelf states) | WebGL / Three r165 CDN | mid (repo is the example) | HTML 2.23 MB + ≈1.64 MB CDN Three |
| VanhDesign WebGPU page | high (one HTML) | high (scene *is* the page) | WebGPU | low | unknown polycount |
| GetLayers | mid (prompt → HTML layer) | depends on layer | WebGL/GLSL in prompts | mid (MCP assemble) | unknown |
| FeralUI | high (React components) | pointer / physics, not camera | WebGL-adjacent CSS/R3F | low | experimental v0.1.1 |
| vgpu | n/a (shader lib) | n/a | WebGPU | high (agent-oriented) | vgpu.sh + vercel-labs/vgpu MIT 1,628★ |
| ORYZO / Utsubo | high | high (studio scroll) | WebGL (implied) | none | studio-grade; no budget numbers |
| Opus 5 jeep / Antigravity Bugatti | high (demo scene) | pointer / orbit | WebGL | one-off prompt loop | 4 min Antigravity claim; 300k context claim |
| Spline opinion | unknown (product live **180,577 B**; H1 Make anything 3D) | unknown | Spline (browser + AI or direct control) | none | no dollar amounts on homepage |

## web-3d-scenes — claims that need a receipt

- Sylva 130k blades / <1 MB — **README says up to 250k blades**. Live first-load ≈1.51 MB (HTML+assets); HTML+JS only ≈0.96 MB. See [sylva](../../tools/sylva.md).
- Complete Shelf “single file” — `index.html` is 2,233,796 bytes uncompressed / 1,574,186 gzip, plus jsDelivr Three r165 ≈1.64 MB. See [complete-shelf](../../tools/complete-shelf.md). CPU rAF on SwiftShader: mean **102.49 ms** (~9.76 fps, n=20). GPU frame time still unknown.
- scroll-world “no cuts, scrubbed to scroll” — skill README. Portable engine is **28,697 + 2,713 = 31,410** bytes ([scroll-world-skill](../../tools/scroll-world-skill.md)). Need one *generated* site under a 3 MB JS budget.
- Graphics skills produce valid R3F vs screenshot-alike HTML — README (2026-09-04) is **vanilla Three + TSL/WebGPU examples**, no R3F. Still need to open one example and diff the scene graph. See [threejs-awesome-graphics-agent-skills](../../tools/threejs-awesome-graphics-agent-skills.md).
- Gemini Antigravity Bugatti in ~4 minutes — demo clock. Official `www.antigravity.google` **136,935 B** names 2.0 / CLI / Extensions / IDE / SDK and a Gemini 3.7 Flash blog (**105,119 B**). Bugatti / W16 / Three.js / 4 min **absent**. leftover9 `covers.step` is text-to-cad, not this scene ([x-2088240171565412733#c3](../../items/x-2088240171565412733/card.md)).
- GetLayers MCP “assembles a whole site” — marketing; no recorded assembly log.
- vgpu “built for coding agents” — announcement thread, 71 replies / 1 captured. Docs are live at **vgpu.sh** (**247,177 B**; CLI / skill / MCP). Repo `vercel-labs/vgpu` MIT **1,628★**.

## web-3d-scenes — do not treat as load-bearing

- Spline-disrupts-legacy-DCC ([x-2090526692427104508](../../items/x-2090526692427104508/card.md)) — three-reply opinion, captured_full, still one person’s take.
- RoundtableSpace one-hour course — the taught process is the X amplify video **3596.421 s** / 2216×1440, not a scene or a separate course page ([scroll-driven-3d](../../techniques/scroll-driven-3d.md)). Thread stays 15/3.
- Secondary splat / LOD / Needle items — they sit here as overlap; judge them in their primary subjects.
- MengTo “60 new Three.js components” ([x-2091571624390881664](../../items/x-2091571624390881664/card.md)) until the component list is in-repo, not a prompt-axis tweet.

## web-3d-scenes — next capture work

1. Gallery is **40 runnable `scene.js` files**. Official `capture-examples.mjs` now has all four `filmic-lens-flare` debug stills (final 647,301 / no-flare 848,177 / plate 482,580 / flare-only 373,499 B; `runtimeErrors: []`) — [threejs-awesome-graphics-agent-skills](../../tools/threejs-awesome-graphics-agent-skills.md). Protocol still requires CPU **and** GPU frame time (never infer GPU from CPU). Remaining: a GPU timer.
2. Transfer sizes + SwiftShader CPU rAF (mean 102.49 ms / ~9.76 fps, n=20) are on [complete-shelf](../../tools/complete-shelf.md). Remaining: headed FPS on a laptop GPU. Fonts blocked the full-page PNG.
3. `/improve-threejs` SKILL.md is in `aidenybai/react-doctor`. `npx react-doctor@latest` **0.9.13** on loopany-platform: React 19 / tanstack-start / **hasThree false** / score 100 with empty rules under `--no-lint`. The 10-row visual rubric was not run (no R3F surface in that clone). Thread still 55/1.
4. Keep splat viewers out of this stack; if the page *is* a splat, use the gaussian-splatting worksheet.
5. utsubo.com live **200 / 72,976 B**; “0% BETTER WITH SPEAKERS ON” is in the HTML ([scroll-driven-3d](../../techniques/scroll-driven-3d.md)). Card is now `ready`.
6. Meng To “40-min” Three.js + Claude Code tutorial is the X amplify video on `MengTo/2088117711868227765` (**2411.133 s**, 2880×2160) — no separate docs/YouTube ([mengto-skills](../../tools/mengto-skills.md)). Pointer card is `ready` (thread `empty`, 0 replies reported).
7. vgpu docs + MIT repo are now on [x-2093012548031254932](../../items/x-2093012548031254932/card.md). Stale `thread-failed` tag dropped (`thread-partial` 71/1). Remaining: more than the one captured Vercel reply.
8. VanhDesign leftover has no public host this pass: `vanh.design` / `.com` / `.io` NXDOMAIN; GitHub user `VanhDesign` **0** repos ([webgpu](../../tools/webgpu.md); [x-2091748299975880994#c3](../../items/x-2091748299975880994/card.md)). 201 KB HTML stays tweet-only.
9. MengTo “60 Three.js components” leftover is not a counted MengTo/Skills inventory ([mengto-skills](../../tools/mengto-skills.md); [x-2091571624390881664#c2](../../items/x-2091571624390881664/card.md)).
10. leftover14 Antigravity homepage + 3.7 Flash blog are on [threejs-awesome-graphics-agent-skills](../../tools/threejs-awesome-graphics-agent-skills.md). Jeep leftover is bpy / 300k-context, not blender-mcp ([x-2086537093120164177#c3](../../items/x-2086537093120164177/card.md)).
11. leftover24 unused GitHub `MengTo/Skills` MIT **5,798★** on the Sylva leftover — not the moss-instancing repo ([mengto-skills](../../tools/mengto-skills.md); [x-2089602918605619401#c4](../../items/x-2089602918605619401/card.md)).
12. leftover27 unused `getlayers.ai` **426,495 B** claims **1,000+** creators + template/3D/MCP library ([getlayers](../../tools/getlayers.md); [web-getlayers-ai#c3](../../items/web-getlayers-ai/card.md)). leftover27 unused `feralui.dev` **10,527 B** is a thin physics-React shell ([feralui](../../tools/feralui.md); [web-feralui-dev#c3](../../items/web-feralui-dev/card.md)). Remaining: an account export / package install, not another homepage.
13. leftover28 unused `oryzo.ai` **71,633 B** is a satirical cork-coaster landing; `lusion.co` **59,671 B** names it as featured work — not a scene exporter ([scroll-world-skill](../../tools/scroll-world-skill.md); [web-oryzo-ai#c3](../../items/web-oryzo-ai/card.md)).

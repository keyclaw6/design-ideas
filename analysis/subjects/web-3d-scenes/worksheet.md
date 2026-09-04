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
| MengTo Sylva + 3 skills | high (reference scene) | mid (interaction, not only scroll) | WebGL / Three.js | high (extracted skills) | ~130k instanced blades, <1 MB code (stated) |
| scroll-world | high (generated landing) | high (scroll-scrub flight) | WebGL (isometric stills + connectors) | high (skill interviews brand) | unknown JS budget |
| Complete Shelf | high (one index.html) | mid (orbit + shelf states) | WebGL | mid (repo is the example) | single-file, no bundler (stated) |
| VanhDesign WebGPU page | high (one HTML) | high (scene *is* the page) | WebGPU | low | unknown polycount |
| GetLayers | mid (prompt → HTML layer) | depends on layer | WebGL/GLSL in prompts | mid (MCP assemble) | unknown |
| FeralUI | high (React components) | pointer / physics, not camera | WebGL-adjacent CSS/R3F | low | experimental v0.1.1 |
| vgpu | n/a (shader lib) | n/a | WebGPU | high (agent-oriented) | “minimal / performant” stated |
| ORYZO / Utsubo | high | high (studio scroll) | WebGL (implied) | none | studio-grade; no budget numbers |
| Opus 5 jeep / Antigravity Bugatti | high (demo scene) | pointer / orbit | WebGL | one-off prompt loop | 4 min Antigravity claim; 300k context claim |
| Spline opinion | unknown | unknown | Spline | none | no numbers |

## web-3d-scenes — claims that need a receipt

- Sylva 130k instanced blades under 1 MB — need the live page’s transfer size, not the tweet.
- scroll-world “no cuts, scrubbed to scroll” — skill README; need one generated site under a 3 MB JS budget (open question on the brief).
- Graphics skills produce valid R3F vs screenshot-alike HTML — README (2026-09-04) is **vanilla Three + TSL/WebGPU examples**, no R3F. Still need to open one example and diff the scene graph. See [threejs-awesome-graphics-agent-skills](../../tools/threejs-awesome-graphics-agent-skills.md).
- Gemini Antigravity Bugatti in ~4 minutes — demo clock, no repo.
- GetLayers MCP “assembles a whole site” — marketing; no recorded assembly log.
- vgpu “built for coding agents” — announcement thread, 71 replies / 1 captured.

## web-3d-scenes — do not treat as load-bearing

- Spline-disrupts-legacy-DCC ([x-2090526692427104508](../../items/x-2090526692427104508/card.md)) — three-reply opinion, captured_full, still one person’s take.
- RoundtableSpace one-hour course — syllabus tweet, not a scene.
- Secondary splat / LOD / Needle items — they sit here as overlap; judge them in their primary subjects.
- MengTo “60 new Three.js components” ([x-2091571624390881664](../../items/x-2091571624390881664/card.md)) until the component list is in-repo, not a prompt-axis tweet.

## web-3d-scenes — next capture work

1. README says vanilla Three + example library (not R3F). Remaining: open one gallery example and record whether it is a runnable scene or a still.
2. Measure Complete Shelf and Sylva transfer size + FPS on a laptop GPU.
3. Re-open [x-2089400082550620636](../../items/x-2089400082550620636/thread.md) (55 replies / 1 captured) for /improve-threejs install path.
4. Keep splat viewers out of this stack; if the page *is* a splat, use the gaussian-splatting worksheet.

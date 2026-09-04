# Three.js graphics agent skills: camera rigs, PBR, WebGPU validation

`github-scottstts-threejs-awesome-graphics-agent-skills` · github · repo · en · [source](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills) · [raw](../../../raw/items/github-scottstts-threejs-awesome-graphics-agent-skills/)
**Author:** scottstts (@—) · **Published:** — · **Captured:** 2026-09-02T17:15:19Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [web-3d-scenes](../../subjects/web-3d-scenes/brief.md) · **Also:** [blockout-to-video-flythrough](../../subjects/blockout-to-video-flythrough/brief.md) · **Roles:** tool, technique · **Platforms:** three-js, cursor, codex

**Summary.** MIT npm skill pack for Three.js that teaches agents camera direction, PBR materials, shaders, TSL/WebGPU effects, and visual validation via fixed-view captures—not an API cheat sheet but implementation vocabulary with examples.
**Question it answers.** Which agent skills help author Three.js cameras, PBR scenes, and diagnostic still captures?

**Claims.**
- `github-scottstts-threejs-awesome-graphics-agent-skills#c1` (capability, stated) threejs-camera-direction covers authored lenses, chase/orbit rigs, and handoffs for flythrough-style camera language in WebGL scenes. — evidence: "threejs-camera-direction — Authored lenses, chase/orbit rigs, handoffs" [linked-page]
- `github-scottstts-threejs-awesome-graphics-agent-skills#c2` (result, demonstrated) Official capture-examples.mjs of filmic-lens-flare wrote a 647,301-byte 1440×900 PNG with empty runtimeErrors (WebGPU/TSL compositor, debugMode final). GPU frame time was not measured. — evidence: "Captured threejs-procedural-vfx/filmic-lens-flare; manifest runtimeErrors []; PNG 647301 bytes; backend WebGPU / TSL fullscreen compositor. See analysis/_work/captures/threejs-filmic/" [note]
- `github-scottstts-threejs-awesome-graphics-agent-skills#c3` (result, demonstrated) The same official capture script with --debug no-flare wrote an 848,177-byte 1440×900 PNG of filmic-lens-flare. GPU frame time still unmeasured. — evidence: "threejs-procedural-vfx-filmic-lens-flare-no-flare.png 848177 bytes; manifest-no-flare.json debugMode no-flare; runtimeErrors []." [note]
- `github-scottstts-threejs-awesome-graphics-agent-skills#c4` (result, demonstrated) Official capture-examples.mjs also wrote filmic-lens-flare plate (482,580 B) and flare-only (373,499 B) 1440×900 PNGs with empty runtimeErrors. GPU frame time still unmeasured. — evidence: "debugMode plate PNG 482580; flare-only PNG 373499; manifests in analysis/_work/captures/threejs-filmic/" [note]
**Numbers.** —
**Recipe.** —
**Techniques.** [blender-blockout-camera](../../techniques/blender-blockout-camera.md), [blender-blockout-camera](../../techniques/blender-blockout-camera.md)
**Tools.** [threejs-awesome-graphics-agent-skills](../../tools/threejs-awesome-graphics-agent-skills.md)
**Links.** repo (https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills), product (https://www.npmjs.com/package/threejs-awesome-graphics-agent-skills)
**Related items.** [github-mengto-skills](../github-mengto-skills/card.md), [github-oso95-scroll-world](../github-oso95-scroll-world/card.md)
**Media.** —
**Judge hints.** must_read: True · compare with: [github-mengto-skills](../github-mengto-skills/card.md), [web-utsubo](../web-utsubo/card.md)

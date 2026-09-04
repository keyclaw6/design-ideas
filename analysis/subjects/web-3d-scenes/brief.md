# Three.js / WebGL / WebGPU / Spline scenes on the web (web-3d-scenes)

## web-3d-scenes — scope

Three.js and R3F sites and templates, graphics agent skills for Three.js, WebGPU shader libraries, scroll-world 3D heroes, Spline, 3D component packs, 3D-driven landing pages, 3D diagram editors that ship as web scenes.

Exclusion: Splat viewers → gaussian-splatting unless the item is about the web scene itself. Non-3D landing motion → landing-ui-motion.

Priority `now`. Owner aliases: three.js, WebGL, scroll world.
Expected primary range [14, 22]. This roster has **18** primary and **11** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## web-3d-scenes — what the owner is trying to decide

Decide which Three.js / R3F / WebGPU / Spline items are shippable landing scenes versus demos. Splat viewers stay in gaussian-splatting unless the page *is* the scene.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## web-3d-scenes — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=9, technique=7, example=11, claim-source=2, reference=4.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (8):
- [oso95 scroll-world: agent skill for scroll-scrubbed isometric flythrough landings](../../items/github-oso95-scroll-world/card.md) — tool, technique — MIT GitHub agent skill (~8.9k stars) that interviews for brand/scene order, generates GPT Image stills plus Monid/Seedance connector…
- [Three.js graphics agent skills: camera rigs, PBR, WebGPU validation](../../items/github-scottstts-threejs-awesome-graphics-agent-skills/card.md) — tool, technique — MIT npm skill pack for Three.js that teaches agents camera direction, PBR materials, shaders, TSL/WebGPU effects, and visual validation…
- [FeralUI v0.1.1: physically inspired React components that swing and crumple](../../items/web-feralui-dev/card.md) — tool, example — FeralUI v0.1.1 is an experimental component library whose drop-in parts swing, grab, crumple, and catch light
- [GetLayers AI prompt library for cinematic WebGL heroes and MCP assembly](../../items/web-getlayers-ai/card.md) — tool, example — Commercial library of copy-paste prompts that recreate self-contained HTML layers—sections, GLSL gradients, and 3D scenes—with…
- [Three.js Awesome Graphics Agent Skills v0.8.0 release with new examples](../../items/x-2088738850705113398/card.md) — tool — Release announcement for Three.js Awesome Graphics Agent Skills v0.8.0 with a Codex installer and three new gallery examples: procedural…
- [Aiden Bai /improve-threejs skill polishes vibe-coded Three.js](../../items/x-2089400082550620636/card.md) — tool — Announcement of a /improve-threejs slash skill that upgrades slow, visually buggy agent-built Three.js prototypes into faster,…
- [MengTo open-sources Sylva Three.js site and three interaction skills](../../items/x-2089602918605619401/card.md) — tool, example — MengTo releases Sylva, a reference-matched Three.js moss scene with about 130k instanced blades under 1 MB code, plus three extracted…
- [vgpu: minimal WebGPU shader library built for coding agents](../../items/x-2093012548031254932/card.md) — tool, claim-source — Vercel engineer announces vgpu, a minimal WebGPU library designed for agents to ship performant shaders; the captured thread opener asks…

First role `technique` (2):
- [Meng To tutorial pointer — Three.js landing pages with Claude Code and Opus 5](../../items/x-2088265078919282836/card.md) — technique, example — Recommendation to watch Meng To walk through advanced Three.js landing pages using Claude Code and Opus 5, covering structure, motion,…
- [VanhDesign WebGPU single-scene page driven by Blender keyboard model](../../items/x-2091748299975880994/card.md) — technique, example — VanhDesign template uses one WebGPU-rendered 3D scene to drive an entire landing page from a single HTML file, with a Blender…

First role `example` (5):
- [MengTo Complete Shelf — single-file Three.js interactive book demo](../../items/github-mengto-complete-shelf/card.md) — example, tool — GitHub repo shipping one index.html Three.js scene: seven clothbound volumes on a shelf with PBR textures, orbit controls, and a…
- [ORYZO AI — Lusion satirical AI-product landing for a cork coaster](../../items/web-oryzo-ai/card.md) — example, reference — High-production satirical marketing site by Lusion presenting a cork coaster as an over-engineered AI product
- [Opus 5 recursive loop builds interactive textureless 3D vehicle](../../items/x-2086537093120164177/card.md) — example, technique — Build-log thread where Opus 5 generates a fully interactive jeep-like terrain vehicle via a recursive loop and subagent QC under a 300k…
- [Gemini Antigravity builds photoreal Bugatti W16 Three.js scene in four minutes](../../items/x-2088240171565412733/card.md) — example, technique — Demo post showing Gemini 3.7 Flash High inside Google Antigravity generating a Bugatti W16 engine in Three.js in about four minutes,…
- [MengTo ships 60 new Three.js components via Claude Code prompts](../../items/x-2091571624390881664/card.md) — example, technique — Meng To added 60 Three.js components built with Claude Code variants, listing prompt axes for environments, colors, styles, typography,…

First role `reference` (3):
- [Utsubo studio site: experiential scroll and 3D brand storytelling](../../items/web-utsubo/card.md) — reference, example — Utsubo is a technology-first creative studio whose own site is the portfolio artifact: immersive scroll, letter-spaced typography…
- [RoundtableSpace free 1-hour Claude interactive 3D web course](../../items/x-2086599657925329347/card.md) — reference — RoundtableSpace promotes a free one-hour course on using Claude to build interactive 3D websites and games from scratch, covering a full…
- [Opinion: Spline is the likely disruptor of legacy 3D software for web](../../items/x-2090526692427104508/card.md) — reference, claim-source — Short opinion tweet that Spline is back and is the most likely tool to disrupt traditional big 3D software for web-native work

Must-read (from `judge_hints.must_read`, ≤ 12):
- [Three.js graphics agent skills: camera rigs, PBR, WebGPU validation](../../items/github-scottstts-threejs-awesome-graphics-agent-skills/card.md)

Secondary membership (11), not in the primary count:
- [kokraf four-view AI texture projection for Three.js meshes](../../items/x-2057113327508345047/card.md) — primary `image-to-3d-world`
- [iCraft Editor for 3D network architecture diagrams (gantFDT/icraft)](../../items/x-2089570022490263586/card.md) — primary `infographics-diagrams`
- [23rd.dev curated shadcn registry for shader and motion components](../../items/x-2089740155179643231/card.md) — primary `landing-ui-motion`
- [3DGS infrastructure advances: LOD, streaming, SPZ, Aholo city-scale viewer](../../items/x-2090589293677023507/card.md) — primary `gaussian-splatting`
- [Browser Gaussian splat training with open-source Splat.js](../../items/x-2090839282831270173/card.md) — primary `gaussian-splatting`
- [Higgsfield + Claude Opus 5 builds animated low-poly Blender world in-prompt](../../items/x-2091497597743612379/card.md) — primary `blockout-to-video-flythrough`
- [Needle browser mesh decimation: 3.2M to 3K triangles in 3 seconds](../../items/x-2091927587471712274/card.md) — primary `image-to-3d-world`
- [SplatPaint browser sandbox for painting and editing Gaussian splats](../../items/x-2091943679317463153/card.md) — primary `gaussian-splatting`
- [Parallax finance landing workflow with Claude Code and ChatGPT](../../items/x-2093915384944414827/card.md) — primary `landing-ui-motion`
- [motionsites.ai library of 590+ anti-slop website animation prompts](../../items/x-2094009989220430084/card.md) — primary `design-agent-skills`
- [Atlas Fields Studio — free 3D EM field viewer for PCB designs](../../items/x-2094840529997410525/card.md) — primary `ai-cad-hardware`

## web-3d-scenes — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [worldgen-to-video](../../techniques/worldgen-to-video.md) — World/mesh generation handed to a video model for a flythrough instead of a real-time engine render.
- [blender-blockout-camera](../../techniques/blender-blockout-camera.md) — Agent or MCP builds a Blender/Unreal blockout and authors a camera path before any video model.
- [ui-motion-physics](../../techniques/ui-motion-physics.md) — Spring, rebound, HUD, and industrial motion languages for UI chrome.
- [scroll-driven-3d](../../techniques/scroll-driven-3d.md) — A Three.js/WebGPU scene where scroll or pointer is the camera rig.
- [faceless-video-pipeline](../../techniques/faceless-video-pipeline.md) — YouTube/TikTok pipelines that regenerate audio or picture without an on-camera talent.
- [image-to-3d-worldgen](../../techniques/image-to-3d-worldgen.md) — One image, panorama, or text prompt → navigable world or posed assets.
- [taste-skill-encoding](../../techniques/taste-skill-encoding.md) — Installable taste/Impeccable/MengTo skills that change defaults, not just prompts.

## web-3d-scenes — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [complete-shelf](../../tools/complete-shelf.md)
- [monid-cli](../../tools/monid-cli.md)
- [higgsfield-cli](../../tools/higgsfield-cli.md)
- [scroll-world-skill](../../tools/scroll-world-skill.md)
- [threejs-awesome-graphics-agent-skills](../../tools/threejs-awesome-graphics-agent-skills.md)
- [feralui](../../tools/feralui.md)
- [getlayers](../../tools/getlayers.md)
- [claude-code](../../tools/claude-code.md)
- [mengto-skills](../../tools/mengto-skills.md)
- [improve-threejs](../../tools/improve-threejs.md)
- [sylva](../../tools/sylva.md)
- [threejs-wireframe-scan-reveal](../../tools/threejs-wireframe-scan-reveal.md)
- [spline](../../tools/spline.md)
- [blender](../../tools/blender.md)
- [webgpu](../../tools/webgpu.md)

## web-3d-scenes — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `github-mengto-complete-shelf#c1` | The entire bookshelf experience ships as one index.html with no bundler or backend. | stated | [MengTo Complete Shelf — single-file T…](../../items/github-mengto-complete-shelf/card.md) |
| `github-mengto-complete-shelf#c2` | Seven themed volumes use a shelf-to-opening-to-inspection state machine with curved page dragging. | stated | [MengTo Complete Shelf — single-file T…](../../items/github-mengto-complete-shelf/card.md) |
| `github-oso95-scroll-world#c1` | scroll-world builds continuous camera flight through AI isometric diorama scenes with no cuts, scrubbed to scroll. | stated | [oso95 scroll-world: agent skill for s…](../../items/github-oso95-scroll-world/card.md) |
| `github-scottstts-threejs-awesome-graphics-agent-skills#c1` | threejs-camera-direction covers authored lenses, chase/orbit rigs, and handoffs for flythrough-style camera language … | stated | [Three.js graphics agent skills: camer…](../../items/github-scottstts-threejs-awesome-graphics-agent-skills/card.md) |
| `web-feralui-dev#c1` | Components are marketed as swinging, grabbing, crumpling, and catching light rather than standard UI motion. | stated | [FeralUI v0.1.1: physically inspired R…](../../items/web-feralui-dev/card.md) |
| `web-feralui-dev#c2` | Homepage lists PullCord, Claw, Crumple, Hologram, Blinds, Blob, and other experimental modules. | stated | [FeralUI v0.1.1: physically inspired R…](../../items/web-feralui-dev/card.md) |
| `web-getlayers-ai#c1` | Each layer ships as a prompt that recreates a self-contained HTML page across sections, gradients, and 3D scenes. | stated | [GetLayers AI prompt library for cinem…](../../items/web-getlayers-ai/card.md) |
| `web-getlayers-ai#c2` | GetLayers MCP assembles a whole site from library layers. | stated | [GetLayers AI prompt library for cinem…](../../items/web-getlayers-ai/card.md) |
| `web-oryzo-ai#c1` | Site sells fake ORYZO SKUs with stack-height tiers and smart-flip encryption gags. | demonstrated | [ORYZO AI — Lusion satirical AI-produc…](../../items/web-oryzo-ai/card.md) |
| `web-oryzo-ai#c2` | Interactive 3D and hover demos accompany the parody AI landing sections. | stated | [ORYZO AI — Lusion satirical AI-produc…](../../items/web-oryzo-ai/card.md) |
| `web-utsubo#c1` | Site is positioned as an experimental, audio-forward web experience rather than a component kit or skill pack. | stated | [Utsubo studio site: experiential scro…](../../items/web-utsubo/card.md) |
| `x-2086537093120164177#c1` | Author steers Opus 5 with a recursive generation loop and subagent QC under 300k context. | stated | [Opus 5 recursive loop builds interact…](../../items/x-2086537093120164177/card.md) |
| `x-2086537093120164177#c2` | Quoted instructions use the Blender Python API with a 300k context window and no Tripo/Hunyuan mesh import. | stated | [Opus 5 recursive loop builds interact…](../../items/x-2086537093120164177/card.md) |
| `x-2086599657925329347#c1` | Course covers interactive 3D experiences, games from scratch, and AI design workflow. | stated | [RoundtableSpace free 1-hour Claude in…](../../items/x-2086599657925329347/card.md) |
| `x-2088240171565412733#c1` | Gemini 3.7 Flash High in Antigravity produced the scene in roughly four minutes. | stated | [Gemini Antigravity builds photoreal B…](../../items/x-2088240171565412733/card.md) |

Full set: claims.jsonl (32 rows)

## web-3d-scenes — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- ships as a web page (not a DCC file)
- scroll or pointer drives the camera
- WebGL vs WebGPU vs Spline
- agent-skill coverage for Three.js
- performance notes (polycount, LOD)

## web-3d-scenes — thread coverage

X items in primary roster: 11. captured_full=1, captured_partial=9, empty=1, failed=0.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2086537093120164177](../../items/x-2086537093120164177/thread.md) | captured_partial | 24 | 1 | 1 |
| [x-2086599657925329347](../../items/x-2086599657925329347/thread.md) | captured_partial | 15 | 3 | 2 |
| [x-2088240171565412733](../../items/x-2088240171565412733/thread.md) | captured_partial | 8 | 3 | 2 |
| [x-2088265078919282836](../../items/x-2088265078919282836/thread.md) | empty | 0 | 0 | 0 |
| [x-2088738850705113398](../../items/x-2088738850705113398/thread.md) | captured_partial | 7 | 3 | 0 |
| [x-2089400082550620636](../../items/x-2089400082550620636/thread.md) | captured_partial | 55 | 1 | 1 |
| [x-2089602918605619401](../../items/x-2089602918605619401/thread.md) | captured_partial | 63 | 3 | 3 |
| [x-2090526692427104508](../../items/x-2090526692427104508/thread.md) | captured_full | 3 | 3 | 1 |
| [x-2091571624390881664](../../items/x-2091571624390881664/thread.md) | captured_partial | 51 | 3 | 2 |
| [x-2091748299975880994](../../items/x-2091748299975880994/thread.md) | captured_partial | 5 | 3 | 1 |
| [x-2093012548031254932](../../items/x-2093012548031254932/thread.md) | captured_partial | 71 | 1 | 1 |

## web-3d-scenes — gaps and open questions

Primary readiness: ready=6, ready-with-gaps=12. Gap tags: linked-page-unfetched=2, thread-partial=2, media-undescribed=1, thread-failed=1.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- Which scroll-world templates stay under a 3 MB JS budget?
- Do graphics-agent skills produce valid R3F or only screenshot-alike HTML?

If this subject drops below 6 primary items after a future reclass, merge it into `landing-ui-motion` and delete the folder.

## web-3d-scenes — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [landing-ui-motion](../landing-ui-motion/brief.md)
- [gaussian-splatting](../gaussian-splatting/brief.md)
- [image-to-3d-world](../image-to-3d-world/brief.md)


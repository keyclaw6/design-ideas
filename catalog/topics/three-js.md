# Three.js

Topic slug: `three-js`. Three.js / WebGL / R3F, graphics agent skills, and web 3D scenes. This is the **in-browser** 3D lane — not Blender blockouts or video models (see [`camera-control`](camera-control.md), [`video-generation`](video-generation.md), [`bess-3d-flythrough`](bess-3d-flythrough.md), [`gaussian-splatting`](gaussian-splatting.md)). Shared items with `design` / `ui-motion` are 3D used as marketing surface, not a separate stack.

The harvest is small and skill-heavy. The main pack is **Three.js Awesome Graphics Agent Skills** (router, camera rigs, PBR/TSL, ocean/clouds, visual-validation mosaics) plus MengTo’s web-design/Three.js skills and the Complete Shelf demo (single-file PBR + OrbitControls). Prompt libraries (GetLayers 3D scenes + GLSL gradients) and physically-weird component kits (FeralUI) sit next to studio references (Utsubo, Lusion’s ORYZO) and one-image → Atlas/spark.js → three.js reconstruction.

Query here for “agent that can light a mesh,” “WebGL hero that isn’t a GIF,” “compose a 3D scene prompt,” or “camera rig in the browser.” For scroll-driven 2D/CSS motion stay on [`ui-motion`](ui-motion.md). Presence is not a recommendation.

## Pipelines

- **Skills pack → scene** — install graphics skills, decompose the visual target (router), author camera, validate with fixed-view captures (`github-scottstts-threejs-awesome-graphics-agent-skills`).
- **Capture → Super Prompt** — screen recording or stitched page → HTML/WebGL recreation prompt (`github-mengto-skills`).
- **Prompted 3D layer** — tune a GetLayers scene/gradient in-browser, copy the HTML prompt, optionally compose with UI (`web-getlayers-ai`).
- **Image → world → three.js** — Atlas fills gaps from one photo; spark.js + three.js present the scene (`x-2094864872853119216`).
- **Single-file showcase** — no bundler; PBR + state machine + embedded atlases (`github-mengto-complete-shelf`).

## Tools

- [Three.js Awesome Graphics Agent Skills](../../raw/items/github-scottstts-threejs-awesome-graphics-agent-skills/) — `github-scottstts-threejs-awesome-graphics-agent-skills` — mesh/lighting/PBR/shaders/TSL/post/particles; `npx … install --agent cursor`.
- [Agent Skills (MengTo)](../../raw/items/github-mengto-skills/) — `github-mengto-skills` — web-design/Three.js/GSAP skills; video-to-prompt and full-page capture.
- [The Complete Shelf](../../raw/items/github-mengto-complete-shelf/) — `github-mengto-complete-shelf` — seven-volume Three.js shelf in one `index.html` + `PROMPT.md`.
- [GetLayers AI](../../raw/items/web-getlayers-ai/) — `web-getlayers-ai` — 3D Scenes + ~1KB WebGL gradients; MCP for whole-site assembly.
- [FeralUI](../../raw/items/web-feralui-dev/) — `web-feralui-dev` — experimental components with 3D/physical motion (Hologram, Blob, Fur, …).

## Techniques

- [threejs-skill-router / camera / visual-validation](../../raw/items/github-scottstts-threejs-awesome-graphics-agent-skills/) — `github-scottstts-threejs-awesome-graphics-agent-skills` — decompose looks; authored lenses/chase-orbit; diagnostic mosaics (also tagged `camera-control`).
- [A Developer's Guide to Taste](../../raw/items/web-opale-ui-taste/) — `web-opale-ui-taste` — encode WebGL/3D taste (brain-on-scroll, liquid sim, noise field) into skills, not generic packs.
- [Atlas + spark.js + three.js from one image](../../raw/items/x-2094864872853119216/) — `x-2094864872853119216` — World Labs Atlas reconstruction presented in three.js (also splat/camera/video tags).
- [GetLayers compose](../../raw/items/web-getlayers-ai/) — `web-getlayers-ai` — scene + gradient + UI into one stack-agnostic prompt.

## Examples

- [ORYZO AI](../../raw/items/web-oryzo-ai/) — `web-oryzo-ai` — Lusion-designed satirical 3D product landing (interactive coaster).
- [Utsubo](../../raw/items/web-utsubo/) — `web-utsubo` — technology-first studio site; scroll/3D brand ambition (also `bess-3d-flythrough`).
- [The Complete Shelf](../../raw/items/github-mengto-complete-shelf/) — `github-mengto-complete-shelf` — orbit, page-turn, cloth/foil PBR as a self-contained demo.
- [Atlas Fields Studios](../../raw/items/x-2094840529997410525/) — `x-2094840529997410525` — EM-field viz around PCB designs (also `keyboard-pcb`).
- [GetLayers scenes](../../raw/items/web-getlayers-ai/) — `web-getlayers-ai` — Orb, Rift Stone, Pinwheel Galaxy as promptable heroes.

## All items

<!-- AUTO:ITEMS -->
- [The Complete Shelf](../../raw/items/github-mengto-complete-shelf/) — `github-mengto-complete-shelf`
- [Agent Skills (MengTo)](../../raw/items/github-mengto-skills/) — `github-mengto-skills`
- [Three.js Awesome Graphics Agent Skills](../../raw/items/github-scottstts-threejs-awesome-graphics-agent-skills/) — `github-scottstts-threejs-awesome-graphics-agent-skills`
- [FeralUI](../../raw/items/web-feralui-dev/) — `web-feralui-dev`
- [GetLayers AI](../../raw/items/web-getlayers-ai/) — `web-getlayers-ai`
- [A Developer's Guide to Taste in the Age of AI](../../raw/items/web-opale-ui-taste/) — `web-opale-ui-taste`
- [ORYZO AI](../../raw/items/web-oryzo-ai/) — `web-oryzo-ai`
- [Utsubo](../../raw/items/web-utsubo/) — `web-utsubo`
- [I'm working on a one-click AI-generated texturing feature for 3D models. I render the model from four sides and project ](../../raw/items/x-2057113327508345047/) — `x-2057113327508345047`
- [Day 15 of the dream game build (yeah I know the real count is higher, but this is update #15) 🚀 I finally figured out ho](../../raw/items/x-2086537093120164177/) — `x-2086537093120164177`
- [Claude can now build 3D websites and most people still don't know how. This free 1-hour course covers interactive 3D exp](../../raw/items/x-2086599657925329347/) — `x-2086599657925329347`
- [Three new models are live in the Arena: ⚫ Hitem3D v3.0 (Preview) - Main Arena ⚫ Meshy 7 - Main Arena ⚫ Tripo P2.0 - Low ](../../raw/items/x-2087905319255257296/) — `x-2087905319255257296`
- [Gemini 3.7 Flash High in Antigravity 🔥🔥 it created this in ~4 mins - pretty fast and perfect > Bugatti W16 engine with m](../../raw/items/x-2088240171565412733/) — `x-2088240171565412733`
- [This is a really useful tutorial if you want to learn how to build more advanced Three.js landing pages with Claude Code](../../raw/items/x-2088265078919282836/) — `x-2088265078919282836`
- [The bike, the ruins, the ramps, the Highlands sky. All of it started as one sentence typed into Atlas. Concept art, 3D a](../../raw/items/x-2088299905324396589/) — `x-2088299905324396589`
- [@threejs Awesome Graphics Agent Skills v0.8.0 is out! npx threejs-awesome-graphics-agent-skills@latest install --agent c](../../raw/items/x-2088738850705113398/) — `x-2088738850705113398`
- [#Threejs Here is how you will create detailed models using ai.  1) You need very good reference images 2) You need to](../../raw/items/x-2089094757750595713/) — `x-2089094757750595713`
- [Introducing /improve-threejs Turn vibe-slop Three.js prototypes into stunning apps It makes slow, visually buggy games r](../../raw/items/x-2089400082550620636/) — `x-2089400082550620636`
- [iCraft Editor designs 3D network architecture diagrams with immersive visual effects. https://github.com/gantFDT/icraft](../../raw/items/x-2089570022490263586/) — `x-2089570022490263586`
- [I open-sourced the Sylva three.js site and the skills behind it. I started with one reference and asked Opus 5 to recrea](../../raw/items/x-2089602918605619401/) — `x-2089602918605619401`
- [Whatttt this existed, why no one showed me this yet, https://23rd.dev](../../raw/items/x-2089740155179643231/) — `x-2089740155179643231`
- [wow spline is so back if anything disrupts the big 3d softwares, it'll be spline](../../raw/items/x-2090526692427104508/) — `x-2090526692427104508`
- [The core claim checks out. For years 3D Gaussian Splatting quality was solid, but huge files, missing streaming/LOD, and](../../raw/items/x-2090589293677023507/) — `x-2090589293677023507`
- [train gaussian splatting straight in the browser with Splat.js. SfM included, open source, and MIT Licensed. Video from ](../../raw/items/x-2090839282831270173/) — `x-2090839282831270173`
- [This blew up, so I added 60 more three.js components from experiments I made over the last two weeks. I'm still amazed b](../../raw/items/x-2091571624390881664/) — `x-2091571624390881664`
- [3d model within a website is just so crazy with Claude. I built this template where one 3D scene drives the whole page. ](../../raw/items/x-2091748299975880994/) — `x-2091748299975880994`
- [3,200,000 → 3,000 triangles, 3 SECONDS for the full bake. In the browser, with @threejs and @NeedleTools. Superb normals](../../raw/items/x-2091927587471712274/) — `x-2091927587471712274`
- [SplatPaint is a real-time browser-based creative sandbox for Gaussian Splats: paint, sculpt, recolor, relight, deform, a](../../raw/items/x-2091943679317463153/) — `x-2091943679317463153`
- [I genuinely don't have any words for this 🤯 Just ONE image of a robotic bee and somehow got this incredibly gooood 3D mo](../../raw/items/x-2092242135504552118/) — `x-2092242135504552118`
- [About 7 months ago, I started designing a WebGPU library to ship performant shaders at Vercel. Today, we are announcing ](../../raw/items/x-2093012548031254932/) — `x-2093012548031254932`
- [Mesh cleanup, UV unwrapping, and texture baking are live on Customuse. AI gives you amazing meshes with messy topology a](../../raw/items/x-2093018082293813509/) — `x-2093018082293813509`
- [I created the world's best library of AI prompts for websites that don’t look like AI slop. 👇 • 590+ Al Animation Websit](../../raw/items/x-2094009989220430084/) — `x-2094009989220430084`
- [Atlas Fields Studios — EM fields around PCB designs, free](../../raw/items/x-2094840529997410525/) — `x-2094840529997410525`
- [Atlas + spark.js + three.js scene from one input image](../../raw/items/x-2094864872853119216/) — `x-2094864872853119216`
- [全网最全的 GPT Astra 提示词和案例，已收录 153 个，每日更新。精选 3D、游戏案例，试了下有些真的能 one shot 直出超炫的效果，3D 创作时代已然来临了！ 立刻复制提示词，玩起来！](../../raw/items/x-2096805641017020530/) — `x-2096805641017020530`
- [Hitem3D 3.0: image-to-mesh at 2048³ with up to 5M faces, small details stay in geometry](../../raw/items/x-2097724373515772361/) — `x-2097724373515772361`
- [Engineer a $15,000 premium 3D-driven SaaS hero: React, Three.js/WebGL, Tailwind, Framer Motion](../../raw/items/x-2097912217207517412/) — `x-2097912217207517412`
- [GPT-6 Astra is a design beast No 3D models used in this demo website I connected LTX API to my coding agent ->](../../raw/items/x-2098464881498370090/) — `x-2098464881498370090`
- [Bordel, avant sa sortie, je trouvais GPT-5.6 Pro incroyable en 3D… mais maintenant que je le compare à Astra, c’était](../../raw/items/x-2098719191817707762/) — `x-2098719191817707762`
- [Atlas beta access is rolling out to users, some ideas for API developers - give Astra "eyes" in Blender, let it place](../../raw/items/x-2100349127620235577/) — `x-2100349127620235577`
- [I used GPT-6 Astra to create a 3D website that pulls apart the brain tech into modeled pieces! we are in a renaissance](../../raw/items/x-2100459591649878516/) — `x-2100459591649878516`
- [The vgpu skill now helps your agent create better 3D models in Blender, optimized for web](../../raw/items/x-2106051894624047547/) — `x-2106051894624047547`
- [🍟 Still using Pinterest for design inspo in 2026? These will replace it in 2027. 👇](../../raw/items/x-2108181934669238593/) — `x-2108181934669238593`
- [Introducing Anatomy](../../raw/items/x-2108948624004526516/) — `x-2108948624004526516`
- [is it legal?](../../raw/items/x-2109716261160538324/) — `x-2109716261160538324`
- [Github is hiding the cure for ugly AI-generated websites.](../../raw/items/x-2109944361408659650/) — `x-2109944361408659650`
- [vgpu 0.6 is out 🔉](../../raw/items/x-2110049100611940501/) — `x-2110049100611940501`
<!-- /AUTO:ITEMS -->

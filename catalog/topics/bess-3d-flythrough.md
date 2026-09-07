# BESS 3D flythrough

Topic slug: `bess-3d-flythrough`. Adjacent: [camera-control](camera-control.md), [video-generation](video-generation.md), [gaussian-splatting](gaussian-splatting.md), [three-js](three-js.md), [ui-motion](ui-motion.md).

This lane is industrial / site flythroughs and scroll-world style landings — the marketing surface for a battery-energy-storage (BESS) cabinet or plant, not a generic 3D toy. Items here are capture-to-asset tools, scroll-scrubbed 3D heroes, and studio craft ceilings. The photoreal *video* hop (Blender → Seedance/Veo/Kling/H3, depth for interiors) is documented in [blender-minimax-h3-video-generation](../../raw/notes/blender-minimax-h3-video-generation.md); that note is the implementation spine for this lane.

The harvest is small and overlapping. scroll-world is the agent-skill path for an isometric diorama landing. Splat2Mesh and ArtiFixer are how a site scan becomes a mesh or a repaired splat before a flythrough. Lucida is indoor video → editable 3D assets (real-to-sim). Utsubo is the experiential-studio bar, not a BESS example.

Query here for “site flythrough landing,” “scan the plant then orbit it,” or “scroll-driven industrial 3D.” For camera paths and depth passes open [camera-control](camera-control.md). For the video model after the blockout open [video-generation](video-generation.md). For PLY/mesh cleanup stay on [gaussian-splatting](gaussian-splatting.md). Presence is not a recommendation.

## Pipelines

- **Scroll-scrubbed 3D hero** — agent skill + Seedance/Monid isometric flythrough on the landing (`github-oso95-scroll-world`; pairs with `github-nateherkai-scroll-craft` on [ui-motion](ui-motion.md)).
- **Scan → repair → mesh** — 3DGS capture, ArtiFixer on sparse/blurry recon, Splat2Mesh PLY → OBJ/GLB (`github-nv-tlabs-ArtiFixer`, `web-arcana-splat2mesh`, `x-2094826117056414132`).
- **Already-shot cabinet internals** — factory phone stills are too sparse for a whole-cabinet splat; split bays and gate on overlap (`note-bess-phone-photos-splat-mesh-plan`).
- **Indoor video → editable assets** — indoor footage to posed 3D objects (`x-2094961942058418268`).
- **Blender blockout → photoreal clip** — MCP camera + first/last frames + optional Z-depth (`note-blender-minimax-h3-video-generation`).

## Tools

- [scroll-world](../../raw/items/github-oso95-scroll-world/) — `github-oso95-scroll-world` — scroll-scrubbed isometric diorama skill (Seedance/Monid).
- [Splat2Mesh](../../raw/items/web-arcana-splat2mesh/) — `web-arcana-splat2mesh` — Windows 3DGS PLY → OBJ/GLB (print/DCC).
- [ArtiFixer](../../raw/items/github-nv-tlabs-ArtiFixer/) — `github-nv-tlabs-ArtiFixer` — NVIDIA diffusion enhancer/extender for 3D reconstructions.

## Techniques

- [Splat2Mesh — free Win tool](../../raw/items/x-2094826117056414132/) — `x-2094826117056414132` — 3DGS PLY → OBJ/GLB; JA launch twin `x-2094648474377839018`.
- [NVIDIA ArtiFixer thread](../../raw/items/x-2094929928865341832/) — `x-2094929928865341832` — video diffusion that rebuilds broken/blurry scans before a flythrough.
- [ByteDance Lucida](../../raw/items/x-2094961942058418268/) — `x-2094961942058418268` — indoor video → VLM/Seed3D 2.0 → individual editable 3D assets.
- [Blender Minimax H3 note](../../raw/notes/blender-minimax-h3-video-generation.md) — `note-blender-minimax-h3-video-generation` — BESS-cabinet interiors need a Blender Z-pass; commercial models invent internals from prompts alone.
- [Salvage phone photos → splat → minimal mesh](../../raw/notes/bess-phone-photos-splat-mesh-plan.md) — `note-bess-phone-photos-splat-mesh-plan` — existing S22 stills of SVOLT/Envicool/PCS bays; splat only if SfM locks.

## Examples

- [Utsubo](../../raw/items/web-utsubo/) — `web-utsubo` — technology-first studio site; scroll/3D craft ceiling (not a BESS case).
- [scroll-world](../../raw/items/github-oso95-scroll-world/) — `github-oso95-scroll-world` — closest harvested pattern for a 3D marketing flythrough on a page.

## All items

<!-- AUTO:ITEMS -->
- [ArtiFixer](../../raw/items/github-nv-tlabs-ArtiFixer/) — `github-nv-tlabs-ArtiFixer`
- [scroll-world](../../raw/items/github-oso95-scroll-world/) — `github-oso95-scroll-world`
- [ArtiFixer GPU run — takeover from hung Gaussian splat chat](../../raw/notes/artifixer-gpu-run.md) — `note-artifixer-gpu-run`
- [Plan of attack: salvage phone photos → Gaussian splat → minimal mesh](../../raw/notes/bess-phone-photos-splat-mesh-plan.md) — `note-bess-phone-photos-splat-mesh-plan`
- [LLM + Blender → AI Video: Photoreal BESS Flythrough](../../raw/notes/blender-minimax-h3-video-generation.md) — `note-blender-minimax-h3-video-generation`
- [Splat2Mesh](../../raw/items/web-arcana-splat2mesh/) — `web-arcana-splat2mesh`
- [Utsubo](../../raw/items/web-utsubo/) — `web-utsubo`
- [codex + blender is insane](../../raw/items/x-2065843739340509693/) — `x-2065843739340509693`
- [BLENDER + SEEDANCE = FULL CAMERA CONTROL Claude Opus 5 builds a simple 3D mockup of the cafe in Blender. Basic blocks fo](../../raw/items/x-2087565352372723955/) — `x-2087565352372723955`
- [Three new models are live in the Arena: ⚫ Hitem3D v3.0 (Preview) - Main Arena ⚫ Meshy 7 - Main Arena ⚫ Tripo P2.0 - Low ](../../raw/items/x-2087905319255257296/) — `x-2087905319255257296`
- [The bike, the ruins, the ramps, the Highlands sky. All of it started as one sentence typed into Atlas. Concept art, 3D a](../../raw/items/x-2088299905324396589/) — `x-2088299905324396589`
- [MiniMax H3 just went unlimited on Runway. Generate responsibly. Or don't. It's unlimited 😌](../../raw/items/x-2090098441200517416/) — `x-2090098441200517416`
- [wow spline is so back if anything disrupts the big 3d softwares, it'll be spline](../../raw/items/x-2090526692427104508/) — `x-2090526692427104508`
- [The core claim checks out. For years 3D Gaussian Splatting quality was solid, but huge files, missing streaming/LOD, and](../../raw/items/x-2090589293677023507/) — `x-2090589293677023507`
- [How about one image straight to an editable UE5 or Blender scene? Lumera just dropped paper - Engine-Native Editable 3D ](../../raw/items/x-2093937170717585657/) — `x-2093937170717585657`
- [Splat2Mesh launch (JA) — 3DGS PLY → OBJ/GLB](../../raw/items/x-2094648474377839018/) — `x-2094648474377839018`
- [Splat2Mesh — free Win tool, 3DGS PLY → OBJ/GLB](../../raw/items/x-2094826117056414132/) — `x-2094826117056414132`
- [NVIDIA ArtiFixer — video diffusion that rebuilds broken/blurry 3D scans](../../raw/items/x-2094929928865341832/) — `x-2094929928865341832`
- [ByteDance Lucida: indoor video → editable 3D assets](../../raw/items/x-2094961942058418268/) — `x-2094961942058418268`
- [This is insane: Hyper3D just dropped WorldGen, an AI that turns ONE photo into a full interactive 3D world Yingmu Techno](../../raw/items/x-2095437841958314100/) — `x-2095437841958314100`
<!-- /AUTO:ITEMS -->

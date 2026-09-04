# Judgment worksheet: image/video → 3D world (image-to-3d-world)

Owner alias: “freedom modeling.” Split the 14 primaries into *world generators*, *mesh generators*, and *cleanup*. They are not interchangeable.

## image-to-3d-world — short stack to try

1. **World from one photo (navigable, maybe not a mesh).** Hyper3D WorldGen ([x-2095437841958314100](../../items/x-2095437841958314100/card.md) — must-read), World Labs Atlas + spark.js ([x-2094864872853119216](../../items/x-2094864872853119216/card.md)), Atlas 3D AI sentence→Unreal ride ([x-2088299905324396589](../../items/x-2088299905324396589/card.md)). Lumera and Lucida are papers with “code soon.”
2. **Mesh from image (asset, not a world).** Top3D arena (Hitem3D / Meshy / Tripo) ([x-2087905319255257296](../../items/x-2087905319255257296/card.md)). The bee-photo one-shot ([x-2092242135504552118](../../items/x-2092242135504552118/card.md)) has no tool name — do not plan around it.
3. **Cleanup after generation.** Customuse unwrap/bake ([x-2093018082293813509](../../items/x-2093018082293813509/card.md)), BQR quads after boolean ([x-2093421870951387625](../../items/x-2093421870951387625/card.md)), Needle in-browser decimate ([x-2091927587471712274](../../items/x-2091927587471712274/card.md)), kokraf four-view texture projection ([x-2057113327508345047](../../items/x-2057113327508345047/card.md) — only `demonstrated` claim in this subject), Marso I2M measured PBR ([x-2095502642218664004](../../items/x-2095502642218664004/card.md)).
4. **Blender MCP from capture.** Equirectangular city ([x-2095159781883597031](../../items/x-2095159781883597031/card.md)) and “photo then paste into Blender” ([x-2095512142766342624](../../items/x-2095512142766342624/card.md)). The second is a one-liner; use it as a reminder, not a recipe.

If the output is a *splat*, leave this lane and open [gaussian-splatting/worksheet.md](../gaussian-splatting/worksheet.md). If the output is a *camera path into Seedance*, open [blockout-to-video-flythrough/brief.md](../blockout-to-video-flythrough/brief.md).

## image-to-3d-world — axis scores

| item | input | editable scene vs bake | topology after gen | engine import | license |
|---|---|---|---|---|---|
| Hyper3D WorldGen | single photo | claimed interactive/physics world | unknown | unknown (research + product) | unknown (Yingmu / SIGGRAPH 2025) |
| Atlas + spark.js | single photo (Marble) | navigable splat; mesh is a paid export | collider 100–200k / HQ 600k–1M | three.js / spark.js + GLB | World Labs; Free cannot export |
| Atlas 3D AI | text sentence | Unreal ride-through; Blender staging claimed | unknown | Blender + Unreal (promo) | product; no license text in capture |
| Lumera | single image | claimed separate meshes + movable lights | claimed object-split | UE5 / Blender | code/weights “coming soon” |
| Lucida | indoor video | claimed scene-graph + Seed3D meshes | unknown | unknown | ByteDance research |
| Top3D (Hitem3D/Meshy/Tripo) | image/text (arena) | mesh, not a world | arena-dependent | typical DCC export | vendor TOS |
| bee one-shot | single photo | mesh | claimed clean, no retries | unnamed tool | n/a |
| Customuse | existing AI mesh | cleanup/UV/bake | this *is* the topology step | DCC | SaaS |
| BQR | boolean hard-surface | quad mesh | claimed clean quads | Blender native modifiers | addon |
| Needle decimate | high-poly mesh | decimated GL for web | 3.2M→3k in 3s (stated) | three.js | “coming soon” |
| kokraf | existing three.js mesh | textured mesh | uses existing topo | three.js | MIT-ish repo stated |
| I2M 1.2 | real object photos | PBR maps, not a mesh | n/a | DCC materials | Marso product |
| Blender MCP panorama | equirectangular | Blender mesh | unknown | Blender | depends on MCP + model |

## image-to-3d-world — claims that need a receipt

- Hyper3D “editable physics world from one photo” — must-read, still a launch thread. Official site is **Rodin**; `/worldgen` 404; `/workspace/worldgen` is an **11,026**-byte login SPA with no public mesh download ([hyper3d-worldgen](../../tools/hyper3d-worldgen.md)). CAST paper tables now quoted there (CLIP 85.77 / 3D-Front CD-S 0.052). Still no engine file.
- Atlas 3D AI “one sentence → Unreal ride” — 35 replies / 3 captured; the ride may be video, not an `.uproject`.
- Lumera object-split meshes + HDR lights — project page is a 1 KB JS shell; weights/code still missing.
- Lucida parse/generate/place + GizmoAct — **project page fetched** (https://lucida-r2s.github.io/): indoor video, scene graph, Seed3D-class assets, tables on R2S / CA-1M / ADT. No weights zip.
- Needle 3.2M→3k in 3s with “superb normals” — demo numbers, tool not shipping in this capture.
- Bee topology with “no prompt, no retries” — tool unnamed; cannot reproduce.
- kokraf four-view projection is the only `demonstrated` claim (media + repo). Use it as the texture-path reference.

## image-to-3d-world — do not treat as load-bearing

- Photo→Blender “paste” ([x-2095512142766342624](../../items/x-2095512142766342624/card.md)) — 123 replies reported, 1 captured, no steps.
- Top3D arena additions — useful as a *comparison surface*, not as a pipeline.
- Anything that only shows a flythrough video. That may belong in blockout-to-video.

## image-to-3d-world — next capture work

1. Lumera paper is **arXiv:2607.20889** (Lumera-2K: 2,513 UE5 projects). Still no weights/GitHub ([hyper3d-worldgen](../../tools/hyper3d-worldgen.md)). Remaining: a logged-in WorldGen export (GLB/USD).
2. World Labs **Marble** docs + public example CDN ([atlas](../../tools/atlas.md)): Free **4** gens / no export; Standard **12** + splat/pano/collider; Pro **25** + HQ mesh; Max **75**. Official rustic-kitchen downloads (no login): collider GLB **2,976,256** B, 500k SPZ **7,582,907** B, pano **3,860,086** B. Remaining: a logged-in export of a *user* world.
3. kokraf README is a VEF modeler, not a four-view bake skill ([kokraf](../../tools/kokraf.md)). Projection path is still tweet/media-only.
4. All 14 primaries are `ready-with-gaps`. Raising even three world-gen cards to `ready` unblocks a real bake-off.

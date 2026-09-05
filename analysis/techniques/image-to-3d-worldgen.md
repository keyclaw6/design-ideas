# Image To 3d Worldgen

**Slug:** `image-to-3d-worldgen` · **Owner subject:** [image-to-3d-world](../subjects/image-to-3d-world/brief.md)
**Subjects:** [ai-video-generation](../subjects/ai-video-generation/brief.md), [blockout-to-video-flythrough](../subjects/blockout-to-video-flythrough/brief.md), [gaussian-splatting](../subjects/gaussian-splatting/brief.md), [image-to-3d-world](../subjects/image-to-3d-world/brief.md), [web-3d-scenes](../subjects/web-3d-scenes/brief.md)
**Referenced by (5):**
- [Gemini Antigravity builds photoreal Bugatti W16 Three.js scene in four minutes](../items/x-2088240171565412733/card.md) — example, technique — web-3d-scenes
- [Atlas 3D AI: one-sentence prompt to Blender staging and Unreal ride-through](../items/x-2088299905324396589/card.md) — tool, example — image-to-3d-world
- [VanhDesign WebGPU single-scene page driven by Blender keyboard model](../items/x-2091748299975880994/card.md) — technique, example — web-3d-scenes
- [World Labs Atlas plus spark.js Three.js scene from one photo](../items/x-2094864872853119216/card.md) — example, technique — image-to-3d-world
- [Hyper3D WorldGen builds editable physics worlds from one photo](../items/x-2095437841958314100/card.md) — tool, claim-source — image-to-3d-world

<!-- NOTES:START -->
One image, panorama, or text prompt → navigable world or posed assets.
Owner subject: `image-to-3d-world`. Referenced by 5 item(s): x-2088240171565412733, x-2088299905324396589, x-2091748299975880994, x-2094864872853119216, x-2095437841958314100.
Score items that use this method on the owner brief's comparison axes. Do not treat the slug as a product name.
If a later pass splits this slug, file a registry alias — do not edit cards by hand.

**2026-09-04 capture — Lumera project page re-fetch.** `GET https://haidilao0328.github.io/Lumera/` **200 / 1,087 B**. Title **Lumera | Engine-Native Editable 3D World Reconstruction**. Meta names object instances, meshes, parametric lights, HDR probes from one image. Still a JS shell. Code/weights missing. Receipt `lumera-project-page-2026-09-04.json`.

**2026-09-05 capture — arXiv 2607.20889 first-party.** `GET https://arxiv.org/abs/2607.20889` **200 / 43,789 B**. ar5iv HTML **506,831 B**. Title *Engine-Native Editable 3D World Reconstruction with Objects and Lighting*. Abstract: Lumera-2K from **2,513** UE5 projects; **3.73M** components, **63M** object instances, **102.6K** parametric lights, **95.1K** camera views. Lumera-Box / Lumera-Light adapt a VLM to parse boxes and light tuples. **No GitHub/weights URL** in the HTML (only ar5iv’s own repo). Receipt `analysis/_work/captures/lumera-arxiv-2607.20889.json`.

**2026-09-05 capture — Lucida first-party.** `GET https://arxiv.org/abs/2608.30821` **200 / 43,008 B**. Title *Lucida: Parse, Generate, and Place for Composable Real-to-Sim Scene Modeling* (Qin et al., submitted 2026-08-31, PDF **31,154 KB**). Abstract: GizmoAct VLM closed-loop gizmo edits; **+69%** mAP vs Boxer on R2S-Scene; ADD-SB@0.05 **57.8% → 83.4%** on CA-1M; scene F-Score **0.794 → 0.924** vs SAM3D. Project page `https://lucida-r2s.github.io/` **200 / 25,570 B**. Table: R2S-Scene Ours key **0.592** vs Boxer all **0.351**. GizmoAct: up to **4** views / **12** steps. **Seed3D 2.0 is tweet-only** (not in this abstract). No weights/repo (OrangeSodahub user only). Card `x-2094961942058418268` is now `ready` (thread `captured_full`). Receipts `lucida-abs.json`, `lucida-page.json`.

**2026-09-05 capture — hayashimon panorama city.** Tweet already EN-glossed on the card. Author estimates **3 person-days** for a manual rebuild. fxtwitter returns **no video** (still-image post). Thread stays `captured_partial` (3/2). Card dropped `translation-needed`. Receipt `hayashimon-2095159781883597031.json`.

**2026-09-05 capture — Marso Studio / I2M.** Quoted `t.co/dPdYG2wjMB` → `https://marso.app` **200 / 180,651 B**. Pricing: Free **$0 / 400** credits; Artist **$29 / 2,400**; Artist Pro **$99 / 9,500**; next listed **40,000**. Page names I2M (API texture set, fine-tuning). Tweet “I2M 1.2” version headline is **not** a homepage H1. Card [x-2095502642218664004](../items/x-2095502642218664004/card.md) gap is now `thread-partial`.

Neighbor (parked; no needle-tools.md): 2026-09-05 `https://needle.tools/` GET 200 / **108,738 B**. First-party Needle Mesh Baker: fewer triangles, baked textures, one draw call. Tweet **3,200,000 → 3,000 / 3 s** and AO quality absent. Receipt `leftover5-2026-09-05.json`.
<!-- NOTES:END -->

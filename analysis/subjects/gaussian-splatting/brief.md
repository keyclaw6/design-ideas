# Gaussian splatting (3DGS) capture, edit, export (gaussian-splatting)

## gaussian-splatting — scope

3DGS training/viewers/editors (Splat.js, LichtFeld Studio, SplatPaint, brush selection), splat→mesh (Splat2Mesh, 3DGS Mesh Converter), splat repair (ArtiFixer), splat research (GaussianGPT, LightFuse), streaming/LOD, camera animation and 4K export from splats, splat→3D print.

Exclusion: Reconstruction that does not produce/consume splats → image-to-3d-world.

Priority `now`. Owner aliases: Gaussian splatting, 3DGS, splats.
Expected primary range [14, 22]. This roster has **17** primary and **1** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## gaussian-splatting — what the owner is trying to decide

Decide a capture → edit → mesh/export path for 3DGS: which viewers and editors are usable, which splat→mesh converters hold up, and when repair (ArtiFixer) is required before print or engine import.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## gaussian-splatting — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=10, technique=3, example=4, claim-source=7, reference=6.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (9):
- [NVIDIA ArtiFixer: diffusion repair for sparse 3D Gaussian reconstructions](../../items/github-nv-tlabs-ArtiFixer/card.md) — tool, technique — Official NVIDIA SIL repo for ArtiFixer (SIGGRAPH 2026): auto-regressive diffusion models that enhance and extend 3DGRUT-based…
- [Arcana Splat2Mesh — Windows 3DGS PLY to OBJ/GLB mesh exporter](../../items/web-arcana-splat2mesh/card.md) — tool — Windows 11 desktop app importing 3D Gaussian Splatting PLY captures and exporting editable OBJ or GLB meshes for Blender, DCC, and 3D…
- [Browser Gaussian splat training with open-source Splat.js](../../items/x-2090839282831270173/card.md) — tool, reference — @RadianceFields post highlighting Splat.js for training Gaussian splatting in the browser with bundled SfM, MIT license, and an attached…
- [SplatPaint browser sandbox for painting and editing Gaussian splats](../../items/x-2091943679317463153/card.md) — tool, example — SplatPaint is a real-time browser creative sandbox for Gaussian splats: paint, sculpt, recolor, relight, deform, animate, and layer…
- [Arcana Splat2Mesh: local CPU 3DGS-to-mesh converter launching free](../../items/x-2093179838249251011/card.md) — tool, claim-source — ArcanaMfg announces upcoming Splat2Mesh software converting 3D Gaussian splats to mesh locally without a GPU, aiming for a mostly free…
- [Spatial Studio: splat capture then in-browser camera animation and 4K export](../../items/x-2094377838774472944/card.md) — tool, technique — ShreyashT25 demos Spatial Studio adding in-browser camera animation and 4K video export to Gaussian splats so camera moves can be…
- [Splat2Mesh: free Windows tool converting 3DGS PLY to OBJ/GLB](../../items/x-2094826117056414132/card.md) — tool — Japanese CG blogger @ymt3d highlights Arcana Mfg's free Windows Splat2Mesh app that converts 3D Gaussian Splatting PLY files to OBJ/GLB…
- [Splat2Mesh converts 3DGS PLY to OBJ/GLB for Blender and print](../../items/x-2095136786095951924/card.md) — tool — Japanese post covering ArcanaMfg's Splat2Mesh release, which turns compatible Gaussian splat PLY files into polygon meshes exported as…
- [Browser beta: IZUTSUYA 3DGS Mesh Converter PLY to GLB/STL/OBJ](../../items/x-2095336950890983773/card.md) — tool, reference — 3dnchu shares IZUTSUYA's browser-only 3DGS Mesh Converter beta at 4dgs.jp, converting PLY splats to GLB, STL, or OBJ without install or…

First role `example` (2):
- [SuperSplat brush selection mode praised by PlayCanvas author](../../items/x-2093397098544648516/card.md) — example — PlayCanvas/SuperSplat maintainer @slimbuck7 demos new brush-based splat selection, calling it a long-overdue editor improvement for…
- [LichtFeldStudio splat to Splat2Mesh to Mimaki 3DUJ-2207 print pipeline](../../items/x-2095375790875840593/card.md) — example, technique — Arcana Manufacturing demo: exported LichtFeldStudio Gaussian splat data, converted with Splat2Mesh, and 3D-printed on a Mimaki 3DUJ-2207…

First role `claim-source` (3):
- [3DGS infrastructure advances: LOD, streaming, SPZ, Aholo city-scale viewer](../../items/x-2090589293677023507/card.md) — claim-source, reference — Technical summary that large-scene 3D Gaussian Splatting is becoming deployable via LOD, progressive streaming, SPZ compression,…
- [LichtFeld Studio 5M-Gaussian training benchmark on RTX 4090](../../items/x-2091899114153754949/card.md) — claim-source, example — Benchmark post reporting LichtFeld Studio training five million Gaussians with mrnf across thirty thousand steps on an RTX 4090, noting…
- [Arcana Splat2Mesh launch: 3DGS PLY to OBJ/GLB (Japanese)](../../items/x-2094648474377839018/card.md) — claim-source, tool — Arcana Mfg announces Splat2Mesh v1.0 converting 3D Gaussian Splatting PLY files to OBJ/GLB locally with free personal non-commercial use

First role `reference` (3):
- [GaussianGPT autoregressive 3D Gaussian scene generation (ECCV 2026)](../../items/x-2093563796237471912/card.md) — reference, claim-source — Announcement of GaussianGPT, an ECCV 2026 method that generates 3D Gaussian scenes autoregressively token-by-token with a GPT-style…
- [LightFuse: relightable multi-scan Gaussian reconstruction with 2DGS ray tracing](../../items/x-2094769581965369822/card.md) — reference, claim-source — MrNeRF presents LightFuse for relightable multi-scan interactive Gaussian reconstruction with material–illumination decomposition,…
- [NVIDIA ArtiFixer tweet: video diffusion repairs sparse 3D scans](../../items/x-2094929928865341832/card.md) — reference, claim-source — Aggregator recap of NVIDIA open-source ArtiFixer: video diffusion synthesizes missing camera angles on broken 3D scans then reconstructs…

Secondary membership (1), not in the primary count:
- [World Labs Atlas plus spark.js Three.js scene from one photo](../../items/x-2094864872853119216/card.md) — primary `image-to-3d-world`

## gaussian-splatting — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [splat-pipeline](../../techniques/splat-pipeline.md) — Train, edit, view, repair, and mesh-export a 3D Gaussian splat as one path.

## gaussian-splatting — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [splat2mesh](../../tools/splat2mesh.md)
- [splat-js](../../tools/splat-js.md)
- [lichtfeld-studio](../../tools/lichtfeld-studio.md)
- [arcana-splat2mesh](../../tools/arcana-splat2mesh.md)
- [supersplat](../../tools/supersplat.md)
- [artifixer](../../tools/artifixer.md)

## gaussian-splatting — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `github-nv-tlabs-ArtiFixer#c1` | ArtiFixer uses auto-regressive diffusion to enhance and extend 3D reconstructions built on 3DGRUT. | stated | [NVIDIA ArtiFixer: diffusion repair fo…](../../items/github-nv-tlabs-ArtiFixer/card.md) |
| `github-nv-tlabs-ArtiFixer#c2` | Hugging Face hosts artifixer-14b.pt (~16.9B) and artifixer-1.3b.pt (~1.68B) checkpoints. | stated | [NVIDIA ArtiFixer: diffusion repair fo…](../../items/github-nv-tlabs-ArtiFixer/card.md) |
| `web-arcana-splat2mesh#c1` | Splat2Mesh imports 3DGS PLY and exports polygon meshes as OBJ or GLB. | stated | [Arcana Splat2Mesh — Windows 3DGS PLY …](../../items/web-arcana-splat2mesh/card.md) |
| `web-arcana-splat2mesh#c2` | The v1.0 Windows installer is free for personal and non-commercial use. | stated | [Arcana Splat2Mesh — Windows 3DGS PLY …](../../items/web-arcana-splat2mesh/card.md) |
| `x-2090589293677023507#c1` | Named advances include LOD systems, progressive streaming, SPZ compression, collision meshes, and true browser render… | stated | [3DGS infrastructure advances: LOD, st…](../../items/x-2090589293677023507/card.md) |
| `x-2090589293677023507#c2` | ManycoreTech open-source Aholo Viewer is cited running city-scale scenes with over a billion splats in the browser. | stated | [3DGS infrastructure advances: LOD, st…](../../items/x-2090589293677023507/card.md) |
| `x-2090839282831270173#c1` | Splat.js trains Gaussian splatting in the browser with SfM included under MIT license. | stated | [Browser Gaussian splat training with …](../../items/x-2090839282831270173/card.md) |
| `x-2091899114153754949#c1` | The capture reports five million Gaussians trained with mrnf for thirty thousand steps on an RTX 4090. | stated | [LichtFeld Studio 5M-Gaussian training…](../../items/x-2091899114153754949/card.md) |
| `x-2091943679317463153#c1` | SplatPaint supports paint, sculpt, recolor, relight, deform, animate, and particle FX on splats in the browser. | stated | [SplatPaint browser sandbox for painti…](../../items/x-2091943679317463153/card.md) |
| `x-2091943679317463153#c2` | Users can convert an image, logo, or 3D model into splats inside SplatPaint without an existing splat file. | stated | [SplatPaint browser sandbox for painti…](../../items/x-2091943679317463153/card.md) |
| `x-2093179838249251011#c1` | Arcana will release software converting 3DGS to mesh that runs locally without a GPU. | stated | [Arcana Splat2Mesh: local CPU 3DGS-to-…](../../items/x-2093179838249251011/card.md) |
| `x-2093179838249251011#c2` | The Splat2Mesh tool is being prepared as basically free for anyone to use. | stated | [Arcana Splat2Mesh: local CPU 3DGS-to-…](../../items/x-2093179838249251011/card.md) |
| `x-2093397098544648516#c1` | SuperSplat added a brush selection mode praised as overdue. | stated | [SuperSplat brush selection mode prais…](../../items/x-2093397098544648516/card.md) |
| `x-2093397098544648516#c2` | The author compares the feature to something that should have existed years ago. | stated | [SuperSplat brush selection mode prais…](../../items/x-2093397098544648516/card.md) |
| `x-2093563796237471912#c1` | GaussianGPT generates 3D Gaussian scenes autoregressively with a GPT-style transformer. | stated | [GaussianGPT autoregressive 3D Gaussia…](../../items/x-2093563796237471912/card.md) |

Full set: claims.jsonl (39 rows)

## gaussian-splatting — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- input (phone video, DSLR, existing splat)
- edit affordance (brush, crop, relight)
- export target (mesh, print, engine, web viewer)
- local vs hosted GPU
- repair step required before use

## gaussian-splatting — thread coverage

X items in primary roster: 15. captured_full=1, captured_partial=6, empty=6, failed=2.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2090589293677023507](../../items/x-2090589293677023507/thread.md) | empty | 0 | 0 | 0 |
| [x-2090839282831270173](../../items/x-2090839282831270173/thread.md) | captured_partial | 4 | 1 | 1 |
| [x-2091899114153754949](../../items/x-2091899114153754949/thread.md) | captured_partial | 13 | 1 | 0 |
| [x-2091943679317463153](../../items/x-2091943679317463153/thread.md) | empty | 0 | 0 | 0 |
| [x-2093179838249251011](../../items/x-2093179838249251011/thread.md) | captured_partial | 10 | 3 | 0 |
| [x-2093397098544648516](../../items/x-2093397098544648516/thread.md) | captured_partial | 4 | 1 | 1 |
| [x-2093563796237471912](../../items/x-2093563796237471912/thread.md) | captured_partial | 5 | 3 | 1 |
| [x-2094377838774472944](../../items/x-2094377838774472944/thread.md) | captured_partial | 2 | 1 | 1 |
| [x-2094648474377839018](../../items/x-2094648474377839018/thread.md) | empty | 0 | 0 | 0 |
| [x-2094769581965369822](../../items/x-2094769581965369822/thread.md) | failed | 1 | 0 | 0 |
| [x-2094826117056414132](../../items/x-2094826117056414132/thread.md) | empty | 0 | 0 | 0 |
| [x-2094929928865341832](../../items/x-2094929928865341832/thread.md) | captured_full | 2 | 2 | 0 |
| [x-2095136786095951924](../../items/x-2095136786095951924/thread.md) | failed | 1 | 0 | 0 |
| [x-2095336950890983773](../../items/x-2095336950890983773/thread.md) | empty | 0 | 0 | 0 |
| [x-2095375790875840593](../../items/x-2095375790875840593/thread.md) | empty | 0 | 0 | 0 |

## gaussian-splatting — gaps and open questions

Primary readiness: ready=6, ready-with-gaps=11. Gap tags: translation-needed=4, thread-failed=2, thread-partial=1.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- Which splat→mesh path survives print or engine collision?
- Is ArtiFixer required on phone-captured splats or only on research scenes?

If this subject drops below 6 primary items after a future reclass, merge it into `image-to-3d-world` and delete the folder.

## gaussian-splatting — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [image-to-3d-world](../image-to-3d-world/brief.md)
- [web-3d-scenes](../web-3d-scenes/brief.md)
- [ai-cad-hardware](../ai-cad-hardware/brief.md)


# Image/video → 3D world, mesh, scene (image-to-3d-world)

## image-to-3d-world — scope

One image / panorama / video → navigable world, editable engine scene, mesh, or posed assets (World Labs Atlas, Hyper3D WorldGen, Lumera, Lucida, Magnific 3D Motion); image→3D model generators and arenas (Hitem3D, Meshy, Tripo); AI texturing / materials (I2M); mesh cleanup, retopo, baking (Customuse, BQR, Needle); Blender MCP builds from photo/panorama input.

Exclusion: Splat-native pipelines → gaussian-splatting. Blockout for video → blockout-to-video-flythrough.

Priority `now`. Owner aliases: freedom modeling, world from image, photogrammetry, text-to-3d.
Expected primary range [12, 22]. This roster has **14** primary and **7** secondary items.
Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.
Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.

## image-to-3d-world — what the owner is trying to decide

The owner called this “freedom modeling.” Decide which image/video→navigable world or mesh tools (Atlas, Hyper3D, Lumera, Meshy, Hitem3D) produce an editable scene rather than a one-shot render, and how cleanup/retopo fits after generation.

The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.
Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.

## image-to-3d-world — roster by role

Role counts (an item may have 1–3 roles; counted once per role): tool=7, technique=4, example=6, claim-source=7, reference=3.
Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.

First role `tool` (6):
- [Atlas 3D AI: one-sentence prompt to Blender staging and Unreal ride-through](../../items/x-2088299905324396589/card.md) — tool, example — Atlas 3D AI promo showing a Highlands bike scene built from one sentence through concept art, 3D assets, Blender staging, and an Unreal…
- [Needle browser mesh decimation: 3.2M to 3K triangles in 3 seconds](../../items/x-2091927587471712274/card.md) — tool, claim-source — hybridherbst demos in-browser mesh decimation via Three.js and Needle Tools reducing 3.2 million triangles to 3,000 in three seconds…
- [Customuse mesh cleanup UV unwrap and texture baking pipeline](../../items/x-2093018082293813509/card.md) — tool — Customuse adds mesh cleanup, UV unwrapping, and texture baking so AI-generated meshes with messy topology can go through generate,…
- [BQR Blender addon: clean quad topology after boolean hard-surface ops](../../items/x-2093421870951387625/card.md) — tool, claim-source — 3DxDEV7 promotes the BQR Blender addon as producing clean quad topology with native modifiers after boolean operations for hard-surface…
- [Hyper3D WorldGen builds editable physics worlds from one photo](../../items/x-2095437841958314100/card.md) — tool, claim-source — Announcement thread for Hyper3D WorldGen (Yingmu Technology, CAST/SIGGRAPH 2025): one 2D image becomes an interactive 3D world with…
- [Marso I2M 1.2: measured PBR materials from real objects](../../items/x-2095502642218664004/card.md) — tool, claim-source — Marso announces I2M 1.2 with improved metallics, roughness, albedo, and IOR maps learned from physically measured real objects rather…

First role `technique` (2):
- [kokraf four-view AI texture projection for Three.js meshes](../../items/x-2057113327508345047/card.md) — technique, example — kokraf3d builds a one-click AI texturing flow for Three.js meshes: render four orthographic sides, generate textures with an image…
- [Photo-to-Blender paste pipeline for real-world previz](../../items/x-2095512142766342624/card.md) — technique, example — Minimal X post describing a two-step pipeline: photograph the real world, then paste it into Blender 3D

First role `example` (3):
- [Single bee photo yields clean-topology 3D mesh without retries](../../items/x-2092242135504552118/card.md) — example, claim-source — @thebuggeddev claims one robotic-bee reference photo produced a high-quality 3D model with good topology in a single pass, with no…
- [World Labs Atlas plus spark.js Three.js scene from one photo](../../items/x-2094864872853119216/card.md) — example, technique — Ian Curtis (World Labs design) shows a navigable interior scene generated from one input photo using Atlas world model, spark.js…
- [Blender MCP plus Fable 5.1 builds city mesh from equirectangular panorama](../../items/x-2095159781883597031/card.md) — example, technique — Japanese X post showing Blender MCP with Fable 5.1 building a dense city model from an equirectangular panorama in one shot

First role `claim-source` (2):
- [Lumera paper: one image to editable UE5/Blender scene with engine lights](../../items/x-2093937170717585657/card.md) — claim-source, reference — Announcement of Lumera research reconstructing a single image into separate editable meshes with movable engine lights and an extracted…
- [ByteDance Lucida indoor video to editable 3D asset meshes](../../items/x-2094961942058418268/card.md) — claim-source, reference — Japanese recap of ByteDance Seed Lucida research parsing indoor video into a scene graph, generating separate editable meshes via Seed3D…

First role `reference` (1):
- [Top3D.ai arena adds Hitem3D v3, Meshy 7, and Tripo P2.0](../../items/x-2087905319255257296/card.md) — reference, tool — Top3D.ai announces Hitem3D v3.0 preview and Meshy 7 in the main arena plus Tripo P2.0 in the low-poly arena, using the same prompt pool…

Must-read (from `judge_hints.must_read`, ≤ 12):
- [Hyper3D WorldGen builds editable physics worlds from one photo](../../items/x-2095437841958314100/card.md)

Secondary membership (7), not in the primary count:
- [NVIDIA ArtiFixer: diffusion repair for sparse 3D Gaussian reconstructions](../../items/github-nv-tlabs-ArtiFixer/card.md) — primary `gaussian-splatting`
- [Gemini Antigravity builds photoreal Bugatti W16 Three.js scene in four minutes](../../items/x-2088240171565412733/card.md) — primary `web-3d-scenes`
- [VanhDesign WebGPU single-scene page driven by Blender keyboard model](../../items/x-2091748299975880994/card.md) — primary `web-3d-scenes`
- [Magnific 3D Motion exports camera paths as Seedance 2.5 references](../../items/x-2091913781236683162/card.md) — primary `blockout-to-video-flythrough`
- [GLM-5.3-Flash agent builds navigable Blender dream kitchen world](../../items/x-2093047548550525165/card.md) — primary `blockout-to-video-flythrough`
- [Claude Code alchemist shop pipeline across Blender MCP and 3D AI Studio](../../items/x-2093064017468145963/card.md) — primary `blockout-to-video-flythrough`
- [NVIDIA ArtiFixer tweet: video diffusion repairs sparse 3D scans](../../items/x-2094929928865341832/card.md) — primary `gaussian-splatting`

## image-to-3d-world — techniques

Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.

- [mesh-cleanup-retopo](../../techniques/mesh-cleanup-retopo.md) — Decimate, quad, bake, and project textures so a generated mesh is editable.
- [image-to-3d-worldgen](../../techniques/image-to-3d-worldgen.md) — One image, panorama, or text prompt → navigable world or posed assets.
- [worldgen-to-video](../../techniques/worldgen-to-video.md) — World/mesh generation handed to a video model for a flythrough instead of a real-time engine render.
- [splat-pipeline](../../techniques/splat-pipeline.md) — Train, edit, view, repair, and mesh-export a 3D Gaussian splat as one path.

## image-to-3d-world — tools

Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.

- [kokraf](../../tools/kokraf.md)
- [atlas-3d-ai](../../tools/atlas-3d-ai.md)
- [bqr-blender-addon](../../tools/bqr-blender-addon.md)
- [atlas](../../tools/atlas.md)
- [spark-js](../../tools/spark-js.md)
- [three-js](../../tools/three-js.md)
- [hyper3d-worldgen](../../tools/hyper3d-worldgen.md)
- [seedance](../../tools/seedance.md)

## image-to-3d-world — claims to adjudicate

A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.

| claim id | text | confidence | item |
|---|---|---|---|
| `x-2057113327508345047#c1` | The pipeline renders a model from four sides and projects generated textures back onto the mesh. | demonstrated | [kokraf four-view AI texture projectio…](../../items/x-2057113327508345047/card.md) |
| `x-2057113327508345047#c2` | Source code is published at github.com/sengchor/kokraf. | stated | [kokraf four-view AI texture projectio…](../../items/x-2057113327508345047/card.md) |
| `x-2087905319255257296#c1` | Hitem3D v3.0 preview and Meshy 7 joined the main Top3D.ai arena with matched prompts and settings. | stated | [Top3D.ai arena adds Hitem3D v3, Meshy…](../../items/x-2087905319255257296/card.md) |
| `x-2087905319255257296#c2` | Tripo P2.0 competes in the low-poly arena track under the same prompt pool. | stated | [Top3D.ai arena adds Hitem3D v3, Meshy…](../../items/x-2087905319255257296/card.md) |
| `x-2088299905324396589#c1` | Atlas builds concept art, 3D assets, a Blender staging pass, and an Unreal ride-through scene from one sentence prompt. | stated | [Atlas 3D AI: one-sentence prompt to B…](../../items/x-2088299905324396589/card.md) |
| `x-2088299905324396589#c2` | Atlas keeps the world on one canvas so the look stays consistent from first image to engine. | stated | [Atlas 3D AI: one-sentence prompt to B…](../../items/x-2088299905324396589/card.md) |
| `x-2091927587471712274#c1` | Demo reports reducing 3,200,000 triangles to 3,000 in three seconds in-browser with Three.js and Needle Tools. | stated | [Needle browser mesh decimation: 3.2M …](../../items/x-2091927587471712274/card.md) |
| `x-2091927587471712274#c2` | Author claims superb normals and ambient-occlusion quality from the bake and says the tool is coming soon. | stated | [Needle browser mesh decimation: 3.2M …](../../items/x-2091927587471712274/card.md) |
| `x-2092242135504552118#c1` | One bee image produced a high-quality 3D model with good topology. | stated | [Single bee photo yields clean-topolog…](../../items/x-2092242135504552118/card.md) |
| `x-2092242135504552118#c2` | The author says no prompt, rework, or retries were needed. | stated | [Single bee photo yields clean-topolog…](../../items/x-2092242135504552118/card.md) |
| `x-2093018082293813509#c1` | Customuse now offers mesh cleanup, UV unwrapping, and texture baking after AI mesh generation. | stated | [Customuse mesh cleanup UV unwrap and …](../../items/x-2093018082293813509/card.md) |
| `x-2093018082293813509#c2` | Pipeline covers generate then clean, unwrap, and bake in one place for production-ready assets. | stated | [Customuse mesh cleanup UV unwrap and …](../../items/x-2093018082293813509/card.md) |
| `x-2093421870951387625#c1` | Author claims BQR yields clean quad topology with native modifiers after booleans. | stated | [BQR Blender addon: clean quad topolog…](../../items/x-2093421870951387625/card.md) |
| `x-2093937170717585657#c1` | Lumera rebuilds each object as a separate mesh and recreates lighting as movable engine lights plus an HDR environment. | stated | [Lumera paper: one image to editable U…](../../items/x-2093937170717585657/card.md) |
| `x-2093937170717585657#c2` | Code and weights are marked as coming soon on the project page linked from the post. | stated | [Lumera paper: one image to editable U…](../../items/x-2093937170717585657/card.md) |

Full set: claims.jsonl (43 rows)

## image-to-3d-world — comparison axes

Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.

- input type (single image, panorama, video)
- output is editable scene vs baked render
- mesh topology quality after generation
- engine import path (Blender, Unreal, three.js)
- commercial license clarity

## image-to-3d-world — thread coverage

X items in primary roster: 14. captured_full=1, captured_partial=13, empty=0, failed=0.
Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.
Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.

| id | thread status | reported | captured | relevant |
|---|---|---|---|---|
| [x-2057113327508345047](../../items/x-2057113327508345047/thread.md) | captured_partial | 9 | 3 | 1 |
| [x-2087905319255257296](../../items/x-2087905319255257296/thread.md) | captured_partial | 2 | 1 | 0 |
| [x-2088299905324396589](../../items/x-2088299905324396589/thread.md) | captured_partial | 35 | 3 | 1 |
| [x-2091927587471712274](../../items/x-2091927587471712274/thread.md) | captured_partial | 7 | 3 | 1 |
| [x-2092242135504552118](../../items/x-2092242135504552118/thread.md) | captured_partial | 51 | 3 | 3 |
| [x-2093018082293813509](../../items/x-2093018082293813509/thread.md) | captured_partial | 45 | 1 | 1 |
| [x-2093421870951387625](../../items/x-2093421870951387625/thread.md) | captured_partial | 3 | 1 | 0 |
| [x-2093937170717585657](../../items/x-2093937170717585657/thread.md) | captured_partial | 11 | 3 | 2 |
| [x-2094864872853119216](../../items/x-2094864872853119216/thread.md) | captured_partial | 16 | 1 | 0 |
| [x-2094961942058418268](../../items/x-2094961942058418268/thread.md) | captured_full | 1 | 1 | 1 |
| [x-2095159781883597031](../../items/x-2095159781883597031/thread.md) | captured_partial | 3 | 2 | 0 |
| [x-2095437841958314100](../../items/x-2095437841958314100/thread.md) | captured_partial | 8 | 3 | 0 |
| [x-2095502642218664004](../../items/x-2095502642218664004/thread.md) | captured_partial | 2 | 1 | 0 |
| [x-2095512142766342624](../../items/x-2095512142766342624/thread.md) | captured_partial | 123 | 1 | 1 |

## image-to-3d-world — gaps and open questions

Primary readiness: ready=0, ready-with-gaps=14. Gap tags: thread-partial=3, translation-needed=2, linked-page-unfetched=1, thread-failed=1.
Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.

Open questions for the later judge:

- Atlas / Hyper3D / Lumera: which output is an editable mesh versus a flythrough video?
- Where does retopo have to happen before a design agent can restyle the scene?

If this subject drops below 6 primary items after a future reclass, merge it into `gaussian-splatting` and delete the folder.

## image-to-3d-world — adjacent subjects

Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.

- [gaussian-splatting](../gaussian-splatting/brief.md)
- [blockout-to-video-flythrough](../blockout-to-video-flythrough/brief.md)
- [web-3d-scenes](../web-3d-scenes/brief.md)


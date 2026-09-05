# ByteDance Lucida indoor video to editable 3D asset meshes

`x-2094961942058418268` · x · paper · ja · [source](https://x.com/tokufxug/status/2094961942058418268) · [raw](../../../raw/items/x-2094961942058418268/)
**Author:** Sadao Tokuyama (@tokufxug) · **Published:** 2026-09-02T01:33:44Z · **Captured:** 2026-09-02T17:25:49Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [image-to-3d-world](../../subjects/image-to-3d-world/brief.md) · **Also:** — · **Roles:** claim-source, reference · **Platforms:** other

**Summary.** Japanese recap of ByteDance Seed Lucida research parsing indoor video into a scene graph, generating separate editable meshes via Seed3D 2.0, and placing objects with a VLM-driven GizmoAct 3D editor loop.
**Question it answers.** How does Lucida turn indoor walkthrough video into editable per-object 3D meshes?

**Claims.**
- `x-2094961942058418268#c1` (capability, stated) Lucida reconstructs indoor video into editable 3D scenes using a VLM and Seed3D 2.0 with object detection and pose alignment. — evidence: "VLMやSeed3D 2.0を活用しReal-to-Simを実現" [post]
- `x-2094961942058418268#c2` (benchmark, demonstrated) Project-page table: scene-level detection AP on R2S-Scene is 0.592 (Ours key) versus 0.351 (Boxer all). Tweet 0.592 vs Boxer 0.351 matches this first-party row. — evidence: "GET https://lucida-r2s.github.io/ 200 25570 B. Table: R2S-Scene All objects Ours key 0.592 vs Boxer all 0.351." [note]
- `x-2094961942058418268#c3` (benchmark, demonstrated) arXiv:2608.30821 abs (200 / 43,008 B, submitted 2026-08-31): Lucida is parse → generate → place. Placement is GizmoAct, a VLM that edits an object gizmo in a closed loop. Abstract integers: mAP +69% vs Boxer on R2S-Scene; ADD-SB@0.05 57.8% → 83.4% on CA-1M; scene F-Score 0.794 (SAM3D) → 0.924. PDF listed 31,154 KB. Seed3D 2.0 is in the JP tweet, not in this abstract. — evidence: "GET https://arxiv.org/abs/2608.30821 200 43008 B. Title Lucida: Parse, Generate, and Place for Composable Real-to-Sim Scene Modeling. Authors Qin et al. ByteDance Seed / PKU / ZJU." [note]
- `x-2094961942058418268#c4` (availability, demonstrated) Project page https://lucida-r2s.github.io/ is 200 / 25,570 B. Parse builds a scene graph (keyframes, masks, partial clouds, 3D boxes). Generate synthesizes an occlusion-free object image then lifts it to an editable mesh. GizmoAct uses up to four views and 12 refinement steps. No weights/repo URL (author user OrangeSodahub only). Thread is captured_full (1/1). — evidence: "GET https://lucida-r2s.github.io/ 200 25570 B. Title Lucida | Composable real-to-sim scene modeling. Interactive preview copy: Could not open the interactive scene." [note]
**Numbers.** R2S-Scene det AP Ours key: 0.592 AP (linked-page); R2S-Scene det AP Boxer all: 0.351 AP (linked-page); CA-1M ADD-SB@0.05: 83.4 percent (linked-page)
**Recipe.** —
**Techniques.** [image-to-3d-worldgen](../../techniques/image-to-3d-worldgen.md)
**Tools.** —
**Links.** paper (https://arxiv.org/abs/2608.30821), https://seed.bytedance.com/en/seed3d_2_0
**Related items.** [x-2093937170717585657](../x-2093937170717585657/card.md), [x-2092242135504552118](../x-2092242135504552118/card.md)
**Media.**
`raw/items/x-2094961942058418268/media/thumb.jpg` (image, carries_technique=true) — Lucida UI still: grey object-level scene reconstruction viewport above a row of indoor keyframe thumbnails from a lab room walkthrough.
`raw/items/x-2094961942058418268/media/video.mp4` (video, carries_technique=true) — 43s demo video showing Lucida parsing indoor keyframes into separate reconstructed 3D objects in a scene editor.
**Thread.** captured_full · reported 1 · captured 1 · relevant 1 · author thread: captured → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: [x-2093937170717585657](../x-2093937170717585657/card.md), [x-2092242135504552118](../x-2092242135504552118/card.md)

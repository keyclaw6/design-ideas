# ByteDance Lucida indoor video to editable 3D asset meshes

`x-2094961942058418268` · x · paper · ja · [source](https://x.com/tokufxug/status/2094961942058418268) · [raw](../../../raw/items/x-2094961942058418268/)
**Author:** Sadao Tokuyama (@tokufxug) · **Published:** 2026-09-02T01:33:44Z · **Captured:** 2026-09-02T17:25:49Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** translation-needed
**Subject:** [image-to-3d-world](../../subjects/image-to-3d-world/brief.md) · **Also:** — · **Roles:** claim-source, reference · **Platforms:** other

**Summary.** Japanese recap of ByteDance Seed Lucida research parsing indoor video into a scene graph, generating separate editable meshes via Seed3D 2.0, and placing objects with a VLM-driven GizmoAct 3D editor loop.
**Question it answers.** How does Lucida turn indoor walkthrough video into editable per-object 3D meshes?

**Claims.**
- `x-2094961942058418268#c1` (capability, stated) Lucida reconstructs indoor video into editable 3D scenes using a VLM and Seed3D 2.0 with object detection and pose alignment. — evidence: "VLMやSeed3D 2.0を活用しReal-to-Simを実現" [post]
- `x-2094961942058418268#c2` (benchmark, stated) The paper reports scene-level det mAP 0.592 versus Boxer 0.351 on R2S-Scene. — evidence: "scene-level det mAP 0.592 vs Boxer 0.351 on R2S-Scene" [linked-page]
**Numbers.** —
**Recipe.** —
**Techniques.** —
**Tools.** —
**Links.** paper (https://arxiv.org/abs/2608.30821), https://seed.bytedance.com/en/seed3d_2_0
**Related items.** [x-2093937170717585657](../x-2093937170717585657/card.md), [x-2092242135504552118](../x-2092242135504552118/card.md)
**Media.**
`raw/items/x-2094961942058418268/media/thumb.jpg` (image, carries_technique=true) — Lucida UI still: grey object-level scene reconstruction viewport above a row of indoor keyframe thumbnails from a lab room walkthrough.
`raw/items/x-2094961942058418268/media/video.mp4` (video, carries_technique=true) — 43s demo video showing Lucida parsing indoor keyframes into separate reconstructed 3D objects in a scene editor.
**Thread.** captured_full · reported 1 · captured 1 · relevant 1 · author thread: captured → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: [x-2093937170717585657](../x-2093937170717585657/card.md), [x-2092242135504552118](../x-2092242135504552118/card.md)

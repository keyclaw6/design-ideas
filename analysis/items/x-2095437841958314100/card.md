# Hyper3D WorldGen builds editable physics worlds from one photo

`x-2095437841958314100` · x · announcement · en · [source](https://x.com/grokkedd/status/2095437841958314100) · [raw](../../../raw/items/x-2095437841958314100/)
**Author:** grokkedd (@grokkedd) · **Published:** — · **Captured:** 2026-09-04T07:50:46Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [image-to-3d-world](../../subjects/image-to-3d-world/brief.md) · **Also:** [ai-video-generation](../../subjects/ai-video-generation/brief.md) · **Roles:** tool, claim-source · **Platforms:** blender, unreal, fal

**Summary.** Announcement thread for Hyper3D WorldGen (Yingmu Technology, CAST/SIGGRAPH 2025): one 2D image becomes an interactive 3D world with per-object meshes, built-in physics, and exports to Blender, Unity, and Unreal — pairable with Seedance for cinematic video on the scene.
**Question it answers.** How does WorldGen turn a single photo into editable physics-ready 3D scenes for engines?

**Claims.**
- `x-2095437841958314100#c1` (capability, stated) WorldGen segments a single image into independently movable 3D objects with inferred hidden geometry. — evidence: "Feed it a single 2D image, and it picks out every object, fills in the hidden parts, and rebuilds each one as its own separate 3D model" [post]
- `x-2095437841958314100#c2` (capability, stated) Physics collisions, mass, and friction are inferred so objects sit and lean realistically. — evidence: "Physics comes built in. It figures out collisions, mass, friction, and how objects actually sit or lean on each other" [post]
- `x-2095437841958314100#c3` (recipe, stated) Pairing WorldGen with Seedance 2.5 yields cinematic video from the reconstructed 3D scene. — evidence: "pair it with video models like Seedance 2.5, and you get a full pipeline." [post]
- `x-2095437841958314100#c4` (availability, demonstrated) Logged-out https://hyper3d.ai/workspace/worldgen is a 11,026 B login SPA (data-app-booting, no title/h1, no gltf/usd/export strings). https://hyper3d.ai/ is Rodin (390,840 B). No public user-scene download this pass. — evidence: "GET /workspace/worldgen 200 / 11,026 B; GET https://hyper3d.ai/ 200 / 390,840 B title Hyper3D Rodin. analysis/_work/captures/2026-09-05-mustread-pages.json" [note]
**Numbers.** —
**Recipe.** —
**Techniques.** [image-to-3d-worldgen](../../techniques/image-to-3d-worldgen.md), [worldgen-to-video](../../techniques/worldgen-to-video.md)
**Tools.** [hyper3d-worldgen](../../tools/hyper3d-worldgen.md), [seedance](../../tools/seedance.md)
**Links.** product (https://hyper3d.ai/workspace/worldgen), https://hyper3d.ai/
**Related items.** [x-2093937170717585657](../x-2093937170717585657/card.md), [note-blender-minimax-h3-video-generation](../note-blender-minimax-h3-video-generation/card.md)
**Media.**
`raw/items/x-2095437841958314100/media/media_0.jpg` (video, carries_technique=true) — Demo video showing a single input photo transformed into an interactive 3D room scene with separately selectable furniture and props.
`raw/items/x-2095437841958314100/media/media_1.jpg` (video, carries_technique=true) — Follow-up demo clip showing physics interaction and engine export from the WorldGen reconstruction.
**Thread.** captured_partial · reported 8 · captured 3 · relevant 0 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: True · compare with: [x-2093937170717585657](../x-2093937170717585657/card.md), [x-2094864872853119216](../x-2094864872853119216/card.md)

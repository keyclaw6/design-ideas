# Lumera paper: one image to editable UE5/Blender scene with engine lights

`x-2093937170717585657` · x · paper · en · [source](https://x.com/Stefan_3D_AI/status/2093937170717585657) · [raw](../../../raw/items/x-2093937170717585657/)
**Author:** Stefan (@Stefan_3D_AI) · **Published:** — · **Captured:** 2026-09-04T08:08:11Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [image-to-3d-world](../../subjects/image-to-3d-world/brief.md) · **Also:** — · **Roles:** claim-source, reference · **Platforms:** unreal, blender

**Summary.** Announcement of Lumera research reconstructing a single image into separate editable meshes with movable engine lights and an extracted HDR environment instead of baking lighting into the reconstruction.
**Question it answers.** What image-to-3D approach keeps lighting as editable engine parameters in UE5 or Blender?

**Claims.**
- `x-2093937170717585657#c1` (capability, stated) Lumera rebuilds each object as a separate mesh and recreates lighting as movable engine lights plus an HDR environment. — evidence: "rebuilds every object as a separate mesh, then recreates the lighting as actual engine lights you can move and tweak. Even pulls an HDR environment out of the shot." [post]
- `x-2093937170717585657#c2` (availability, stated) Code and weights are marked as coming soon on the project page linked from the post. — evidence: "Code and weights marked as "Soon"." [post]
- `x-2093937170717585657#c3` (availability, demonstrated) Live GET https://haidilao0328.github.io/Lumera/ is 200 / 1,087 B. Title Lumera | Engine-Native Editable 3D World Reconstruction. Meta names object instances, meshes, parametric lights, and HDR environment probes from a single image. Page is a JS shell. Code/weights still missing. — evidence: "analysis/_work/captures/lumera-project-page-2026-09-04.json" [note]
- `x-2093937170717585657#c4` (capability, demonstrated) arXiv 2607.20889 (abs 43,789 B; ar5iv HTML 506,831 B) is Engine-Native Editable 3D World Reconstruction with Objects and Lighting. Abstract: Lumera-2K from 2,513 UE5 projects; 3.73M components, 63M object instances, 102.6K parametric lights, 95.1K camera views. No GitHub/weights URL in the HTML. — evidence: "GET https://arxiv.org/abs/2607.20889 200 / 43,789 B. ar5iv HTML 506,831 B. Abstract: Lumera-2K is built from 2,513 UE5 projects and provides 3.73M components, 63M object instances, 102.6K engine-native parametric lights, and 95.1K camera views." [note]
**Numbers.** Lumera-2K UE5 projects: 2513 projects (note); ar5iv HTML: 506831 bytes (note)
**Recipe.** —
**Techniques.** [image-to-3d-worldgen](../../techniques/image-to-3d-worldgen.md)
**Tools.** —
**Links.** paper (https://arxiv.org/abs/2607.20889), https://ar5iv.labs.arxiv.org/html/2607.20889
**Related items.** [x-2094961942058418268](../x-2094961942058418268/card.md), [x-2092242135504552118](../x-2092242135504552118/card.md)
**Media.** —
**Thread.** captured_partial · reported 11 · captured 3 · relevant 2 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: [x-2094961942058418268](../x-2094961942058418268/card.md), [x-2092242135504552118](../x-2092242135504552118/card.md)

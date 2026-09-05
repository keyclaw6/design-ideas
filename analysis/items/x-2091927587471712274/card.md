# Needle browser mesh decimation: 3.2M to 3K triangles in 3 seconds

`x-2091927587471712274` · x · announcement · en · [source](https://x.com/hybridherbst/status/2091927587471712274) · [raw](../../../raw/items/x-2091927587471712274/)
**Author:** herbst (@hybridherbst) · **Published:** — · **Captured:** 2026-09-04T06:49:34Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [image-to-3d-world](../../subjects/image-to-3d-world/brief.md) · **Also:** [web-3d-scenes](../../subjects/web-3d-scenes/brief.md) · **Roles:** tool, claim-source · **Platforms:** three-js, browser

**Summary.** hybridherbst demos in-browser mesh decimation via Three.js and Needle Tools reducing 3.2 million triangles to 3,000 in three seconds with strong normals and AO, teasing an upcoming public release.
**Question it answers.** How fast can Needle Tools decimate a high-poly mesh in the browser?

**Claims.**
- `x-2091927587471712274#c1` (benchmark, stated) Demo reports reducing 3,200,000 triangles to 3,000 in three seconds in-browser with Three.js and Needle Tools. — evidence: "3,200,000 → 3,000 triangles,
3 SECONDS for the full bake." [post]
- `x-2091927587471712274#c2` (capability, stated) Author claims superb normals and ambient-occlusion quality from the bake and says the tool is coming soon. — evidence: "Superb normals+ao quality now too... such a great tool to have! Coming soon!" [post]
- `x-2091927587471712274#c3` (capability, demonstrated) needle.tools 200 / 108,738 B first-party names Needle Mesh Baker: optimize 3D models in the browser — fewer triangles, baked textures, one draw call. Tweet 3,200,000 → 3,000 triangles / 3 seconds and AO quality are absent from that HTML. — evidence: "GET https://needle.tools/ 108738 B title Needle Engine. leftover5-2026-09-05.json" [note]
**Numbers.** input triangles: 3200000  (post); output triangles: 3000  (post); bake duration: 3 seconds (post)
**Recipe.** —
**Techniques.** [mesh-cleanup-retopo](../../techniques/mesh-cleanup-retopo.md)
**Tools.** —
**Links.** —
**Related items.** [github-scottstts-threejs-awesome-graphics-agent-skills](../github-scottstts-threejs-awesome-graphics-agent-skills/card.md)
**Media.** —
**Thread.** captured_partial · reported 7 · captured 3 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —

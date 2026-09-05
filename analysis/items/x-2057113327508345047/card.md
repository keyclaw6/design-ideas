# kokraf four-view AI texture projection for Three.js meshes

`x-2057113327508345047` · x · demo-video · en · [source](https://x.com/kokraf3d/status/2057113327508345047) · [raw](../../../raw/items/x-2057113327508345047/)
**Author:** kokraf3d (@kokraf3d) · **Published:** — · **Captured:** 2026-09-04T07:07:41Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [image-to-3d-world](../../subjects/image-to-3d-world/brief.md) · **Also:** [web-3d-scenes](../../subjects/web-3d-scenes/brief.md) · **Roles:** technique, example · **Platforms:** three-js

**Summary.** kokraf3d builds a one-click AI texturing flow for Three.js meshes: render four orthographic sides, generate textures with an image model, and project them back onto the mesh. Open-source at github.com/sengchor/kokraf.
**Question it answers.** How can I texture a gray 3D mesh for a web scene without manual lookdev?

**Claims.**
- `x-2057113327508345047#c1` (recipe, demonstrated) The pipeline renders a model from four sides and projects generated textures back onto the mesh. — evidence: "I render the model from four sides and project the generated textures back onto the model." [post]
- `x-2057113327508345047#c2` (availability, stated) Source code is published at github.com/sengchor/kokraf. — evidence: "Project Source Code: https://github.com/sengchor/kokraf" [post]
- `x-2057113327508345047#c3` (counter-claim, demonstrated) github.com/sengchor/kokraf README is a browser VEF mesh modeler (Three.js render; Vertex–Edge–Face edit). Live kokraf.com is collaborative 3D modeling. README and homepage HTML have no four-view / AI texture-projection copy. Tweet four-view projection stays tweet/media-only — do not treat the repo as a texture-projection skill. — evidence: "kokraf NOTES 2026-09-04: README VEF modeler; kokraf.com no four-view string." [note]
**Numbers.** —
**Recipe.** —
**Techniques.** [mesh-cleanup-retopo](../../techniques/mesh-cleanup-retopo.md)
**Tools.** [kokraf](../../tools/kokraf.md)
**Links.** repo (https://github.com/sengchor/kokraf), product (https://kokraf.com/)
**Related items.** [github-scottstts-threejs-awesome-graphics-agent-skills](../github-scottstts-threejs-awesome-graphics-agent-skills/card.md), [github-mengto-skills](../github-mengto-skills/card.md), [web-oryzo-ai](../web-oryzo-ai/card.md), [x-2086599657925329347](../x-2086599657925329347/card.md)
**Media.**
`raw/items/x-2057113327508345047/media/media_0.jpg` (video, carries_technique=true) — Screen recording demo cycling a gray 3D mesh through four orthographic renders and showing AI-generated textures projected back onto the model.
**Thread.** captured_partial · reported 9 · captured 3 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: [x-2086599657925329347](../x-2086599657925329347/card.md), [web-oryzo-ai](../web-oryzo-ai/card.md)

# World Labs Atlas plus spark.js Three.js scene from one photo

`x-2094864872853119216` · x · demo-video · en · [source](https://x.com/XRarchitect/status/2094864872853119216) · [raw](../../../raw/items/x-2094864872853119216/)
**Author:** Ian Curtis (@XRarchitect) · **Published:** 2026-09-01T19:08:01Z · **Captured:** 2026-09-02T17:23:28Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [image-to-3d-world](../../subjects/image-to-3d-world/brief.md) · **Also:** [gaussian-splatting](../../subjects/gaussian-splatting/brief.md) · **Roles:** example, technique · **Platforms:** three-js, browser

**Summary.** Ian Curtis (World Labs design) shows a navigable interior scene generated from one input photo using Atlas world model, spark.js Gaussian splat renderer, and three.js, with a follow-up still of the source image.
**Question it answers.** How does World Labs Atlas with spark.js and three.js build a splat scene from one still?

**Claims.**
- `x-2094864872853119216#c1` (capability, stated) Scene was generated from one input image with Atlas filling unseen regions, rendered via spark.js and three.js. — evidence: "This scene was generated from one input image. Atlas fills the remaining gaps." [post]
- `x-2094864872853119216#c2` (recipe, stated) Pipeline names atlas (World Labs), spark.js splat renderer, and three.js as the web stack. — evidence: "→ atlas (world labs)  
→ spark.js  
→ three.js" [post]
- `x-2094864872853119216#c3` (result, demonstrated) World Labs publishes unauthenticated example exports: rustic-kitchen collider GLB 2,976,256 bytes, 500k SPZ 7,582,907 bytes, and a 3,860,086-byte 360 PNG. — evidence: "GET wlt-ai-cdn.art/example_exports/rustic_kitchen_with_natural_light/{collider.glb,500k.spz,pano.png} HTTP 200; glTF magic / gzip / PNG signatures." [note]
**Numbers.** video views at capture: 19490  (note); rustic-kitchen collider GLB: 2976256 bytes (note); rustic-kitchen 500k SPZ: 7582907 bytes (note)
**Recipe.** —
**Techniques.** [image-to-3d-worldgen](../../techniques/image-to-3d-worldgen.md), [splat-pipeline](../../techniques/splat-pipeline.md)
**Tools.** [atlas](../../tools/atlas.md), [spark-js](../../tools/spark-js.md), [three-js](../../tools/three-js.md)
**Links.** product (https://www.worldlabs.ai/blog/atlas), https://sparkjs.dev, https://www.worldlabs.ai/blog/spark-2.0, https://xrarchitect.xyz, https://x.com/XRarchitect/status/2094881923764199717
**Related items.** [x-2095437841958314100](../x-2095437841958314100/card.md)
**Media.**
`raw/items/x-2094864872853119216/media/atlas-spark-three-scene-thumb.jpg` (image, carries_technique=true) — Wide monitor showing a navigable Rococo ballroom 3D interior with FPS overlay, demo of Atlas spark.js three.js output.
`raw/items/x-2094864872853119216/media/atlas-spark-three-scene.mp4` (video, carries_technique=true) — Twenty-nine second camera move through the reconstructed ballroom interior generated from a single source photo.
`raw/items/x-2094864872853119216/media/input-image.jpg` (image, carries_technique=false) — Single source photograph of an ornate green and gold drawing room with piano, chandelier, and sunlight through arched windows.
**Thread.** captured_partial · reported 16 · captured 1 · relevant 0 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —

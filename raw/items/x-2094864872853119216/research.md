## What they are actually doing

Ian Curtis (design at World Labs) shows a navigable 3D scene built from **one still**, then viewed in a web 3D stack. The pipeline in the post is three named pieces:

1. **Atlas (World Labs)** — generate / reconstruct the world, including unseen regions.  
2. **spark.js** — Gaussian splat renderer on Three.js.  
3. **three.js** — the scene/runtime.

The attached clip is a camera move through a reconstructed interior/exterior; the follow-up still is the single source photo. A World Labs product teammate asks about VR; Curtis says he still needs to test that.

## Atlas

From [worldlabs.ai/blog/atlas](https://www.worldlabs.ai/blog/atlas) (2026-09-01): Atlas is an “omni” world model (multimodal autoregressive diffusion transformer) on text, images, video, camera poses, and depth. Tasks they list:

- Camera-controlled generation (native camera geometry, up to ~1 min at 1440p).
- Spatial reconstruction from 1–many images; novel views plus **point clouds / 3D Gaussian splats**.
- Space-time simulation (reframe video; Real-to-Sim).
- Image / 360 generation.

Directly matching the tweet: *“From a single input image, Atlas produces a full 3D world by jointly generating new views and estimating their geometry… Atlas fills in regions that no camera ever saw.”* Splats are the same representation as Marble. Early access for partners at capture time.

## spark.js

[sparkjs.dev](https://sparkjs.dev): “An advanced 3D Gaussian Splatting renderer for THREE.js,” built by World Labs. Mixes splats with other meshes; WebGL2; formats ply, sogs, spz, splat, ksplat. [Spark 2.0 post](https://www.worldlabs.ai/blog/spark-2.0) adds LoD streaming and a `.RAD` format. Spark is the web viewer; Atlas/Marble produce the splat.

## Author context

Portfolio [xrarchitect.xyz](https://xrarchitect.xyz): Niantic Spatial, Scaniverse Gaussian splat UX, WebAR (8th Wall), mixed-reality maps. The post is a World Labs design/engineering show of Atlas output in the Spark+Three stack, not a public app URL.

## Open questions

- Whether the clip is Spark in-browser, a native player, or an Atlas video export.
- VR path (Spark WebXR vs headset app) — flagged in-thread, not shown.
- Public Atlas access vs partner-only at capture.

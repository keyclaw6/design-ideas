# Gaussian splatting

Topic slug: `gaussian-splatting`. Adjacent: [bess-3d-flythrough](bess-3d-flythrough.md), [camera-control](camera-control.md), [three-js](three-js.md), [video-generation](video-generation.md).

This lane is 3D Gaussian splat (3DGS) capture, repair, and export — PLY in, mesh or a repaired splat out — so a site or product scan can enter DCC, print, or a web viewer. It is not the scroll landing (see [bess-3d-flythrough](bess-3d-flythrough.md)) and not the video model that polishes a camera path (see [video-generation](video-generation.md)).

The harvest is a short toolchain. ArtiFixer (NVIDIA, SIGGRAPH 2026) is diffusion post-process on sparse or blurry reconstructions. Splat2Mesh is a free Windows desktop converter (PLY → OBJ/GLB). Atlas + spark.js is a one-image world presented in three.js — reconstruction adjacent, tagged here because the output is a splat-like navigable scene.

Query here for “fix a thin splat,” “PLY to GLB,” or “one photo to an orbitable scan.” For the marketing flythrough that consumes the mesh, open [bess-3d-flythrough](bess-3d-flythrough.md). For in-browser presentation, open [three-js](three-js.md). Presence is not a recommendation.

## Pipelines

- **Repair sparse recon** — run ArtiFixer on broken/blurry 3DGS before any flythrough (`github-nv-tlabs-ArtiFixer`, `x-2094929928865341832`).
- **PLY → mesh** — desktop export to OBJ/GLB for Blender / Three.js / print (`web-arcana-splat2mesh`, `x-2094826117056414132`, `x-2094648474377839018`).
- **One image → world** — Atlas fills gaps; spark.js + three.js present the scene (`x-2094864872853119216`).
- **Existing phone stills (no recapture)** — per-asset overlap audit, then salvage 3DGS *or* skip-splat mesh + decimate (`note-bess-phone-photos-splat-mesh-plan`).

## Tools

- [ArtiFixer](../../raw/items/github-nv-tlabs-ArtiFixer/) — `github-nv-tlabs-ArtiFixer` — auto-regressive diffusion that enhances and extends 3D reconstructions.
- [Splat2Mesh](../../raw/items/web-arcana-splat2mesh/) — `web-arcana-splat2mesh` — Windows 11, 3DGS PLY in, OBJ/GLB out; personal/non-commercial license on the capture.

## Techniques

- [NVIDIA ArtiFixer thread](../../raw/items/x-2094929928865341832/) — `x-2094929928865341832` — video diffusion rebuilds missing/blurry regions on scans.
- [Splat2Mesh — free Win tool](../../raw/items/x-2094826117056414132/) — `x-2094826117056414132` — cleanup/export before web or DCC; JA launch `x-2094648474377839018`.
- [Atlas + spark.js + three.js](../../raw/items/x-2094864872853119216/) — `x-2094864872853119216` — World Labs Atlas reconstruction as a three.js scene (also `camera-control`, `video-generation`).
- [Salvage phone photos → splat → minimal mesh](../../raw/notes/bess-phone-photos-splat-mesh-plan.md) — `note-bess-phone-photos-splat-mesh-plan` — Drive `SPLAT images` (544 stills, 8 vision clusters) + COLMAP-gate / skip-splat / CAD-hybrid attack order.

## Examples

- [Splat2Mesh](../../raw/items/web-arcana-splat2mesh/) — `web-arcana-splat2mesh` — the harvested export step after a plant/product splat.
- [Atlas one-image scene](../../raw/items/x-2094864872853119216/) — `x-2094864872853119216` — reconstruction presented as an orbit clip, not a raw PLY.

## All items

<!-- AUTO:ITEMS -->
- [ArtiFixer](../../raw/items/github-nv-tlabs-ArtiFixer/) — `github-nv-tlabs-ArtiFixer`
- [Plan of attack: salvage phone photos → Gaussian splat → minimal mesh](../../raw/notes/bess-phone-photos-splat-mesh-plan.md) — `note-bess-phone-photos-splat-mesh-plan`
- [Splat2Mesh](../../raw/items/web-arcana-splat2mesh/) — `web-arcana-splat2mesh`
- [The core claim checks out. For years 3D Gaussian Splatting quality was solid, but huge files, missing streaming/LOD, and](../../raw/items/x-2090589293677023507/) — `x-2090589293677023507`
- [train gaussian splatting straight in the browser with Splat.js. SfM included, open source, and MIT Licensed. Video from ](../../raw/items/x-2090839282831270173/) — `x-2090839282831270173`
- [LichtFeld Studio is getting faster recently... 5m Gaussians, mrnf, 30k steps on RTX 4090](../../raw/items/x-2091899114153754949/) — `x-2091899114153754949`
- [SplatPaint is a real-time browser-based creative sandbox for Gaussian Splats: paint, sculpt, recolor, relight, deform, a](../../raw/items/x-2091943679317463153/) — `x-2091943679317463153`
- [3DGSをメッシュ変換するソフトを近日公開予定です。 ローカル環境で動作し、GPUなども不要です。 基本無料でどなたでもご利用いただけるように準備しています！ #3DGS #LichtFeldStudio #3DPrint](../../raw/items/x-2093179838249251011/) — `x-2093179838249251011`
- [OMG the new brush selection mode is awesome. As in "we should have added this years ago" type awesome.](../../raw/items/x-2093397098544648516/) — `x-2093397098544648516`
- [GaussianGPT: Towards Autoregressive 3D Gaussian Scene Generation ECCV 2026 https://github.com/nicolasvonluetzow/Gaussian](../../raw/items/x-2093563796237471912/) — `x-2093563796237471912`
- [Gaussian splats let you choose the camera move after you've left the location. We added animation tools and 4K video exp](../../raw/items/x-2094377838774472944/) — `x-2094377838774472944`
- [Splat2Mesh launch (JA) — 3DGS PLY → OBJ/GLB](../../raw/items/x-2094648474377839018/) — `x-2094648474377839018`
- [LightFuse: Relightable Interactive Gaussian Scene Reconstruction via Multi-Scan Fusion and 2D Gaussian Ray Tracing Contr](../../raw/items/x-2094769581965369822/) — `x-2094769581965369822`
- [Splat2Mesh — free Win tool, 3DGS PLY → OBJ/GLB](../../raw/items/x-2094826117056414132/) — `x-2094826117056414132`
- [Atlas + spark.js + three.js scene from one input image](../../raw/items/x-2094864872853119216/) — `x-2094864872853119216`
- [NVIDIA ArtiFixer — video diffusion that rebuilds broken/blurry 3D scans](../../raw/items/x-2094929928865341832/) — `x-2094929928865341832`
- [3DGSは見た目がリアルでも「面」を持たず、Blender編集や3Dプリントにそのまま使いにくい。 - 長野の@ArcanaMfg製作所がSplat2Meshを公開 - 対応PLYからポリゴンMeshを生成し、OBJ／GLBへ出力 - Wi](../../raw/items/x-2095136786095951924/) — `x-2095136786095951924`
- [3DGSのPLYデータをブラウザだけでメッシュ化！ GLB・STL・OBJへ変換可能なWebサービスがβ公開！ 3DGS Mesh Converter https://3dnchu.com/archives/3dgs-mesh-conver](../../raw/items/x-2095336950890983773/) — `x-2095336950890983773`
- [LichtFeldStudioで出力したデータをSplat2Meshで変換し、そのままMimakiの3DUJ-2207で出力しました。 https://arcana-mfg.com/splat2mesh/ English: https://](../../raw/items/x-2095375790875840593/) — `x-2095375790875840593`
<!-- /AUTO:ITEMS -->

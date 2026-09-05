# Splat Pipeline

**Slug:** `splat-pipeline` · **Owner subject:** [gaussian-splatting](../subjects/gaussian-splatting/brief.md)
**Subjects:** [gaussian-splatting](../subjects/gaussian-splatting/brief.md), [image-to-3d-world](../subjects/image-to-3d-world/brief.md)
**Referenced by (5):**
- [Arcana Splat2Mesh: local CPU 3DGS-to-mesh converter launching free](../items/x-2093179838249251011/card.md) — tool, claim-source — gaussian-splatting
- [SuperSplat brush selection mode praised by PlayCanvas author](../items/x-2093397098544648516/card.md) — example — gaussian-splatting
- [LightFuse: relightable multi-scan Gaussian reconstruction with 2DGS ray tracing](../items/x-2094769581965369822/card.md) — reference, claim-source — gaussian-splatting
- [World Labs Atlas plus spark.js Three.js scene from one photo](../items/x-2094864872853119216/card.md) — example, technique — image-to-3d-world
- [NVIDIA ArtiFixer tweet: video diffusion repairs sparse 3D scans](../items/x-2094929928865341832/card.md) — reference, claim-source — gaussian-splatting

<!-- NOTES:START -->
Train, edit, view, repair, and mesh-export a 3D Gaussian splat as one path.
Owner subject: `gaussian-splatting`. Referenced by 5 item(s): x-2093179838249251011, x-2093397098544648516, x-2094769581965369822, x-2094864872853119216, x-2094929928865341832.
Score items that use this method on the owner brief's comparison axes. Do not treat the slug as a product name.
If a later pass splits this slug, file a registry alias — do not edit cards by hand.

IZUTSUYA 3DGS Mesh Converter (card `x-2095336950890983773`): live https://4dgs.jp/ja/3dgs-mesh-converter/ re-fetched 2026-09-05 **200 / 76,302 B**. Browser beta; email required; **.ply ≤ 500 MB**. Two modes: **計算変換** (geometry, “faithful,” 1–5 min, free **5/month**) with optional “keep thin points” / “fill holes (bad for rails/grids)”; **高精細AI変換** (looks, 2–4 min, **paid plan required**, AI infill). Downloads: GLB (color/texture), STL (print), OBJ (**calc mode only**). AI download disclaimer: not an accurate reproduction; license copy bars **EU / UK / Korea**. One free AI trial per account. `/en/3dgs-mesh-converter/` **404**. 3dnchu article `https://3dnchu.com/archives/3dgs-mesh-converter/` **200 / 312,202 B** (posted 2026-08-24, updated 2026-09-03). Distinct from Arcana Splat2Mesh (local Windows). STL manifold/print check **not run**. Press (FabScene) names yen tiers; not on this converter HTML. Card is now `ready` (thread `empty`).

LightFuse (card `x-2094769581965369822`, thread still `failed`): paper is Zhou et al. 2026, arXiv:2608.29269. Real project page is **https://zhn202.github.io/LightFuse/** (`lightfuse.github.io` 404). 2D Gaussian multi-scan fusion + ray-tracing-oriented geometry refine + staged inverse rendering (shared metallic–roughness, per-state env map, differentiable one-bounce path tracing). **First-party abs 42,527 B + html 192,093 B** quote +9.74 dB PSNR / +0.121 SSIM vs strongest baseline on synthetic novel-state relighting (now on the card `#c4`). Project page **200 / 22,365 B** says **Code Soon**; GitHub hrefs are IG-Fuse / nerfies templates, not weights. Authors ZJU-UIUC / Sichuan / ZJU / Chengdu Minto. Do not confuse with the 2021 CNN HDR “LightFuse.” Root amplify video is **33 s** / 1280×720 (`analysis/_work/captures/lightfuse-video-2094769581965369822.json`). One reply still unfetched. Receipt `lightfuse-arxiv-2608.29269-2026-09-05.json`.

**2026-09-05 capture — Spatial Studio host.** Quoted `t.co/7OebUDN1n4` → `https://studio.realhorizons.ai/` **200 / 8,035 B** SPA, title *Spatial Studio | Real Horizons*. Park tour `t.co/Iow579owe9` → `/tours/8b1bf25c-f2ee-4a78-8940-2516351d78b1/view` (same shell). `https://spatial.studio` is a West Footscray architecture firm (**91,131 B**) — different product. 4K export still tweet-only. Card [x-2094377838774472944](../items/x-2094377838774472944/card.md) gap is now `thread-partial`.
<!-- NOTES:END -->

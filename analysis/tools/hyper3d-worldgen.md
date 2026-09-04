# Hyper3d Worldgen

**Slug:** `hyper3d-worldgen` · **Kind:** product · **URL:** https://x.com/grokkedd/status/2095437841958314100 · **Canonical item:** [x-2095437841958314100](../items/x-2095437841958314100/card.md)
**Subjects:** [ai-video-generation](../subjects/ai-video-generation/brief.md), [image-to-3d-world](../subjects/image-to-3d-world/brief.md)
**Referenced by (1):**
- [Hyper3D WorldGen builds editable physics worlds from one photo](../items/x-2095437841958314100/card.md) — tool, claim-source — image-to-3d-world

<!-- NOTES:START -->
Fetched 2026-09-04.

- Marketing home https://hyper3d.ai is **Rodin** (image/text → 3D asset), not a WorldGen explainer. Re-fetch 2026-09-04: `https://hyper3d.ai/worldgen` still **404**. `https://www.hyper3d.ai/workspace/worldgen` HTTP **200**, **11,026**-byte login SPA. CAST arXiv:2502.12894 still 200. No public export.
- Press (Yingmu / 影眸, 2026-09-01): one photo → per-object meshes (Rodin) + background as 3DGS; CAST reconstructs pose/scale/contact. CAST paper: Yao et al., arXiv:2502.12894, “CAST: Component-Aligned 3D Scene Reconstruction from an RGB Image” (ShanghaiTech + Deemos). Pipeline in the abstract: open-vocab 2D seg + relative depth → GPT inter-object relations → occlusion-aware ObjectGen (MAE + partial point cloud) → AlignGen similarity transform → physics-aware SDF correction (penetration / float / contact). SIGGRAPH 2025 Best Paper (ACM awards post). Official workflow URL cited by 量子位: https://hyper3d.ai
- CAST paper tables (quote the paper, not the trailer): open-vocab Table 1 CAST CLIP 85.77 / GPT-4 rank 1.125 / user VQ 88.07% / PP 71.42% vs ACDC and Gen3DSR. 3D-Front Table 2: CD-S 0.052, FS-S 56.18, CD-O 0.057, FS-O 56.50, IoU-B 0.603. AlignGen: 150M params, ~1 s/object at inference; trained ~2 days on 64 A800. Project page for CAST itself 404s from this host; no public engine file on WorldGen.
- Still no public WorldGen export, EULA, or weights in this bank. Do not schedule production on the trailer.

Lumera project page https://haidilao0328.github.io/Lumera/ is a 1 KB HTML shell that loads `/Lumera/assets/project2NoDemo-B9J-SJip.js` (605,695 bytes). Bundle cites **arXiv:2607.20889** “Engine-Native Editable 3D World Reconstruction with Objects and Lighting” and a YouTube embed `x7s8649kAO4`. Abstract (fetched): Lumera-2K from **2,513 UE5 projects**; 3.73M components, 63M object instances, 102.6K parametric lights, 95.1K camera views; Lumera-Box / Lumera-Light parse boxes and light tuples. **No GitHub / weights URL in the bundle.** Lucida https://lucida-r2s.github.io/ is a real paper page: parse → generate → place with GizmoAct; indoor video; quantitative tables on R2S / CA-1M / ADT. Weights/code still not linked there.
<!-- NOTES:END -->

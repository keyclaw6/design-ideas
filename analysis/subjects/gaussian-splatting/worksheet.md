# Judgment worksheet: Gaussian splatting (gaussian-splatting)

Decision: a capture → edit → mesh/export path. The 17 primaries collapse to one technique slug (`splat-pipeline`) because workers named the same path 17 ways.

## gaussian-splatting — short stack to try

1. **Train / view.** LichtFeld Studio on a real GPU ([x-2091899114153754949](../../items/x-2091899114153754949/card.md) — 5M Gaussians / 30k steps / 4090, stated). Splat.js in the browser ([x-2090839282831270173](../../items/x-2090839282831270173/card.md)) when you want MIT + SfM in-tab, not a workstation bake.
2. **Edit.** SuperSplat brush select ([x-2093397098544648516](../../items/x-2093397098544648516/card.md)). SplatPaint for paint/sculpt/relight in-browser ([x-2091943679317463153](../../items/x-2091943679317463153/card.md)). Spatial Studio if the next step is a 4K camera export rather than a mesh ([x-2094377838774472944](../../items/x-2094377838774472944/card.md)).
3. **Splat → mesh.** Arcana Splat2Mesh Windows app ([web-arcana-splat2mesh](../../items/web-arcana-splat2mesh/card.md) and the JP launch posts). IZUTSUYA browser converter at 4dgs.jp ([x-2095336950890983773](../../items/x-2095336950890983773/card.md)) when install is the blocker. The LichtFeld → Splat2Mesh → Mimaki print ([x-2095375790875840593](../../items/x-2095375790875840593/card.md)) is the only end-to-end *print* example.
4. **Repair sparse captures.** NVIDIA ArtiFixer ([github-nv-tlabs-ArtiFixer](../../items/github-nv-tlabs-ArtiFixer/card.md), tweet [x-2094929928865341832](../../items/x-2094929928865341832/card.md)). 14B and 1.3B checkpoints are named. This is research-weight, not a one-click phone-splat fixer.

LOD / streaming / Aholo ([x-2090589293677023507](../../items/x-2090589293677023507/card.md)), GaussianGPT, and LightFuse stay in the “read if the path dies at scale or relight” bin.

## gaussian-splatting — axis scores

| item | input | edit | export | local vs hosted | repair needed |
|---|---|---|---|---|---|
| LichtFeld Studio | video / images (implied) | train-centric | splat; feeds Splat2Mesh in the print demo | local GPU (4090 cited) | if capture is sparse → ArtiFixer |
| Splat.js | images in-browser + SfM | train in-tab | web splat | local browser | unknown on phone video |
| SuperSplat | existing splat | brush select (tweet; not on README/homepage) | editor (OSS MIT **9,947★**; live superspl.at/editor) | local / web | n/a |
| SplatPaint | splat *or* image/logo/model | paint, sculpt, relight, FX | browser scene | hosted sandbox | n/a |
| Spatial Studio | splat capture | camera path | 4K video | in-browser | n/a (leaves splat-land) |
| Splat2Mesh (Arcana) | 3DGS PLY | none | OBJ/GLB; print via Mimaki demo | local CPU, no GPU claimed | mesh quality unknown |
| IZUTSUYA 4dgs.jp | PLY ≤500 MB | none | GLB / STL / OBJ (OBJ = calc only) | browser, server-side, no local GPU | hole-fill mode exists; manifold unknown |
| ArtiFixer | sparse 3DGRUT / broken scan | diffusion fill | repaired splat/scan | local, heavy weights | this *is* the repair step |
| Aholo / LOD / SPZ | city-scale splat | view | browser stream | viewer | n/a |
| LightFuse | multi-scan RGB + masks/depth/normals | rearrange + relight + edit material | research recon (2DGS + one-bounce RT) | research; no public weights | n/a |
| GaussianGPT | tokens (gen, not capture) | none | generated splat scene | research MIT **403★**; ECCV’26 Oral; weights not on API listing | n/a |

## gaussian-splatting — claims that need a receipt

- Splat2Mesh “free personal / non-commercial” — **EULA v1.0 (2026-08-21) now fetched**; company R&D/prototyping/print-for-pay is commercial even with no revenue. See [splat2mesh](../../tools/splat2mesh.md).
- Splat2Mesh “no GPU” — **not on the English product page** (re-fetched **200 / 73,796 B**). It appears in the JP launch `og:description` (`x-2095136786095951924`). Same og text says the mesh is **not** automatically watertight for print. ymt3d + Arcana launch cards are now `ready` (threads `empty`); 3dnchu write-up **299,442 B**.
- Timed conversion of the public `sample.ply` (1.5 MB, HTTP 200) — not run (Windows installer; this host is Linux).
- LichtFeld 5M / 30k / 4090 — one benchmark tweet; no wall-clock, no VRAM, no quality still.
- Aholo “billion splats in the browser” — secondary citation in a roundup, not a first-party capture.
- ArtiFixer checkpoint sizes (~16.9B / ~1.68B) — from the card’s HF note; confirm filenames before planning VRAM.
- Print path LichtFeld → Splat2Mesh → Mimaki 3DUJ-2207 — empty thread, demo only. Need whether the mesh is watertight.

Two threads in this subject are still `failed` (no reply DOM): LightFuse ([x-2094769581965369822](../../items/x-2094769581965369822/thread.md)) and Splat2Mesh JP ([x-2095136786095951924](../../items/x-2095136786095951924/thread.md)). Replies still empty. **Paper + project page now fetched** (arXiv:2608.29269, https://zhn202.github.io/LightFuse/): +9.74 dB PSNR / +0.121 SSIM vs strongest baseline; no code repo found. See [splat-pipeline](../../techniques/splat-pipeline.md). Do not read empty replies as “no discussion.”

## gaussian-splatting — do not treat as load-bearing

- Four Japanese launch posts that only restated Splat2Mesh v1.0. One product page is enough ([web-arcana-splat2mesh](../../items/web-arcana-splat2mesh/card.md)).
- GaussianGPT / LightFuse until there is a runnable repo in this bank. GaussianGPT GitHub is live (MIT **403★**, ECCV’26 Oral) but weights/checkpoints were not on the API listing (parked on [splat-js](../../tools/splat-js.md)).
- Spatial Studio 4K export if the owner’s question is *mesh*, not *video*. Product host is **studio.realhorizons.ai** (8,035 B SPA), not spatial.studio (architecture firm).

## gaussian-splatting — next capture work

1. EULA + sample.ply URL are on the tool page. Remaining: run the Windows app on `sample.ply` and record wall-clock + whether the OBJ is watertight.
2. LightFuse abs + html are now first-party on the card `#c4` ([splat-pipeline](../../techniques/splat-pipeline.md)): **+9.74 dB / +0.121 SSIM**. Project page **22,365 B** says **Code Soon**. Remaining: X replies, and a code/weights drop if one appears. Splat2Mesh JP replies still 0 tweet nodes; JP launch clip is **16.24 s** / 1148×652. leftover24 unused English `arcana-mfg.com/en/splat2mesh/` **73,796 B** restates PLY→OBJ/GLB / Windows 11 / personal-free; still no watertight claim ([arcana-splat2mesh](../../tools/arcana-splat2mesh.md); [x-2095136786095951924#c5](../../items/x-2095136786095951924/card.md)).
3. IZUTSUYA converter page re-fetched **200 / 76,302 B** and folded onto [x-2095336950890983773](../../items/x-2095336950890983773/card.md) (`ready`, thread `empty`). Extra first-party copy: one free AI trial / account; AI download disclaimer; EU/UK/Korea license bar; `/en/` 404. 3dnchu article **312,202 B**. Remaining: convert `sample.ply` and check whether the STL is manifold.
4. Decide ArtiFixer: phone capture vs research scan. Nothing in this bank tests a handheld video.
5. Splat.js is `arrival-space/splat.js` MIT **116★** — in-browser WebGPU trainer + JS SfM; live `arrival.space/splat-js` ([x-2090839282831270173#c2](../../items/x-2090839282831270173/card.md); [splat-js](../../tools/splat-js.md)). Do not collapse with GaussianSplats3D or the 2D SplatJS engine.
6. LichtFeld Studio repo is GPL-3.0 **3,656★** ([x-2091899114153754949#c2](../../items/x-2091899114153754949/card.md)). Tweet 5M / 30k / 4090 stays tweet-only. lichtfeld.io **403** — do not hammer.
7. SuperSplat is first-party on [supersplat](../../tools/supersplat.md): MIT **9,947★**; live `superspl.at` **177,574 B** (Explore / Editor / Convert). Brush selection stays tweet-only ([x-2093397098544648516#c3](../../items/x-2093397098544648516/card.md)).
8. leftover27 unused ArtiFixer abs **44,589 B** claims **1–3 dB** PSNR (SIGGRAPH 2026; v2 5 May 2026; PDF **91,742 KB**); NVIDIA page **18,793 B** names ArtiFixer / ArtiFixer3D / ArtiFixer3D+; HF **65** likes ([artifixer](../../tools/artifixer.md); [github-nv-tlabs-ArtiFixer#c3](../../items/github-nv-tlabs-ArtiFixer/card.md)). Remaining: download the PDF or a handheld-video test — not another abs fetch.
9. leftover28 unused `alpha.splatpaint.app` **5,686 B** is an invite / Patreon Founding Alpha shell ([splat-js](../../tools/splat-js.md); [x-2091943679317463153#c3](../../items/x-2091943679317463153/card.md)). Did not paint a splat.
10. leftover30 unused GitHub org `ArcanaMfg` **1,237 B**: Organization, **2** public repos, Nagano Japan ([splat2mesh](../../tools/splat2mesh.md); [x-2094648474377839018#c3](../../items/x-2094648474377839018/card.md)). leftover30 unused EN splat2mesh + ZIP leftovers stay leftover24 — do not download the ZIP. leftover30 unused ArtiFixer leftover27 leftovers now on the READY tweet card ([artifixer](../../tools/artifixer.md)).

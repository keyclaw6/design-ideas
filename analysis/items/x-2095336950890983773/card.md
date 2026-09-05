# Browser beta: IZUTSUYA 3DGS Mesh Converter PLY to GLB/STL/OBJ

`x-2095336950890983773` · x · product · ja · [source](https://x.com/ymt3d/status/2095336950890983773) · [raw](../../../raw/items/x-2095336950890983773/)
**Author:** 3D人-3dnchu- CG情報ブログ (@ymt3d) (@@ymt3d) · **Published:** — · **Captured:** 2026-09-04T06:50:10Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [gaussian-splatting](../../subjects/gaussian-splatting/brief.md) · **Also:** — · **Roles:** tool, reference · **Platforms:** browser, other

**Summary.** 3dnchu shares IZUTSUYA's browser-only 3DGS Mesh Converter beta at 4dgs.jp, converting PLY splats to GLB, STL, or OBJ without install or GPU, with a free tier. Distinct from Arcana Splat2Mesh desktop tool.
**Question it answers.** Is there a browser-only 3DGS PLY to mesh converter with a free plan?

**Claims.**
- `x-2095336950890983773#c1` (availability, stated) Web beta converts 3DGS PLY to GLB/STL/OBJ entirely in the browser with a free tier. — evidence: "GLB・STL・OBJへ変換可能なWebサービスがβ公開！" [post]
- `x-2095336950890983773#c2` (capability, demonstrated) Live converter https://4dgs.jp/ja/3dgs-mesh-converter/ is 200 / 76,302 B. Upload is .ply ≤ 500 MB. Email required. Calc conversion (計算変換) is free 5/month, 1–5 min, “faithful.” High-detail AI conversion (高精細AI変換) needs a paid plan, 2–4 min, AI infill. Downloads: GLB (color/texture), STL (print), OBJ (calc mode only). — evidence: "GET https://4dgs.jp/ja/3dgs-mesh-converter/ 200 76302 B. Visible copy: .ply・500MBまで / 無料・計算変換は毎月5回まで / 所要時間 1〜5分 / プラン契約 必須 / 2〜4分 / GLB（色・テクスチャ付き） STL（3Dプリント用） OBJ（計算変換のみ）." [note]
- `x-2095336950890983773#c3` (availability, demonstrated) Calc options: keep thin points (rails/leaves/ground) and hole-fill (ground/slopes/interiors/statues; bad for rails/grids). AI download disclaimer: not an accurate reproduction; license copy bars EU, UK, and Korea. One free AI trial per account. STL manifold/print check not run. EN path /en/3dgs-mesh-converter/ 404s. — evidence: "Same converter HTML: 細部を残す / 穴埋め優先 / 元データの正確な再現ではありません / EU・英国・韓国では利用できません / 高精細AI変換は1アカウントにつき1回." [note]
- `x-2095336950890983773#c4` (availability, demonstrated) 3dnchu article https://3dnchu.com/archives/3dgs-mesh-converter/ is 200 / 312,202 B (posted 2026-08-24, updated 2026-09-03). Title restates browser-only PLY→GLB/STL/OBJ beta. Thread status is empty (0 replies). — evidence: "GET https://3dnchu.com/archives/3dgs-mesh-converter/ 200 312202 B. Title: 3DGS Mesh Converter | 3DGSのPLYデータをブラウザだけでメッシュ化！" [note]
**Numbers.** PLY upload cap: 500 MB (linked-page); Free calc conversions per month: 5 jobs (linked-page); Converter page bytes: 76302 bytes (note)
**Recipe.** —
**Techniques.** [splat-pipeline](../../techniques/splat-pipeline.md)
**Tools.** —
**Links.** product (https://4dgs.jp/ja/3dgs-mesh-converter), https://3dnchu.com/archives/3dgs-mesh-converter/
**Related items.** [web-arcana-splat2mesh](../web-arcana-splat2mesh/card.md)
**Media.**
`raw/items/x-2095336950890983773/media/media_0.jpg` (image, carries_technique=false) — 4dgs.jp landing for 3DGS Mesh Converter beta showing PLY input to GLB/STL/OBJ output with no-install workflow.
**Thread.** empty · reported 0 · captured 0 · relevant 0 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: [web-arcana-splat2mesh](../web-arcana-splat2mesh/card.md), [x-2094648474377839018](../x-2094648474377839018/card.md)

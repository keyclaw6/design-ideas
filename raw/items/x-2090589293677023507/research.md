## What it is

Technical summary: 3D Gaussian Splatting quality was always decent, but huge files, no streaming/LOD, and weak deployment blocked large scenes; those gaps are closing.

## How it works

- Named advances: LOD systems, progressive streaming, SPZ compression, collision meshes, true browser rendering.
- ManycoreTech open-source Aholo Viewer cited as city-scale, >1B splats in-browser.
- Thesis: 3DGS moved from research demo to usable infrastructure.
- Directly relevant to site-scale BESS captures that cannot ship a 10GB PLY.
- Pairs with Splat2Mesh / ArtiFixer / Splat.js items for repair, mesh export, and in-browser training.

## Why saved

KB's flythrough path may be splat-first if streaming/LOD is real; this is the infrastructure bookmark.

## Topics

`gaussian-splatting`, `bess-3d-flythrough`, `three-js`

## Related

`web-arcana-splat2mesh`, `github-nv-tlabs-ArtiFixer`, `x-2094826117056414132`, `x-2090839282831270173`

## Use when

Planning a large-scene splat deployment (streaming, LOD, compression, collision), or evaluating Aholo-class viewers vs custom Three.js.

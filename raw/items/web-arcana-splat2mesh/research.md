# Research

## What it is

Arcana Mfg. Splat2Mesh: Windows desktop tool converting 3D Gaussian Splatting (PLY) into polygon meshes (OBJ/GLB) for 3D printing, Blender/DCC, and standard 3D apps. Free personal/non-commercial; commercial via contact.

## How it works

- Import 3DGS PLY → set mesh parameters → export OBJ or GLB (~110 MB installer, not stored in this bank).
- Splats stay view-dependent Gaussians; meshes get vertices/faces that print and edit. Visual quality drops vs splat, editability rises.
- Use cases on site: print scanned objects, building/outdoor conversion, game/sim assets.
- YouTube overview/example linked; EULA on arcana-mfg.com.
- Sits after capture/repair (ArtiFixer) and before web/Three.js or CAD.

## Why saved

BESS/site 3DGS needs a mesh path for clients who cannot view splats. This is the practical export tool next to NVIDIA’s research repair model.

## Topics

`gaussian-splatting`, `bess-3d-flythrough`

## Related

`github-nv-tlabs-ArtiFixer`, `github-oso95-scroll-world`, `github-scottstts-threejs-awesome-graphics-agent-skills`, `web-utsubo`, `web-fal-ai`

## Use when

Exporting a splat capture to Blender/print/GLB; handing a plant scan to a DCC artist; comparing mesh vs keeping 3DGS for web.

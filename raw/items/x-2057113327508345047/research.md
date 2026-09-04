# Research

## What it is
In-progress one-click AI texturing for 3D models: render four orthographic views, generate textures, project them back onto the mesh. Open-source as kokraf (`github.com/sengchor/kokraf`).

## How it works
- Capture the mesh from four sides (front/back/left/right).
- Run an image model on those renders to invent albedo (and likely related maps).
- Project generated images back onto UV/mesh space so the asset stays a real 3D object, not a video.
- Built in public on Three.js (`#threejs #kokraf`).
- Media on disk is an MP4 demo of the projection loop.

## Why saved
BESS marketing and product landings need textured CAD/scan meshes without a full lookdev artist. Four-view bake is a cheap path from blockout → web-ready asset.

## Topics
- `three-js`
- `design`

## Related
- `github-scottstts-threejs-awesome-graphics-agent-skills` — graphics agent skills for web 3D
- `github-mengto-skills` — Three.js / motion skill pack
- `web-oryzo-ai` — AI 3D/site look
- `x-2086599657925329347` — Claude building interactive 3D websites

## Use when
Texturing a site flythrough mesh, product hero, or Three.js scene from a gray model. Pair with splat→mesh cleanup if the source is a scan.

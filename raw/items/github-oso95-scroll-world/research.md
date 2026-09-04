# Research

## What it is

oso95/scroll-world (~8.9k stars, MIT): agent skill that builds Apple-style scroll-scrubbed landings — continuous camera flight through AI-generated isometric diorama scenes with no cuts.

## How it works

- Interview: subject, brand kit, art direction, scene order, optional mobile 9:16, budget.
- Generate: scene stills (GPT Image 2), dive-in clips, connector clips frame-locked at seams.
- Wire: portable vanilla-JS scrub engine (blob-seek, lazy load, seam crossfade) into HTML/Next/Vue/Python pages.
- Video backend: Monid CLI (Seedance 2.0 default) or Higgsfield CLI; ffmpeg/ffprobe; Python+Pillow; optional Codex CLI for image_gen.
- Install: `npx skills add oso95/scroll-world` or Claude Code marketplace plugin.

## Why saved

Primary recipe for BESS/industrial 3D marketing flythroughs that are *web-scroll* rather than YouTube. Complements scroll-craft (HTML craft) and ArtiFixer (real captured splats).

## Topics

`bess-3d-flythrough`, `camera-control`, `video-generation`, `agent-skills`, `ui-motion`

## Related

`github-nateherkai-scroll-craft`, `web-fal-ai`, `github-nv-tlabs-ArtiFixer`, `web-utsubo`, `web-getlayers-ai`

## Use when

A landing needs a continuous isometric/world flythrough scrubbed to scroll; generating seam-locked clip sequences; choosing Seedance vs Higgsfield for marketing 3D.

# Research

## What it is
Pipeline for full camera control in Seedance: Claude Opus 5 blockouts a cafe in Blender, animates the real camera in the .blend, then that move becomes the Seedance motion reference.

## How it works
- Agent builds a crude 3D mockup (furniture as blocks, simple character shapes) — not a hero render.
- Camera path is keyed inside Blender so composition and timing are explicit, not prompt-guessed.
- That 3D camera move is fed to Seedance 2.0 / 2.5 as the reference; claimed results: starting-frame match, continuous push through a window, controlled timing.
- Same pattern as the library’s Blender → MiniMax H3 / Veo / Kling note: blockout + camera path first, video model second.
- Directly reusable for BESS site flythroughs: industrial geometry blockout, camera along a defined path, photoreal video model for look.

## Why saved
This is the exact BESS 3D flythrough recipe KB already researched, shown here with Seedance instead of MiniMax/Veo. Bookmark of a working Opus-5 + Blender + Seedance instance.

## Topics
`camera-control`, `video-generation`, `bess-3d-flythrough`

## Related
- `note-blender-minimax-h3-video-generation` — full Blender→video-model pipeline writeup
- `github-oso95-scroll-world` — scroll-driven 3D hero landings
- `x-2065843739340509693` — Codex + Blender
- `web-fal-ai` — generative media API for the video step
- `github-nv-tlabs-ArtiFixer` — splat/video repair when reconstruction is sparse

## Use when
Building a BESS or industrial flythrough and you need a locked camera path (not text-to-camera). Start in Blender, then Seedance/MiniMax/Veo.

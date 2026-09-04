# Research

## What it is

nexu-io/html-video (~4.5k stars, Apache-2.0): programmatic video for coding agents — HTML/CSS/data on the laptop becomes a real MP4. Meta-layer over render engines; default is Hyperframes (headless Chromium + ffmpeg). Product page: open-design.ai/html-video.

## How it works

- Pipeline: prompt/link/repo → fetch → agent loop → content-graph storyboard → per-frame HTML → Hyperframes → ffmpeg → MP4.
- Claims 14 coding agents (Open Design, Claude Code, Cursor, Codex, …) and 21 templates (data viz, kinetic type, cinematic frames).
- Can ingest WeChat articles and GitHub READMEs server-side into a video storyboard.
- Optional AI soundtrack (MiniMax music + narration). No per-render cloud fee; local studio via `node packages/cli/dist/bin.js studio` on 127.0.0.1:3071.
- Sibling of OpenDesign and motion-anything in the same org.

## Why saved

Deterministic HTML-to-video is an alternative to Seedance/Veo for explainers, changelog films, and infographic motion — useful when the source of truth is already a page or repo.

## Topics

`video-generation`, `agent-skills`

## Related

`github-nexu-io-open-design`, `github-nexu-io-motion-anything`, `web-open-design-ai`, `web-fal-ai`, `web-animos-editor`

## Use when

Turning a README, article, or DESIGN.md landing into an MP4 without a video model; needing kinetic-type/data-viz templates agents can fill; comparing Hyperframes vs fal video APIs.

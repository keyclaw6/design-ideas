# html-video

**Repo:** nexu-io/html-video  
**Stars:** 4,505 · **License:** Apache-2.0 · **Homepage:** open-design.ai/html-video

Programmatic video for coding agents — HTML/CSS/data → real MP4 on your laptop. Meta-layer over render engines; default engine is Hyperframes (headless Chromium + ffmpeg).

## Pipeline

```
prompt / link / repo → source fetch → agent loop → content-graph storyboard
→ per-frame HTML → Hyperframes render → ffmpeg → MP4
```

## At a glance

- **14 coding agents** supported (Open Design, Claude Code, Cursor, Codex, etc.)
- **21 templates** (data viz, kinetic type, cinematic frames)
- Article/repo → video: fetches WeChat articles, GitHub READMEs server-side
- Optional AI soundtrack (MiniMax music + narration)
- Apache-2.0, no per-render fees

## Quick start

```bash
pnpm install && pnpm -r build
node packages/cli/dist/bin.js studio  # http://127.0.0.1:3071
```

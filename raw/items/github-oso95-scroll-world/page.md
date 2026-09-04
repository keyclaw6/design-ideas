# scroll-world

**Repo:** oso95/scroll-world  
**Stars:** 8,906 · **License:** MIT

Agent skill that builds scroll-scrubbed "fly through the world" landing pages — continuous camera flight through AI-generated isometric diorama scenes with no cuts (Apple-style scroll-through product pages).

## Pipeline

1. **Interview** — subject, brand kit, art direction, scene order, mobile 9:16 option, budget approval
2. **Generate assets** — scene stills (GPT Image 2), dive-in clips, connector clips frame-locked at seams
3. **Wire up** — portable vanilla-JS scrub engine (blob-seek, lazy load, seam crossfade)

## Requirements

- Monid CLI (default video backend, Seedance 2.0) or Higgsfield CLI fallback
- ffmpeg/ffprobe, Python 3 + Pillow
- Optional Codex CLI for image_gen via ChatGPT subscription

## Install

```bash
npx skills add oso95/scroll-world
/plugin marketplace add oso95/scroll-world  # Claude Code
```

Framework-agnostic: drops into HTML, Next.js, Vue, or Python-served pages.

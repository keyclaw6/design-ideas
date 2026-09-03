# X Capture 5 — Ingest Manifest

Captured: 2026-09-02T17:38:09Z  
Scope: two bookmark IDs only. **Did not unsave.** HTTP APIs only (no OS computer-use / agent-browser).

| # | ID | URL | Status | Notes |
|---|-----|-----|--------|-------|
| 1 | x-2095081419202560010 | https://x.com/gojiberryai/status/2095081419202560010 | complete | Note-tweet + **37.8s video** (3.6 MB, 1080×1080). Repo `romangojiberryAI/gojiberryai-sales-os` (not in thread; BOT comments login-walled). Topics: `mcp`, `agent-skills`, `seo-agents`. |
| 2 | x-2094929928865341832 | https://x.com/0x0SojalSec/status/2094929928865341832 | complete | Note-tweet + **16.3s video** (15 MB, 1654×1080; native 3308×2160). Model **ArtiFixer** — HF `nvidia/ArtiFixer`, code `nv-tlabs/ArtiFixer`, arXiv:2603.00492. 0/2 replies. Topics: `video-generation`, `camera-control`, `gaussian-splatting`, `bess-3d-flythrough`. |

## Files per item

- source.json (`source_type: x`, `unsaved: false`)
- post.md
- comments.md
- research.md
- media/ (`video.mp4`, `thumb.jpg`)

## Fetch path

- `https://api.fxtwitter.com/{user}/status/{id}` (primary)
- `https://api.vxtwitter.com/status/{id}` (media URLs)
- `https://r.jina.ai/http://x.com/...` (visible replies + product pages)
- GitHub API + raw README/SKILL; Hugging Face API; arXiv Atom; NVIDIA SIL project page
- Video: direct `video.twimg.com` MP4

## Gaps

- Post 1: 0/87 replies (BOT lead-magnet behind login); SaaS dollar prices not in Framer HTML
- Post 2: 0/2 replies; Threadreader empty
- Catalog not touched (lane: `raw/items/` + this manifest)

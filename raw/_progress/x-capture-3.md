# X Capture 3 — Ingest Manifest

Captured: 2026-09-02T17:31:40Z  
Scope: two bookmark IDs only. **Did not unsave.** HTTP APIs only (no OS computer-use / agent-browser).

| # | ID | URL | Status | Notes |
|---|-----|-----|--------|-------|
| 1 | x-2095123902947090682 | https://x.com/kyleanthony/status/2095123902947090682 | complete | Swiss-grid / Neo Industrialism still (3456×2234). Author CTA → brasshands.com/contact. 3/18 replies via jina+fx. Topic: `design`. |
| 2 | x-2094984529853530345 | https://x.com/himanshubuildss/status/2094984529853530345 | complete | Note-tweet + **748s video** (60.4 MB, 1280×720 via yt-dlp). Full 3-tweet thread + 1 comment. Funnel to scrolltide.co/ebook. Topics: `ui-motion`, `design`, `agent-skills`. |

## Files per item

- source.json (`source_type: x`, `unsaved: false`)
- post.md
- comments.md
- research.md
- media/

## Fetch path

- `https://api.fxtwitter.com/{user}/status/{id}` (primary)
- `https://api.vxtwitter.com/status/{id}` (media URLs)
- `https://r.jina.ai/http://x.com/...` (visible replies + thread)
- Product pages via jina: brasshands.com, brasshands.com/contact, scrolltide.co, /ebook, /pricing
- Video: yt-dlp guest GraphQL, format `http-2176` (720p)

## Gaps

- Post 1: 16/18 replies behind login
- Post 2: remaining replies behind login; Threadreader empty; demo live URL not in thread
- Catalog not touched (lane: `raw/items/` + this manifest)

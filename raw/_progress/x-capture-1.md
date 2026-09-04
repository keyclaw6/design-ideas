# X capture 1 — ingest manifest

Captured: 2026-09-02T17:23:28Z  
Lane: `raw/items/` only (catalog/ not touched). Bookmarks **not** unsaved.

| # | ID | URL | Status | Notes |
|---|-----|-----|--------|-------|
| 1 | x-2094927852399624557 | https://x.com/levikmunneke/status/2094927852399624557 | complete | Instantly + MapsData; 3 replies + author reply via jina/fxtwitter; no media; topics `[]` (no SCHEMA match) |
| 2 | x-2094864872853119216 | https://x.com/XRarchitect/status/2094864872853119216 | complete | Atlas/spark/three; **video downloaded** (26.8 MB, 1766×994, 29.7s) + thumb + author input still; author VR reply captured |
| 3 | x-2095060844547592437 | https://x.com/paolo_scales/status/2095060844547592437 | complete | LinkedIn lead magnets; banner JPEG saved; **comments APIs failed** (12 replies, none listed) |

## Files per item

- source.json (`source_type: x`, `unsaved: false`)
- post.md
- comments.md
- research.md
- media/ when downloadable

## Fetch path

- `https://api.fxtwitter.com/{user}/status/{id}` (primary)
- `https://api.vxtwitter.com/status/{id}` (media URLs)
- `https://r.jina.ai/http://x.com/...` (visible replies)
- Product pages: instantly.ai, mapsdata.ai, worldlabs.ai/blog/atlas, sparkjs.dev, xrarchitect.xyz, starbornai.com
- Video: direct `video.twimg.com` MP4 (yt-dlp not required)

## Gaps

- Post 1: 8/11 replies behind login
- Post 2: most of 14 replies behind login; VR test not shown
- Post 3: 0/12 replies; syndication + jina search empty

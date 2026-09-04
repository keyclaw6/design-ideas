# X Capture 6 — Ingest Manifest

Captured: 2026-09-02T17:53:08Z  
Scope: five bookmark IDs only. **Did not unsave.** HTTP APIs only (no OS computer-use / agent-browser).

| # | ID | URL | Status | Notes |
|---|-----|-----|--------|-------|
| 1 | x-2094826117056414132 | https://x.com/ymt3d/status/2094826117056414132 | complete | JA recap + **7.36s video** (388 KB, 718×396). **Download:** `https://arcana-mfg.com/splat2mesh_dl/Splat2Mesh_v1.0.zip` (110 MB, from `update.json`; 3dnchu URL is the article). 0/0 replies. Topics: `gaussian-splatting`, `bess-3d-flythrough`. |
| 2 | x-2095055297949610427 | https://x.com/iannuttall/status/2095055297949610427 | complete | Feedback ask. Repo `iannuttall/seo` (378★, Apache-2.0, npm `seo@0.2.40`, MCP + skill). 3/26 replies (no status IDs). Topics: `seo-agents`, `agent-skills`, `mcp`. |
| 3 | x-2094770895021572502 | https://x.com/a_shimanski/status/2094770895021572502 | complete | Full free-tool method in note-tweet + quoted GSC (1.01m / 16.3k). 3/26 replies + nested. Topics: `seo-agents`. |
| 4 | x-2094684433546985907 | https://x.com/samigrows/status/2094684433546985907 | complete | **15 directories in post** (Crunchbase, G2, … AngelList). LIST sheet DM-gated, not in comments. 3/21 replies. Topics: `seo-agents`. |
| 5 | x-2094742312433684496 | https://x.com/hridoyreh/status/2094742312433684496 | complete | 6-step Reddit page-1 comment hack + SERP still. 3/8 replies + author nested. Topics: `seo-agents`. |

## Files per item

- source.json (`source_type: x`, `unsaved: false`)
- post.md
- comments.md
- research.md
- media/ (video/thumb, cards, or stills)

## Fetch path

- `https://api.fxtwitter.com/{user}/status/{id}` (primary)
- `https://api.vxtwitter.com/status/{id}` (media URLs)
- `https://r.jina.ai/http://x.com/...` and `https://x.com/...` (visible replies)
- GitHub API + npm registry; Arcana `update.json` + 3dnchu/product HTML
- Video: direct `video.twimg.com` MP4; stills via `pbs.twimg.com`

## Gaps

- Post 1: 0/0 replies; 2 quotes not listed; zip not stored (110 MB)
- Post 2: 3/26 replies; no reply status IDs
- Post 3: 3/26; nested “no, it's for…” truncated (which domain got the traffic)
- Post 4: 3/21; LIST sheet not public
- Post 5: 3/8 replies
- Catalog not touched (lane: `raw/items/` + this manifest)

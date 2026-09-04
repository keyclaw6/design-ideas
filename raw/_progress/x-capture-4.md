# X Capture 4 — Ingest Manifest

Captured: 2026-09-02T17:39:26Z  
Scope: three bookmark IDs only. **Did not unsave.** HTTP APIs only (no OS computer-use / agent-browser).

| # | ID | URL | Status | Notes |
|---|-----|-----|--------|-------|
| 1 | x-2094978216146452971 | https://x.com/nateherk/status/2094978216146452971 | complete | Quotes Fable 5.1 article + **149.2s video** (13.3 MB, 1280×720 via yt-dlp). Skill reply → github.com/nateherkai/scroll-craft (1547★). 3/29 replies visible. Topics: `ui-motion`, `design`, `agent-skills`. |
| 2 | x-2094840529997410525 | https://x.com/Trevs_Dev/status/2094840529997410525 | complete | **15.8s video** (3.8 MB, 1280×720). Atlas Fields Studio + Heaviside-1 paper. 2/22 replies + 1 nested Arena reply. Topics: `three-js`, `design`, `keyboard-pcb`. |
| 3 | x-2095078647652917329 | https://x.com/tranmautritam/status/2095078647652917329 | partial-comments | Note-tweet + 4096² PNG. **9 post URLs + sokosumi from comments.** 2/29 replies visible; rest of “what am I missing?” login-walled. Topics: `design`, `agent-skills`. |

## Files per item

- source.json (`source_type: x`, `unsaved: false`)
- post.md
- comments.md
- research.md
- media/

## Fetch path

- `https://api.fxtwitter.com/{user}/status/{id}` (primary; article body from quote payload)
- `https://api.vxtwitter.com/status/{id}` (media URLs)
- `https://r.jina.ai/http://x.com/...` (visible replies + thread)
- Product pages via jina: fields-studio.arenaphysica.com, arenaphysica.com/publications/heaviside-1, getdesign.md, sokosumi.com/tools/design-md
- GitHub: api.github.com + raw README (jina github.com 403)
- Video: yt-dlp guest GraphQL, format `http-2176` (720p)
- Tried and empty/login: Threadreader, x.com search `conversation_id`, quotes tab, xcancel, nitter.poast, guest TweetDetail

## Gaps

- Post 1: ~26/29 replies behind login
- Post 2: ~20/22 replies behind login; Heaviside self-reply truncated at 280 chars
- Post 3: ~27/29 replies + 4 quotes behind login (extra DESIGN.md URLs likely there)
- Catalog not touched (lane: `raw/items/` + this manifest)

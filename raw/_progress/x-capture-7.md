# X Capture 7 — Ingest Manifest

Captured: 2026-09-02T18:10:58Z  
Scope: five bookmark IDs only. **Did not unsave.** HTTP APIs only (no OS computer-use / agent-browser / CDP). Catalog not touched. No edits to other `raw/items/*`.

| # | ID | URL | Status | Notes |
|---|-----|-----|--------|-------|
| 1 | x-2094740953554932149 | https://x.com/pmitu/status/2094740953554932149 | complete | Quotes Jason Zhou treg people-search. Photo 3832×2150 (330 KB) + **quoted 49.3s video** (6.6 MB, 1920×1080). Repo `superdesigndev/treg` (1020★). **3/34** first-level + 2 nested. Topics: `seo-agents`, `agent-skills`, `mcp`. |
| 2 | x-2094688982940741816 | https://x.com/hridoyreh/status/2094688982940741816 | complete | Quotes 2093964632562253866 (Brave submit-url) **in this folder only**. GA still 1935×1523 (159 KB); quoted form 1320×528; quoted-after 1320×591. **3/13** replies. Topics: `seo-agents`. |
| 3 | x-2094893065202803014 | https://x.com/codyschneider/status/2094893065202803014 | complete | Note-tweet IQ meme; no media. 3 Graphed/YT self-replies + 1 comment. **4 visible / 29**. Topics: `[]`. |
| 4 | x-2094771557864292784 | https://x.com/jakezward/status/2094771557864292784 | complete | 5-layer infographic 3240×4050 (705 KB). **3/35** replies (incl. nqz.ai). Topics: `seo-agents`, `infographics`. |
| 5 | x-2094892848042725416 | https://x.com/pierreeliottlal/status/2094892848042725416 | complete | CEO tree + **39.9s video** (3.7 MB, 1080×1080). Links existing `github-romangojiberryAI-gojiberryai-sales-os` (70★ at capture; folder not rewritten) and `x-2095081419202560010`. **0/163** replies (BOT magnet). Topics: `mcp`, `agent-skills`, `seo-agents`. |

## Files per item

- source.json (`source_type: x`, `unsaved: false`)
- post.md
- comments.md
- research.md
- media/ when downloadable (item 3: none)

## Fetch path

- `https://api.fxtwitter.com/{user}/status/{id}` (primary)
- `https://api.vxtwitter.com/status/{id}` (media URLs)
- `https://r.jina.ai/http://x.com/...` — **blocked** AbuseAlleviation until 2026-09-02T18:55:15Z
- `https://r.jina.ai/http://fixupx.com/...` (visible replies; 403 on Pierre + Jason thread)
- GitHub API + raw README; `treg.to/llms.txt`; r.jina.ai on treg.to, graphed.com, known.agency, nqz.ai, search.brave.com/submit-url, gojiberry.ai
- Video/stills: direct `video.twimg.com` / `pbs.twimg.com` (no yt-dlp)
- Tried empty/login: Threadreader, xcancel (C&D), nitter.poast/tiekoetter, syndication `tweet-result`, rsshub, oembed

## Gaps

- Post 1: ~31/34 replies; Jason “Git Repo below” self-reply missing (inferred `superdesigndev/treg` from product page)
- Post 2: ~10/13 parent replies; quoted tweet’s 16 replies mostly unlisted (1 self-reply + Csaba one-liner)
- Post 3: ~25/29 replies
- Post 4: ~32/35 replies; 7 quotes unlisted
- Post 5: 0/163 replies
- Catalog not touched (lane: `raw/items/` + this manifest)

## Follow-on URLs

GitHub / web for a later ingest lane (do not create folders in this capture):

- https://github.com/superdesigndev/treg
- https://github.com/LessieAI/people-search-bench
- https://treg.to/people-search
- https://treg.to
- https://treg.to/llms.txt
- https://arxiv.org/abs/2603.27476
- https://search.brave.com/submit-url
- https://www.graphed.com/
- https://www.graphed.com/mcp
- https://cal.com/team/graphed-com/discovery
- https://www.youtube.com/@codyschneiderx
- https://known.agency/
- https://nqz.ai/ai-search-prompt-generator
- https://www.flowmapp.com/
- https://seowins.io/
- https://x.com/i/article/2091990303062593536 (Devansh KYC Genie; X article)

Already in library (linked only): `github-romangojiberryAI-gojiberryai-sales-os`, `x-2095081419202560010`.

# X Capture 8 — Ingest Manifest

Captured: 2026-09-02T18:33:15Z  
Scope: five bookmark IDs only. **Did not unsave.** HTTP APIs only (no OS computer-use / agent-browser / CDP). Catalog not touched. No edits to other `raw/items/*` (including `web-arcana-splat2mesh`, `x-2094826117056414132`).

| # | ID | URL | Status | Notes |
|---|-----|-----|--------|-------|
| 1 | x-2095133695480873023 | https://x.com/derrickcchoi/status/2095133695480873023 | complete | ChatGPT Training card 800×419 (17 KB). **4 visible / 28** (3 first-level + Derrick nested). Topics: `agent-skills`. |
| 2 | x-2094467179320119498 | https://x.com/robinstetic/status/2094467179320119498 | complete | ES; no URL in tweet. Video 55.7s 1350×720 (7.7 MB). MCP from video = AIDesigner (`api.aidesigner.ai/api/v1/mcp`). **4 visible / 22**. Topics: `mcp`, `design`. |
| 3 | x-2094558408259272998 | https://x.com/medriscoll/status/2094558408259272998 | complete | Collage 1536×1024 (302 KB). Linked Ramp/Cerebras/Anthropic tweets in `related_urls` only (no extra x-* folders). **3/6** replies. Topics: `agent-skills`, `mcp`, `infographics`. |
| 4 | x-2094648474377839018 | https://x.com/ArcanaMfg/status/2094648474377839018 | complete | JA launch. Quotes 70.6s 1080p teaser (32.7 MB). Zip HEAD 110 MB **not downloaded**. Links existing `web-arcana-splat2mesh` + `x-2094826117056414132`. **0/0** replies; 10 quotes unlisted. Topics: `gaussian-splatting`, `bess-3d-flythrough`. |
| 5 | x-2094427822064279870 | https://x.com/0xJokker/status/2094427822064279870 | complete | ES Obscura claims. Self-reply repo `h4ckf0r0day/obscura` (23,982★). PNG 541×583 (40 KB). **5 visible / 46**. Topics: `agent-skills`. |

## Files per item

- source.json (`source_type: x`, `unsaved: false`)
- post.md
- comments.md
- research.md
- media/ when downloadable (all five have media; zip skipped)

## Fetch path

- `https://api.fxtwitter.com/{user}/status/{id}` (primary; `/status/{id}` without user for replies)
- `https://api.vxtwitter.com/status/{id}` (media URLs + reply bodies)
- `https://r.jina.ai/http://fixupx.com/...` and `http://fxtwitter.com/...` (visible replies; some 403 truncated)
- `https://r.jina.ai/http://x.com/...` — not relied on (prior AbuseAlleviation window)
- GitHub API + npm registry; r.jina.ai on learn.chatgpt.com/training, aidesigner.ai MCP/docs, obscura.sh, docs.obscura.sh, Ramp/Cerebras/Anthropic blogs
- Video/stills: direct `video.twimg.com` / `pbs.twimg.com` (no yt-dlp)
- Zip: HTTP HEAD only
- Tried empty/login: Threadreader, nitter.net (offline), nitter.poast (NXDOMAIN), nitter.tiekoetter (429)

## Gaps

- Post 1: ~24/28 replies; Nick’s 1 nested unlisted
- Post 2: ~18/22 replies; no MCP URL in thread (video + product site)
- Post 3: ~3/6 replies; RMB nested unlisted; 1 quote unlisted
- Post 4: 0 replies; 10 quotes unlisted
- Post 5: ~41/46 replies; 12 quotes unlisted
- Catalog not touched (lane: `raw/items/` + this manifest)

## Follow-on URLs

GitHub / web for a later ingest lane (do not create folders in this capture):

- https://learn.chatgpt.com/training
- https://learn.chatgpt.com/llms.txt
- https://www.aidesigner.ai/ai-ui-design-mcp
- https://www.aidesigner.ai/docs/mcp
- https://www.aidesigner.ai/
- https://www.aidesigner.ai/website-cloner
- https://www.npmjs.com/package/@aidesigner/agent-skills
- https://github.com/h4ckf0r0day/obscura
- https://obscura.sh
- https://docs.obscura.sh
- https://www.iandmacomber.com/blog/post-ai-data-stack
- https://www.cerebras.ai/blog/how-we-built-our-knowledge-base
- https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
- https://davidgasquez.com/context-engineering-is-a-data-problem
- https://blog.cloudflare.com/kitesurf/
- https://cal.com/obscura/quick-chat

Already in library (linked only): `web-arcana-splat2mesh`, `x-2094826117056414132`.

# X Capture 9 — Ingest Manifest

Captured: 2026-09-02T18:49:18Z  
Scope: five bookmark IDs only. **Unsaved on X** (verified 2026-09-03 via agent-browser: all five show aria-label `Bookmark`, not `Remove Bookmark`). Follow-ons ingested — see `links-from-x-capture-9.md`. Catalog updated in rebuild (110 entries).

| # | ID | URL | Status | Notes |
|---|-----|-----|--------|-------|
| 1 | x-2094328961522397530 | https://x.com/chrissyinspace/status/2094328961522397530 | complete | TinyShelf DR 14→46; TinyShots listed. Own still DR 46 (44 KB); quoted 2093895489364316594 still DR 35 (19 KB) in this folder only. **0/21** replies (quoted 0/22). Topics: `seo-agents`. |
| 2 | x-2094524951025914278 | https://x.com/olavlj/status/2094524951025914278 | complete | X article `2094493136743473152` (68 blocks) from fxtwitter. Cover + 3 stills + 3 article videos (16.4s / 11.8s / 19.3s, 1420×926). **0/13** replies. Topics: `design`, `ui-motion`. |
| 3 | x-2094553318031024285 | https://x.com/Crowdreply_io/status/2094553318031024285 | complete | 11.4s 1080p (6.1 MB). Quotes Dawood article tweet — `related_urls` only (cover stored). MCP `mcp.crowdreply.io/mcp` 401 JSON. **6 visible / 8** (3 first-level + CrowdReply/Toma/Grok nested). Topics: `seo-agents`, `mcp`, `agent-skills`. |
| 4 | x-2094462971598754010 | https://x.com/garrytan/status/2094462971598754010 | complete | Table PNG 1542×1352 (266 KB). Repo `garrytan/gbrain-evals` 406★ MIT; `garrytan/gbrain` 29,487★. **3 visible / 99** (no status IDs on fixupx). Topics: `agent-skills`. |
| 5 | x-2094326291906310180 | https://x.com/pierreeliottlal/status/2094326291906310180 | complete | Calendly Slack still 1344×300 (41 KB). Links existing `github-romangojiberryAI-gojiberryai-sales-os` (70★ at capture; folder not rewritten). **2 visible / 12**. Topics: `mcp`, `agent-skills`, `seo-agents`. |

## Files per item

- source.json (`source_type: x`, `unsaved: true`)
- post.md
- comments.md
- research.md
- media/ (all five have media; nothing >80 MB)

## Fetch path

- `https://api.fxtwitter.com/{user}/status/{id}` (primary; article payloads for olav + Dawood quote)
- `https://api.vxtwitter.com/status/{id}` (media URLs + counts)
- `https://r.jina.ai/http://fixupx.com/...` and `http://fxtwitter.com/...` (visible replies; some embed-only / article-only)
- `https://r.jina.ai/http://x.com/...` — AbuseAlleviation until 2026-09-02T19:31:55Z
- GitHub API (read-only on gojiberry); r.jina.ai on tinyshelf.co, tinyshots.app, tinylaunch.com/directories, blume.codes, crowdreply.io, crowdreply.io/mcp
- Video/stills: direct `video.twimg.com` / `pbs.twimg.com`
- Tried: Threadreader login wall; nitter.space Cloudflare 403; syndication.twimg.com tweet-result (parent only)

## Gaps

- Post 1: 21/21 parent replies; 22/22 on quoted Aug 30 tweet
- Post 2: 13/13 replies (fixupx served the article, not the thread)
- Post 3: ~2/8 replies; Dawood article inline images/prompts not stored as extra media (cover only)
- Post 4: ~96/99 replies; 3 visible lack tweet IDs
- Post 5: ~10/12 replies
- Catalog not touched at capture time (lane: `raw/items/` + this manifest)

## Follow-on URLs — ingested (2026-09-03)

All seven web follow-ons captured; see `links-from-x-capture-9.md`. Catalog rebuilt.

| URL | Item ID | Status |
|-----|---------|--------|
| https://tinyshelf.co | web-tinyshelf | complete |
| https://tinyshots.app | web-tinyshots | complete |
| https://www.tinylaunch.com/directories | web-tinylaunch-directories | complete |
| https://blume.codes | web-blume-codes | complete |
| https://fal.ai | web-fal-ai | complete |
| https://www.dicebear.com | web-dicebear | complete |
| https://crowdreply.io | web-crowdreply | complete |

Still linked only (not new folders):


- https://tinyshelf.co/submit (metadata in web-tinyshelf)
- https://tinyshelf.co/tools/tinyshots (metadata in web-tinyshelf)
- https://x.com/i/article/2094493136743473152 (in x-2094524951025914278)
- https://crowdreply.io/mcp (in web-crowdreply)
- https://mcp.crowdreply.io/mcp (probe in web-crowdreply)
- https://crowdreply.io/features/citation-outreach (in web-crowdreply)
- https://calendly.com/d/d3hw-zsm-rm4/citation-outreach-demo
- https://x.com/i/article/2094451432208711681
- https://x.com/dawoodkhan254/status/2094451439573881015
- https://github.com/garrytan/gbrain-evals
- https://github.com/garrytan/gbrain
- https://arxiv.org/abs/2604.21284
- https://gojiberry.ai/
- https://mcp.gojiberry.ai/mcp

Already in library (linked only): `github-romangojiberryAI-gojiberryai-sales-os`, `x-2094892848042725416`, `x-2095081419202560010`.

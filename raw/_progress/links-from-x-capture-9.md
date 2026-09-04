# Links from X Capture 9 — Ingest Manifest

Captured: 2026-09-03T12:00:00Z  
Source tweets: [chrissyinspace TinyShelf](https://x.com/chrissyinspace/status/2094328961522397530), [olavlj landing page article](https://x.com/olavlj/status/2094524951025914278), [Crowdreply_io AEO](https://x.com/Crowdreply_io/status/2094553318031024285), [garrytan GBrain](https://x.com/garrytan/status/2094462971598754010), [pierreeliottlal Gojiberry demo](https://x.com/pierreeliottlal/status/2094326291906310180)  
Fetch: HTTP + r.jina.ai + GitHub API + curl (MCP probe)

| # | ID | URL | Status | Notes |
|---|-----|-----|--------|-------|
| 1 | web-tinyshelf | https://tinyshelf.co | complete | Landing + `/submit` (Google OAuth) + `/tools/tinyshots`; 19 categories |
| 2 | web-tinyshots | https://tinyshots.app | complete | macOS Sonoma 14+; early bird $39 lifetime |
| 3 | web-tinylaunch-directories | https://www.tinylaunch.com/directories | complete | 110-directory submission service; 30k+ makers |
| 4 | web-blume-codes | https://blume.codes | complete | Agent sidecar for Codex / Claude Code / Cursor |
| 5 | web-fal-ai | https://fal.ai | complete | Generative media API; docs overview + llms.txt in related_urls |
| 6 | web-dicebear | https://www.dicebear.com | complete | 61 avatar styles; MIT core; playground + API |
| 7 | web-crowdreply | https://crowdreply.io | complete | Landing + `/mcp` + citation-outreach; MCP 401 without key |

## Skipped (per brief)

| URL | Reason |
|-----|--------|
| https://tinyshelf.co/submit | Login-walled — flow metadata only in `web-tinyshelf` |
| https://x.com/i/article/2094493136743473152 | X article — captured in `x-2094524951025914278` post.md |
| https://x.com/i/article/2094451432208711681 | Dawood article — related_urls on `x-2094553318031024285` only |
| https://x.com/dawoodkhan254/status/2094451439573881015 | Quoted tweet — related_urls only |
| https://calendly.com/d/d3hw-zsm-rm4/citation-outreach-demo | Calendly booking — skip |
| https://mcp.crowdreply.io/mcp | Endpoint probe only — docs in `web-crowdreply` |
| https://crowdreply.io/features/citation-outreach | Merged into `web-crowdreply` folder |
| https://github.com/garrytan/gbrain-evals | GitHub repos — not in follow-on brief |
| https://github.com/garrytan/gbrain | GitHub repos — not in follow-on brief |
| https://arxiv.org/abs/2604.21284 | arXiv — not in follow-on brief |
| https://gojiberry.ai/ | Already linked via existing items |
| https://mcp.gojiberry.ai/mcp | Already in `github-romangojiberryAI-gojiberryai-sales-os` |

## Already in library (linked only, not edited)

- `x-2094328961522397530`, `x-2094524951025914278`, `x-2094553318031024285`, `x-2094462971598754010`, `x-2094326291906310180` (capture-9 posts)
- `github-romangojiberryAI-gojiberryai-sales-os`
- `x-2094892848042725416`, `x-2095081419202560010`

## Summary

- **7/7** required item folders created
- **7/7** complete captures
- **7/7** source.json + page.md + research.md
- **0** comments.md (web items)
- **0** media saved (web items)
- Catalog rebuilt; capture-9 X bookmarks: 3 unsaved on X (`unsaved: false`), 2 still bookmarked

## related_urls graph (high level)

```
x-capture-9 posts
  ├─► chrissyinspace directory cluster
  │     ├─► web-tinyshelf (+ /submit, /tools/tinyshots)
  │     ├─► web-tinyshots
  │     └─► web-tinylaunch-directories
  ├─► olavlj landing-page article
  │     ├─► web-blume-codes
  │     ├─► web-fal-ai (layer gen)
  │     └─► web-dicebear (daily flowers)
  ├─► Crowdreply_io AEO
  │     └─► web-crowdreply (+ /mcp, citation-outreach)
  ├─► garrytan GBrain (repos in related_urls only)
  └─► pierreeliottlal Gojiberry demo
        └─► github-romangojiberryAI-gojiberryai-sales-os (existing)
```

# X Capture 2 — Ingest Manifest

Captured: 2026-09-02T17:25:49Z  
Scope: three bookmark IDs only. **Did not unsave.** HTTP APIs + yt-dlp only (no OS computer-use / agent-browser).

| # | ID | URL | Status | Notes |
|---|-----|-----|--------|-------|
| 1 | x-2094820035344621901 | https://x.com/harris/status/2094820035344621901 | complete | Note-tweet + 13.6s video. FRM beta site Vercel 429. 3/4 replies via jina+fx. Topics: mcp, agent-skills. |
| 2 | x-2095130625976176754 | https://x.com/karakhanyanS/status/2095130625976176754 | partial | Note-tweet complete. **First comment (free-version link) not captured** — 2 replies login-walled. Free tool URL inferred from blogr.ai/tools. Card image saved. Topic: seo-agents. |
| 3 | x-2094961942058418268 | https://x.com/tokufxug/status/2094961942058418268 | complete | JA post + 42.9s video. Author reply → LinkedIn → lucida-r2s.github.io + arXiv:2608.30821. Topic: bess-3d-flythrough. |

## Summary

- **3/3** folders: `source.json` + `post.md` + `comments.md` + `research.md`
- **unsaved:** false on all
- **Media:** harris video 758k + thumb; lucida video 5.4M + thumb; blogr card.jpg
- **Fetch:** api.fxtwitter.com, api.vxtwitter.com, r.jina.ai, yt-dlp (guest GraphQL)
- **Blockers:** frm.theventurecodex.com checkpoint; blogr first comment; lucida GitHub 404 (project page only)

## Tools researched

- FRM / Venture Codex (MCP fundraising platform; UI gated)
- blogr.ai topical maps + free generator
- Lucida parse–generate–place (Seed3D 2.0 + GizmoAct)

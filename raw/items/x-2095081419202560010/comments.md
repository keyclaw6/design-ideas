# Comments / thread

fx/vx return counts only. Conversation list APIs failed:

- `api.fxtwitter.com/.../status/{id}` and `/replies` / `/quotes` — parent tweet only, no replies array
- `api.vxtwitter.com` — reply *count* (87), no thread
- `cdn.syndication.twimg.com/tweet-result` — truncated note-tweet + media, no conversation
- `r.jina.ai` on `http://x.com/gojiberryai/status/…` and `/i/status/…` — post body only
- `r.jina.ai` on `x.com/search?q=conversation_id:2095081419202560010` — login/marketing shell
- Threadreader — login wall
- xcancel — service shut down (X C&D)

No author self-replies in the fxtwitter payload (`replying_to` null). Thread text is the note-tweet itself in `post.md`.

87 replies at capture. Post asks people to comment **“BOT”** so the author can DM the repo — that is a lead magnet, not a public thread dump. Remaining replies behind X login / official conversation API.

## Repo (not from comments)

Public GitHub, found independently of the thread:

- **https://github.com/romangojiberryAI/gojiberryai-sales-os** — MIT, 69★ / 20 forks at capture, created 2026-09-01. Grok/Claude plugin `sales-os` + `skills/sales-os/SKILL.md` + 13 `agents/*.md`. Hosted MCP `https://mcp.gojiberry.ai/mcp`. Also listed in [RongleCat/awesome-grok-bot](https://github.com/RongleCat/awesome-grok-bot).

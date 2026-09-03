# Comments / thread

Conversation list APIs failed:

- `api.fxtwitter.com/.../status/{id}` and `/replies` — tweet only, no replies array
- `api.vxtwitter.com` — reply *count* (12), no thread
- `cdn.syndication.twimg.com/tweet-result` — empty
- `r.jina.ai` on `http://` and `https://x.com/paolo_scales/status/2095060844547592437` — post body only (no first replies)
- `r.jina.ai` on `x.com/search?q=conversation_id:2095060844547592437` — login/marketing shell, no tweets

No author self-replies in the fxtwitter payload (`replying_to` null). Thread text is the note-tweet itself in `post.md`. Remaining 12 replies not captured without X login / official conversation API.

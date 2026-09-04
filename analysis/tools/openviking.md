# Openviking

**Slug:** `openviking` · **Kind:** repo · **URL:** https://github.com/volcengine/OpenViking · **Canonical item:** [x-2091169290661838965](../items/x-2091169290661838965/card.md)
**Subjects:** [agent-memory-knowledge](../subjects/agent-memory-knowledge/brief.md)
**Referenced by (1):**
- [OpenViking: ByteDance agent memory with filesystem-style context search](../items/x-2091169290661838965/card.md) — tool, claim-source — agent-memory-knowledge

<!-- NOTES:START -->
Fetched 2026-09-04 README https://github.com/volcengine/OpenViking

**AGPLv3** OSS context DB. `viking://` URIs; agent uses `ls` / `tree` / `find` / `ov grep`. Studio https://openviking.ai/studio is a JS shell this pass (no method text). Docs fetched: https://docs.openviking.ai/en/concepts/03-context-layers

Official layer table (defaults): **L0** Abstract = directory `.abstract.md`, 256 characters, vector recall; **L1** Overview = `.overview.md`, 4000 characters, rerank/navigation; **L2** Detail = original files, no uniform limit. L0/L1 are **directory sidecars**, not per-file. FAQ still says “~100 tokens / ~2000 tokens” — that is the marketing token gloss; the concept page’s character limits are the configured defaults (`semantic.abstract_max_chars` / `overview_max_chars`). Retrieval: intent analysis → vector on L0 → rerank on L1 → load L2. `find()` vs `search()` (search adds conversation-aware expansion). Commercial edition exists (license key) on top of the OSS tree.

**2026-09-04 capture — MCP tool list** (`docs/en/guides/06-mcp-integration.md` in `volcengine/OpenViking`). Endpoint `http://<server>:1933/mcp` (same process as REST). Auth: `X-Api-Key` or `Authorization: Bearer`; localhost needs no auth. Docs name **15 tools**: `find`, `search` (`mode=list|context`; context mode replaces former `recall`), `read` (`viking://`; PNG/JPEG/GIF/WebP as MCP image; WAV/MP3/FLAC/OGG/M4A as MCP audio; video not supported), `list`, `tree`, `remember`, `write`, `edit`, `add_resource`, `list_watches`, `cancel_watch`, `grep`, `glob`, `forget`, `health`. Remaining: a live `viking://` session log.
<!-- NOTES:END -->

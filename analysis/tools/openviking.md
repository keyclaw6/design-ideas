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

**2026-09-04 capture — pip 0.4.17.1 + `openviking-server doctor`.** `pip install openviking` → package **0.4.17.1**; CLI banner `OpenViking v0.4.17.2.dev0`. `ov` lists `health`, `status`, `ls`, `tree`, `find`, `read`, `write`. Doctor on this host with no `~/.openviking/ov.conf`: Config **FAIL**; Python 3.12.3 **PASS**; Native Engine **PASS** `variant=x86_avx512`; AGFS SDK **0.1.7 PASS**; Embedding/VLM **FAIL** (no config); Ollama **PASS** (not configured); Disk **218.0 GB**. `openviking-server` help default port is unset (reads `ov.conf`). This is a local binary/doctor receipt, **not** a `viking://` read. Remaining: write a provider `ov.conf` and log one `ov ls viking://…` / `health`.

**2026-09-04 capture — doctor with a written `ov.conf`.** Minimal JSON (`storage.workspace=/tmp/ov-data`, vectordb+agfs `local`, embedding `provider=local` `model=bge-small-zh-v1.5-f16` dim 512, server `127.0.0.1:1933`). `openviking-server doctor --config /tmp/ov.conf`: Config **PASS**; Authentication **PASS** `dev`; Embedding **FAIL** `local/bge-small-zh-v1.5-f16 (missing llama-cpp-python)` — fix `pip install "openviking[local-embed]"`; VLM **FAIL** “No VLM provider configured”; Disk **217.9 GB** in `/tmp/ov-data`. Docs list embedding providers including `local` / `ollama`. Still no `ov health` / `viking://` session.
<!-- NOTES:END -->

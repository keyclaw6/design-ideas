# Openviking

**Slug:** `openviking` · **Kind:** repo · **URL:** https://github.com/volcengine/OpenViking · **Canonical item:** [x-2091169290661838965](../items/x-2091169290661838965/card.md)
**Subjects:** [agent-memory-knowledge](../subjects/agent-memory-knowledge/brief.md)
**Referenced by (1):**
- [OpenViking: ByteDance agent memory with filesystem-style context search](../items/x-2091169290661838965/card.md) — tool, claim-source — agent-memory-knowledge

<!-- NOTES:START -->

Fetched 2026-09-04 README https://github.com/volcengine/OpenViking

**AGPLv3** OSS context DB. `viking://` URIs; agent uses `ls` / `tree` / `find` / `ov grep`. Three write-time tiers: L0 abstract (~100 tokens), L1 overview, L2 full. Directory-recursive retrieval; each query keeps a browsable trajectory. Studio demo: https://openviking.ai/studio (no install). Docs: https://docs.openviking.ai/. Commercial edition exists (license key) on top of the OSS tree. “Viking protocol” is this URI + tier scheme, not a mystery RPC.

<!-- NOTES:END -->

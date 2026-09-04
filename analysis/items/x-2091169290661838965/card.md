# OpenViking: ByteDance agent memory with filesystem-style context search

`x-2091169290661838965` · x · repo · en · [source](https://x.com/defileo/status/2091169290661838965) · [raw](../../../raw/items/x-2091169290661838965/)
**Author:** defileo (@defileo) · **Published:** — · **Captured:** 2026-09-04T07:01:49Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [agent-memory-knowledge](../../subjects/agent-memory-knowledge/brief.md) · **Also:** — · **Roles:** tool, claim-source · **Platforms:** claude-code, codex

**Summary.** Hype post for OpenViking (volcengine/OpenViking): a Viking-protocol memory layer where agents explore context with ls/tree/find at three detail levels, traceable searches, and claimed up to 91% token savings for Claude Code, Codex, and OpenClaw.
**Question it answers.** What is OpenViking and how does its filesystem-style agent memory differ from black-box vector stores?

**Claims.**
- `x-2091169290661838965#c1` (capability, stated) OpenViking layers agent memory, RAG, and skills so agents explore context with ls/tree/find at three detail levels with traceable searches instead of opaque vector retrieval. — evidence: "one layer for agent memory, rag, and skills under the viking protocol
> agents explore their own context with ls/tree/find, not a black-box vector store
> 3 detail levels from summary to full, loading only what's needed
> every search is traceable" [post]
- `x-2091169290661838965#c2` (capability, demonstrated) OpenViking MCP endpoint exposes 15 named tools on :1933/mcp, including find, search (list|context), read of viking:// URIs, write/edit, and health. — evidence: "docs/en/guides/06-mcp-integration.md: Once connected, OpenViking exposes 15 tools; table lists find, search, read, list, tree, remember, write, edit, add_resource, list_watches, cancel_watch, grep, glob, forget, health." [note]
- `x-2091169290661838965#c3` (result, demonstrated) pip install openviking 0.4.17.1 on this host; openviking-server doctor passes Python/native-engine/AGFS and fails Config/Embedding/VLM because ~/.openviking/ov.conf is missing. Not a viking:// session. — evidence: "doctor: Config FAIL; Native Engine PASS variant=x86_avx512; AGFS SDK 0.1.7; Ollama not configured. See openviking NOTES." [note]
**Numbers.** claimed token reduction: 91 % (reply); documented MCP tools: 15 tools (note)
**Recipe.** —
**Techniques.** [filesystem-context-memory](../../techniques/filesystem-context-memory.md), [context-etl](../../techniques/context-etl.md)
**Tools.** [openviking](../../tools/openviking.md)
**Links.** repo (https://github.com/volcengine/OpenViking)
**Related items.** [x-2087143369181114868](../x-2087143369181114868/card.md), [x-2088231655177924993](../x-2088231655177924993/card.md)
**Media.** —
**Thread.** captured_partial · reported 4 · captured 1 · relevant 0 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: True · compare with: [x-2087143369181114868](../x-2087143369181114868/card.md), [x-2088231655177924993](../x-2088231655177924993/card.md)

# Thread — CopilotKit aimock — single-port mock stack for LLM, MCP, and search (x-2087151521121419648)

**Status:** captured_partial · **Author thread:** none · **Replies reported:** 0 · **Captured:** 0 · **Relevant:** 0 · **Unfetched:** 0 · **Truncated:** False
**Fetch log:** x-web-dom→ok (2026-09-04T17:54:20Z); fxtwitter-api→ok (2026-09-04T17:54:20Z)
**Raw payloads:** `raw/items/x-2087151521121419648/thread-raw/x-web-dom-20260904T175303Z.html`

**Author continuation (0 posts).**
**Quoted.**
> **@CopilotKit** · 2087151338136510876
> aimock just crossed 1,000,000 weekly downloads.

Mock every API your AI app talks to: 13 providers across 15 API surfaces. MCP, A2A, AG-UI, vector DBs, search, TTS. One port, zero dependencies.

npm i @copilotkit/aimock

Here's what's inside 🧵 https://t.co/zjyVhhUPGN

> **@CopilotKit** · 2087151359439294965
> 0/ Trusted and used by top AI Teams:

- @openclaw
- @mastra
- @tan_stack

All use AI mock to streamline testing https://t.co/06ydan3ntm

> **@CopilotKit** · 2087151375406989742
> 1/ AGUIMock

Your AG-UI frontend (CopilotKit) needs a live agent to test against.

Agent to UI Mock replaces it. Streams text. Tool calls. State updates. https://t.co/BBqTvwOsdm

> **@CopilotKit** · 2087151394096861210
> 2/ LLMock

13 LLM providers. Full streaming. Tool calls. Reasoning models.

OpenAI, Claude, Gemini, Bedrock, Azure, Vertex AI, Ollama, Cohere - one fixture format works across all of them.

Point your OpenAI client at the mock URL. Same response every time. No API keys. No tokens https://t.co/kGQYOp87ru

> **@CopilotKit** · 2087151410999889965
> 3/ MCPMock

Your agent calls MCP tools. Every tool call in your tests hits a live server.

MCPMock gives you a local MCP server - full JSON-RPC, session
management, tools, resources, prompts.

Your agent connects to it like the real thing. You control every response. https://t.co/w2Zmj1Qrt4

> **@CopilotKit** · 2087151427470942453
> 4/ A2AMock

Multi-agent systems are great until you try to test them.

Agent A calls B calls C. One goes down. CI is red.

A2AMock - local A2A server with agent cards, message routing, task management, SSE streaming. Test the whole conversation
without a single agent running. https://t.co/Wfkzd84DXv

> **@CopilotKit** · 2087151443728076828
> 5/ VectorMock

 Your RAG tests pass or fail depending on what's in your dev index today. That's not a test.

VectorMock speaks Pinecone, Qdrant, and ChromaDB APIs. Same retrieval results every run. No live database. https://t.co/rrIkpLaSbB

> **@CopilotKit** · 2087151459330818318
> 6/ Record &amp; Replay

Stop hand-writing fixtures.

Point AIMock at your real APIs. It proxies the requests, saves the responses as JSON fixtures, replays them forever.

Works across OpenAI SSE, Anthropic SSE, Gemini SSE, Cohere SSE, Ollama NDJSON, and Bedrock EventStream. https://t.co/LnP9jGjsZH

> **@CopilotKit** · 2087151475839717423
> 7/ Search, Rerank, Moderation

  The APIs everyone forgets to mock.

Tavily search. Cohere reranking. OpenAI moderation. All built in. Register patterns, get deterministic results. No separate servers. https://t.co/3xCfqh5PTl

> **@CopilotKit** · 2087151493363458483
> 8/ Drift Detection

This one nobody else does.

Your mocks are a snapshot. APIs change. Your mocks still pass. Then prod breaks.

AIMock runs daily CI checks against live endpoints - SDK types vs real API vs mock output. Three-way comparison. You know within 24 hours. https://t.co/n6wQ2bEcyo

> **@CopilotKit** · 2087151508861386790
> 9/ Chaos Testing

LLM APIs fail without warning. Your tests should too.

Drop requests. Return malformed JSON. Kill the TCP connection mid-stream. Set it per server, per fixture, or per request. https://t.co/iVqhgGiMZh

**Relevant replies (0 of 0 captured).**
**Dropped as noise:** 0 replies (praise, emoji, bots, unrelated promo).

# Qwen Open Sources zg Local Search Tool for Code and Docs

> Source: https://www.reddit.com/r/aicuriosity/comments/1w5dab4/qwen_open_sources_zg_local_search_tool_for_code/
> Author: u/techspecsmart
> Posted: 2026-09-02T15:17:20+00:00
> Captured: 2026-10-15T08:55:18+00:00
> Score: 77 · Comments: 4
> Community: r/aicuriosity

## Post

Qwen Developers just released zg also known as zvec-grep as open source. It is a local first search tool built for both people and AI agents that need to dig through scattered files on their own machines.

Traditional tools like ripgrep work great when you already know the exact keyword or function name. But agents and developers often search with natural language questions such as “how does theme restore work” or “what is the access request process.” Those queries rarely match the exact words used in code or docs. That forces extra searches more file reads and higher token use.

zg combines vector search BM25 hybrid ranking and classic ripgrep in one place. It indexes local code documentation and other text files keeps everything on device by default and returns ranked results with source locations. You can use it through a simple CLI or connect it straight to agents via MCP. Installation is straightforward and it automatically sets up popular coding tools.

Early tests show it cuts tool calls and input tokens by a large margin while keeping or improving answer quality on code and research tasks. Everything stays private unless you deliberately enable remote embeddings.

The project is available on GitHub under Apache 2.0. The team is looking for feedback real world use cases and contributions especially around new file formats better ranking and agent workflows.

## Media

![](media/01-reddit-media.jpeg)

> Original media URL: https://i.redd.it/3ita3jv3j4nh1.jpeg

![](media/02-reddit-media.jpeg)

> Original media URL: https://preview.redd.it/3ita3jv3j4nh1.jpeg?auto=webp&s=081a5861a9373f191df6734d4c780ac57186176c

## Thread

> u/techspecsmart · 2026-09-02T15:17:48+00:00 · score 1 · [comment](https://www.reddit.com/r/aicuriosity/comments/1w5dab4/qwen_open_sources_zg_local_search_tool_for_code/p7e48qw/)

GitHub 
https://github.com/zvec-ai/zvec-grep

## Comments

> u/andy012345 · 2026-09-03T20:20:02+00:00 · score 1 · [comment](https://www.reddit.com/r/aicuriosity/comments/1w5dab4/qwen_open_sources_zg_local_search_tool_for_code/p7nc3bo/)

What links this to qwen? Was the commit history rewrote at some point as github lists claude in the UI?

> u/Androoideka · 2026-09-03T20:49:47+00:00 · score 1 · [comment](https://www.reddit.com/r/aicuriosity/comments/1w5dab4/qwen_open_sources_zg_local_search_tool_for_code/p7nisi7/)

Zvec is by Alibaba, so is Qwen. [https://github.com/alibaba/zvec](https://github.com/alibaba/zvec)

> u/purealgo · 2026-09-04T23:11:52+00:00 · score 1 · [comment](https://www.reddit.com/r/aicuriosity/comments/1w5dab4/qwen_open_sources_zg_local_search_tool_for_code/p7vij9g/)

Interesting. I've already been building something similar for months before this release  
  
[https://github.com/itsmostafa/qi](https://github.com/itsmostafa/qi)


## What they are actually doing

Brand account amplifying founder Dawood’s X article as a **three-step Grok Bot setup**: install a bot named Chief of AI Visibility, connect **CrowdReply MCP**, paste the article (six bot prompts). The $100k/90-days line is the tweet’s hook; [@grok](https://x.com/grok) replied on-thread that it is marketing hype.

**Quoted article** (related_urls only; no extra item folder) — “How I use Grok Bots to rank brands on AI answers that it feels illegal.” CrowdReply tracks which pages ChatGPT / Grok / Perplexity / Gemini / Google AI cite for buying questions across 10,000+ brands. Method they call **Citation Outreach**: pull cited URLs → keep editorial pages the models reuse → get a mention on those pages → watch answers move. Receipt in the article: an online design tool **4% → 40%** visibility in 11 weeks; on the main question, named on 76/847 cited pages → 127/847 (TL;DR also says 2/17 → 9/17 source pages for the ChatGPT question that mattered). First movement “around month three.”

Six Grok Bots (approve send and spend only):

| Bot | Job | Connect |
|-----|-----|---------|
| Scout | Cited URLs → editorial shortlist | CrowdReply MCP, Sheets, browser |
| Finder | Editor/owner + verified email | Snov, Prospeo, Hunter, ZeroBounce, Google |
| Writer | Sequence into Smartlead, never sends | Sheets, Smartlead |
| Closer | Sort replies, draft fee cards, never pays | Smartlead, Sheets, Slack optional |
| Watcher | Confirm live mention + weekly visibility | CrowdReply MCP, browser |
| Chief of Staff | Monday digest, stalls, never sends/spends | Sheets, Slack optional |

One-click templates in the article (`x.ai/bot/...` URLs in `related_urls`). Managed product: https://crowdreply.io/features/citation-outreach — Calendly https://calendly.com/d/d3hw-zsm-rm4/citation-outreach-demo.

**MCP** — docs https://crowdreply.io/mcp (“first MCP that shows you where you're invisible”). Claude custom-connector URL uses `https://mcp.crowdreply.io/mcp/client`. Unauthenticated GET `https://mcp.crowdreply.io/mcp` → `401 {"error":"Unauthorized"}` (`application/json`). Docs list 18+ tools (visibility/citations read; `create_task` etc. writes behind two-step confirm). Site: “#1 AI Search Visibility Tool”; 7-day trial; “Trusted by 5,000+ brands” on the MCP page.

On-thread TLDR from the brand to Robby Frank: models rank on owned content + offsite mentions; CrowdReply does the second by placing the brand on pages already cited for “best [category] for [job].”

## Open questions

- Whether “Chief of AI Visibility” is a seventh bot or a rename of Chief of Staff.
- AgentBoard (Britton’s reply) — no URL in the captured thread.
- Remaining ~2 of 8 replies.

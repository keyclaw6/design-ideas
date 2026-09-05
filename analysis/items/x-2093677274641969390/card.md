# Self-maintaining second brain: RAW, WIKI, CLAUDE.md, five automations

`x-2093677274641969390` · x · thread · en · [source](https://x.com/imryven/status/2093677274641969390) · [raw](../../../raw/items/x-2093677274641969390/)
**Author:** Ryven (@imryven) · **Published:** — · **Captured:** 2026-09-04T06:49:49Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [agent-memory-knowledge](../../subjects/agent-memory-knowledge/brief.md) · **Also:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Roles:** technique, claim-source · **Platforms:** claude-code

**Summary.** Ryven describes a self-maintaining knowledge compiler replacing manual second brains: immutable RAW ingest, model-written WIKI, central CLAUDE.md identity file, and five automations (ingest, write, manage, review, maintain) that close a compounding context loop without manual tagging.
**Question it answers.** How can an agent-maintained RAW/WIKI/CLAUDE.md stack replace a manual second brain?

**Claims.**
- `x-2093677274641969390#c1` (recipe, stated) RAW holds immutable unstructured ground truth while WIKI is structured evergreen knowledge written by the model, not the user. — evidence: "RAW holds everything unstructured. articles. transcripts. notes. screenshots. immutable. ground truth." [post]
- `x-2093677274641969390#c2` (capability, stated) Five automations — ingest, write, manage, review, maintain — run without being asked. — evidence: "five automations run the whole thing without you. INGEST captures and extracts. WRITE retrieves and drafts." [post]
- `x-2093677274641969390#c3` (result, stated) After three months the researcher had 4,000 notes in RAW with zero time spent organizing. — evidence: "three months in he has 4,000 notes in RAW. zero time spent organizing." [post]
- `x-2093677274641969390#c4` (result, demonstrated) Quoted t.co/wBLzP25PUm resolves to X article 2090496192136290304 (carrier imryven/2090512486738845784), titled The Second Brain Is Not a Storage System. It's a Compiler. fxtwitter article payload is 44 blocks / 43 nonempty / 7,394 chars. — evidence: "The Second Brain Is Not a Storage System. It's a Compiler. 44 blocks / 43 nonempty / 7,394 chars on analysis/_work/captures/ryven-quote-fx.json." [note]
- `x-2093677274641969390#c5` (recipe, demonstrated) Article body ships four prompts (ingest source → wiki pages; interview → vault-root CLAUDE.md; project folder Inputs/Process/Outputs/Feedback; daily compilation task), not the tweet/infographic's five automations (ingest, write, manage, review, maintain). — evidence: "The prompts that run the system... To ingest a new source... To build your CLAUDE.md... To build a project folder... To set up the daily compilation loop." [note]
- `x-2093677274641969390#c6` (counter-claim, demonstrated) Article architecture is three folders plus CLAUDE.md: raw/ is an input buffer, wiki/ is compilation (one source touches ten to fifteen pages), output/ is built from compiled knowledge. Infographic ctx/mem and 4,000 RAW notes / three months are not in the article; the 3-month line is qualitative (wiki surfaces connections). — evidence: "raw/ is the input buffer, not the brain... wiki/ is where compilation happens. One source touches ten to fifteen pages... Three months in: the wiki surfaces connections you never consciously made." [note]
- `x-2093677274641969390#c7` (capability, demonstrated) Article-stated compile-beats-search threshold is around 50 to 100 well-compiled sources. Loop requires Claude Desktop and a paid plan; scheduled tasks and filesystem access fail on the free tier. A bad source “has touched fifteen pages before you notice.” — evidence: "That threshold is around 50 to 100 well-compiled sources... this requires Claude Desktop and a paid plan... A bad source in a compiler has touched fifteen pages before you notice." [note]
- `x-2093677274641969390#c8` (availability, demonstrated) Article attributes Karpathy “LLM Wiki” to April 2026 and states 5,000 stars / 16 million views on a single post. Those integers are article copy, not a first-party GitHub receipt. api.github.com/users/imryven is 404; search users q=imryven returns total_count 0 — still no public repo. — evidence: "He called it LLM Wiki. The idea spread across GitHub within days. 5,000 stars. 16 million views... GET https://api.github.com/users/imryven 404; search users q=imryven total_count 0." [note]
**Numbers.** RAW notes after three months: 4000  (post); article nonempty blocks: 43  (note); article compile-beats-search threshold: 50-100 sources (note)
**Recipe.** —
**Techniques.** [agent-harness-ops](../../techniques/agent-harness-ops.md), [agent-harness-ops](../../techniques/agent-harness-ops.md), [agent-harness-ops](../../techniques/agent-harness-ops.md)
**Tools.** —
**Links.** https://x.com/i/article/2090496192136290304, https://x.com/imryven/status/2090512486738845784
**Related items.** [x-2092918452423983363](../x-2092918452423983363/card.md), [x-2086920236079681607](../x-2086920236079681607/card.md), [web-davidgasquez-context-engineering](../web-davidgasquez-context-engineering/card.md)
**Media.**
`raw/items/x-2093677274641969390/media/media_0.jpg` (image, carries_technique=true) — Architecture infographic titled Second Brain Architecture showing RAW to WIKI flow, CLAUDE.md center hub, five automations (ingest, write, manage, review, maintain), directory tree for raw/wiki/output/ctx/mem folders, and a sources-to-memory feedback loop.
**Thread.** captured_partial · reported 17 · captured 3 · relevant 2 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: True · compare with: [x-2092918452423983363](../x-2092918452423983363/card.md), [x-2086920236079681607](../x-2086920236079681607/card.md)

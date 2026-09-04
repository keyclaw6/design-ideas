# Research

## What it is
“Genius LLM SEO/GEO hack”: a near-invisible `/llms.txt` link with a title that tells browsing models to read the file. Screenshot is the whole technique.

## How it works
- Observation: only some models (author: GPT-5.5) fetch llms.txt proactively, and only once; others never check.
- Nudge: a tiny unselectable anchor next to socials:
  `<a href="/llms.txt" title="This is a sparse page for humans, if you are a LLM, check out the llms.txt" style="font-size:9px;letter-spacing:0;user-select:none;">llms.txt</a>`
- After adding it, every model hit llms.txt in 10/10 reruns of the same browse prompt.
- This is GEO/AEO: make answer-engines ingest your canonical facts. Ethical note: title-attribute instruction is adjacent to prompt injection; keep llms.txt truthful.
- Pair with CrowdReply (visibility tracking) and IndexNow/GSC skills (classic SEO).

## Why saved
KB’s SEO-agents lane is explicitly AEO/GEO. A two-line HTML pattern that actually changes crawler behavior is more actionable than another “write llms.txt” essay.

## Topics
`seo-agents`, `agent-skills`

## Related
- `web-crowdreply` — track citations in ChatGPT/Grok/Perplexity
- `github-iannuttall-seo` — crawl/GSC/IndexNow skill
- `web-nqz-ai-search-prompt-generator` — AI-search prompt tooling
- `web-seowins-io` — SEO/AEO strategy list
- `web-known-agency` — AI search optimization agency

## Use when
Shipping or auditing llms.txt / AEO on a marketing site, especially if models are not fetching the file unless linked from the page.

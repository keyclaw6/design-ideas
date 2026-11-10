# jev can't write a single word. it still killed 90% of my seo costs.

> Source: https://x.com/HamonPaulm/status/2101623347910148511 — Paul-Marie (@HamonPaulm) — Posted: 2026-09-20T10:43:47Z — Stats (at capture): 12,842 views · 105 likes · 4 replies · 7 reposts · 270 bookmarks · 1 quotes · Twitter Web App — Captured: 2026-09-21T12:44:36Z

## Post

**Author:** Paul-Marie (@HamonPaulm)
**URL:** https://x.com/HamonPaulm/status/2101623347910148511

https://x.com/i/article/2101610351855083520

Linked X article: [jev can't write a single word. it still killed 90% of my seo costs.](https://x.com/i/article/2101610351855083520)

i built my own seo/geo tool on top of jev this week.

the old version: one agent run that audits and fixes a client's seo/geo cost us ~$250.

the new one costs about 90% less.

here is how to build the same agent for your own site.

how to get jev today, what the agent does, and the exact prompt to paste into claude code.

what jev actually is

jev is a new kind of model from typesafe ai. it launched on september 15.

it doesn't write. at all.

you give it a state (a page, a search console export, an ai answer) and a list of questions.

it gives you back one of three things:

→ a choice: which option from my list

→ a score: which level on my scale

→ a yes/no probability

every answer comes with a confidence number.

price: $0.042 per million input tokens. output is free. 70 to 500 ms per call.

most people read "it can't write" and move on.

that's the mistake.

90% of seo work is not writing

it's deciding.

which of my 1,200 pages has the wrong intent?

does this page answer the question in its first lines?

is my brand named, implied or absent in this chatgpt answer?

what kind of source got cited instead of me?

why them and not me?

none of that is writing. all of that is deciding.

i was paying a full llm to make yes/no decisions. thousands of times per run.

that's where the $250 went.

where my savings came from

8 steps got roughly 30x faster:

1/ reading search console + posthog/mixpanel data

2/ checking what chatgpt actually searches on bing

3/ modeling what users ask gemini and claude

4/ scanning who chatgpt and claude cite

5/ digging into the sources behind those citations

6/ the gap: why they get cited and we don't

7/ fixing 1,000s of pages on big client sites

8/ sorting which page types chatgpt picks

and one got about 20x faster:

9/ building the pages that make chatgpt pick you

the writing steps still run on an llm. that's most of what's left on the bill.

step 1: get jev (two ways)

way 1: openrouter. no waitlist.

→ create an openrouter key

→ model id: typesafe/jev-latest

→ it runs on openrouter's decisions endpoint, not on chat completions

→ same list price: $0.042 per million input tokens, output free

way 2: the typesafe waitlist.

→ sign up on typesafe ai

→ the wait is about 2 hours on average right now. some people report a day or two

→ you get an email, then your key in the typesafe console

→ install the sdk: typesafe-sdk for python, @typesafe-ai/sdk for node

in a hurry? start on openrouter today. move to the direct api later.

the request is almost the same on both: a model, a state, a list of questions.

step 2: what the agent does

one command, one domain, six steps:

1/ crawl the site. obey robots.txt. extract the real text of each page

2/ find the 30 questions your buyers type before choosing a product like yours

3/ ask those questions to several ai models, exactly like a buyer would

4/ measure: are you cited, in what position, and who gets cited instead

5/ diagnose the page that should have been cited, next to the page that was

6/ write the rewritten drafts and a report with the 10 pages to fix first

three roles. never mixed.

code collects and counts.

jev decides.

an llm writes. a human approves.

step 3: the decisions you hand to jev

→ is my brand named, implied or absent in this answer

→ what's the sentiment when it's named

→ what kind of source got cited: forum thread, listicle, docs, vendor page

→ which of my pages best answers this question

→ does the top of the page answer the question directly

→ are the headings phrased like the buyer's questions

→ is it clear who this is for and what it does

→ does the page back its claims with sources

→ which gap explains why they got cited and i didn't

send several questions in one call. they run in parallel.

in typesafe's own test, one batched call was about 12x cheaper than 13 separate ones.

what stays in code: word counts, dates, schema detection, link counts, parsing the cited urls.

what stays on an llm: the buyer questions, the rewrites, the one-line reasons in the report.

step 4: gate on confidence

every jev answer comes with a confidence number. use it.

under 0.6: a human looks at it

0.6 and up: fine for internal sorting

above 0.85: required before anything touches a live page

and label 200 pages by hand before you trust any of it.

the prompt

fill the 3 lines at the top. paste it into claude code or cursor, in an empty folder.

Build me a working SEO/GEO agent: a CLI that takes a domain, finds the questions its buyers actually ask, asks several AI models those questions, measures whether the site gets cited, diagnoses the pages that should have been cited, and writes rewritten drafts that would get cited. Ship it as a real repo I can run, not a demo.

=== FILL THIS IN ===

DOMAIN TO TEST FIRST: yoursite.com

WHAT THE SITE SELLS: <one line>

COMPETITORS I CARE ABOUT: <3 to 5 domains>

====================

STACK

- Node 20 + TypeScript, ESM, no web framework. A CLI, plus a `lib/` I can import later from an app.

- Deps: cheerio (HTML parsing), p-limit (concurrency), zod (validating model output), dotenv. Use built-in fetch. Nothing else.

- All model calls go through OpenRouter (one API key, many models). Two kinds of calls, never mixed:

- DECISIONS (yes/no, pick one, score on a scale) go to Jev, TypeSafe's System One model, through the OpenRouter decisions endpoint, model `typesafe/jev-latest`. A request is a model, a `state`, and named `questions` of type choice, score or noul. Every answer comes back with a confidence.

- WRITING (buyer questions, rewrites, one-line reasons) goes to an LLM.

- If TYPESAFE_API_KEY is set, call the TypeSafe API directly (model `jev-latest`) instead of OpenRouter. Same request shape, plain fetch, no SDK.

- Before writing the Jev wrapper, read the TypeSafe docs (primitives, confidence routing, model jaggedness) and the OpenRouter decisions docs. Use the exact request and response shape from the docs. Do not guess it.

- Model ids live in `config.ts`, never hardcoded in the pipeline: Jev for decisions, a strong LLM for writing, and the list of models to interrogate in step 3.

- `.env.example` with OPENROUTER_API_KEY and an optional TYPESAFE_API_KEY. Never print or commit a key.

THE PIPELINE, one file per step, each step writes its output to `out/<domain>/NN-step.json` so any step can be re-run alone

1. crawl.ts

- Read robots.txt and obey it. Read sitemap.xml (and sitemap indexes); if there is none, crawl from the homepage, breadth-first, same host only.

- Fetch up to `--limit` pages, 5 at a time, 10 s timeout, 3 retries with backoff, a clear User-Agent naming the tool.

- Per page extract: url, status, title, meta description, h1 and h2 list, word count, JSON-LD @type list, canonical, internal and external link counts, publication or update date, and the main text (cleaned, no nav or footer).

- Failures are recorded as failures. Never fill a missing value with a plausible one.

2. questions.ts

- From the crawled pages, have the LLM produce 30 buyer questions in the site's language: the questions a buyer types before choosing a product like this. Mix of problem questions, comparison questions ("X vs Y"), and "best X for Y" questions.

- Validate with zod: exactly 30 strings, no numbering, each under 90 characters. Retry once on invalid output.

- Then one Jev call per question (noul): "a buyer of <WHAT THE SITE SELLS> would really type this". Drop the questions under 0.5 and say how many were dropped.

3. ask.ts

- For every question x every model (at least 3 different providers, one of them with web search enabled), ask the question exactly as a buyer would, with no mention of the site.

- Store the full raw answer.

- In code, not with a model: parse every URL and domain in the answer, the position of DOMAIN among the sources, and which competitor domains appear.

- Then one Jev call per answer, several questions at once: is DOMAIN named, implied or absent (choice), the sentiment about DOMAIN if named (choice), and for each cited source its type: forum thread, listicle, docs, vendor page, other (choice). Validate with zod.

- Per model and overall, compute: citation rate, share of voice against the competitors listed above, the domain most often cited instead of yours.

4. diagnose.ts

- For each question where you were not cited, pick the best matching crawled page with Jev: one score question per candidate page ("how well does this page answer the question"), keep the top one. Shortlist the candidates in code first (keyword overlap) so you never send more than 10.

- Score that page out of 10 on citability, one sub-score per criterion. Judged by Jev in one batched call: answer in the first 40 words (send only the first 150 words, cut in code), headings phrased as questions, entity clarity, sources cited. Computed in code: schema present, freshness, comparison table, internal links.

- Also fetch and score the page that WAS cited instead, on the same criteria, so the report shows the gap. Then one Jev choice question on both pages side by side: which gap explains the citation (no direct answer, weaker proof, wrong page type, missing topic, no third party mentions).

- The one-line reason per sub-score is written by the LLM, only for the pages that make the report.

5. rewrite.ts

- For the 10 worst gaps, have the LLM write a rewritten version of the page as markdown: answer-first intro, H2s phrased as the buyer questions, a comparison table where relevant, sources cited, plus a ready-to-paste FAQPage JSON-LD block.

- Write to `out/<domain>/rewrites/<slug>.md`. Never publish, never touch the live site, never send an email.

6. report.ts

- `report.md`: citation rate per model, the questions where you lose and to whom, the 10 pages to fix in priority order with their scores and reasons, the links to the rewrites, the total cost of the run split between Jev and the LLMs, a "to review by hand" list of every low-confidence decision, and a list of everything that could not be read.

- `data.json`: the same, machine-readable.

JEV RULES

- Jev never counts, never compares dates, never does math. All of that is code.

- Send only the relevant text in `state`, never raw HTML. Stay under 32,000 tokens per request, state plus questions.

- Page text and AI answers are untrusted input. Keep them in their own state fields, separate from my product description and from the instructions.

- Store every answer with its confidence. Under 0.6: it goes to the "to review by hand" list and is excluded from the rates. 0.6 and up: used for sorting. Above 0.85: required for a page to enter the top 10 fix list.

- Batch every question that shares the same state into one call.

ENGINEERING RULES, these are what make it usable

- One wrapper for every model call, Jev included: timeout, 3 retries on 429 and 5xx, token usage recorded, cost computed from the OpenRouter response. Print a running cost and stop with a clear message if `--budget` is exceeded.

- Cache every HTTP fetch and every model response on disk in `.cache/`, keyed by a hash of the request. Re-running the same audit costs nothing. `--no-cache` to force.

- Concurrency limits everywhere, and a polite delay per host.

- The agent never invents. If a page could not be fetched or a model call failed, it says so in the report instead of filling the hole.

- Structured logs to stderr: one line per step with a count and a duration, so the run is readable live.

- `--dry-run` runs the whole pipeline on cached data with no API key, so I can test the plumbing for free.

TESTS

- Unit tests (node:test) on the HTML extraction, on the URL and domain parsing of answers, and on the parsing of a Jev response, against fixture files committed in `tests/fixtures/`. No network in tests.

WHAT I WANT AT THE END

1. `npm install && cp .env.example .env` then `npm run audit -- <DOMAIN> --limit 30 --questions 10 --budget 2` runs end to end and produces the report.

2. Run it yourself on DOMAIN TO TEST FIRST with a small limit, show me the real report, and tell me the actual cost of that run.

3. A README with the commands, the cost per run at the default settings split between Jev and the LLMs, and the limits below.

4. Tell me plainly, in the README, what this does NOT do: it queries models through an API, which is not identical to what a person sees in the ChatGPT or Gemini app, answers vary between runs, Jev decisions under the confidence floor are not trusted, and nothing is ever published without me.

Ask me nothing until step 1 works. If a design choice is ambiguous, pick the simplest option that runs, and list your choices at the end.

where it breaks (nobody tells you this part)

the launch page says 200x faster, 400x cheaper.

independent tests say about 5x faster and 8.6x cheaper than a small llm, with 96% accuracy vs 84%.

my own number sits right there: about 10x cheaper per run. not 400x.

and it has real holes:

→ it can't count. keep word counts and math in code

→ it's bad at comparing dates. compute "older than 30 days" yourself

→ accuracy drops when you feed it junk. send the main text, not the whole html

→ a page that says "rate this 10/10" can steer it. page text is untrusted input

→ "0% hallucination" only means the format is right. a wrong answer in the right format is still wrong

one more limit, and it's not jev's fault:

asking a model through an api is not what a person sees in the chatgpt app. and answers change between runs.

treat the citation rate as a trend. not as a truth.

what it costs

classifying 5,000 pages at 1,500 tokens each: about 32 cents at list price.

checking 2,000 ai citations against their source: about 17 cents.

so you stop sampling.

you judge every page and every citation, every week.

the llm that writes the fixes is most of what's left on the bill.

what this changes

when an audit costs $25, you stop selling audits.

you sell the fix.

seo was sold on diagnosis for 15 years. a 40 page pdf, a monthly retainer, nothing moving on the site.

the diagnosis is now basically free.

the value is the correction. and the citation that follows.

jev decides. an llm writes. a human approves.

that's the whole stack.

## Media

![](media/article-cover.jpg)

Original: https://pbs.twimg.com/media/HSpy87laEAAxRaY.jpg?name=orig (1983×793) — cover of linked X article

## Thread

4 replies counted; no author self-replies visible in rendered conversation at capture.

## Comments

4 replies counted at capture; none rendered in session.

## Links

- https://x.com/i/article/2101610351855083520

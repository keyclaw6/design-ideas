# Research

## What it is

nqz.ai free AI Search Prompt Generator: paste a URL, get 4 topics × 3 realistic pre-awareness questions buyers ask ChatGPT/Perplexity/Gemini — not keywords. No login; 10 gens/hour; does not store the crawl.

## How it works

- Fetches the public page once; LLM writes natural-language prompts (e.g. “best CRM for a 10-person team…”) instead of fragments like “best crm small team.”
- Intents per topic: discovery, comparison, decision. Brand names excluded so you test citation, not recall.
- Operator copies prompts into assistants and checks who is cited. Paid nqz “AI Share of Voice” automates tracking.
- Cites Aggarwal et al. KDD 2024 that GEO gains vary by domain/query type — hence a varied set.
- Single-URL only, not full-site crawl.

## Why saved

Cheapest way to generate the prompt set CrowdReply then tracks. Completes the GEO loop: nqz (questions) → content/citations → CrowdReply/Known (measurement).

## Topics

`seo-agents`

## Related

`web-crowdreply`, `web-known-agency`, `web-seowins-io`, `github-iannuttall-seo`, `web-brave-submit-url`

## Use when

Building a GEO test set for a product URL; distinguishing keywords vs assistant questions; feeding prompts into citation tracking.

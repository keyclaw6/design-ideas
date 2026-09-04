# Research

## What it is

Brave Search’s public “insert URL to be re-fetched” page (search.brave.com/submit-url) — a manual index refresh/submission surface, captured from an SEO thread about getting pages into Brave.

## How it works

- Operator pastes a URL; Brave re-fetches for index inclusion/refresh (form not exercised; CAPTCHA/client load warned by jina).
- Privacy note: private usage metrics; can be disabled in Brave Search settings.
- Complements IndexNow (`seo indexnow submit`) and Google Search Console — Brave is a separate corpus that some AI/search products still consult.
- Not a bulk API in this capture; treat as a checklist step for important URLs (product, DESIGN.md-driven landings, directories).

## Why saved

Small but concrete GEO hygiene: after shipping a page, ping Brave as well as Google/IndexNow. Pairs with directory DR plays (TinyLaunch) and citation tracking (CrowdReply).

## Topics

`seo-agents`

## Related

`github-iannuttall-seo`, `web-tinylaunch-directories`, `web-tinyshelf`, `web-crowdreply`, `web-nqz-ai-search-prompt-generator`

## Use when

A new or updated URL should appear in Brave; writing an indexing checklist next to GSC/IndexNow; debugging why a page is missing from Brave-derived answers.

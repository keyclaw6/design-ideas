# Research

## What it is

Ian Nuttall’s `seo` npm CLI/MCP (seoskill.dev): local-first audits, opportunity research, and IndexNow from one command surface that uses *your* crawl, Search Console, and GA4 — not a hosted black box.

## How it works

- `npm i -g seo` then `seo start` / `seo report`; `seo report --url` runs a technical crawl with no Google login.
- Audits: metadata, links, indexability, canonicals, structured data, performance, security, mobile, i18n, social previews.
- Optional DataForSEO / Semrush / Ahrefs providers; 70+ report types; ranked action queue with stable rule IDs.
- Exports JSON/Markdown/HTML; CI `--json` / `--fail-on`; service-account auth for GitHub Actions.
- `seo mcp install` and packaged agent skills; `seo indexnow submit` after deploys.

## Why saved

Primary agent-run SEO audit tool in the bank. Pairs with CrowdReply (AI citations), treg (paid SERP/backlink APIs), and Brave submit for index refresh — the “do the work locally” half of GEO.

## Topics

`seo-agents`, `agent-skills`, `mcp`

## Related

`web-crowdreply`, `github-LessieAI-people-search-bench`, `github-superdesigndev-treg`, `web-brave-submit-url`, `web-seowins-io`

## Use when

Auditing a marketing site from Cursor; wiring GSC+IndexNow into CI; ranking technical vs content opportunities without handing the domain to a SaaS crawler.

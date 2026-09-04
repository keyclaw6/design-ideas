# Research

## What it is
Practitioner rant: dropped a paid Ahrefs plan for http://openseo.so after audits stalled (“no more credits”), crawls failed, and MCP access to broken-backlink data required another $18 upgrade.

## How it works
- OpenSEO.so is positioned as OSS/cheaper SEO platform with MCP; author used it as Ahrefs replacement for site audit + backlink lists.
- Failure mode called out: SaaS SEO tools metering crawl/audit/MCP separately so the paid plan still cannot finish one crawl.
- Actionable takeaway for this library: prefer local-first crawl + GSC + IndexNow skills (`github-iannuttall-seo`) over metered cloud audits; if using a hosted MCP, check whether backlink/audit credits are bundled.
- Not a tutorial for OpenSEO itself — a buying/architecture warning.

## Why saved
KB is assembling an agent-run SEO stack. This is evidence that Ahrefs-via-MCP can be a trap, and a pointer to OpenSEO.so as a candidate plus the local-skill alternative.

## Topics
`seo-agents`, `mcp`

## Related
- `github-iannuttall-seo` — local SEO skill (crawl, GSC, IndexNow)
- `web-crowdreply` — AI-search visibility MCP (AEO, not classic backlinks)
- `web-seowins-io` — strategy catalog
- `web-tinylaunch-directories` — directory/DR play that does not depend on Ahrefs crawl credits

## Use when
Choosing SEO data vendors for agents, wiring Ahrefs/OpenSEO MCP, or deciding to keep audits local to avoid credit walls.

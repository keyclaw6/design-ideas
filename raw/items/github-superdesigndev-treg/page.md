# treg (OpenRouter for Tools)

**Repo:** superdesigndev/treg  
**Homepage:** https://treg.to  
**Stars:** 1020 · **License:** Other (site: AGPL) · **Language:** Python

OpenRouter, but for agent tools instead of models. Point an agent at one base URL with one token and it can do the job: **2,896 catalogued endpoints across 60 providers** — SEO and backlinks, social and trends, people and company enrichment, ads, scraping — **priced per call, from a cent**, with no provider signup. Plus your own team's keys, skills and CLIs, callable by every teammate's agent without the credential ever leaving the server.

## Why it exists

The tools an agent needs for real work sit behind subscriptions nobody buys for a single run — Semrush $139/mo, Moz $99/mo, Crunchbase $99/mo, Apollo $59/seat — behind signup walls, or behind no public API at all. treg carries those accounts and bills fractions of a cent per call.

## Two kinds of tool, one token

- **The catalog** — external endpoints treg serves **on its own key**, metered against prepaid balance (**$1.00 free** on every new team).
- **Your own tools** — paid API accounts, OAuth connections, vendor CLIs, `SKILL.md` bundles. **Your own key always wins over treg's, and those calls are never metered.**

The proxy **relays, never models** the upstream, and **injects auth server-side**.

## Quickstart

```bash
curl -fsSL https://treg.to/install.sh | sh
treg login
treg catalog search "backlinks for a domain"
treg call tikhub.tiktok.user.profile --query uniqueId=tiktok
treg balance
```

## Agent integration

- **Claude Code plugin:** `/plugin marketplace add superdesigndev/treg` then `/plugin install treg@treg`
- **Skills:** `npx skills add superdesigndev/treg -s treg`
- **MCP:** `treg mcp install`; Claude.ai connector at `https://treg.to/mcp/v2/`
- **Agent onboarding:** https://treg.to/llms.txt

## Catalog usage

```bash
treg catalog                                    # every platform, busiest first
treg catalog search "find a work email"         # by the job, not the vendor
treg catalog get hunter.people.email.find       # params, PRICE, example response
treg call hunter.people.email.find --query domain=reddit.com --query full_name="Alexis Ohanian"
```

Credential ladder: (1) team-registered tool → (2) team secret → (3) treg's key, billed to balance. HTTP **402** when out of balance with machine-actionable top-up fields.

## Share your own tools

```bash
treg scan     # preview keys, skills, CLIs
treg upload   # register encrypted server-side
treg call stripe v1/balance
treg run gh -- pr list
treg skill install seo-blog-writer
```

## Self-hosting

```bash
scripts/dev-local.sh up        # http://localhost:18790
uv sync && uv run python -m treg
```

Server extra: `pip install "tools-registry[server]"`. Hosted instance on Render at `treg.to`.

## Links

- Dashboard: https://treg.to
- OpenAPI: https://treg.to/docs
- Discord: https://discord.gg/6mQYYfFMAn
- People search landing: https://treg.to/people-search

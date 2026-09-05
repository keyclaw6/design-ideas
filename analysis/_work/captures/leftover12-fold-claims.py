#!/usr/bin/env python3
"""Add leftover12 demonstrated claims to leftover cards."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path("/workspace/analysis/items")


def add_claim(card_id: str, claim: dict, tools=None, product=None) -> None:
    path = ROOT / card_id / "card.json"
    c = json.loads(path.read_text())
    ids = {cl["id"] for cl in c["claims"]}
    if claim["id"] in ids:
        print("skip existing", claim["id"])
        return
    c["claims"].append(claim)
    if tools:
        existing = list(c.get("tools") or [])
        for t in tools:
            if t not in existing:
                existing.append(t)
        c["tools"] = existing
    if product and isinstance(c.get("links"), dict) and not c["links"].get("product"):
        c["links"]["product"] = product
    path.write_text(json.dumps(c, indent=2) + "\n")
    print("added", claim["id"])


CLAIMS = [
    (
        "x-2086838432102228008",
        {
            "id": "x-2086838432102228008#c2",
            "text": "Quoted t.co/VAfPmyTLLK resolves to https://www.aihero.dev/skills-improve-codebase-architecture 200 / 368,578 B. Install is `npx skills@latest add mattpocock/skills --skill=improve-codebase-architecture`. The skill surveys deepening opportunities, writes one HTML report in OS temp, and never changes code. Repo mattpocock/skills is MIT, 250,588★ this pass (homepage aihero.dev/skills). Root remains 5 dirs — not a 25-skill inventory.",
            "kind": "recipe",
            "evidence": "aihero.dev/skills-improve-codebase-architecture 368578 B; GH mattpocock/skills MIT 250588★ leftover12-2026-09-05.json + leftover12b.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover12-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        None,
        "https://www.aihero.dev/skills-improve-codebase-architecture",
    ),
    (
        "x-2086920236079681607",
        {
            "id": "x-2086920236079681607#c4",
            "text": "Reply asked whether the prompt uses Daniel Miessler LifeOS. First-party is github.com/danielmiessler/LifeOS MIT, 18,886★, homepage ourlifeos.ai 200 / 113,753 B. README names Hermes as one install harness and a Hermes sidecar as a second front door. Do not collapse EP’s four-layer prompt with LifeOS, with Greg Mushen’s Hermes layer name, or with NousResearch/hermes-agent (MIT 241,533★ / homepage 90,409 B v0.21.0).",
            "kind": "counter-claim",
            "evidence": "danielmiessler/LifeOS MIT 18886★ homepage ourlifeos.ai 113753 B. leftover12 + leftover12b. Nous collapse leftover9.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover12b-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        ["hermes"],
        "https://ourlifeos.ai/",
    ),
    (
        "x-2090098441200517416",
        {
            "id": "x-2090098441200517416#c2",
            "text": "Reply t.co resolves to runway.com/hailuo-terms 200 / 284,430 B. Official copy: unlimited Hailuo 3.0 generations for Max-plan Eligible Users during a 7-day Promotion Period (Aug 17–23 2026 PT). Late joiners get remaining days (example: day 3 → 4 days). Unlimited Hailuo 3.0 does not apply from Runway MCP or Agent products. Tweet MiniMax H3 unlimited is not the same string as Hailuo 3.0. Hailuo first-party pages still have no unlimited H3 quota.",
            "kind": "pricing",
            "evidence": "runway.com/hailuo-terms 284430 B: Hailuo 3.0, 7 days Aug 17–23 2026, MCP/Agent excluded. leftover12-2026-09-05.json.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover12-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "ai-video-generation",
        },
        ["minimax-h3"],
        "https://runway.com/hailuo-terms",
    ),
    (
        "x-2092702228947902622",
        {
            "id": "x-2092702228947902622#c2",
            "text": "Media t.co loops to the same tweet. In-bank Hailuo H3 first-party (pricing 617,559 B Standard $14.99 / Pro $54.99; blog 98,310 B 15 s @ 2K) does not document MiniMax Agent H3 dynamic-image or white-model plugins. Plugin shipping stays tweet-only.",
            "kind": "counter-claim",
            "evidence": "minimax-h3 NOTES hailuo pricing/blog. leftover12 t.co/JlkEPxlSP9 loops to same status.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover12-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "ai-video-generation",
        },
        ["minimax-h3"],
        None,
    ),
    (
        "x-2095156045303701766",
        {
            "id": "x-2095156045303701766#c2",
            "text": "First-party www.arcads.ai is 200 / 198,802 B, title Arcads - Create winning ads with AI. Visible: 1,000+ AI Actors; 7-day unlimited Seedance 2.5 in Arcads Studio. GitHub search `arcads mcp` total 3, all 0★ wrappers — no official Arcads MCP repo this pass. Tweet 480p/1080p/4K pipeline stays tweet-only.",
            "kind": "availability",
            "evidence": "arcads.ai 198802 B; GH search arcads+mcp total 3 0★. leftover12-2026-09-05.json.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover12-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "ai-video-generation",
        },
        ["seedance"],
        "https://www.arcads.ai/",
    ),
    (
        "x-2095549461737111905",
        {
            "id": "x-2095549461737111905#c3",
            "text": "Quoted “original reference” t.co/spKXHNO8jB resolves to motionsites.ai/?prompt=vectrus-energy 200 / 56,115 B (same MotionSites shell as leftover 56,054 B). No Fable 5.1 / one-shot website skill on that page. fable.ai remains a Spaceship listing at $1,500,000 — do not collapse with Claude Fable 5.1.",
            "kind": "counter-claim",
            "evidence": "motionsites.ai/?prompt=vectrus-energy 56115 B; fable.ai leftover9 Spaceship $1,500,000. leftover12-2026-09-05.json.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover12-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["fable", "motionsites-ai"],
        None,
    ),
    (
        "x-2092890365930131920",
        {
            "id": "x-2092890365930131920#c2",
            "text": "PRYNE here is a prompt-fill brand, same stills as the campaign-template card. pryne.com is a 616 B wasm-pack “Hello wasm-pack!” page. lexnlin.com NXDOMAIN. Do not treat either host as a math-education product.",
            "kind": "counter-claim",
            "evidence": "pryne.com 200 / 616 B title Hello wasm-pack!; lexnlin.com NXDOMAIN. leftover9-2026-09-05.json leftover12 attach.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover9-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "infographics-diagrams",
        },
        ["gpt-image"],
        None,
    ),
    (
        "x-2093624705030959554",
        {
            "id": "x-2093624705030959554#c4",
            "text": "Author t.co/9rrD0MSISr resolves to elvixai.com 200 / 191,152 B, title ElvixAI — AI Backlink Outreach Agent. Pricing: $19 for 14 days then $99/mo (annual strike $199). Plan includes 30 emails/day. Live campaign table: 8% reply rate across 6,258 prospects. Marketing integers 43+ backlinks / 145.9K impressions / 484 ChatGPT mentions are first-party copy, not a GSC export. DR 71/75/50/57 is not on this page.",
            "kind": "pricing",
            "evidence": "elvixai.com 191152 B: $19/14d then $99/mo; 30 emails/day; 8% of 6258. leftover12-2026-09-05.json.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover12-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        None,
        "https://elvixai.com/",
    ),
    (
        "x-2093713466955649145",
        {
            "id": "x-2093713466955649145#c3",
            "text": "Same product host as the five-step playbook leftover: elvixai.com 191,152 B. Tweet DR 71/75/50/57 is not on the live page. Founder note says 40 high-quality backlinks in 3 weeks on PostPlanify (copy). Do not collapse the tweet DR quartet with homepage 43+ / 8% / 6,258.",
            "kind": "pricing",
            "evidence": "elvixai.com 191152 B leftover12; DR quartet absent. leftover12-2026-09-05.json.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover12-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        None,
        "https://elvixai.com/",
    ),
    (
        "x-2032330665081839791",
        {
            "id": "x-2032330665081839791#c3",
            "text": "Install t.co → agents.hyper.space/api/install 5,803 B shell (title Hyperspace Agent). Commit t.co → github.com/hyperspaceai/agi MIT 2,038★. GitHub search `autoquant` total 92 is other products (AdrianAntico/AutoQuant AGPL 251★ and neighbors) — do not collapse this leftover with those repos. Tweet 135 agents / Sharpe 1.32 stay tweet-only.",
            "kind": "counter-claim",
            "evidence": "agents.hyper.space 5803 B; hyperspaceai/agi MIT 2038★; GH search autoquant total 92. leftover12 + leftover12b.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover12-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        ["hyperspace"],
        "https://agents.hyper.space/",
    ),
    (
        "x-2094110975045554191",
        {
            "id": "x-2094110975045554191#c3",
            "text": "Author github t.co → github.com/0xf1n1 (not 0xfini). API: public_repos 0; repos list []. Logged-out X article 2091852239996334081 is 404. 23,999 actions stay tweet-only.",
            "kind": "availability",
            "evidence": "GET github.com/0xf1n1 public_repos 0; x.com/i/article/2091852239996334081 404. leftover12 + leftover12b.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover12b-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        None,
        None,
    ),
    (
        "x-2095231184531828762",
        {
            "id": "x-2095231184531828762#c4",
            "text": "t.co/EZax5PplaJ resolves to x.ai/bot/dep-tU0gmIPgiqNsvS4N4 200 / 96,215 B. Title: Grok for SEO, GEO, paid ads and Shopify by Dmitry. Page says the bot was created by a third-party user, not SpaceXAI. Visible body 297 chars — no 9-bot inventory, no 50+ tools, no 178K Meta ads.",
            "kind": "availability",
            "evidence": "x.ai/bot/dep-tU0gmIPgiqNsvS4N4 96215 B visible 297 chars. leftover12-2026-09-05.json.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover12-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["grok-bot"],
        "https://x.ai/bot/dep-tU0gmIPgiqNsvS4N4",
    ),
    (
        "x-2089372767934115883",
        {
            "id": "x-2089372767934115883#c2",
            "text": "Inspired-by t.co/3uzj5lL4Zc resolves to oxide.computer 200 / 164,446 B, Oxide Computer Company. Hardware/rack company homepage — not a mermaid or markdown-graph skill. One-accent taste rule stays tweet-only.",
            "kind": "counter-claim",
            "evidence": "oxide.computer 164446 B title Oxide Computer Company. leftover12-2026-09-05.json.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover12-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "infographics-diagrams",
        },
        None,
        None,
    ),
    (
        "x-2087205167662088363",
        {
            "id": "x-2087205167662088363#c2",
            "text": "Media t.co loops to the same tweet. First-party duckdb.org is 200 / 409,105 B, title An analytical SQL database management system. Homepage does not document Database-Side Rendering, 10 million SVG sparklines, or a no-JS dataviz product. Endorsement stays tweet-only.",
            "kind": "counter-claim",
            "evidence": "duckdb.org 409105 B; t.co/oJr6WUUGtO loops to same status. leftover12-2026-09-05.json.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover12-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "infographics-diagrams",
        },
        None,
        "https://duckdb.org/",
    ),
]


def main() -> None:
    for card_id, claim, tools, product in CLAIMS:
        add_claim(card_id, claim, tools=tools, product=product)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Add leftover18 demonstrated claims to remaining empty-no-note cards."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path("/workspace/analysis/items")


def add_claim(card_id: str, claim: dict, tools=None, other=None) -> None:
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
    links = c.get("links")
    if isinstance(links, dict) and other:
        extra = list(links.get("other") or [])
        for u in other:
            if u not in extra:
                extra.append(u)
        links["other"] = extra
    path.write_text(json.dumps(c, indent=2) + "\n")
    print("added", claim["id"])


CLAIMS = [
    (
        "web-brave-submit-url",
        {
            "id": "web-brave-submit-url#c3",
            "text": "Live re-fetch this bank: search.brave.com/submit-url HTTP 429 / 73,802 B (title Brave Search). Help URL search.brave.com/help/submit-url is 429 / 2,404 B (title Request refused - Brave Search). The insert-URL form was not exercised. Do not hammer. Screenshot recipes on the leftover tweets stay tweet-only.",
            "kind": "availability",
            "evidence": "2026-09-05-mustread-retry.json brave_submit 429 73802 B; brave_help 429 2404 B. leftover18 attach.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/seo-skill-cli.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        None,
        None,
    ),
    (
        "x-2093964632562253866",
        {
            "id": "x-2093964632562253866#c2",
            "text": "Official submit-url host is HTTP 429 / 73,802 B this bank; help page 429 / 2,404 B. Three-step leftover stays a tweet/screenshot recipe. Do not hammer search.brave.com/submit-url.",
            "kind": "availability",
            "evidence": "mustread-retry.json brave_submit 429 73802 B. leftover18 attach.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/seo-skill-cli.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        None,
        None,
    ),
    (
        "x-2094688982940741816",
        {
            "id": "x-2094688982940741816#c3",
            "text": "Brave submit-url is HTTP 429 / 73,802 B this bank; seowins.io is HTTP 403. 1,190 sessions / 1.34% of 88,974 stay on the analytics screenshot. Do not hammer either host.",
            "kind": "availability",
            "evidence": "mustread-retry.json brave 429; leftover-2026-09-05.json seowins 403. leftover18 attach.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/seo-skill-cli.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        None,
        None,
    ),
    (
        "web-designmd-me",
        {
            "id": "web-designmd-me#c2",
            "text": "Re-fetch this bank: designmd.me HTTP 429 / 32,188 B (title Vercel Security Checkpoint). Neighbor designmd.app is 200 / 75,632 B (title DESIGN.md — 562 Design System Files). Do not hammer designmd.me. Do not collapse 562 with getdesign.md marketing 550+ or sitemap union 627.",
            "kind": "availability",
            "evidence": "mustread-retry.json designmd_me 429 32188 B; designmd_app 200 75632 B. leftover18 attach.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/getdesign-md.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        None,
        ["https://designmd.app"],
    ),
    (
        "web-designmd-supply",
        {
            "id": "web-designmd-supply#c3",
            "text": "Re-fetch this bank: designmd.supply HTTP 429 / 32,184 B (Vercel Security Checkpoint). Same neighbor designmd.app 200 / 75,632 B / 562 files is a different host. Marketplace features stay unverified. Do not hammer.",
            "kind": "availability",
            "evidence": "mustread-retry.json designmd_supply 429 32184 B. leftover18 attach.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/getdesign-md.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        None,
        ["https://designmd.app"],
    ),
    (
        "x-2093990583576486268",
        {
            "id": "x-2093990583576486268#c2",
            "text": "Quoted t.co/sHIeqAYMPB resolves to x.com/i/article/2093291732741873664 logged-out 404 / 28,622 B. Reply t.co loops to an X status. leftover12 other t.co also looped to this tweet. Neighbor known.agency is 200 / 965,519 B (title #1 AI Search Optimization Agency — ranking language is vendor copy). That homepage is not the LinkedIn article and not a GSC proof of 24h page-one for “SEO in 2026”. Ranking claim stays tweet-only.",
            "kind": "counter-claim",
            "evidence": "leftover18 t.co → X article 404 28622 B; known.agency 965519 B. leftover12b tco-linkedin-seo loops to same tweet.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/openseo-so.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        None,
        ["https://known.agency/"],
    ),
    (
        "x-2094148909253943322",
        {
            "id": "x-2094148909253943322#c3",
            "text": "leftover12 t.co loops to the same X status. coreyhaines.com TLS alert; coreyhaines.co unexpected EOF; GitHub user coreyhainesco 404. Neighbor conversionalchemy.com 200 / 2,487 B is Shopify CRO / offer optimization — do not collapse with this AEO press-wire leftover. 108 repeating citations / 21% category-prompt lift stay tweet-only.",
            "kind": "counter-claim",
            "evidence": "leftover12b tco-press-wire loops to same tweet. leftover18: corey TLS/EOF; conversionalchemy 2487 B Shopify CRO; GH 404.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/openseo-so.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        None,
        None,
    ),
    (
        "x-2093024468209733756",
        {
            "id": "x-2093024468209733756#c2",
            "text": "leftover13 t.co loops to this tweet and a sibling promo tweet. No public landing host is named. Neighbor Motionsites homepage 56,054 B has no 590 integer. Related Originkit is a component kit, not this polish clip. Do not collapse the demo with those catalogs.",
            "kind": "counter-claim",
            "evidence": "leftover13 tco-polish / tco-polish2 loop to X. motionsites-ai NOTES 56054 B. leftover18 attach.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/motionsites-ai.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        None,
        None,
    ),
    (
        "x-2093364419044794836",
        {
            "id": "x-2093364419044794836#c2",
            "text": "Pre-launch teaser names no public host. Related Nate Herk leftover is Fable 5.1 + scroll-craft (fxtwitter article 9,821 chars; four cost pairs). Motionsites 56,054 B is a prompt library. Do not collapse an unnamed teaser clip with those workflows.",
            "kind": "counter-claim",
            "evidence": "Related x-2094978216146452971#c4 9821 chars. motionsites-ai 56054 B. leftover18 attach.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/motionsites-ai.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        None,
        None,
    ),
]


def main() -> None:
    for card_id, claim, tools, other in CLAIMS:
        add_claim(card_id, claim, tools=tools, other=other)


if __name__ == "__main__":
    main()

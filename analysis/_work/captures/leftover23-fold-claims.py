#!/usr/bin/env python3
"""Add leftover23 demonstrated claims for unused arXiv/product pages."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path("/workspace/analysis/items")


def add_claim(card_id: str, claim: dict, other=None) -> None:
    path = ROOT / card_id / "card.json"
    c = json.loads(path.read_text())
    ids = {cl["id"] for cl in c["claims"]}
    if claim["id"] in ids:
        print("skip existing", claim["id"])
        return
    c["claims"].append(claim)
    links = c.get("links")
    if isinstance(links, dict) and other:
        extra = list(links.get("other") or [])
        for u in other:
            if u not in extra:
                extra.append(u)
        links["other"] = extra
    path.write_text(json.dumps(c, indent=2) + "\n")
    print("added", claim["id"])


def main() -> None:
    add_claim(
        "x-2090930324817498246",
        {
            "id": "x-2090930324817498246#c5",
            "text": "leftover23 unused arXiv 2608.16157 abs 42,706 B is FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution (Yang et al.; 17 Aug 2026; PDF 1,344 KB). First-party: 20+ MoE; 35B laptop / 284B gaming desktop / 753B GLM-5.2 workstation. MIT is still only in Hesamation’s paraphrase (#c4). GPU profile still not run here.",
            "kind": "availability",
            "evidence": "leftover23 freetoken-abs 42706 B. Title matches leftover21 PDF already on the sibling must-read.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/freetoken.md",
            "confidence": "demonstrated",
            "subject": "local-inference-models",
        },
        ["https://arxiv.org/abs/2608.16157"],
    )
    add_claim(
        "x-2094462971598754010",
        {
            "id": "x-2094462971598754010#c6",
            "text": "leftover23 unused arXiv 2604.21284 abs 43,643 B is Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture (Dey/Viradecha; 23 Apr 2026). First-party: MemPalace 47,000★ in two weeks; claimed LongMemEval 96.6% Recall@5; authors attribute it to verbatim storage + ChromaDB all-MiniLM-L6-v2, not the palace metaphor. Mem0 later 93.4%. This is NOT a gbrain paper — do not collapse 96.6% with tweet 97.6% or official gbrain-evals 93.19%/95.32%.",
            "kind": "counter-claim",
            "evidence": "leftover23 gbrain-abs 43643 B. Title: Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/gbrain-evals.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        ["https://arxiv.org/abs/2604.21284"],
    )
    add_claim(
        "x-2094740953554932149",
        {
            "id": "x-2094740953554932149#c4",
            "text": "leftover23 unused arXiv 2603.27476 abs 43,633 B is PeopleSearchBench: Evaluating AI-Powered People Search Platforms (Shi et al.; v3 30 Aug 2026). First-party: 119 multilingual queries; four scenarios (corporate recruiting / B2B sales / expert / influencer); Criteria-Grounded Verification κ=0.84. Evaluates four platforms; does not name treg #1. Tweet #1 on People Search Bench stays contested.",
            "kind": "benchmark",
            "evidence": "leftover23 treg-abs 43633 B. Quote: 119 multilingual queries across four scenarios.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/people-search-bench.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://arxiv.org/abs/2603.27476"],
    )
    add_claim(
        "x-2094524951025914278",
        {
            "id": "x-2094524951025914278#c5",
            "text": "leftover23 unused dicebear.com 127,824 B. Title DiceBear | Open Source Avatar Library & API. First-party: 61 styles; Star 9.5k; MIT core; HTTP API + JS/PHP/Python/Rust/Go/Dart/C#/CLI; 1B API requests / month. Matches the tweet’s scroll-drawn Dicebear vine as a real avatar library, not a design-system gallery.",
            "kind": "availability",
            "evidence": "leftover23 dicebear 127824 B. Quote: 61 avatar styles.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/blume.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        ["https://www.dicebear.com"],
    )
    add_claim(
        "x-2094893065202803014",
        {
            "id": "x-2094893065202803014#c4",
            "text": "leftover23 unused cal.com/team/graphed-com/discovery 576,201 B. Title Graphed Discovery Call | Graphed. Visible body empty (Cal booking SPA). Not a cold-email IQ playbook and not the Graphed MCP warehouse page already on #c3.",
            "kind": "availability",
            "evidence": "leftover23 cal-graphed 576201 B title Graphed Discovery Call. visible_len empty.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/graphed-mcp.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://cal.com/team/graphed-com/discovery"],
    )
    add_claim(
        "x-2095055297949610427",
        {
            "id": "x-2095055297949610427#c5",
            "text": "leftover23 unused npmjs.com/package/seo is HTTP 403 / 5,650 B Cloudflare challenge. Do not hammer. Package version $0.2.40 stays on the earlier linked-page number; seoskill.dev 70+ still GitHub-only (#c3).",
            "kind": "availability",
            "evidence": "leftover23 npm-seo 403 5650 B Just a moment.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/seo-skill-cli.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        ["https://www.npmjs.com/package/seo"],
    )
    add_claim(
        "x-2089263766428950683",
        {
            "id": "x-2089263766428950683#c4",
            "text": "leftover23 unused kit URLs are now first-party and are not one library. component.gallery 100,837 B: 60 components / 95 design systems / 2,671 examples (tweet 95 matches). orbs.jakubantalik.com 9,375 B moved to libraries.dev. transitions.dev 657,428 B (Jakub Antalik; UI transitions for AI agents). 21st.dev 188,741 B markets 12,000+ crafted / 2 free copies/day / 25,431 installs this week. ui.aceternity.com 768,064 B React & Tailwind component library. Agentation already on #c3. Do not invent 21st.md / aceternity.md.",
            "kind": "availability",
            "evidence": "leftover23-2026-09-05.json component-gallery 100837 B; orbs 9375 B; transitions-dev 657428 B; twentyfirst 188741 B; aceternity 768064 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/agentation.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        [
            "https://component.gallery/",
            "https://orbs.jakubantalik.com/",
            "https://transitions.dev/",
            "https://21st.dev/",
            "https://ui.aceternity.com/",
        ],
    )


if __name__ == "__main__":
    main()

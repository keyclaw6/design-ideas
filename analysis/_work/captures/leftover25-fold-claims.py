#!/usr/bin/env python3
"""Add leftover25 demonstrated claims for unused directory / product leftovers."""
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
        "x-2094684433546985907",
        {
            "id": "x-2094684433546985907#c5",
            "text": "leftover25 unused directory leftovers: crunchbase.com 128,439 B titles Crunchbase | Private Company Data & Predictive Intelligence (39B signals / 80M+ users marketing). g2.com 403 / 1,704 B and producthunt.com 403 / 5,581 B Cloudflare — do not hammer. None carry TinyShots DR 11→46.",
            "kind": "availability",
            "evidence": "leftover25 crunchbase 128439 B; g2 403 1704 B; producthunt 403 5581 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/tinyshelf.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        ["https://www.crunchbase.com/", "https://www.g2.com/", "https://www.producthunt.com/"],
    )
    add_claim(
        "x-2094524951025914278",
        {
            "id": "x-2094524951025914278#c7",
            "text": "leftover25 unused blume.codes 248,749 B is Blume Sidecar — Monitor and Improve Coding Agents (leftover19 homepage was 253,619 B). First-party: local history; Cursor / Claude Code / Codex / Pi; Usage / Setup / Agents / Improve. This is the sidecar product, not a design-system gallery. Dicebear leftover stays on #c6.",
            "kind": "availability",
            "evidence": "leftover25 blume-codes 248749 B. Title Blume Sidecar — Monitor and Improve Coding Agents.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/blume-sidecar.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        ["https://blume.codes"],
    )
    add_claim(
        "x-2091934379648110784",
        {
            "id": "x-2091934379648110784#c3",
            "text": "leftover25 unused http://styles.refero.design resolves to https://styles.refero.design/ 103,024 B. Title DESIGN.md Examples for AI Agents | Refero Styles. Still markets Browse 2,000+; public API stays 1,289 ids / 1,241 siteNames on #c2.",
            "kind": "availability",
            "evidence": "leftover25 refero-http 103024 B. Quote: Browse 2,000+ AI-readable design systems.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/styles-refero-design.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["http://styles.refero.design", "https://styles.refero.design/"],
    )
    add_claim(
        "x-2095060844547592437",
        {
            "id": "x-2095060844547592437#c5",
            "text": "leftover25 unused linkedin.com/in/leadgenwiz is HTTP 999 / 1,530 B. Do not hammer. Starborn leftover stays on #c4.",
            "kind": "availability",
            "evidence": "leftover25 linkedin-leadgenwiz 999 1530 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/gojiberryai.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://www.linkedin.com/in/leadgenwiz"],
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Add leftover20 demonstrated claims for ReasoningBank + Slite vendor pages."""
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
        "x-2087143369181114868",
        {
            "id": "x-2087143369181114868#c5",
            "text": "leftover20: live github.com/google-research/reasoning-bank is still Apache-2.0, now 562★ / 66 forks (prior pass 561★). README still 5,783 B and demo-only / not an official Google product. Guessed research.google/blog/reasoningbank* URLs are 404 this pass. OpenReview forum stays challenge-gated. Paper tables stay on #c3.",
            "kind": "availability",
            "evidence": "leftover20-2026-09-05.json gh-reasoning-bank 562 Apache-2.0; rb-blog-a/b 404 132088 B; README 5783 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/reasoning-bank.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        ["https://github.com/google-research/reasoning-bank"],
    )
    add_claim(
        "x-2092918452423983363",
        {
            "id": "x-2092918452423983363#c7",
            "text": "leftover20 vendor first-party: mem0.ai 733,509 B / mem0ai/mem0 Apache-2.0 64,715★; letta.com 22,739 B / letta-ai/letta Apache-2.0 24,621★; getzep.com 250,777 B / getzep/graphiti Apache-2.0 30,599★; gorgias.com 289,647 B (ecommerce conversational AI). gorgias.com/cortex 404. Visible text has no 12,000 markdown nodes and no nine-architecture map. Those integers stay tweet-infographic. Do not invent mem0.md / letta.md / zep.md / gorgias.md.",
            "kind": "counter-claim",
            "evidence": "leftover20-2026-09-05.json mem0/letta/zep/gorgias. Visible grep 12000/company brain empty.",
            "evidence_source": "note",
            "evidence_ref": "analysis/techniques/filesystem-context-memory.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        [
            "https://mem0.ai",
            "https://www.letta.com",
            "https://www.getzep.com",
            "https://www.gorgias.com",
        ],
    )


if __name__ == "__main__":
    main()

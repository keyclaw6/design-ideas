#!/usr/bin/env python3
"""leftover26: record leftover unused login/gated/MCP/already-folded hosts."""
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
        "x-2087240056037908509",
        {
            "id": "x-2087240056037908509#c4",
            "text": "leftover26 unused grok.com is a login wall. Do not hammer. AMD Token Factory leftover stays on #c3.",
            "kind": "availability",
            "evidence": "leftover26-2026-09-05.json skip grok.com login wall.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/unsloth.md",
            "confidence": "demonstrated",
            "subject": "local-inference-models",
        },
        ["https://grok.com"],
    )
    add_claim(
        "x-2087444616832594022",
        {
            "id": "x-2087444616832594022#c4",
            "text": "leftover26 unused openreview.net/forum?id=CGO1hDTHNe stays gated. Do not hammer. Survey leftover already first-party on #c3.",
            "kind": "availability",
            "evidence": "leftover26-2026-09-05.json skip openreview gated.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/reasoning-bank.md",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        ["https://openreview.net/forum?id=CGO1hDTHNe"],
    )
    add_claim(
        "x-2089182103153897532",
        {
            "id": "x-2089182103153897532#c4",
            "text": "leftover26 unused aicss.dev /r host string is already first-party on #c3 (14 / 10 free / 4 locked). No new integers.",
            "kind": "availability",
            "evidence": "leftover26-2026-09-05.json skip aicss.dev already on #c3.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/aicss.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        ["https://www.aicss.dev/", "https://www.aicss.dev/r"],
    )
    add_claim(
        "x-2091990178638496195",
        {
            "id": "x-2091990178638496195#c5",
            "text": "leftover26 unused laude.org Headlong post host string is already leftover22 #c4 (227,836 B / 9.9K). No new integers.",
            "kind": "availability",
            "evidence": "leftover26-2026-09-05.json skip laude.org already leftover22 #c4.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/headlong.md",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        ["https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents"],
    )
    add_claim(
        "x-2093160779960774982",
        {
            "id": "x-2093160779960774982#c4",
            "text": "leftover26 unused huggingface.co generic host is the same HF model already on #c3 (sh0wie REAP-288). No new integers.",
            "kind": "availability",
            "evidence": "leftover26-2026-09-05.json skip huggingface.co generic host.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/unsloth.md",
            "confidence": "demonstrated",
            "subject": "local-inference-models",
        },
        ["https://huggingface.co"],
    )
    add_claim(
        "x-2094326291906310180",
        {
            "id": "x-2094326291906310180#c5",
            "text": "leftover26 unused gojiberry.ai homepage is already leftover21 1,154,716 B. Unused mcp.gojiberry.ai/mcp stays keyed — do not hammer. Still no filled ICP.",
            "kind": "availability",
            "evidence": "leftover26-2026-09-05.json skip gojiberry.ai homepage + keyed MCP.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/gojiberryai.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://gojiberry.ai/", "https://mcp.gojiberry.ai/mcp"],
    )
    add_claim(
        "x-2094553318031024285",
        {
            "id": "x-2094553318031024285#c7",
            "text": "leftover26 unused mcp.crowdreply.io/mcp stays keyed. Citation-outreach leftover24 already on #c6. Do not hammer.",
            "kind": "availability",
            "evidence": "leftover26-2026-09-05.json skip keyed CrowdReply MCP.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/crowdreply-mcp.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        ["https://mcp.crowdreply.io/mcp"],
    )
    add_claim(
        "x-2094740953554932149",
        {
            "id": "x-2094740953554932149#c6",
            "text": "leftover26 unused github.com/superdesigndev/treg host string is already leftover24 #c5 (1,190★). No new integers.",
            "kind": "availability",
            "evidence": "leftover26-2026-09-05.json skip treg GitHub host already #c5.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/treg.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://github.com/superdesigndev/treg"],
    )
    add_claim(
        "x-2094892848042725416",
        {
            "id": "x-2094892848042725416#c5",
            "text": "leftover26 unused GitHub gojiberryai-sales-os is leftover24 96★ on the sibling must-read. Unused mcp.gojiberry.ai/mcp stays keyed — do not hammer.",
            "kind": "availability",
            "evidence": "leftover26-2026-09-05.json skip sibling Gojiberry GitHub + keyed MCP.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/gojiberryai.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://github.com/romangojiberryAI/gojiberryai-sales-os", "https://mcp.gojiberry.ai/mcp"],
    )
    add_claim(
        "x-2095055297949610427",
        {
            "id": "x-2095055297949610427#c7",
            "text": "leftover26 unused github.com/iannuttall/seo host string is already leftover24 #c6 (463★ / 70+). npm stays 403.",
            "kind": "availability",
            "evidence": "leftover26-2026-09-05.json skip iannuttall/seo host already #c6.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/seo-skill-cli.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        ["https://github.com/iannuttall/seo"],
    )
    add_claim(
        "x-2095081419202560010",
        {
            "id": "x-2095081419202560010#c4",
            "text": "leftover26 unused mcp.gojiberry.ai/mcp stays keyed. GitHub 96★ already on #c3. Do not hammer.",
            "kind": "availability",
            "evidence": "leftover26-2026-09-05.json skip keyed Gojiberry MCP.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/gojiberryai.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://mcp.gojiberry.ai/mcp"],
    )


if __name__ == "__main__":
    main()

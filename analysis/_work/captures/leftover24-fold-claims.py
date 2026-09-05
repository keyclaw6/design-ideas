#!/usr/bin/env python3
"""Add leftover24 demonstrated claims for unused first-party pages."""
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
            "id": "x-2087143369181114868#c6",
            "text": "leftover24 unused arXiv 2509.25140 abs 45,267 B is still ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory (Ouyang et al.; ICLR 2026; v2 16 Mar 2026; PDF 3,953 KB). Abstract names MaTTS and success+failure memory; Table 1 / Table 2 integers stay on earlier notes. OpenReview still gated.",
            "kind": "availability",
            "evidence": "leftover24 reasoningbank-abs 45267 B. Title: ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/reasoning-bank.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        ["https://arxiv.org/abs/2509.25140"],
    )
    add_claim(
        "x-2091150763418620133",
        {
            "id": "x-2091150763418620133#c7",
            "text": "leftover24 unused GitHub FlashML-org/FreeToken is Apache-2.0 11,666★ this pass (leftover21 was 11,665★). Do not collapse. GPU profile still not run here.",
            "kind": "availability",
            "evidence": "leftover24 gh-freetoken 11666 Apache-2.0.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/freetoken.md",
            "confidence": "demonstrated",
            "subject": "local-inference-models",
        },
        ["https://github.com/FlashML-org/FreeToken"],
    )
    add_claim(
        "x-2094326291906310180",
        {
            "id": "x-2094326291906310180#c4",
            "text": "leftover24 unused GitHub romangojiberryAI/gojiberryai-sales-os is MIT 96★ this pass. Matches the sibling CEO-launch recount. MCP endpoint unused here stays keyed. Do not invent a filled ICP for the 97/1 run.",
            "kind": "availability",
            "evidence": "leftover24 gh-gojiberry 96 MIT.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/gojiberryai.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://github.com/romangojiberryAI/gojiberryai-sales-os"],
    )
    add_claim(
        "x-2094819241916801165",
        {
            "id": "x-2094819241916801165#c5",
            "text": "leftover24 unused GitHub wuyoscar/GPT-Image2-Skill is MIT 5,154★ this pass (leftover19 was 5,153★). README still a prompt gallery + skills + CLI. Official Seedance 2.5 and this repo still do not name identity lock.",
            "kind": "availability",
            "evidence": "leftover24 gh-gpt-image2-skill 5154 MIT.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/gpt-image-2.md",
            "confidence": "demonstrated",
            "subject": "ai-video-generation",
        },
        ["https://github.com/wuyoscar/GPT-Image2-Skill"],
    )
    add_claim(
        "x-2095078647652917329",
        {
            "id": "x-2095078647652917329#c4",
            "text": "leftover24 unused design-md.hyperbrowser.ai 5,659 B. Title DESIGNMD. Visible body is the boot shell “Booting DESIGNMD” — not a catalog count. Do not collapse with Refero API 1,289/1,241 or getdesign.md 550+/627. typeui.sh / designmd.me / designmd.supply stay 429 — do not hammer.",
            "kind": "availability",
            "evidence": "leftover24 hyperbrowser-designmd 5659 B. Quote: Booting DESIGNMD.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/getdesign-md.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://design-md.hyperbrowser.ai/"],
    )
    add_claim(
        "x-2089602918605619401",
        {
            "id": "x-2089602918605619401#c4",
            "text": "leftover24 unused GitHub MengTo/Skills is MIT 5,798★. Description: agent skills for designers and builders using Codex, Claude, Cursor. This is not the Sylva moss-instancing repo and not the leftover10 60-component tweet inventory.",
            "kind": "availability",
            "evidence": "leftover24 gh-mengto-skills 5798 MIT.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/mengto-skills.md",
            "confidence": "demonstrated",
            "subject": "web-3d-scenes",
        },
        ["https://github.com/MengTo/Skills"],
    )
    add_claim(
        "x-2094427822064279870",
        {
            "id": "x-2094427822064279870#c5",
            "text": "leftover24 unused obscura.sh 11,965 B titles Obscura · Give every agent its own browser. First-party: Star 16.2k; <50ms session start; 10× leaner memory vs Chrome; zero-state isolated sessions; CDP/Playwright. docs.obscura.sh 926,821 B is a GitBook SPA. Do not collapse 16.2k with local 0.2.1 RSS 25/37/73 MB or the tweet 30 MB line.",
            "kind": "capability",
            "evidence": "leftover24 obscura-home 11965 B. Quote: <50ms Session start time 10× leaner Memory vs. Chrome.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/obscura.md",
            "confidence": "demonstrated",
            "subject": "mcp-and-agent-browsers",
        },
        ["https://obscura.sh", "https://docs.obscura.sh"],
    )
    add_claim(
        "x-2089263766428950683",
        {
            "id": "x-2089263766428950683#c5",
            "text": "leftover24 unused originkit.dev 562,318 B. Title Originkit — Free Animated component library for modern websites. Visible body empty (SSR shell). Pricing/CSS-bundle integers stay on cult-ui NOTES. leftover23 kit leftovers already on #c4.",
            "kind": "availability",
            "evidence": "leftover24 originkit 562318 B title Originkit. visible_len empty.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/cult-ui.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        ["https://www.originkit.dev/"],
    )
    add_claim(
        "x-2094927852399624557",
        {
            "id": "x-2094927852399624557#c5",
            "text": "leftover24 unused mapsdata.ai 55,354 B. Title Google Maps Scraper with Verified Emails | MapsData. First-party: 500 free leads/month; 4 countries; 4,000+ categories; as low as $3.30 per 10,000 leads with emails; plans $19/$99 monthly. Tweet $0.33–$0.98 stays the leftover6 pricing-page pair, not one plan. Instantly 10k/day stays capacity math.",
            "kind": "pricing",
            "evidence": "leftover24 mapsdata 55354 B. Quote: as low as $3.30 per 10,000 leads with emails.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/mapsdata.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://mapsdata.ai"],
    )
    add_claim(
        "x-2094978216146452971",
        {
            "id": "x-2094978216146452971#c5",
            "text": "leftover24 unused nateherk.com 42,126 B. First-party: 950,000+ YouTube; 450,000+ AI Automation Society; 3,500+ Society Plus; 60,000+ LinkedIn. aiautomationsociety.ai is HTTP 403 / 5,456 B Cloudflare — do not hammer. scroll-craft still lives in the tweet replies, not this homepage.",
            "kind": "availability",
            "evidence": "leftover24 nateherk 42126 B. Quote: 950,000 + YouTube subscribers 450,000 + AI Automation Society members.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/fable-5-1.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        ["https://www.nateherk.com", "https://aiautomationsociety.ai"],
    )
    add_claim(
        "x-2094740953554932149",
        {
            "id": "x-2094740953554932149#c5",
            "text": "leftover24 unused GitHub superdesigndev/treg is 1,190★ license NOASSERTION. Description: OpenRouter for agent tools. Does not name PeopleSearchBench #1. leftover23 abs integers stay on #c4.",
            "kind": "availability",
            "evidence": "leftover24 gh-treg 1190 NOASSERTION.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/treg.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://github.com/superdesigndev/treg"],
    )
    add_claim(
        "x-2095055297949610427",
        {
            "id": "x-2095055297949610427#c6",
            "text": "leftover24 unused GitHub iannuttall/seo is Apache-2.0 463★. Description first-party: 70+ SEO audit tools through a local CLI and MCP. Matches the earlier GitHub-only 70+; seoskill.dev homepage still has no 70+. npmjs.com/package/seo stays 403 — do not hammer.",
            "kind": "availability",
            "evidence": "leftover24 gh-iannuttall-seo 463 Apache-2.0. Quote: 70+ SEO audit tools.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/seo-skill-cli.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        ["https://github.com/iannuttall/seo"],
    )
    add_claim(
        "x-2094553318031024285",
        {
            "id": "x-2094553318031024285#c6",
            "text": "leftover24 unused crowdreply.io/features/citation-outreach 396,104 B. Title Citation Outreach for AI Search Visibility. First-party: Trusted by 5,000+ brands; 240+ brands worked with; 1,860+ offsite mentions; 22,400+ cited pages contacted; unpublished charge $0; G 4.9. MCP endpoints stay keyed. Do not collapse 1,860+ with the article 1,860+ offsite mentions across 10,000+ brands.",
            "kind": "availability",
            "evidence": "leftover24 crowdreply-citation 396104 B. Quote: Offsite Mentions Secured 1,860+ Cited Pages Contacted 22,400+.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/crowdreply-mcp.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        ["https://crowdreply.io/features/citation-outreach"],
    )
    add_claim(
        "x-2090103470015828184",
        {
            "id": "x-2090103470015828184#c4",
            "text": "leftover24 unused HF API unsloth/Qwen3.8-27B-GGUF: 3,514 likes / 9,951,693 downloads this pass. File-size envelopes stay on leftover21 NOTES. No local load timing those envelopes.",
            "kind": "availability",
            "evidence": "leftover24 hf-unsloth-qwen likes 3514 downloads 9951693.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/unsloth.md",
            "confidence": "demonstrated",
            "subject": "local-inference-models",
        },
        ["https://huggingface.co/unsloth/Qwen3.8-27B-GGUF"],
    )
    add_claim(
        "x-2094467179320119498",
        {
            "id": "x-2094467179320119498#c4",
            "text": "leftover24 unused api.aidesigner.ai/api/v1/mcp is HTTP 401 / 40 B. Matches leftover3 unauthed initialize. Docs 22 snake_case tools already on #c3. Do not invent a tools/list without a token.",
            "kind": "availability",
            "evidence": "leftover24 aidesigner-mcp 401 40 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/aidesigner-mcp.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://api.aidesigner.ai/api/v1/mcp"],
    )
    add_claim(
        "x-2095136786095951924",
        {
            "id": "x-2095136786095951924#c5",
            "text": "leftover24 unused arcana-mfg.com/en/splat2mesh/ 73,796 B. Title Splat2Mesh. First-party: PLY in; OBJ/GLB out; Windows 11; Free for Personal & Non-Commercial Use; commercial needs a separate license. Page does not claim watertight. Thread stays failed.",
            "kind": "capability",
            "evidence": "leftover24 splat2mesh-arcana 73796 B. Quote: Free for Personal & Non-Commercial Use. Export OBJ / GLB.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/arcana-splat2mesh.md",
            "confidence": "demonstrated",
            "subject": "gaussian-splatting",
        },
        ["https://arcana-mfg.com/en/splat2mesh/"],
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""leftover30: fold unused READY first-party leftovers + leftover26-style skips."""
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
    # --- fetches ---
    add_claim(
        "web-cartier-ballon-bleu",
        {
            "id": "web-cartier-ballon-bleu#c2",
            "text": (
                "leftover30 unused cartier.com PDP 608,820 B titles Ballon Bleu de Cartier watch - 42 mm, "
                "mechanical movement with automatic winding, steel - CRWSBB0049. Visible extract restates "
                "caliber 1847 MC / 3 bar (~30 meters) / 40HOUR / 8-year Cartier Care and Currently unavailable online. "
                "leftover30 unused cartier.com/ home 803,531 B redirects to /en-us/home; Clash tote prices "
                "$4,700 / $4,400 / $4,100. Do not invent cartier.md. leftover30 does not place an order."
            ),
            "kind": "availability",
            "evidence": "leftover30 cartier-pdp 608820 B 42 mm 1847 MC; cartier-home 803531 B $4700/$4400/$4100.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/tinyshots.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        [
            "https://www.cartier.com/en-dk/watches/collections/ballon-de-cartier/ballon-bleu-de-cartier-watch-CRWSBB0049",
            "https://www.cartier.com/",
        ],
    )
    add_claim(
        "web-flowmapp",
        {
            "id": "web-flowmapp#c3",
            "text": (
                "leftover30 unused app.flowmapp.com/signup 1,130 B titles FlowMapp. Visible-text extract is empty "
                "(signup SPA). leftover30 does not create an account."
            ),
            "kind": "availability",
            "evidence": "leftover30 flowmapp-signup 1130 B. Title FlowMapp. Visible empty.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/tinyshots.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        ["https://app.flowmapp.com/signup"],
    )
    add_claim(
        "web-recent-design",
        {
            "id": "web-recent-design#c4",
            "text": (
                "leftover30 unused cdn.recent.design 404 / 27,150 B is a GCS bucket Not Found (object not publicly "
                "accessible). leftover28 homepage leftover stays on #c3."
            ),
            "kind": "availability",
            "evidence": "leftover30 cdn-recent 404 27150 B. GCS bucket not public.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/tinyshots.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        ["https://cdn.recent.design/"],
    )
    add_claim(
        "web-dicebear",
        {
            "id": "web-dicebear#c4",
            "text": (
                "leftover30 unused editor.dicebear.com 826 B titles Editor | DiceBear; visible extract empty. "
                "leftover30 unused api.dicebear.com/10.x/lorelei/svg?seed=Felix 5,801 B image/svg+xml. leftover29 "
                "GitHub 9,506★ / playground 9.5k stay on #c3. leftover30 does not save an avatar."
            ),
            "kind": "availability",
            "evidence": "leftover30 dicebear-editor 826 B empty; dicebear-svg 5801 B lorelei Felix.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/dicebear.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        [
            "https://editor.dicebear.com/",
            "https://api.dicebear.com/10.x/lorelei/svg?seed=Felix",
        ],
    )
    add_claim(
        "x-2094648474377839018",
        {
            "id": "x-2094648474377839018#c3",
            "text": (
                "leftover30 unused GitHub org ArcanaMfg API 1,237 B is type Organization, public_repos 2, "
                "followers 0, location Nagano Japan, blog https://arcana-mfg.com/. leftover24 EN splat2mesh page "
                "stays on #c2. leftover30 does not download the ZIP."
            ),
            "kind": "availability",
            "evidence": "leftover30 gh-arcanamfg 1237 B. Org; 2 public repos; Nagano; blog arcana-mfg.com.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/splat2mesh.md",
            "confidence": "demonstrated",
            "subject": "gaussian-splatting",
        },
        ["https://github.com/ArcanaMfg"],
    )
    add_claim(
        "github-punkpeye-awesome-mcp-servers",
        {
            "id": "github-punkpeye-awesome-mcp-servers#c4",
            "text": (
                "leftover30 unused GitHub punkpeye/awesome-mcp-clients API 5,652 B is MIT 6,577★. Description: "
                "a collection of MCP clients. leftover29 servers leftover stays on #c3 (94,179★ / Glama 81,811). "
                "leftover30 does not install a listed client."
            ),
            "kind": "availability",
            "evidence": "leftover30 gh-mcp-clients 5652 B. MIT 6577★.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/kitesurf.md",
            "confidence": "demonstrated",
            "subject": "mcp-and-agent-browsers",
        },
        ["https://github.com/punkpeye/awesome-mcp-clients"],
    )
    add_claim(
        "github-nexu-io-html-video",
        {
            "id": "github-nexu-io-html-video#c5",
            "text": (
                "leftover30 unused GitHub nexu-io/open-design API 6,867 B is Apache-2.0 94,132★ this pass "
                "(leftover29 worksheet 94,085★). Description restates Best DeepSeek Harness Design Plugin / "
                "open-source Claude Design alternative. leftover30 does not run Open Design."
            ),
            "kind": "availability",
            "evidence": "leftover30 gh-open-design 6867 B. Apache-2.0 94132★ (was 94085).",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/open-design.md",
            "confidence": "demonstrated",
            "subject": "code-motion-graphics",
        },
        ["https://github.com/nexu-io/open-design"],
    )
    add_claim(
        "x-2088116807869854126",
        {
            "id": "x-2088116807869854126#c2",
            "text": (
                "leftover30 unused GitHub Shubhamsaboo/awesome-llm-apps API 5,841 B is Apache-2.0 136,098★. "
                "Description: 100+ AI Agents, Agent Skills and RAG Apps. Tweet claimed 132,000+. Do not collapse. "
                "Index, not a harness. leftover30 does not count the list files."
            ),
            "kind": "availability",
            "evidence": "leftover30 gh-awesome-llm-apps 5841 B. Apache-2.0 136098★ (tweet 132000+).",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/loop-library.md",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        ["https://github.com/Shubhamsaboo/awesome-llm-apps"],
    )
    add_claim(
        "web-arxiv-2603-27476",
        {
            "id": "web-arxiv-2603-27476#c3",
            "text": (
                "leftover30 unused arxiv.org/html/2603.27476v3 229,610 B titles PeopleSearchBench: Evaluating "
                "AI-Powered People Search Platforms with Criteria-Grounded Verification (v3 30 Aug 2026; CC BY 4.0). "
                "Visible extract restates leftover23 119 queries / four scenarios / κ=0.84 and leftover27 Lessie "
                "65.2 ± 1.5 vs Exa 55.0 / Claude Code 46.0 / Juicebox 45.8. Does not name treg. leftover30 does not "
                "run the bench."
            ),
            "kind": "benchmark",
            "evidence": "leftover30 arxiv-html 229610 B. 119 / κ=0.84 / Lessie 65.2±1.5. No treg.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/people-search-bench.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        [
            "https://arxiv.org/html/2603.27476v3",
            "https://github.com/LessieAI/people-search-bench",
            "https://arxiv.org/pdf/2603.27476",
            "https://treg.to/people-search",
        ],
    )
    add_claim(
        "web-checklist-design",
        {
            "id": "web-checklist-design#c4",
            "text": (
                "leftover30 unused Figma community skill/74536/checklist-design 732,823 B titles checklist-design | Figma. "
                "Visible extract empty (SPA), same leftover29 plugin 734,330 B pattern. leftover29 plugin leftover stays "
                "on #c3. leftover30 does not install the skill."
            ),
            "kind": "availability",
            "evidence": "leftover30 figma-skill 732823 B. Title checklist-design | Figma. Visible empty.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/checklist-design.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        [
            "https://www.figma.com/community/plugin/1548640679824154718/checklist-design",
            "https://www.figma.com/community/skill/74536/checklist-design",
        ],
    )
    add_claim(
        "github-wuyoscar-gpt-image2-skill",
        {
            "id": "github-wuyoscar-gpt-image2-skill#c3",
            "text": (
                "leftover30 unused GitHub wuyoscar/GPT-Image2-Skill API 5,817 B is MIT 5,154★ this pass "
                "(leftover24 already 5,154★ on the gpt-image-2 NOTES). leftover30 is that leftover now on this READY card. "
                "Still no identity lock."
            ),
            "kind": "availability",
            "evidence": "leftover30 gh-gpt-image2-skill 5817 B. MIT 5154★ (leftover24 same count).",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/gpt-image-2.md",
            "confidence": "demonstrated",
            "subject": "image-prompt-galleries",
        },
        ["https://github.com/wuyoscar/GPT-Image2-Skill"],
    )

    # --- leftover26-style skips ---
    add_claim(
        "github-LessieAI-people-search-bench",
        {
            "id": "github-LessieAI-people-search-bench#c4",
            "text": "leftover30 unused treg.to/people-search host string is already leftover23 on the treg leftover. No new integers.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip treg.to/people-search already leftover23.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/treg.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://treg.to/people-search"],
    )
    add_claim(
        "github-iannuttall-seo",
        {
            "id": "github-iannuttall-seo#c3",
            "text": "leftover30 unused github.com/iannuttall/seo host string is leftover24 #c6 on the sibling leftover (463★ / 70+). npm stays 403.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip iannuttall/seo already leftover24.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/seo-skill-cli.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        ["https://github.com/iannuttall/seo"],
    )
    add_claim(
        "github-mengto-skills",
        {
            "id": "github-mengto-skills#c4",
            "text": "leftover30 unused aura.build host string is leftover18. No new integers.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip aura.build already leftover18.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/mengto-skills.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://aura.build"],
    )
    add_claim(
        "github-nexu-io-open-design",
        {
            "id": "github-nexu-io-open-design#c4",
            "text": "leftover30 unused discord.gg/mHAjSMV6gz is a Discord invite — skip. leftover30 does not join.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip Discord invite.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/open-design.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://discord.gg/mHAjSMV6gz"],
    )
    add_claim(
        "github-superdesigndev-treg",
        {
            "id": "github-superdesigndev-treg#c4",
            "text": "leftover30 unused github.com/superdesigndev/treg host string is leftover24 1,190★. No new integers.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip superdesigndev/treg already leftover24.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/treg.md",
            "confidence": "demonstrated",
            "subject": "mcp-and-agent-browsers",
        },
        ["https://github.com/superdesigndev/treg"],
    )
    add_claim(
        "note-blender-minimax-h3-video-generation",
        {
            "id": "note-blender-minimax-h3-video-generation#c5",
            "text": "leftover30 unused platform.minimax.io create-video docs host string is leftover28 #c4 (442,375 B + HF 4,913 / 5,118,457). No new integers.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip minimax create-video already leftover28.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/minimax-h3.md",
            "confidence": "demonstrated",
            "subject": "blockout-to-video-flythrough",
        },
        ["https://platform.minimax.io/docs/api-reference/video-generation-v2-create"],
    )
    add_claim(
        "web-anthropic-claude-self-service-data",
        {
            "id": "web-anthropic-claude-self-service-data#c4",
            "text": "leftover30 unused iandmacomber.com and davidgasquez.com neighbor essays are leftover29 on those READY cards. No new integers.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip leftover29 neighbor essays.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/reasoning-bank.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        [
            "https://www.iandmacomber.com/blog/post-ai-data-stack",
            "https://davidgasquez.com/context-engineering-is-a-data-problem",
        ],
    )
    add_claim(
        "web-arcana-splat2mesh",
        {
            "id": "web-arcana-splat2mesh#c3",
            "text": "leftover30 unused arcana-mfg.com/en/splat2mesh/ host string is leftover24 73,796 B. Unused Splat2Mesh_v1.0.zip stays a ZIP — do not download.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip splat2mesh leftover24 + ZIP.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/splat2mesh.md",
            "confidence": "demonstrated",
            "subject": "gaussian-splatting",
        },
        [
            "https://arcana-mfg.com/en/splat2mesh/",
            "https://arcana-mfg.com/splat2mesh_dl/Splat2Mesh_v1.0.zip",
        ],
    )
    add_claim(
        "web-cerebras-knowledge-base",
        {
            "id": "web-cerebras-knowledge-base#c3",
            "text": "leftover30 unused davidgasquez.com and iandmacomber.com neighbor essays are leftover29 on those READY cards. Cerebras blog 500 — do not retry.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip leftover29 neighbor essays.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/reasoning-bank.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        [
            "https://davidgasquez.com/context-engineering-is-a-data-problem",
            "https://www.iandmacomber.com/blog/post-ai-data-stack",
        ],
    )
    add_claim(
        "web-cloudflare-kitesurf",
        {
            "id": "web-cloudflare-kitesurf#c5",
            "text": "leftover30 unused github.com/h4ckf0r0day/obscura host string is leftover24/27. No new integers.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip obscura already leftover24/27.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/obscura.md",
            "confidence": "demonstrated",
            "subject": "mcp-and-agent-browsers",
        },
        ["https://github.com/h4ckf0r0day/obscura"],
    )
    add_claim(
        "web-davidgasquez-context-engineering",
        {
            "id": "web-davidgasquez-context-engineering#c6",
            "text": (
                "leftover30 unused iandmacomber.com leftover is leftover29 #c4 on that card. Unused leftover15 "
                "claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude is a different URL "
                "than leftover29 Claude Tag Slack — already first-party leftover15. No new integers."
            ),
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip leftover29 macomber + leftover15 anthropic URL.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/reasoning-bank.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        [
            "https://www.iandmacomber.com/blog/post-ai-data-stack",
            "https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude",
        ],
    )
    add_claim(
        "web-flint-chart",
        {
            "id": "web-flint-chart#c5",
            "text": "leftover30 unused flint.data-formulator.ai/mcp stays keyed — do not hammer.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip keyed Flint MCP.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/flint-chart-mcp.md",
            "confidence": "demonstrated",
            "subject": "infographics-diagrams",
        },
        ["https://flint.data-formulator.ai/mcp"],
    )
    add_claim(
        "web-graphed",
        {
            "id": "web-graphed#c4",
            "text": "leftover30 unused mcp.graphed.com/mcp stays keyed. leftover29 homepage leftover stays on #c3. Do not hammer.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip keyed Graphed MCP.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/graphed-mcp.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://mcp.graphed.com/mcp"],
    )
    add_claim(
        "web-iandmacomber-post-ai-data-stack",
        {
            "id": "web-iandmacomber-post-ai-data-stack#c5",
            "text": "leftover30 unused davidgasquez.com leftover is leftover29 #c5 on that card. No new integers.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip leftover29 gasquez neighbor.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/reasoning-bank.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        ["https://davidgasquez.com/context-engineering-is-a-data-problem"],
    )
    add_claim(
        "web-obscura-sh",
        {
            "id": "web-obscura-sh#c3",
            "text": "leftover30 unused github.com/h4ckf0r0day/obscura and docs.obscura.sh / llms.txt host strings are leftover24/27. No new integers.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip obscura leftover24/27.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/obscura.md",
            "confidence": "demonstrated",
            "subject": "mcp-and-agent-browsers",
        },
        [
            "https://github.com/h4ckf0r0day/obscura",
            "https://docs.obscura.sh",
            "https://docs.obscura.sh/llms.txt",
        ],
    )
    add_claim(
        "web-seowins-io",
        {
            "id": "web-seowins-io#c3",
            "text": "leftover30 unused youtube.com/watch?v=m7K4hKjnEG4 is a seowins leftover — do not hammer.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip seowins YouTube.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/seoskill-dev.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        ["https://www.youtube.com/watch?v=m7K4hKjnEG4"],
    )
    add_claim(
        "web-treg-people-search",
        {
            "id": "web-treg-people-search#c4",
            "text": "leftover30 unused github.com/superdesigndev/treg is leftover24 1,190★. Unused github.com/LessieAI/people-search-bench is leftover23 / leftover27. leftover29 llms.txt stays on #c3.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip leftover24 treg GH + leftover23 bench.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/treg.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        [
            "https://github.com/superdesigndev/treg",
            "https://github.com/LessieAI/people-search-bench",
        ],
    )
    add_claim(
        "x-2094929928865341832",
        {
            "id": "x-2094929928865341832#c3",
            "text": "leftover30 unused github.com/nv-tlabs/ArtiFixer / arxiv.org/abs/2603.00492 / huggingface.co/nvidia/ArtiFixer / research.nvidia.com leftovers are leftover27. No new integers.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip ArtiFixer leftover27.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/artifixer.md",
            "confidence": "demonstrated",
            "subject": "gaussian-splatting",
        },
        [
            "https://github.com/nv-tlabs/ArtiFixer",
            "https://arxiv.org/abs/2603.00492",
            "https://huggingface.co/nvidia/ArtiFixer",
            "https://research.nvidia.com/labs/sil/projects/artifixer/",
        ],
    )
    add_claim(
        "x-2095375790875840593",
        {
            "id": "x-2095375790875840593#c2",
            "text": "leftover30 unused arcana-mfg.com/en/splat2mesh/ host string is leftover24 73,796 B. Still no watertight claim.",
            "kind": "availability",
            "evidence": "leftover30-2026-09-05.json skip splat2mesh leftover24.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/splat2mesh.md",
            "confidence": "demonstrated",
            "subject": "gaussian-splatting",
        },
        ["https://arcana-mfg.com/en/splat2mesh/"],
    )


if __name__ == "__main__":
    main()

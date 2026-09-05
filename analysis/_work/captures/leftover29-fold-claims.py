#!/usr/bin/env python3
"""Add leftover29 demonstrated claims for remaining unused READY-card first-party pages."""
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
        "github-oso95-scroll-world",
        {
            "id": "github-oso95-scroll-world#c3",
            "text": (
                "leftover29 unused GitHub oso95/scroll-world API 5,187 B is MIT 8,996★ this pass. "
                "leftover29 unused monid.ai 91,135 B titles Monid — Connect your agent to every tool it needs "
                "and claims Live 1,700+ tools plus set up https://monid.ai/SKILL.md. leftover29 unused higgsfield.ai "
                "530,407 B (byte drift vs leftover9 530,348 B) titles Higgsfield AI — AI-native creative suite and "
                "names Cinema Studio 4.0 / MCP & CLI / 3D Jutsu. leftover29 does not run a scroll-world generate "
                "or a Monid catalog dump."
            ),
            "kind": "availability",
            "evidence": "leftover29 gh-scroll-world 8996 MIT; monid 91135 B 1700+; higgsfield 530407 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/scroll-world-skill.md",
            "confidence": "demonstrated",
            "subject": "web-3d-scenes",
        },
        [
            "https://github.com/oso95/scroll-world",
            "https://monid.ai",
            "https://higgsfield.ai",
        ],
    )
    add_claim(
        "github-scottstts-threejs-awesome-graphics-agent-skills",
        {
            "id": "github-scottstts-threejs-awesome-graphics-agent-skills#c5",
            "text": (
                "leftover29 unused GitHub scottstts/Threejs-Awesome-Graphics-Agent-Skills API 6,503 B is MIT 782★. "
                "Description: a three.js agent skills for producing awesome graphics for scenes and games. "
                "leftover29 does not rerun capture-examples.mjs."
            ),
            "kind": "availability",
            "evidence": "leftover29 gh-scottstts 6503 B. MIT 782★.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/threejs-awesome-graphics-agent-skills.md",
            "confidence": "demonstrated",
            "subject": "web-3d-scenes",
        },
        ["https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills"],
    )
    add_claim(
        "web-feralui-dev",
        {
            "id": "web-feralui-dev#c4",
            "text": (
                "leftover29 unused GitHub mortspace/feral-blob API 5,387 B is MIT 17★. Description: playful "
                "themeable SVG jelly-blob mascot for React — part of FeralUI. leftover29 does not install the package."
            ),
            "kind": "availability",
            "evidence": "leftover29 feral-blob 5387 B. MIT 17★. Part of FeralUI.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/feralui.md",
            "confidence": "demonstrated",
            "subject": "web-3d-scenes",
        },
        ["https://github.com/mortspace/feral-blob"],
    )
    add_claim(
        "github-pbakaus-impeccable",
        {
            "id": "github-pbakaus-impeccable#c10",
            "text": (
                "leftover29 unused raw anthropics/skills frontend-design/SKILL.md 9,390 B. Front matter name "
                "frontend-design; license Complete terms in LICENSE.txt. Body is aesthetic-direction guidance "
                "(palette / type / anti-template tells). Neighbor Anthropic skill, not Impeccable 61 detectors "
                "and not Taste Skill v2. leftover29 does not run it on a fixture."
            ),
            "kind": "capability",
            "evidence": "leftover29 frontend-design 9390 B. SKILL.md name frontend-design.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/impeccable.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://github.com/anthropics/skills/tree/main/skills/frontend-design"],
    )
    add_claim(
        "web-checklist-design",
        {
            "id": "web-checklist-design#c3",
            "text": (
                "leftover29 unused Figma community plugin Checklist Design 734,330 B titles Checklist Design | Figma. "
                "Visible-text extract is empty (client-rendered community SPA). leftover29 does not install the plugin "
                "or the sibling skill/74536 page."
            ),
            "kind": "availability",
            "evidence": "leftover29 figma-plugin 734330 B. Title: Checklist Design | Figma. Visible empty.",
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
        "web-open-design-ai",
        {
            "id": "web-open-design-ai#c3",
            "text": (
                "leftover29 unused open-design.ai 339,680 B restates leftover18 (Best Open Source Claude Design "
                "Alternative) and names Fable 5.1 Pro/Max $20 / $100 bonus credits. leftover29 does not create a "
                "workspace. GitHub nexu-io/open-design star recount stays on the worksheet (94,085★)."
            ),
            "kind": "availability",
            "evidence": "leftover29 open-design-ai 339680 B. Same leftover18 byte count.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/open-design.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://open-design.ai", "https://github.com/nexu-io/open-design"],
    )
    add_claim(
        "web-dicebear",
        {
            "id": "web-dicebear#c3",
            "text": (
                "leftover29 unused GitHub dicebear/dicebear API 6,314 B is MIT 9,506★. leftover29 unused "
                "dicebear.com/playground 25,069 B titles Playground | DiceBear and shows Star 9.5k. leftover23 "
                "homepage already had 61 / 9.5k / MIT / 1B on the Blume leftover — leftover29 is the READY-card "
                "GitHub + playground recount. Do not collapse 9,506★ with 9.5k marketing."
            ),
            "kind": "availability",
            "evidence": "leftover29 dicebear-gh 9506 MIT; dicebear-play 25069 B Star 9.5k.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/dicebear.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        [
            "https://github.com/dicebear/dicebear",
            "https://www.dicebear.com/playground/",
        ],
    )
    add_claim(
        "github-punkpeye-awesome-mcp-servers",
        {
            "id": "github-punkpeye-awesome-mcp-servers#c3",
            "text": (
                "leftover29 unused GitHub punkpeye/awesome-mcp-servers API 5,662 B is MIT 94,179★. leftover29 unused "
                "glama.ai/mcp/servers 244,196 B titles Open-Source MCP Servers – 81,811 in the Glama Registry "
                "(updated 2026-09-05 05:28) and splits Remote 34,954 / Python 34,181 / TypeScript 28,944 / Local 27,943. "
                "leftover29 unused modelcontextprotocol.io 279,547 B redirects to docs/2026-07-28/getting-started/intro. "
                "leftover29 does not install a listed server."
            ),
            "kind": "availability",
            "evidence": "leftover29 gh-punkpeye 94179 MIT; glama 244196 B 81811 servers; mcp-io 279547 B spec 2026-07-28.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/kitesurf.md",
            "confidence": "demonstrated",
            "subject": "mcp-and-agent-browsers",
        },
        [
            "https://github.com/punkpeye/awesome-mcp-servers",
            "https://glama.ai/mcp/servers",
            "https://modelcontextprotocol.io/",
        ],
    )
    add_claim(
        "github-sindresorhus-awesome",
        {
            "id": "github-sindresorhus-awesome#c3",
            "text": (
                "leftover29 unused awesome.re 542,276 B redirects to github.com/sindresorhus/awesome#readme. "
                "Title notes pull requests are temporarily disabled. Index, not a harness. leftover29 does not "
                "count the list files."
            ),
            "kind": "availability",
            "evidence": "leftover29 awesome-re 542276 B. Redirect sindresorhus/awesome; PRs temporarily disabled.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/loop-library.md",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        ["https://awesome.re", "https://github.com/sindresorhus/awesome"],
    )
    add_claim(
        "x-2087178722420171020",
        {
            "id": "x-2087178722420171020#c2",
            "text": (
                "leftover29 unused GitHub cloudflare/cloudflare-os API 6,672 B is Apache-2.0 9,655★. Description: "
                "agent workspace built on Cloudflare Workers. leftover29 does not deploy a worker."
            ),
            "kind": "availability",
            "evidence": "leftover29 gh-cloudflare-os 6672 B. Apache-2.0 9655★.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/kitesurf.md",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        ["https://github.com/cloudflare/cloudflare-os"],
    )
    add_claim(
        "x-2088260067204137135",
        {
            "id": "x-2088260067204137135#c2",
            "text": (
                "leftover29 unused raw mattpocock/skills grilling/SKILL.md 1,987 B restates leftover14: design-tree "
                "interview / frontier / rounds. grill-me alias stays 157 B. leftover29 is that file now on this leftover card."
            ),
            "kind": "capability",
            "evidence": "leftover29 grilling 1987 B. Same leftover14 grilling SKILL.md.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/taste-skill.md",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        ["https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md"],
    )
    add_claim(
        "github-youmind-openlab-nano-banana-pro-prompts",
        {
            "id": "github-youmind-openlab-nano-banana-pro-prompts#c6",
            "text": (
                "leftover29 unused GitHub youmind-openlab/nano-banana-pro-prompts-recommend-skill API 8,178 B is "
                "1,848★ with license null. Description claims recommend from 10000+ Nano Banana Pro prompts. "
                "Do not collapse repo 10,000+ with leftover27 title 10,000+ / footer 15,508 / tree 14,965."
            ),
            "kind": "availability",
            "evidence": "leftover29 gh-youmind 8178 B. 1848★ license null; description 10000+.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/nano-banana-pro-prompts-recommend.md",
            "confidence": "demonstrated",
            "subject": "image-prompt-galleries",
        },
        ["https://github.com/youmind-openlab/nano-banana-pro-prompts-recommend-skill"],
    )
    add_claim(
        "x-2092222199620833420",
        {
            "id": "x-2092222199620833420#c4",
            "text": (
                "leftover29 unused GitHub freestylefly/awesome-gpt-image-2 API 6,160 B is MIT 28,060★ this pass "
                "(worksheet already had API 28,017★). Description: 530+ cases / 20+ industrial templates. Do not collapse."
            ),
            "kind": "availability",
            "evidence": "leftover29 gh-awesome-gpt-image2 6160 B. MIT 28060★ (was 28017).",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/gpt-image-2.md",
            "confidence": "demonstrated",
            "subject": "image-prompt-galleries",
        },
        ["https://github.com/freestylefly/awesome-gpt-image-2"],
    )
    add_claim(
        "github-nexu-io-motion-anything",
        {
            "id": "github-nexu-io-motion-anything#c4",
            "text": (
                "leftover29 unused GitHub nexu-io/motion-anything API 6,591 B is Apache-2.0 756★. Description: "
                "the agentic motion layer — chat-native motion engine. leftover29 unused sibling nexu-io/open-design "
                "star recount stays on the design worksheet (94,085★). leftover29 does not run a motion compile."
            ),
            "kind": "availability",
            "evidence": "leftover29 gh-motion-anything 6591 B. Apache-2.0 756★.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/motion-anything.md",
            "confidence": "demonstrated",
            "subject": "code-motion-graphics",
        },
        [
            "https://github.com/nexu-io/motion-anything",
            "https://github.com/nexu-io/open-design",
        ],
    )
    add_claim(
        "web-davidgasquez-context-engineering",
        {
            "id": "web-davidgasquez-context-engineering#c5",
            "text": (
                "leftover29 unused davidgasquez.com/context-engineering-is-a-data-problem 13,726 B titles Context "
                "Engineering Is a Data Problem (Aug 2, 2026). leftover29 unused context.ai/blog/a-filesystem-for-context "
                "38,717 B (6 Jun 2026) argues a filesystem beats default vector-chunk RAG for institutional knowledge. "
                "leftover29 does not run either recipe."
            ),
            "kind": "opinion",
            "evidence": "leftover29 gasquez 13726 B; context-ai 38717 B. Filesystem vs vector-chunk default.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/reasoning-bank.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        [
            "https://davidgasquez.com/context-engineering-is-a-data-problem",
            "https://www.context.ai/blog/a-filesystem-for-context",
        ],
    )
    add_claim(
        "web-iandmacomber-post-ai-data-stack",
        {
            "id": "web-iandmacomber-post-ai-data-stack#c4",
            "text": (
                "leftover29 unused iandmacomber.com/blog/post-ai-data-stack 67,426 B titles The Shape and Feel of "
                "the Post-AI Data Stack (August 30, 2026) and names agent-readable artifacts / agent-operable tools / "
                "agent-agnostic context. leftover29 unused rilldata.com 88,734 B titles Rill | The fastest business "
                "intelligence tool for humans and agents and shows 3k. leftover29 does not deploy a Rill project."
            ),
            "kind": "capability",
            "evidence": "leftover29 macomber 67426 B; rilldata 88734 B 3k.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/reasoning-bank.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        [
            "https://www.iandmacomber.com/blog/post-ai-data-stack",
            "https://www.rilldata.com/",
        ],
    )
    add_claim(
        "web-anthropic-claude-self-service-data",
        {
            "id": "web-anthropic-claude-self-service-data#c3",
            "text": (
                "leftover29 unused claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions "
                "517,319 B titles Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc "
                "questions. Visible extract is a large product-nav shell around that title. leftover29 does not replay "
                "a Slack Tag session. Neighbor Macomber / Gasquez pages stay on their own cards."
            ),
            "kind": "availability",
            "evidence": "leftover29 anthropic-slack 517319 B. Title: Claude Tag for ad-hoc questions.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/reasoning-bank.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        [
            "https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions"
        ],
    )
    add_claim(
        "x-2088623462109593792",
        {
            "id": "x-2088623462109593792#c2",
            "text": (
                "leftover29 unused GitHub pipeshub-ai/pipeshub-ai API 6,827 B is Apache-2.0 3,724★. Description: "
                "open-source platform for connecting enterprise knowledge to AI with permission-aware search. "
                "leftover29 does not run a connector."
            ),
            "kind": "availability",
            "evidence": "leftover29 gh-pipeshub 6827 B. Apache-2.0 3724★.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/pipeshub.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        ["https://github.com/pipeshub-ai/pipeshub-ai"],
    )
    add_claim(
        "web-treg-people-search",
        {
            "id": "web-treg-people-search#c3",
            "text": (
                "leftover29 unused treg.to/llms.txt 40,139 B. Lead copy: 2,600+ catalogued endpoints across 60+ "
                "providers; later agent-setup line says 2,800+ tools across 60 providers; $1.00 free on every new team; "
                "MCP at https://treg.to/mcp/ with five tools (catalog_search / catalog_get / call / balance / my_tools). "
                "Do not collapse 2,600+ / 2,800+ with leftover README 2,896 / 60 or homepage hero 2,630 / 47. "
                "Authed catalog dump still missing."
            ),
            "kind": "capability",
            "evidence": "leftover29 treg-llms 40139 B. 2600+ / 60+ and 2800+ / 60; $1.00 free; five MCP tools.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/treg.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://treg.to/llms.txt", "https://treg.to/people-search"],
    )
    add_claim(
        "web-graphed",
        {
            "id": "web-graphed#c3",
            "text": (
                "leftover29 unused graphed.com 292,950 B titles Graphed - Deploy AI Agents for Marketing. Visible "
                "extract is forward-deployed engineers + warehouse hosting; example Facebook Ads Agent Shifted $2.4k. "
                "leftover23 Cal.com Graphed Discovery Call stays a booking SPA. leftover29 does not open the keyed MCP."
            ),
            "kind": "availability",
            "evidence": "leftover29 graphed-home 292950 B. Marketing agents; example $2.4k shift.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/graphed-mcp.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://www.graphed.com/"],
    )
    add_claim(
        "x-2093256024635666465",
        {
            "id": "x-2093256024635666465#c2",
            "text": (
                "leftover29 unused note.com/acarcane/n/nfb705e6cf9f1 316,890 B is a Ponyo fan-movie Blender timelapse "
                "write-up (2026-08-28; Geometry Nodes / crayon look). YouTube youtu.be/a7doGx4R9rY was not fetched. "
                "Not a MiniMax H3 blockout recipe."
            ),
            "kind": "availability",
            "evidence": "leftover29 note-acarcane 316890 B. Ponyo Blender timelapse; not H3.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/minimax-h3.md",
            "confidence": "demonstrated",
            "subject": "blockout-to-video-flythrough",
        },
        ["https://note.com/acarcane/n/nfb705e6cf9f1"],
    )
    print("leftover29 claims folded")


if __name__ == "__main__":
    main()

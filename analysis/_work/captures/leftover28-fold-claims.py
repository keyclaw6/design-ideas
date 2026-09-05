#!/usr/bin/env python3
"""Add leftover28 demonstrated claims for remaining unused READY-card first-party pages."""
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
        "web-nqz-ai-search-prompt-generator",
        {
            "id": "web-nqz-ai-search-prompt-generator#c3",
            "text": (
                "leftover28 unused nqz.ai/ai-search-prompt-generator 36,810 B restates leftover22: 4 topics × 3 intents, "
                "10 generations/hour, no login. leftover28 unused /free-ai-tools 28,162 B is the hub: GEO Scorecard "
                "(6 pillars) + this generator; FAQ says IP rate-limit 10/hour and 30/day, no signup. Not a citation tracker."
            ),
            "kind": "capability",
            "evidence": "leftover28 nqz-gen 36810 B; nqz-tools 28162 B. 4×3 / 6 pillars / 10 per hour / 30 per day.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/nqz-ai-search-prompt-generator.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        [
            "https://nqz.ai/ai-search-prompt-generator",
            "https://nqz.ai/free-ai-tools",
        ],
    )
    add_claim(
        "web-known-agency",
        {
            "id": "web-known-agency#c3",
            "text": (
                "leftover28 unused known.agency 965,519 B titles known.agency — #1 AI Search Optimization Agency "
                "(source ranking language; do not echo as a finding). Visible extract claims Trusted by 100+ companies "
                "and a first-30-days visibility baseline. Same byte count already sits on leftover18 NOTES as vendor copy, "
                "not GSC proof. leftover28 is that homepage now on the READY card. Do not invent known-agency.md."
            ),
            "kind": "availability",
            "evidence": "leftover28 known-agency 965519 B. Title #1 AI Search Optimization Agency; 100+ companies.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/tinyshelf.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        ["https://known.agency/"],
    )
    add_claim(
        "web-tinylaunch-directories",
        {
            "id": "web-tinylaunch-directories#c3",
            "text": (
                "leftover28 unused tinylaunch.com/directories 106,620 B restates leftover22: Showing 15 of 691; "
                "30,000+ makers; paid 110 directories $279. leftover28 visible extract lists DR rows (sample Makerthrive "
                "DR 45 … AppSumo DR 84). Do not collapse 691 with TinyShelf listing counts. DR 11→46 still tweet-only."
            ),
            "kind": "availability",
            "evidence": "leftover28 tinylaunch-dirs 106620 B. 691 listed / 30000+ makers / $279 for 110.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/tinyshots.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        ["https://www.tinylaunch.com/directories"],
    )
    add_claim(
        "web-opale-ui-taste",
        {
            "id": "web-opale-ui-taste#c2",
            "text": (
                "leftover28 unused opale-ui.design 23,680 B titles Opale UI | Next.js Templates with Craft-Level Design. "
                "Visible extract is a template shop (48h AI Chat template free for a limited time) — not the taste-encoding "
                "essay already on this card. Do not treat the template catalog as a DESIGN.md pack."
            ),
            "kind": "availability",
            "evidence": "leftover28 opale 23680 B. Title: Next.js Templates with Craft-Level Design.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/taste-skill.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://opale-ui.design/"],
    )
    add_claim(
        "web-sceneai-art",
        {
            "id": "web-sceneai-art#c3",
            "text": (
                "leftover28 unused sceneai.art 307,798 B titles SceneAI: The Best UI Prompt Library on the Internet "
                "(source ranking language). Visible extract still has 36 Copy Prompt buttons and 60% OFF. Byte drift vs "
                "leftover Sol marketplace 308,165 B — do not collapse. HTML still has no GPT 5.6 and no unlimited."
            ),
            "kind": "availability",
            "evidence": "leftover28 sceneai 307798 B. 36 Copy Prompt; 60% OFF; no GPT 5.6 / unlimited.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/gpt-5-6-sol.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://sceneai.art/"],
    )
    add_claim(
        "github-leonxlnx-taste-skill",
        {
            "id": "github-leonxlnx-taste-skill#c4",
            "text": (
                "leftover28 unused GitHub vercel-labs/agent-skills API 6,440 B is 30,848★ with license null this pass. "
                "Description: Vercel's official collection of agent skills. Neighbor catalog, not Taste Skill v2 and not "
                "MengTo/Skills. Do not collapse 30,848★ with Taste Skill or Emil install counts."
            ),
            "kind": "availability",
            "evidence": "leftover28 vercel-skills 6440 B. vercel-labs/agent-skills 30848★ license null.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/taste-skill.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://github.com/vercel-labs/agent-skills"],
    )
    add_claim(
        "web-styles-refero-design",
        {
            "id": "web-styles-refero-design#c4",
            "text": (
                "leftover28 unused styles.refero.design/ai-agents/design-md-examples 157,432 B titles DESIGN.md Examples "
                "for AI Agents. Visible extract: Start with 24 curated references from 1,200+ matching styles. Do not "
                "collapse 24 / 1,200+ with leftover19 API 1,289 / 1,241 or marketing 2,000+."
            ),
            "kind": "availability",
            "evidence": "leftover28 refero-examples 157432 B. 24 curated from 1,200+ matching styles.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/styles-refero-design.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://styles.refero.design/ai-agents/design-md-examples"],
    )
    add_claim(
        "web-recent-design",
        {
            "id": "web-recent-design#c3",
            "text": (
                "leftover28 unused recent.design 311,079 B titles Recent — Design Inspiration. Visible extract is a "
                "thin inspiration + jobs shell (Web / Interface / Branding / Product / Typography / Motion / Illustration "
                "/ 3D / Editorial / Print / Packaging). No DESIGN.md inventory and no component count."
            ),
            "kind": "availability",
            "evidence": "leftover28 recent-design 311079 B. Title: Recent — Design Inspiration.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/tinyshots.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        ["https://recent.design/"],
    )
    add_claim(
        "web-tinyshots",
        {
            "id": "web-tinyshots#c2",
            "text": (
                "leftover28 unused tinyshots.app 70,112 B restates the product NOTES: $39 early-bird, 97 spots left, "
                "then $49; 180+ wallpapers; macOS Sonoma 14+; one-time / offline. DR 11→46 still absent. leftover28 is "
                "that homepage now on the READY card."
            ),
            "kind": "pricing",
            "evidence": "leftover28 tinyshots 70112 B. $39 / 97 spots / $49 / 180+ wallpapers.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/tinyshots.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        ["https://tinyshots.app"],
    )
    add_claim(
        "x-2089775679600812150",
        {
            "id": "x-2089775679600812150#c2",
            "text": (
                "leftover28 unused great-ui.com 72,561 B titles Great UI - Accessible React & Tailwind Components. "
                "Visible extract names stagger / multilingual quote / text-on-path / pixel-to-ASCII / scramble plus "
                "an open-source GitHub path Saurabh-2607/GreatUI. leftover28 does not install the library or time a scroll demo."
            ),
            "kind": "capability",
            "evidence": "leftover28 great-ui 72561 B. Accessible React & Tailwind; Saurabh-2607/GreatUI.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/great-ui.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        ["https://www.great-ui.com/"],
    )
    add_claim(
        "web-oryzo-ai",
        {
            "id": "web-oryzo-ai#c3",
            "text": (
                "leftover28 unused oryzo.ai 71,633 B is a satirical cork-coaster / AI-slop landing designed by Lusion "
                "(ORYZO-1 open-weight joke; ISSUE NO. 00124). leftover28 unused lusion.co 59,671 B is the studio site "
                "and names Oryzo AI as featured work. Neither page is a Three.js skill pack or a scene exporter."
            ),
            "kind": "counter-claim",
            "evidence": "leftover28 oryzo 71633 B; lusion 59671 B. Cork-coaster satire; Lusion featured work.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/scroll-world-skill.md",
            "confidence": "demonstrated",
            "subject": "web-3d-scenes",
        },
        ["https://oryzo.ai/", "https://lusion.co/"],
    )
    add_claim(
        "x-2094961942058418268",
        {
            "id": "x-2094961942058418268#c5",
            "text": (
                "leftover28 unused seed.bytedance.com/en/seed3d_2_0 136,088 B titles ByteDance Seed. Visible extract "
                "lists Seed2.1 / Seedance 2.5 / Seedream 5.0 Pro / SeedRealtime / Seed Audio 1.0 / Seed GR-RL — it does "
                "not name Seed3D 2.0, Lucida, or a mesh export. leftover28 does not close a Seed3D user export. "
                "Lucida integers stay on #c2–#c4."
            ),
            "kind": "counter-claim",
            "evidence": "leftover28 seed3d 136088 B. Seed hub; Seed3D 2.0 string absent.",
            "evidence_source": "note",
            "evidence_ref": "analysis/techniques/image-to-3d-worldgen.md",
            "confidence": "demonstrated",
            "subject": "image-to-3d-world",
        },
        ["https://seed.bytedance.com/en/seed3d_2_0"],
    )
    add_claim(
        "x-2091943679317463153",
        {
            "id": "x-2091943679317463153#c3",
            "text": (
                "leftover28 unused alpha.splatpaint.app 5,686 B titles SplatPaint Founding Alpha. Visible extract is "
                "an invite / Patreon sign-in shell for a browser Gaussian-splat playground. Unapproved email does not "
                "create an account. leftover28 does not paint a splat or export a PLY."
            ),
            "kind": "availability",
            "evidence": "leftover28 splatpaint 5686 B. Title: SplatPaint Founding Alpha. Invite/Patreon gate.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/splat-js.md",
            "confidence": "demonstrated",
            "subject": "gaussian-splatting",
        },
        ["https://alpha.splatpaint.app"],
    )
    add_claim(
        "note-blender-minimax-h3-video-generation",
        {
            "id": "note-blender-minimax-h3-video-generation#c4",
            "text": (
                "leftover28 unused MiniMax Create Video Generation Task docs 442,375 B titles the H3 video-generation "
                "POST and names MiniMax-H3 as a new-generation open general-purpose multimodal video model. leftover28 "
                "unused HF api/models/MiniMaxAI/MiniMax-H3 20,848 B: 4,913 likes, 5,118,457 downloads, pipeline "
                "image-text-to-video, license other / minimax-h3-community-license-agreement. leftover28 does not submit "
                "a create-task call or run a Blender blockout through H3."
            ),
            "kind": "availability",
            "evidence": "leftover28 minimax-docs 442375 B; hf-minimax-h3 4913 likes / 5118457 downloads.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/minimax-h3.md",
            "confidence": "demonstrated",
            "subject": "blockout-to-video-flythrough",
        },
        [
            "https://platform.minimax.io/docs/api-reference/video-generation-v2-create",
            "https://huggingface.co/MiniMaxAI/MiniMax-H3",
        ],
    )
    add_claim(
        "web-lottiefiles",
        {
            "id": "web-lottiefiles#c3",
            "text": (
                "leftover28 unused lottiefiles.com 403 / 5,598 B Cloudflare checkpoint (Just a moment…). Visible extract "
                "empty. Do not hammer. leftover28 does not open /features."
            ),
            "kind": "availability",
            "evidence": "leftover28 lottiefiles 403 / 5598 B Cloudflare. Do not hammer.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/remotion.md",
            "confidence": "demonstrated",
            "subject": "code-motion-graphics",
        },
        ["https://lottiefiles.com/"],
    )
    add_claim(
        "web-fal-ai",
        {
            "id": "web-fal-ai#c3",
            "text": (
                "leftover28 unused fal.ai/docs/llms.txt 95,947 B is a docs index: 198 unique fal.ai doc links this pass, "
                "and copy claiming 1,000+ models plus MCP / genmedia CLI / Platform MCP. leftover28 does not call a model "
                "or an authed MCP session."
            ),
            "kind": "capability",
            "evidence": "leftover28 fal-llms 95947 B. 198 unique doc links; 1,000+ models.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/fal-api.md",
            "confidence": "demonstrated",
            "subject": "ai-video-generation",
        },
        ["https://fal.ai/docs/llms.txt"],
    )
    add_claim(
        "x-2089717063921332378",
        {
            "id": "x-2089717063921332378#c2",
            "text": (
                "leftover28 unused cadxstudio.in 3,111 B titles CadXStudio | AI Design Engine in the Browser. Visible "
                "extract is empty (thin marketing shell). Meta/og still says text-to-CAD / BREP / no install. leftover28 "
                "does not export a STEP."
            ),
            "kind": "availability",
            "evidence": "leftover28 cadx 3111 B. Title: AI Design Engine in the Browser.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/cadx-studio.md",
            "confidence": "demonstrated",
            "subject": "ai-cad-hardware",
        },
        ["https://cadxstudio.in"],
    )
    add_claim(
        "x-2090535643353153833",
        {
            "id": "x-2090535643353153833#c2",
            "text": (
                "leftover28 unused cadxstudio.in 3,111 B on this sibling card is the same leftover28 cadx receipt "
                "(AI Design Engine in the Browser; visible extract empty). Still no STEP export."
            ),
            "kind": "availability",
            "evidence": "leftover28 cadx 3111 B. Same sibling leftover as x-2089717063921332378#c2.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/cadx-studio.md",
            "confidence": "demonstrated",
            "subject": "ai-cad-hardware",
        },
        ["https://cadxstudio.in"],
    )
    add_claim(
        "github-youmind-openlab-nano-banana-pro-prompts",
        {
            "id": "github-youmind-openlab-nano-banana-pro-prompts#c5",
            "text": (
                "leftover28 unused clawhub.com/skill/nano-banana-pro-prompts-recommend 63,154 B redirects to "
                "clawhub.ai/skill/skills/nano-banana-pro-prompts-recommend. Title matches the skill slug. Visible extract "
                "is an OpenClaw ecosystem catalog shell — it does not restate leftover27 title 10,000+ / footer 15,508. "
                "Do not collapse ClawHub with the YouMind footer inventory."
            ),
            "kind": "availability",
            "evidence": "leftover28 clawhub-nano 63154 B. Redirect clawhub.ai; title nano-banana-pro-prompts-recommend.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/clawhub.md",
            "confidence": "demonstrated",
            "subject": "image-prompt-galleries",
        },
        ["https://clawhub.com/skill/nano-banana-pro-prompts-recommend"],
    )
    add_claim(
        "x-2087151521121419648",
        {
            "id": "x-2087151521121419648#c3",
            "text": (
                "leftover28 unused aimock.copilotkit.dev 135,659 B titles aimock — Deterministic mock infrastructure "
                "for AI apps. Visible extract: npx -p @copilotkit/aimock llmock; docker ghcr.io/copilotkit/aimock on "
                "port 4010. leftover28 does not run a fixture replay."
            ),
            "kind": "capability",
            "evidence": "leftover28 aimock 135659 B. npx @copilotkit/aimock; docker port 4010.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/copilotkit-aimock.md",
            "confidence": "demonstrated",
            "subject": "mcp-and-agent-browsers",
        },
        ["https://aimock.copilotkit.dev"],
    )
    add_claim(
        "web-cloudflare-kitesurf",
        {
            "id": "web-cloudflare-kitesurf#c4",
            "text": (
                "leftover28 unused developers.cloudflare.com/browser-run/ 138,466 B is the Browser Run overview: "
                "/content /screenshot /pdf /markdown /snapshot /accessibilityTree /scrape /json /links /crawl plus "
                "Live View / Human in the Loop / Session recording / WebMCP (Beta). leftover24/25 already have limits "
                "NOTES. leftover28 does not start a live Browser Run session (needs a CF token)."
            ),
            "kind": "capability",
            "evidence": "leftover28 cf-browser-run 138466 B. Named REST actions + Beta Live View / WebMCP.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/kitesurf.md",
            "confidence": "demonstrated",
            "subject": "mcp-and-agent-browsers",
        },
        ["https://developers.cloudflare.com/browser-run/"],
    )
    add_claim(
        "x-2087329201451855933",
        {
            "id": "x-2087329201451855933#c2",
            "text": (
                "leftover28 unused GitHub imxv/Pretty-mermaid-skills API 5,816 B is MIT 1,182★. Description: 15 themes, "
                "6 diagram types, batch CLI, SVG or terminal ASCII, no browser. leftover28 does not render a fixture SVG."
            ),
            "kind": "availability",
            "evidence": "leftover28 pretty-mermaid 5816 B. MIT 1182★; 15 themes / 6 diagram types.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/diagram-design.md",
            "confidence": "demonstrated",
            "subject": "infographics-diagrams",
        },
        ["https://github.com/imxv/Pretty-mermaid-skills"],
    )
    add_claim(
        "web-chatgpt-training",
        {
            "id": "web-chatgpt-training#c4",
            "text": (
                "leftover28 unused academy.openai.com/home/events 612,752 B redirects to /public/events. Title Events | "
                "OpenAI Academy. Visible extract lists livestream / in-person sessions (this pass: 24 Register CTAs / "
                "17 Livestream labels). leftover28 does not complete a signed-in event."
            ),
            "kind": "availability",
            "evidence": "leftover28 openai-academy 612752 B. 24 Register / 17 Livestream labels.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/chatgpt-training.md",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        ["https://academy.openai.com/home/events"],
    )
    print("leftover28 claims folded")


if __name__ == "__main__":
    main()

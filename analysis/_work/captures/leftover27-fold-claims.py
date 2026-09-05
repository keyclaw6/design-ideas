#!/usr/bin/env python3
"""Add leftover27 demonstrated claims for unused READY-card first-party pages."""
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
        "github-google-labs-code-design-md",
        {
            "id": "github-google-labs-code-design-md#c4",
            "text": (
                "leftover27 unused stitch.withgoogle.com/docs/design-md/specification 25,497 B titles "
                "Stitch - Design with AI. Visible-text extract is empty (client-rendered Stitch docs SPA); "
                "the dump does not expose DesignMD spec headings, schema fields, or version integers. "
                "Does not close a logged-in Stitch workspace walkthrough."
            ),
            "kind": "availability",
            "evidence": "leftover27 stitch-designmd-spec 25497 B. Title: Stitch - Design with AI.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/getdesign-md.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://stitch.withgoogle.com/docs/design-md/specification"],
    )
    add_claim(
        "github-pbakaus-impeccable",
        {
            "id": "github-pbakaus-impeccable#c8",
            "text": (
                "leftover27 unused impeccable.style 109,943 B restates Impeccable 4.1 as 66k+ lines, 61 checks, "
                "23 CLI commands, 177 custom ESLint worlds, plus npx impeccable install and Node 22.12+. "
                "Those 4.1 homepage integers already sit on leftover19 / must-read NOTES — leftover27 is a "
                "same-day homepage recount, not a new 4.1 inventory. Do not collapse 4.1 homepage copy with "
                "GitHub skill 4.2.0."
            ),
            "kind": "capability",
            "evidence": "leftover27 impeccable-style 109943 B. 66k / 61 / 23 / 177 / Node 22.12+.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/impeccable.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://impeccable.style"],
    )
    add_claim(
        "github-pbakaus-impeccable",
        {
            "id": "github-pbakaus-impeccable#c9",
            "text": (
                "leftover27 unused GitHub skill-v4.2.0 release JSON 5,961 B names skill 4.2.0 published "
                "2026-09-04T20:28:37Z with a static binary (no Node), hook 10.6 ms vs 46.9 ms, CLI 110 files "
                "in 132 ms vs 282 ms, and replay 830 / 16,058. Those 4.2.0 release integers already sit on "
                "leftover05 impeccable NOTES. leftover27 is a same-tag API recount on the github-pbakaus-impeccable "
                "card. Do not collapse 4.2.0 with the 4.1.0 / 4.1 homepage lane."
            ),
            "kind": "availability",
            "evidence": "leftover27 gh-impeccable-420 5961 B. skill-v4.2.0 published 2026-09-04T20:28:37Z.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/impeccable.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://api.github.com/repos/pbakaus/impeccable/releases/tags/skill-v4.2.0"],
    )
    add_claim(
        "github-emilkowalski-skills",
        {
            "id": "github-emilkowalski-skills#c3",
            "text": (
                "leftover27 unused animations.dev/skills 125,328 B is a thin newsletter / AI skills for design "
                "engineers landing — it does not list Emil skill names, install counts, or a version. "
                "skills.sh/emilkowalski/skills 63,314 B names 12 skills with 1.2M total installs: emil-design-eng "
                "250.4K, react-render-perf 213.8K, web-design-guidelines 211.8K, web-animation-skills 133.2K, "
                "webpage-design-review 120.3K, react-best-practices 117.2K, polish 78.2K, compose 41.6K, extract "
                "34.1K, adapt 29.4K, critique 25.8K, write-swift 24.4K. skills.sh counts are a third-party catalog "
                "snapshot, not GitHub star/download totals."
            ),
            "kind": "availability",
            "evidence": "leftover27 animations-dev-skills 125328 B; skills-sh-emil 63314 B. 12 skills / 1.2M installs.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/taste-skill.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        [
            "https://animations.dev/skills",
            "https://skills.sh/emilkowalski/skills",
        ],
    )
    add_claim(
        "github-leonxlnx-taste-skill",
        {
            "id": "github-leonxlnx-taste-skill#c3",
            "text": (
                "leftover27 unused tasteskill.dev 255,878 B names Taste Skill v2 as experimental, lists 13 named "
                "skills (adapt, animate, compose, critique, extract, overdrive, polish, tautology, typography, "
                "on-brand, arrange, clarify, bolder), shows 16 sponsors, and installs via npx skills add "
                "Leonxlnx/taste-skill. Does not score those skills against a shared fixture or name a stable v1."
            ),
            "kind": "capability",
            "evidence": "leftover27 tasteskill 255878 B. v2 experimental / 13 skills / 16 sponsors.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/taste-skill.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://tasteskill.dev"],
    )
    add_claim(
        "github-mengto-skills",
        {
            "id": "github-mengto-skills#c3",
            "text": (
                "leftover27 unused ui-skills.com 211,608 B is a third-party catalog of other authors' skills "
                "(ibelick, emilkowalski, jakubkrehel, pbakaus, Leonxlnx, and others) — not an inventory of "
                "MengTo/Skills. Do not treat ui-skills.com counts as MengTo repo stats."
            ),
            "kind": "availability",
            "evidence": "leftover27 ui-skills 211608 B. Third-party catalog, not MengTo/Skills.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/mengto-skills.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://ui-skills.com"],
    )
    add_claim(
        "github-jakubkrehel-skills",
        {
            "id": "github-jakubkrehel-skills#c3",
            "text": (
                "leftover27 unused jakub.kr/skills 235,058 B names better-ui, typography, colors, accessibility, "
                "layout, writing, interface-review, explain-interface, break, and variant. interfaces.dev "
                "620,860 B is Design Engineering Magazine. leftover27 does not run those skills against a shared fixture."
            ),
            "kind": "capability",
            "evidence": "leftover27 jakub-skills 235058 B; interfaces-dev 620860 B. Named better-* skills.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/better-interface.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://jakub.kr/skills", "https://interfaces.dev"],
    )
    add_claim(
        "github-antvis-infographic",
        {
            "id": "github-antvis-infographic#c3",
            "text": (
                "leftover27 unused infographic.antv.vision 79,156 B names AntV Infographic v0.2.20 (Build "
                "Infographics with Words). /gallery 382,873 B is a large client bundle; the visible-text extract "
                "does not list a template count. leftover27 does not walk a saved gallery item or publish a "
                "rendered infographic."
            ),
            "kind": "availability",
            "evidence": "leftover27 antv-home 79156 B v0.2.20; antv-gallery 382873 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/antv-infographic.md",
            "confidence": "demonstrated",
            "subject": "infographics-diagrams",
        },
        [
            "https://infographic.antv.vision",
            "https://infographic.antv.vision/gallery",
        ],
    )
    add_claim(
        "github-cathrynlavery-diagram-design",
        {
            "id": "github-cathrynlavery-diagram-design#c5",
            "text": (
                "leftover27 unused littlemight.com 61,395 B is Business & life strategies for ambitious "
                "millennials — not a diagram-design tool, not Cathryn Lavery's library, and not an infographic "
                "renderer. Treat littlemight.com as a leftover host-string collision, not as diagram-design evidence."
            ),
            "kind": "counter-claim",
            "evidence": "leftover27 littlemight 61395 B. Quote: Business & life strategies for ambitious millennials.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/diagram-design.md",
            "confidence": "demonstrated",
            "subject": "infographics-diagrams",
        },
        ["https://littlemight.com"],
    )
    add_claim(
        "github-nv-tlabs-ArtiFixer",
        {
            "id": "github-nv-tlabs-ArtiFixer#c3",
            "text": (
                "leftover27 unused arXiv 2603.00492 abs 44,589 B names ArtiFixer (de Lutio et al.; SIGGRAPH 2026; "
                "v2 5 May 2026) and claims 1–3 dB PSNR over 3DGS baselines, with PDF artifixer.pdf listed at "
                "91,742 KB. research.nvidia.com/labs/sil/projects/artifixer/ 18,793 B names ArtiFixer / ArtiFixer3D / "
                "ArtiFixer3D+ on MipNeRF 360, DL3DV, and Nerfbusters. huggingface.co/api/models/nvidia/ArtiFixer "
                "850,636 B and 65 likes. leftover27 does not download the 91,742 KB PDF or rerun those PSNR tables."
            ),
            "kind": "benchmark",
            "evidence": "leftover27 artifixer-abs 44589 B; artifixer-nvidia 18793 B; hf-artifixer 65 likes. 1–3 dB PSNR.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/artifixer.md",
            "confidence": "demonstrated",
            "subject": "gaussian-splatting",
        },
        [
            "https://arxiv.org/abs/2603.00492",
            "https://research.nvidia.com/labs/sil/projects/artifixer/",
            "https://huggingface.co/api/models/nvidia/ArtiFixer",
        ],
    )
    add_claim(
        "web-chatgpt-training",
        {
            "id": "web-chatgpt-training#c3",
            "text": (
                "leftover27 unused learn.chatgpt.com/training 305,746 B lists ChatGPT Training walkthroughs for "
                "ChatGPT (Work) and Codex. leftover27 does not complete a signed-in training module or export a "
                "completion receipt."
            ),
            "kind": "availability",
            "evidence": "leftover27 chatgpt-training 305746 B. Work + Codex walkthroughs.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/chatgpt-training.md",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        ["https://learn.chatgpt.com/training"],
    )
    add_claim(
        "web-blume-codes",
        {
            "id": "web-blume-codes#c2",
            "text": (
                "leftover27 unused careers.blume.codes 51,037 B is Teamtailor listing Head of Growth and Founding "
                "Engineer and says the company was founded in 2025. leftover27 does not apply or confirm headcount "
                "beyond those two open roles."
            ),
            "kind": "availability",
            "evidence": "leftover27 blume-careers 51037 B. Head of Growth + Founding Engineer; founded 2025.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/blume-sidecar.md",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        ["https://careers.blume.codes"],
    )
    add_claim(
        "web-animos-editor",
        {
            "id": "web-animos-editor#c3",
            "text": (
                "leftover27 unused animos.app 2,864 B titles animos — Motion templates; visible-text extract is "
                "empty (thin client shell). leftover27 does not open the editor or export a template."
            ),
            "kind": "availability",
            "evidence": "leftover27 animos 2864 B. Title: animos — Motion templates.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/animos-editor.md",
            "confidence": "demonstrated",
            "subject": "code-motion-graphics",
        },
        ["https://animos.app"],
    )
    add_claim(
        "github-h4ckf0r0day-obscura",
        {
            "id": "github-h4ckf0r0day-obscura#c7",
            "text": (
                "leftover27 unused docs.obscura.sh/llms.txt 2,687 B lists 21 documentation links plus a GitBook "
                "?ask= query endpoint. leftover27 does not run that ask endpoint or time the leftover24 Star 16.2k / "
                "<50ms / 10× claims."
            ),
            "kind": "capability",
            "evidence": "leftover27 obscura-llms 2687 B. 21 doc links + GitBook ?ask=.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/obscura.md",
            "confidence": "demonstrated",
            "subject": "mcp-and-agent-browsers",
        },
        ["https://docs.obscura.sh/llms.txt"],
    )
    add_claim(
        "web-getlayers-ai",
        {
            "id": "web-getlayers-ai#c3",
            "text": (
                "leftover27 unused getlayers.ai 426,495 B claims 1,000+ creators and a template / 3D / section / "
                "gradient / background library with MCP. leftover27 does not create an account or export a layered scene."
            ),
            "kind": "capability",
            "evidence": "leftover27 getlayers 426495 B. 1000+ creators; template/3D/MCP library.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/getlayers.md",
            "confidence": "demonstrated",
            "subject": "web-3d-scenes",
        },
        ["https://getlayers.ai"],
    )
    add_claim(
        "web-feralui-dev",
        {
            "id": "web-feralui-dev#c3",
            "text": (
                "leftover27 unused feralui.dev 10,527 B titles FeralUI · playful, physics-driven React elements; "
                "visible-text extract is empty (thin marketing shell). leftover27 does not install the package or "
                "render a physics element."
            ),
            "kind": "availability",
            "evidence": "leftover27 feralui 10527 B. Title: FeralUI · playful, physics-driven React elements.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/feralui.md",
            "confidence": "demonstrated",
            "subject": "web-3d-scenes",
        },
        ["https://feralui.dev"],
    )
    add_claim(
        "github-youmind-openlab-nano-banana-pro-prompts",
        {
            "id": "github-youmind-openlab-nano-banana-pro-prompts#c4",
            "text": (
                "leftover27 unused youmind.com/nano-banana-pro-prompts 1,244,866 B titles 10,000+ prompts; footer "
                "visible text says TOTAL 15,508. Do not collapse title 10,000+, footer 15,508, and any 30,000+ "
                "repo copy into one inventory. leftover27 does not download the prompt set."
            ),
            "kind": "availability",
            "evidence": "leftover27 youmind-nano 1244866 B. Title 10000+; footer TOTAL 15508.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/nano-banana-pro-prompts-recommend.md",
            "confidence": "demonstrated",
            "subject": "image-prompt-galleries",
        },
        ["https://youmind.com/nano-banana-pro-prompts"],
    )
    add_claim(
        "github-LessieAI-people-search-bench",
        {
            "id": "github-LessieAI-people-search-bench#c3",
            "text": (
                "leftover27 unused lessie.ai 1,469,320 B homepage comparison table claims Lessie 65.2, Exa 55, "
                "Claude 46, Juicebox 45.8 on 119 queries. leftover23 already folded arXiv abs/2603.27476 "
                "PeopleSearchBench 119 queries / four scenarios / κ=0.84 and does not name treg #1. Do not collapse "
                "this homepage 65.2 score with treg #1 or with the abs paper's scenario table. leftover27 does not "
                "rerun those 119 queries."
            ),
            "kind": "benchmark",
            "evidence": "leftover27 lessie-ai 1469320 B. Homepage 65.2 / Exa 55 / Claude 46 / Juicebox 45.8 on 119 queries.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/lessie.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["https://lessie.ai"],
    )
    print("leftover27 claims folded")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Add leftover19 demonstrated claims to must-read / failed-thread cards."""
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
        "x-2074912810803560497",
        {
            "id": "x-2074912810803560497#c5",
            "text": "leftover19 GitHub: gpu-mode/popcorn-cli MIT 178★ (Rust). README still names popcorn submit --leaderboard qr_v2 --profile-brev and the qr_v2 starter under gpu-mode/reference-kernels (303★, license NOASSERTION). Nsight hosted profiling writes ncu-details.txt/csv locally. No public submit_logs/ tree. Harbor 796445 / tweet 212× vs blog 232× vs live 26th 3916.103 µs stay as already quoted.",
            "kind": "availability",
            "evidence": "leftover19-2026-09-05.json gh-popcorn-cli 178 MIT; gh-ref-kernels 303 NOASSERTION; README 12,541 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/codex.md",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        None,
        ["https://github.com/gpu-mode/popcorn-cli", "https://github.com/gpu-mode/reference-kernels"],
    ),
    (
        "x-2093915384944414827",
        {
            "id": "x-2093915384944414827#c3",
            "text": "leftover19: quoted layer-separation t.co/cRrGTKGJwH resolves to remove.bg 200 / 60,038 B (title Remove Background from Image for Free). That is a generic background-remove site, not a custom parallax layer tool. Thread stays failed. Do not invent a remove-bg.md.",
            "kind": "availability",
            "evidence": "leftover19 tco-parallax-layers final https://www.remove.bg/ 200 60038 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/techniques/parallax-scroll-landing.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        None,
        ["https://www.remove.bg/"],
    ),
    (
        "x-2093051654937423887",
        {
            "id": "x-2093051654937423887#c5",
            "text": "leftover19: remaining Mint Studio t.co links all loop to X sibling tweets (render 2093051656426406288, city 2093051658016035321, World Labs 2093051659383390332). No first-party Studio camera-path or city-import docs. mint.gg still has no documented camera exporter.",
            "kind": "counter-claim",
            "evidence": "leftover19 tco-mint-render/city/worldlabs final x.com/tamrrat/status/209305165…",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/mint-studio.md",
            "confidence": "demonstrated",
            "subject": "blockout-to-video-flythrough",
        },
        None,
        None,
    ),
    (
        "x-2095368133070700884",
        {
            "id": "x-2095368133070700884#c3",
            "text": "leftover19: failed-thread reply t.co/qlVOgcGt83 resolves to sceneai.art 200 / 307,798 B (same host as the sibling teaser leftover). Title SceneAI: The Best UI Prompt Library on the Internet (source ranking language). Sol prompt body still missing. Do not treat this as a second marketplace.",
            "kind": "availability",
            "evidence": "leftover19 tco-sol-reply final https://sceneai.art/ 200 307798 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/gpt-5-6-sol.md",
            "confidence": "demonstrated",
            "subject": "image-prompt-galleries",
        },
        None,
        ["https://sceneai.art/"],
    ),
    (
        "x-2087151807965401320",
        {
            "id": "x-2087151807965401320#c6",
            "text": "leftover19: quoted HF t.co resolve to public datasets. razzant/ouroboros-osworld-verified-opus5 Apache-2.0, 361 rows / 112 MB, self-reported 90.69% (327.39/361) Opus 5 screenshot-only vs Intelligence-Indeed 90.19%. razzant/ouroboros-clbench-traces MIT+Apache-2.0, 6 rows / 840 MB, self-reported CL-Bench 0.2301 rank 1 Sonnet 4.6. Ranking language is the dataset cards’. Thread stays failed.",
            "kind": "benchmark",
            "evidence": "leftover19 tco-ouroboros-hf1 huggingface.co/datasets/razzant/ouroboros-osworld-verified-opus5 628234 B; hf2 ouroboros-clbench-traces 256259 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/techniques/agent-harness-ops.md",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        None,
        [
            "https://huggingface.co/datasets/razzant/ouroboros-osworld-verified-opus5",
            "https://huggingface.co/datasets/razzant/ouroboros-clbench-traces",
        ],
    ),
    (
        "x-2095437841958314100",
        {
            "id": "x-2095437841958314100#c5",
            "text": "leftover19 re-fetched CAST HTML arxiv.org/html/2502.12894 200 / 376,208 B (title CAST: Component-Aligned 3D Scene Reconstruction from an RGB Image). Paper tables already quoted on hyper3d-worldgen NOTES (open-vocab CLIP 85.77 / GPT-4 rank 1.125; 3D-Front CD-S 0.052). Logged-out WorldGen stays the 11,026 B login SPA. No public user-scene download.",
            "kind": "benchmark",
            "evidence": "leftover19-2026-09-05.json cast-arxiv-html 376208 B. Tables on analysis/tools/hyper3d-worldgen.md.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/hyper3d-worldgen.md",
            "confidence": "demonstrated",
            "subject": "image-to-3d-world",
        },
        None,
        ["https://arxiv.org/html/2502.12894"],
    ),
    (
        "x-2091169290661838965",
        {
            "id": "x-2091169290661838965#c8",
            "text": "leftover19: docs.openviking.ai 200 / 61,649 B is a docs index (Agent Context / Retrieval Architecture / Operations; Apache-2.0 footer). No VLM provider, abstract.md, or 91% token-savings copy on this page. L0 abstracts stay not ready without a VLM, as in the local ov session.",
            "kind": "availability",
            "evidence": "leftover19 openviking-docs 61649 B title OpenViking.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/openviking.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        None,
        ["https://docs.openviking.ai"],
    ),
    (
        "x-2088254428730085690",
        {
            "id": "x-2088254428730085690#c6",
            "text": "leftover19: impeccable.style 200 / 109,943 B markets 61 checks, 23 commands, and 177 highest-rated worlds. Install copy is npx impeccable install (Node 22.12+). Homepage does not name skill-v4.1.0 vs skill-v4.2.0 — do not collapse those GitHub tags. Testimonial ranking language is source quotes, not a finding.",
            "kind": "capability",
            "evidence": "leftover19 impeccable-style 109943 B. 61 checks / 23 commands / 177 worlds visible.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/impeccable.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        None,
        ["https://impeccable.style"],
    ),
    (
        "x-2093766772029559077",
        {
            "id": "x-2093766772029559077#c5",
            "text": "leftover19: styles.refero.design 200 / 103,024 B still markets Browse 2,000+ AI-readable design systems. Public API recount on this card stays 1,289 style ids / 1,241 siteNames. Records are JSON designSystem blobs, not DESIGN.md files.",
            "kind": "counter-claim",
            "evidence": "leftover19 refero-styles 103024 B title DESIGN.md Examples for AI Agents | Refero Styles.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/styles-refero-design.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        None,
        ["https://styles.refero.design/"],
    ),
    (
        "x-2094770895021572502",
        {
            "id": "x-2094770895021572502#c9",
            "text": "leftover19: fixmebot.com 200 / 328,304 B. First-party: 600,000+ people / 90+ languages / 10 tools; Free 10,000 characters; paid €4.99–€29.99/mo. Built by shimanski.dev; also lists AI Edit, Post Formatter, Blurr. This is a writing assistant, not GSC proof of 1.01M / 16.3K.",
            "kind": "pricing",
            "evidence": "leftover19 fixmebot 328304 B. Visible 600,000+ / 90+ / €4.99 / €29.99.",
            "evidence_source": "note",
            "evidence_ref": "analysis/techniques/serp-keyword-research.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        None,
        ["https://fixmebot.com"],
    ),
    (
        "x-2094819241916801165",
        {
            "id": "x-2094819241916801165#c4",
            "text": "leftover19: wuyoscar/GPT-Image2-Skill MIT 5,153★. README (2026-09-04) is a prompt gallery + 2 agent skills + CLI; edits use POST /v1/images/edits with repeatable -i for multi-reference. Official developers.openai.com image-generation guide 200 / 1,248,104 B. Neither page names identity lock. Face-swap stills stay the tweet recipe.",
            "kind": "capability",
            "evidence": "leftover19 gh-gpt-image2-skill 5153 MIT; openai-image-gen 1248104 B. README multi-reference edit section.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/gpt-image-2.md",
            "confidence": "demonstrated",
            "subject": "ai-video-generation",
        },
        None,
        [
            "https://github.com/wuyoscar/GPT-Image2-Skill",
            "https://developers.openai.com/api/docs/guides/image-generation",
        ],
    ),
]


def main() -> None:
    for card_id, claim, tools, other in CLAIMS:
        add_claim(card_id, claim, tools, other)


if __name__ == "__main__":
    main()

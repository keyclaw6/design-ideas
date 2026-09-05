#!/usr/bin/env python3
"""Add leftover21 demonstrated claims."""
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
        "x-2094462971598754010",
        {
            "id": "x-2094462971598754010#c5",
            "text": "leftover21: github.com/garrytan/gbrain-evals MIT 413★ (prior card snapshot 406★). README first-party official LongMemEval recall_all@5 is 93.19% reranker off (438/470) / 95.32% Voyage rerank-2.5 (448/470) at gbrain v0.48.2.0. Tweet/media 97.6% R@5 is a different row — do not collapse. Cat 35 write-path 88.1% salient-unit recall / 91% usable matches the tweet write number.",
            "kind": "benchmark",
            "evidence": "leftover21 gbrain-evals README 22081 B; gh API 413 MIT. Quote: 93.19% official recall_all@5 reranker off / 95.32% with the default Voyage reranker.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/gbrain-evals.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        ["https://github.com/garrytan/gbrain-evals"],
    )
    add_claim(
        "x-2092918452423983363",
        {
            "id": "x-2092918452423983363#c8",
            "text": "leftover21 remaining Slite names are now first-party products, not the tweet map. slite.com/slite-agent 536,317 B: 20+ connected tools, human-approval drafts, MCP. getnao/sylph 195★ license null: git-repo company brain (domains/skills/agents/self-improving loop). pletor.ai/blog/…/meet-brain 119,137 B is brand-memory for creative production (Brain beta). None carry Gorgias 12,000 markdown nodes. Do not invent sylph.md / pletor.md.",
            "kind": "availability",
            "evidence": "leftover21-2026-09-05.json slite-agent 536317 B; gh-sylph 195; pletor-brain 119137 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/techniques/filesystem-context-memory.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        [
            "https://slite.com/slite-agent",
            "https://github.com/getnao/sylph",
            "https://www.pletor.ai/blog/meet-brain-persistent-brand-memory-for-ai-creative-production",
        ],
    )
    add_claim(
        "x-2091169290661838965",
        {
            "id": "x-2091169290661838965#c9",
            "text": "leftover21: volcengine/OpenViking README 16,499 B first-party LoCoMo 80–83% vs 24–57% native memory; input tokens drop 34.3–91.0% (the 91% reply). docs/en/guides/01-configuration 381,283 B: VLM providers OpenAI / Volcengine / Kimi / GLM / OpenAI Codex; if VLM is not configured, L0/L1 generate from content directly (less accurate). Server config names vlm object for summaries. Local ov abstract still not ready without a keyed VLM.",
            "kind": "benchmark",
            "evidence": "leftover21 ov-readme 16499 B; ov-guide-config 381283 B; ov-server-config 141639 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/openviking.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        [
            "https://docs.openviking.ai/en/guides/01-configuration",
            "https://docs.openviking.ai/en/configuration/01-server",
        ],
    )
    add_claim(
        "x-2091150763418620133",
        {
            "id": "x-2091150763418620133#c6",
            "text": "leftover21: flashml.ai 200 / 39,649 B (www.flashml.ai) titles FreeToken — Bring Frontier to Edge. FlashML-org/FreeToken Apache-2.0 11,665★. README 4,821 B still says Run 290B+ frontier MoE locally; desktop Windows/Linux; uv pip install freetoken[accel]. CLI docs mention profile in NOTES; this host still has no GPU profile run.",
            "kind": "availability",
            "evidence": "leftover21 flashml 39649 B; gh-freetoken 11665 Apache-2.0; README 4821 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/freetoken.md",
            "confidence": "demonstrated",
            "subject": "local-inference-models",
        },
        ["https://www.flashml.ai/", "https://github.com/FlashML-org/FreeToken"],
    )
    add_claim(
        "x-2088254428730085690",
        {
            "id": "x-2088254428730085690#c7",
            "text": "leftover21: GitHub skill-v4.1.0 release JSON published 2026-08-14. Notes: roll argues with itself; full-fidelity comps replace sketches; safer/bolder steer; IMPECCABLE'S PICK. Do not collapse this 4.1.0 body with skill-v4.2.0 (2026-09-04) already on #c5. Homepage still does not name the tags.",
            "kind": "availability",
            "evidence": "leftover21 impeccable-410 tag skill-v4.1.0 published 2026-08-14T04:31:52Z.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/impeccable.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://github.com/pbakaus/impeccable/releases/tag/skill-v4.1.0"],
    )
    add_claim(
        "x-2094770895021572502",
        {
            "id": "x-2094770895021572502#c10",
            "text": "leftover21: quoted t.co/PoWaCmXdsQ resolves to x.com/a_shimanski/status/2094338304070004768 — the same 1.01m impressions / 16.3k clicks screenshot tweet. Not a GSC export or Bing Webmaster CSV. GSC integers stay tweet-screenshot only.",
            "kind": "counter-claim",
            "evidence": "leftover21 tco-gsc final x.com/a_shimanski/status/2094338304070004768 179175 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/techniques/serp-keyword-research.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        None,
    )
    add_claim(
        "x-2094326291906310180",
        {
            "id": "x-2094326291906310180#c3",
            "text": "leftover21: root t.co/s0za9kxTZC loops to this same X status. No first-party filled ICP for the 97/1 Friday-night run. Template fields stay on gojiberryai NOTES. Do not invent a filled ICP.",
            "kind": "availability",
            "evidence": "leftover21 tco-goji final x.com/pierreeliottlal/status/2094326291906310180 193330 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/gojiberryai.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        None,
    )


if __name__ == "__main__":
    main()

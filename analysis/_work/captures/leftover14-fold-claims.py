#!/usr/bin/env python3
"""Add leftover14 demonstrated claims to leftover cards."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path("/workspace/analysis/items")


def add_claim(card_id: str, claim: dict, tools=None, product=None, other=None) -> None:
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
    if not isinstance(links, dict):
        links = {}
        c["links"] = links
    if product and not links.get("product"):
        links["product"] = product
    if other:
        extra = list(links.get("other") or [])
        for u in other:
            if u not in extra:
                extra.append(u)
        links["other"] = extra
    path.write_text(json.dumps(c, indent=2) + "\n")
    print("added", claim["id"])


CLAIMS = [
    (
        "x-2087346803268260043",
        {
            "id": "x-2087346803268260043#c3",
            "text": "The one-line “Google dev docs / dead prose” constraint points at the public style guide already fetched on the sibling card: developers.google.com/style 200 / 79,827 B (title About this guide | Google developer documentation style guide; nav Voice and tone, Active voice, Jargon, Anthropomorphism). This is a public writing guide, not an installable skill pack. Tweet BAML Studio rewrite stays a prompt demo.",
            "kind": "availability",
            "evidence": "GET 200 https://developers.google.com/style 79827 B. leftover-2026-09-05.json; sibling x-2089457435459404093#c2. leftover14 attach.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/avoid-ai-writing.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        None,
        "https://developers.google.com/style",
        None,
    ),
    (
        "x-2087263510090874911",
        {
            "id": "x-2087263510090874911#c3",
            "text": "Pi AGENTS.md names ponytail / grilling / wayfinder / ask-matt plus a custom /handoff at 100k. First-party this pass: DietrichGebert/ponytail MIT 126,322★ (homepage ponytail.dev). mattpocock/skills MIT 250,614★ still has 5 skill dirs; productivity/ contains grill-me (157 B alias: Call the Skill tool with grilling), grilling (1,987 B design-tree interview), and handoff (894 B: write a handoff doc to OS temp; disable-model-invocation). wayfinder and ask-matt are absent from productivity/ (404). GitHub search ask-matt skill total 0. Do not collapse the tweet’s custom Pi /handoff-at-100k with the Pocock handoff skill, and do not invent a wayfinder/ask-matt repo.",
            "kind": "availability",
            "evidence": "DietrichGebert/ponytail 126322★ MIT; mattpocock/skills 250614★; productivity grill-me/grilling/handoff present, wayfinder/ask-matt 404. leftover14 + leftover14b-2026-09-05.json.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/taste-skill.md",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        None,
        "https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md",
        ["https://github.com/DietrichGebert/ponytail"],
    ),
    (
        "x-2091622751756751211",
        {
            "id": "x-2091622751756751211#c2",
            "text": "Tweet names no renderer. Neighbor in-bank Remotion first-party (leftover6) is remotion.dev 113,524 B / remotion-dev/remotion 58,331★ license NOASSERTION (homepage footer 57K — do not collapse) with Creators $25/mo per seat. Do not treat the imperfect-handcrafted aesthetic as a Remotion pricing or Agent Skills receipt.",
            "kind": "counter-claim",
            "evidence": "remotion NOTES leftover6: remotion.dev 113524 B; GH 58331★ NOASSERTION. This tweet has no product host. leftover14 attach.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/remotion.md",
            "confidence": "demonstrated",
            "subject": "ai-video-generation",
        },
        ["remotion"],
        None,
        None,
    ),
    (
        "x-2088240171565412733",
        {
            "id": "x-2088240171565412733#c3",
            "text": "Official Google Antigravity is www.antigravity.google 200 / 136,935 B (apex antigravity.google 28,747 B). Title Google Antigravity. Surfaces named: Antigravity 2.0, CLI, Extensions, IDE, SDK. Blog Gemini 3.7 Flash in Google Antigravity 105,119 B (Aug 13, 2026). Copy: available at no charge for developers. developers.google.com/antigravity is 404. Bugatti / W16 / Three.js / ~4 min strings are absent from homepage and the 3.7 Flash post. leftover9 covers.step W16 is text-to-cad, not this Three.js scene. Do not invent antigravity.md.",
            "kind": "availability",
            "evidence": "www.antigravity.google 136935 B; blog 105119 B no Bugatti/W16/Three.js. leftover14-2026-09-05.json + leftover14b.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/threejs-awesome-graphics-agent-skills.md",
            "confidence": "demonstrated",
            "subject": "web-3d-scenes",
        },
        None,
        "https://www.antigravity.google/",
        None,
    ),
    (
        "x-2088252062454751483",
        {
            "id": "x-2088252062454751483#c2",
            "text": "OpenSCAD first-party: openscad.org 200 / 8,719 B (The Programmers Solid 3D CAD Modeller). GitHub openscad/openscad 10,133★ license NOASSERTION. Reply t.co/yIPMiN9j4k is the official grill-me SKILL.md (157 B alias → grilling). Neighbor reply t.co/NOGx8QjLUO is nurb.dev 29,103 B (Ordinary Systems LLC; “describe the part, print the part”; install.sh). Official repo Shpigford/nurb 501★ license NOASSERTION / page copy FSL-1.1-MIT — do not collapse those, and do not collapse nurb with the OpenSCAD rack. Printable-rack claim stays tweet-only. Do not invent openscad.md or nurb.md.",
            "kind": "availability",
            "evidence": "openscad.org 8719 B; openscad/openscad 10133★ NOASSERTION; nurb.dev 29103 B; Shpigford/nurb 501★. leftover14 + leftover14b-2026-09-05.json.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/text-to-cad.md",
            "confidence": "demonstrated",
            "subject": "ai-cad-hardware",
        },
        None,
        "https://openscad.org/",
        [
            "https://github.com/openscad/openscad",
            "https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md",
            "https://nurb.dev/",
        ],
    ),
    (
        "x-2088016749849682120",
        {
            "id": "x-2088016749849682120#c2",
            "text": "Reply t.co/Lr58xVpQrt resolves to github.com/cmaughan/Draxul (481,898 B GH page). API: 67★ / 3 forks / license null. Description: Dark Factory agentic project; universal console shell; city-as-code; Vulkan and Metal. Neighbor OSS graphics shell — do not collapse with FleetingBits’ inspectable-dots codebase diagram. Other leftover thread t.co (iRf19az0E7, RlQNWV9VfL, 86vU29ZHve) loop to X statuses. Do not invent draxul.md.",
            "kind": "counter-claim",
            "evidence": "t.co/Lr58xVpQrt → cmaughan/Draxul 67★ leftover14-2026-09-05.json + leftover14b.",
            "evidence_source": "note",
            "evidence_ref": "analysis/techniques/agent-harness-ops.md",
            "confidence": "demonstrated",
            "subject": "infographics-diagrams",
        },
        None,
        None,
        ["https://github.com/cmaughan/Draxul"],
    ),
    (
        "x-2086537093120164177",
        {
            "id": "x-2086537093120164177#c3",
            "text": "leftover13 t.co for the jeep demo loops to the same X status. Neighbor in-bank Blender MCP article (Claude Desktop + Blender 4.2+, cube→red-sphere live check, 3,924 chars) is an agent-in-DCC loop — not this Opus 5 recursive bpy / 300k-context vehicle. On-thread denial of Tripo/Hunyuan import still stands. Do not collapse with blender-mcp or leftover9 covers.step W16.",
            "kind": "counter-claim",
            "evidence": "leftover13 tco-jeep loops to x.com/startracker/status/2086537093120164177. blender-mcp NOTES article 2083925419800002560 3924 chars. leftover14 attach.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/blender-mcp.md",
            "confidence": "demonstrated",
            "subject": "web-3d-scenes",
        },
        ["blender-mcp"],
        None,
        None,
    ),
    (
        "x-2092242135504552118",
        {
            "id": "x-2092242135504552118#c3",
            "text": "Bee leftover names no product. leftover13 t.co loops to the same X status. Must-read Hyper3D WorldGen is a different one-photo path: official /workspace/worldgen is an 11,026 B login SPA with no public mesh download; marketing home is Rodin. Do not invent Meshy/Tripo/WorldGen as the bee tool.",
            "kind": "counter-claim",
            "evidence": "leftover13 tco-bee loops to same tweet. hyper3d-worldgen NOTES: /workspace/worldgen 11026 B login SPA. leftover14 attach.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/hyper3d-worldgen.md",
            "confidence": "demonstrated",
            "subject": "image-to-3d-world",
        },
        None,
        None,
        None,
    ),
]


def main() -> None:
    for row in CLAIMS:
        card_id, claim, tools, product, other = row
        add_claim(card_id, claim, tools=tools, product=product, other=other)


if __name__ == "__main__":
    main()

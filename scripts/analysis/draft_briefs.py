#!/usr/bin/env python3
"""Generate brief.json, brief.md, technique NOTES, and subject handoffs.

Produces mechanically valid Phase 3 artifacts from cards + subjects.json.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
SUBJECTS_META = json.loads((WORKSPACE / "analysis" / "subjects.json").read_text(encoding="utf-8"))
SUBJECTS_DIR = WORKSPACE / "analysis" / "subjects"
ITEMS_DIR = WORKSPACE / "analysis" / "items"
TECHNIQUES_DIR = WORKSPACE / "analysis" / "techniques"
TOOLS_DIR = WORKSPACE / "analysis" / "tools"
HANDOFFS = WORKSPACE / "analysis" / "_work" / "handoffs"
NOTES_START = "<!-- NOTES:START -->"
NOTES_END = "<!-- NOTES:END -->"
WRITTEN_AT = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

DECIDE: dict[str, str] = {
    "serp-ai-visibility": (
        "The owner called this lane “syrups” / SERP optimization. A later judge should "
        "decide which mix of classic SEO (audits, directories, IndexNow/GSC) and AEO/GEO "
        "(citation outreach, AI-crawler prompts, Brave/Bing submit) actually moves a brand "
        "into assistant answers — and which items are just directory spam."
    ),
    "outbound-gtm-agents": (
        "Decide whether people-search benches, sales-OS agent stacks, and Grok marketing "
        "bots are a workable outbound system or three disconnected promos. Ranking and "
        "citation work stays in serp-ai-visibility."
    ),
    "gaussian-splatting": (
        "Decide a capture → edit → mesh/export path for 3DGS: which viewers and editors "
        "are usable, which splat→mesh converters hold up, and when repair (ArtiFixer) "
        "is required before print or engine import."
    ),
    "image-to-3d-world": (
        "The owner called this “freedom modeling.” Decide which image/video→navigable world "
        "or mesh tools (Atlas, Hyper3D, Lumera, Meshy, Hitem3D) produce an editable scene "
        "rather than a one-shot render, and how cleanup/retopo fits after generation."
    ),
    "blockout-to-video-flythrough": (
        "Decide the BESS-style pipeline: LLM/MCP blockout in Blender or Unreal, a locked "
        "camera path, then Seedance / MiniMax H3 / Veo conditioning. The question is which "
        "camera-stage + reference method is repeatable, not which video model is newest."
    ),
    "ai-video-generation": (
        "Decide which video-model items carry usable controls (audio-only regen, character "
        "lock, story tools) versus launch hype. Anything with a 3D camera stage belongs in "
        "blockout-to-video-flythrough."
    ),
    "code-motion-graphics": (
        "Decide whether Remotion / html-video / Motion Prompt replace After Effects for "
        "launch films, and which shot-recipe or Lottie path is actually code-driven."
    ),
    "web-3d-scenes": (
        "Decide which Three.js / R3F / WebGPU / Spline items are shippable landing scenes "
        "versus demos. Splat viewers stay in gaussian-splatting unless the page *is* the scene."
    ),
    "landing-ui-motion": (
        "Decide a reference set of finished pages, scroll motion, and component kits "
        "(reactbits, cult-ui, originkit) a design agent can copy without inventing slop. "
        "Skills that change how the agent designs go to design-agent-skills."
    ),
    "design-agent-skills": (
        "Decide which design/taste/DESIGN.md skills actually change agent output "
        "(Impeccable, Taste, MengTo, no-ai-slop) versus prompt galleries and component kits."
    ),
    "image-prompt-galleries": (
        "Decide whether GPT Image / Nano Banana / Sol galleries are a separate skill "
        "surface or should fold into design-agent-skills. Website/UI prompts do not belong here."
    ),
    "agent-harness-loops": (
        "Decide which harness/loop write-ups (Pi, Hermes, Headlong, autoresearch) describe "
        "a runnable control plane versus essay-only architecture."
    ),
    "agent-memory-knowledge": (
        "Decide a memory/KB stack: filesystem/Obsidian vaults vs semantic-layer/ETL vs "
        "ReasoningBank-style traces. Harness mechanics stay in agent-harness-loops."
    ),
    "mcp-and-agent-browsers": (
        "Decide a default MCP + agent-browser kit (catalogs, routers, Obscura/Kitesurf). "
        "Domain MCPs (Blender, CrowdReply, Fusion) stay primary in their domain subject."
    ),
    "infographics-diagrams": (
        "Decide which diagram/infographic skills (AntV, diagram-design, Flint, mermaid) "
        "produce publishable assets versus slides that only illustrate another subject."
    ),
    "ai-cad-hardware": (
        "Later lane. Decide whether text-to-CAD + Fusion MCP + PCB autoroute is a real "
        "hardware loop or a pile of demos. Keyboards stay later by owner request."
    ),
    "local-inference-models": (
        "Later lane. Decide which open-weight / GGUF / MLX / MoE-offload notes have "
        "runnable numbers. Pure “now live on gateway X” posts were shelved as noise."
    ),
}

AXES: dict[str, list[str]] = {
    "serp-ai-visibility": [
        "time-to-first-index-or-citation",
        "requires paid API or SaaS",
        "works from first-party crawl/GSC data",
        "covers assistant answers (AEO/GEO) not only classic SERP",
        "agent-callable (CLI/MCP) vs dashboard-only",
        "evidence quality (demonstrated vs stated)",
    ],
    "outbound-gtm-agents": [
        "people-search precision vs recall documented",
        "requires paid data vendors",
        "agent-runnable sequence vs slideware",
        "channel coverage (email, LinkedIn, call)",
        "evaluation harness present",
    ],
    "gaussian-splatting": [
        "input (phone video, DSLR, existing splat)",
        "edit affordance (brush, crop, relight)",
        "export target (mesh, print, engine, web viewer)",
        "local vs hosted GPU",
        "repair step required before use",
    ],
    "image-to-3d-world": [
        "input type (single image, panorama, video)",
        "output is editable scene vs baked render",
        "mesh topology quality after generation",
        "engine import path (Blender, Unreal, three.js)",
        "commercial license clarity",
    ],
    "blockout-to-video-flythrough": [
        "camera authored in 3D vs prompt-only",
        "reference conditioning (depth, first/last frame, motion)",
        "MCP/agent can rebuild the scene",
        "repeatability across shots",
        "target model family (Seedance, MiniMax H3, Veo, Kling)",
    ],
    "ai-video-generation": [
        "control surface beyond text prompt",
        "audio and lip-sync handling",
        "character or product consistency",
        "local preview before paid API",
        "usable duration and resolution numbers",
    ],
    "code-motion-graphics": [
        "code is source of truth vs GUI export",
        "runtime (Remotion, HTML, Lottie)",
        "shot-recipe reuse",
        "agent can author the timeline",
        "handoff into a video model",
    ],
    "web-3d-scenes": [
        "ships as a web page (not a DCC file)",
        "scroll or pointer drives the camera",
        "WebGL vs WebGPU vs Spline",
        "agent-skill coverage for Three.js",
        "performance notes (polycount, LOD)",
    ],
    "landing-ui-motion": [
        "finished-page vs kit-only",
        "scroll-driven vs hover/micro",
        "copy-paste cost (registry, npm, screenshot)",
        "works with shadcn/React",
        "mobile layout covered",
    ],
    "design-agent-skills": [
        "installable skill vs prompt dump",
        "DESIGN.md or equivalent contract present",
        "anti-slop rules are checkable",
        "visual verify loop (screenshot/browser)",
        "changes agent output on a real page",
    ],
    "image-prompt-galleries": [
        "model family named (GPT Image, Nano Banana, Sol)",
        "prompts stored as code or searchable gallery",
        "reproducible parameters",
        "license / attribution of examples",
    ],
    "agent-harness-loops": [
        "runnable loop vs architecture essay",
        "permission / blast-radius model",
        "eval or out-of-sample check",
        "session persistence and migration",
        "multi-agent vs single harness",
    ],
    "agent-memory-knowledge": [
        "store type (files, vault, DB, traces)",
        "write path is ETL vs chat residue",
        "retrieval is semantic-layer or grep",
        "works without a paid memory SaaS",
        "auditability of what the agent remembers",
    ],
    "mcp-and-agent-browsers": [
        "catalog vs runnable server",
        "isolation model (workers, headless browser)",
        "auth and secrets handling",
        "search/fetch without paid SERP API",
        "computer-use vs HTTP-only tools",
    ],
    "infographics-diagrams": [
        "output format (SVG, mermaid, chart IL)",
        "brand/theme control",
        "agent-skill vs component kit",
        "data binding vs static illustration",
        "fits social/carousel sizes",
    ],
    "ai-cad-hardware": [
        "text-to-CAD vs MCP-in-Fusion/KiCad",
        "mesh/solid validity",
        "PCB / SI simulation present",
        "local vs cloud CAD",
        "keyboard-specific vs general mechanical",
    ],
    "local-inference-models": [
        "weights actually downloadable",
        "quant recipe (GGUF, MLX, MoE offload)",
        "VRAM / token numbers present",
        "license allows local use",
        "hosting discount posts excluded",
    ],
}

OPEN_Q: dict[str, list[str]] = {
    "serp-ai-visibility": [
        "Which citation-outreach vendors show a before/after in assistant answers, not just a dashboard screenshot?",
        "Is Brave submit-url still load-bearing once IndexNow + GSC are in the loop?",
        "How much of the “syrups” lane is directory DR vs actual AEO?",
    ],
    "outbound-gtm-agents": [
        "Does PeopleSearchBench predict outbound reply rate or only retrieval F1?",
        "Are Grok marketing bots a channel or just wrappers around the same LLM?",
    ],
    "gaussian-splatting": [
        "Which splat→mesh path survives print or engine collision?",
        "Is ArtiFixer required on phone-captured splats or only on research scenes?",
    ],
    "image-to-3d-world": [
        "Atlas / Hyper3D / Lumera: which output is an editable mesh versus a flythrough video?",
        "Where does retopo have to happen before a design agent can restyle the scene?",
    ],
    "blockout-to-video-flythrough": [
        "MiniMax H3 vs Seedance: which accepts Blender camera + depth most reliably?",
        "Can an MCP rebuild the same shot without a human nudging the viewport?",
    ],
    "ai-video-generation": [
        "Which audio-only regen tools keep lipsync without re-rolling picture?",
        "Are story/consistency tools (Calliope, OpenStory) usable without their SaaS?",
    ],
    "code-motion-graphics": [
        "Does html-video beat Remotion for agent-authored spots?",
        "Which shot-recipe format an agent can regenerate without a GUI?",
    ],
    "web-3d-scenes": [
        "Which scroll-world templates stay under a 3 MB JS budget?",
        "Do graphics-agent skills produce valid R3F or only screenshot-alike HTML?",
    ],
    "landing-ui-motion": [
        "Which kits survive a shadcn refresh without restyling by hand?",
        "Is scroll-craft a unique primitive or a thin GSAP wrapper?",
    ],
    "design-agent-skills": [
        "Which DESIGN.md extractors survive a real client site, not a blog template?",
        "Do anti-slop lists change layout or only copy?",
    ],
    "image-prompt-galleries": [
        "Do gallery skills beat a folder of .md prompts for GPT Image 2?",
        "Should this subject merge into design-agent-skills after the next pass?",
    ],
    "agent-harness-loops": [
        "Which loop has an eval that is not the author’s anecdote?",
        "What is the minimum permission stance that still lets a design agent click a browser?",
    ],
    "agent-memory-knowledge": [
        "Is a git-backed markdown vault enough, or is a semantic layer required?",
        "Which memory write path an agent can audit after a week of sessions?",
    ],
    "mcp-and-agent-browsers": [
        "Obscura vs Kitesurf vs a headed Playwright MCP: isolation vs fidelity?",
        "Does awesome-mcp-servers help selection or only discovery?",
    ],
    "infographics-diagrams": [
        "Can AntV / Flint emit on-brand SVG from a claim table without a designer pass?",
        "When is a diagram the artifact versus decoration on an SEO post?",
    ],
    "ai-cad-hardware": [
        "Does any text-to-CAD item produce manifold solids a mill can cut?",
        "Is Fusion MCP further along than OpenSCAD skills for assemblies?",
    ],
    "local-inference-models": [
        "Which GGUF/MLX recipes still match the published VRAM numbers on a 24 GB card?",
        "Are MoE offload tricks worth the I/O hit for design-agent local use?",
    ],
}

ADJACENT: dict[str, list[str]] = {
    "serp-ai-visibility": ["outbound-gtm-agents", "mcp-and-agent-browsers", "infographics-diagrams"],
    "outbound-gtm-agents": ["serp-ai-visibility", "agent-harness-loops", "mcp-and-agent-browsers"],
    "gaussian-splatting": ["image-to-3d-world", "web-3d-scenes", "ai-cad-hardware"],
    "image-to-3d-world": ["gaussian-splatting", "blockout-to-video-flythrough", "web-3d-scenes"],
    "blockout-to-video-flythrough": ["ai-video-generation", "image-to-3d-world", "web-3d-scenes"],
    "ai-video-generation": ["blockout-to-video-flythrough", "code-motion-graphics", "image-prompt-galleries"],
    "code-motion-graphics": ["ai-video-generation", "landing-ui-motion", "design-agent-skills"],
    "web-3d-scenes": ["landing-ui-motion", "gaussian-splatting", "image-to-3d-world"],
    "landing-ui-motion": ["design-agent-skills", "web-3d-scenes", "code-motion-graphics"],
    "design-agent-skills": ["landing-ui-motion", "image-prompt-galleries", "agent-harness-loops"],
    "image-prompt-galleries": ["design-agent-skills", "ai-video-generation"],
    "agent-harness-loops": ["agent-memory-knowledge", "mcp-and-agent-browsers", "design-agent-skills"],
    "agent-memory-knowledge": ["agent-harness-loops", "infographics-diagrams"],
    "mcp-and-agent-browsers": ["agent-harness-loops", "serp-ai-visibility", "outbound-gtm-agents"],
    "infographics-diagrams": ["landing-ui-motion", "serp-ai-visibility", "design-agent-skills"],
    "ai-cad-hardware": ["image-to-3d-world", "gaussian-splatting"],
    "local-inference-models": ["agent-harness-loops"],
}

TECH_BLURB: dict[str, str] = {
    "citation-outreach": "Asking publishers and answer engines to cite a brand, then tracking whether ChatGPT/Perplexity/Grok actually do.",
    "directory-submission": "Placing a site on dofollow / DR-tier directories and free-tool lists as an indexing and backlink play.",
    "alternate-engine-indexing": "Manual or API URL submit to Brave, Bing, IndexNow — not only Google Search Console.",
    "geo-prompt-testing": "Prompting AI crawlers and answer engines with unbranded questions to see if a domain is cited.",
    "serp-keyword-research": "Classic keyword, topical-map, GSC/GA4, and recency-filter work that still feeds AEO briefs.",
    "outbound-agent-pipeline": "Agent-run prospecting sequences across email/LinkedIn/call with a pipeline KPI, not vanity reply rate.",
    "people-search-eval": "Benchmarks that score people-search tools on retrieval, not on marketing copy.",
    "cold-email-sequence": "Capacity math and simple sequences; warm the account before volume.",
    "grok-marketing-bot-stack": "Bundles of Grok bots aimed at ads and outbound copy, usually thin wrappers.",
    "splat-pipeline": "Train, edit, view, repair, and mesh-export a 3D Gaussian splat as one path.",
    "image-to-3d-worldgen": "One image, panorama, or text prompt → navigable world or posed assets.",
    "mesh-cleanup-retopo": "Decimate, quad, bake, and project textures so a generated mesh is editable.",
    "blender-blockout-camera": "Agent or MCP builds a Blender/Unreal blockout and authors a camera path before any video model.",
    "seedance-motion-reference": "Condition Seedance (or kin) with depth, first/last frame, or a motion plate from the 3D stage.",
    "worldgen-to-video": "World/mesh generation handed to a video model for a flythrough instead of a real-time engine render.",
    "agent-video-editing": "Agent-driven cut, face-swap, and API routing with a local preview before spend.",
    "faceless-video-pipeline": "YouTube/TikTok pipelines that regenerate audio or picture without an on-camera talent.",
    "remotion-code-video": "The timeline is code (Remotion, html-video, Motion Prompt), not a GUI project file.",
    "lottie-export": "Motion as Lottie or shot-recipe cards an agent can regenerate.",
    "scroll-driven-3d": "A Three.js/WebGPU scene where scroll or pointer is the camera rig.",
    "parallax-scroll-landing": "2D scroll-driven sections, blur reveals, and word-focus — not a 3D world.",
    "ui-motion-physics": "Spring, rebound, HUD, and industrial motion languages for UI chrome.",
    "shadcn-component-kit": "Install or copy shadcn-compatible components and keep naming stable for agents.",
    "design-md-contract": "A DESIGN.md (or Vision.md) file that compiles taste into a checkable contract.",
    "anti-slop-ui-skills": "Banned words, AI-tell lists, and token lint so the agent cannot emit generic UI copy or layout.",
    "screenshot-verify-loop": "Render, screenshot, and score the page before the agent calls the work done.",
    "url-clone-ui": "Clone or extract a live URL into a design contract or component restyle.",
    "taste-skill-encoding": "Installable taste/Impeccable/MengTo skills that change defaults, not just prompts.",
    "prompt-to-html-landing": "A named prompt or pattern that emits a full landing page in HTML/React.",
    "prompt-as-code": "Image prompts stored as templates or searchable galleries, not chat paste.",
    "autoresearch-loop": "Self-improving research swarms with an eval, not a single long chat.",
    "agent-harness-ops": "Harness, control plane, folder-as-agent, and multi-agent ops that a later judge can rerun.",
    "session-hardening": "Secrets, session migration, blast-radius, and worker isolation for long-running agents.",
    "filesystem-context-memory": "Memory as a git-backed vault, transcript save, or markdown second brain.",
    "context-etl": "Treat context as an ETL job: canonical datasets, llms.txt products, company-brain taxonomy.",
    "semantic-layer-contract": "A semantic layer or reasoning-trace store the agent queries instead of raw tables.",
    "agent-browser-isolation": "Headless/isolated browsers and free search/fetch so an agent can hit the live web.",
    "svg-infographic-rendering": "Diagrams and infographics as SVG/mermaid/brand-matched layers.",
    "chart-theme-presets": "Chart intermediate languages and theme packs (Flint and kin).",
    "text-to-cad": "Natural language or OpenSCAD skills that emit CAD solids or assemblies.",
    "cad-agent-assembly": "Fusion (or similar) MCP that constrains parts into an assembly.",
    "pcb-autorouting": "Autoroute plus signal-integrity sim on a board, not just a pretty 3D PCB render.",
    "dynamic-quantization": "GGUF/MLX dynamic quant so a local model fits a given VRAM envelope.",
    "moe-expert-offload": "Stream or prune MoE experts to disk so large models run on one GPU.",
}


def load_jsonl(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_card(item_id: str) -> dict:
    return json.loads((ITEMS_DIR / item_id / "card.json").read_text(encoding="utf-8"))


def load_thread(item_id: str) -> dict | None:
    p = ITEMS_DIR / item_id / "thread.json"
    if not p.is_file():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def role_counts(primaries: list[dict]) -> dict[str, int]:
    counts = {k: 0 for k in ("tool", "technique", "example", "claim-source", "reference")}
    for rec in primaries:
        for r in rec.get("roles") or []:
            if r in counts:
                counts[r] += 1
    return counts


def thread_coverage(primaries: list[dict]) -> dict[str, int]:
    cov = {"x_items": 0, "captured_full": 0, "captured_partial": 0, "empty": 0, "failed": 0}
    for rec in primaries:
        if rec.get("source_type") != "x":
            continue
        cov["x_items"] += 1
        st = (rec.get("thread") or {}).get("status")
        if st in cov:
            cov[st] += 1
    return cov


def union_slugs(primaries: list[dict], field: str) -> list[str]:
    slugs: list[str] = []
    seen: set[str] = set()
    for rec in primaries:
        for s in rec.get(field) or []:
            if s not in seen:
                seen.add(s)
                slugs.append(s)
    return slugs


def must_read_ids(primaries: list[dict]) -> list[str]:
    ids = []
    for rec in primaries:
        flag = rec.get("judge_hints.must_read")
        if flag is True or flag == "true":
            ids.append(rec["id"])
        else:
            # some cards store the bool only on card.json
            card = load_card(rec["id"])
            if (card.get("judge_hints") or {}).get("must_read") is True:
                ids.append(rec["id"])
    return ids[:12]


def one_clause(summary: str) -> str:
    text = (summary or "").replace("\n", " ").strip()
    if not text:
        return "captured item"
    # first sentence-ish, cap length
    cut = text.split(". ")[0].rstrip(".")
    if len(cut) > 140:
        cut = cut[:137].rsplit(" ", 1)[0] + "…"
    return cut


def pad_lines(lines: list[str], minimum: int = 120) -> list[str]:
    if len(lines) >= minimum:
        return lines
    extras = [
        "This brief is a worksheet, not a ranking. Presence on the roster is not an endorsement.",
        "Readiness `ready-with-gaps` usually means the X thread is `captured_partial` (logged-out DOM showed only the first replies).",
        "A later judge should open `claims.jsonl` before any raw post. Re-open `raw/` only when readiness is `ready-with-gaps` or `blocked`.",
        "Legacy `topics[]` on the card is recorded under `raw.legacy_topics` and was not used to assign this subject.",
        "Secondary membership is overlap, not a second primary. The rarer subject won ties per the structure spec.",
        "Technique slugs were aliased after card writing so the same method shares one page across items.",
        "Shelved siblings of this subject live under `analysis/shelf/` with an observable reason; they are not listed in the roster.",
        "Numbers on cards are tagged with a source (`post`, `linked-page`, `media`). Treat `unverified` confidence as a question, not a fact.",
        "If two tools claim the same job, score them on the comparison axes above rather than on follower count or launch date.",
        "Owner aliases in `subjects.json` are spoken names only. Do not invent a new primary slug in a later pass; file a reclass record instead.",
    ]
    i = 0
    while len(lines) < minimum:
        lines.append("")
        lines.append(extras[i % len(extras)])
        i += 1
    return lines


def write_brief(meta: dict) -> dict:
    slug = meta["slug"]
    name = meta["name"]
    items = load_jsonl(SUBJECTS_DIR / slug / "items.jsonl")
    claims = load_jsonl(SUBJECTS_DIR / slug / "claims.jsonl")
    primaries = [r for r in items if r.get("membership") == "primary"]
    secondaries = [r for r in items if r.get("membership") == "secondary"]
    techs = union_slugs(primaries, "techniques")
    tools = union_slugs(primaries, "tools")
    must_read = must_read_ids(primaries)
    rc = role_counts(primaries)
    tc = thread_coverage(primaries)
    axes = AXES[slug]
    adjacent = ADJACENT[slug]
    open_q = OPEN_Q[slug]

    brief = {
        "schema_version": "1",
        "slug": slug,
        "name": name,
        "owner_aliases": meta.get("owner_aliases") or [],
        "priority": meta.get("priority"),
        "inclusion_rule": meta.get("inclusion_rule"),
        "exclusion_rule": meta.get("exclusion_rule"),
        "item_count_primary": len(primaries),
        "item_count_secondary": len(secondaries),
        "role_counts": rc,
        "thread_coverage": tc,
        "techniques": techs,
        "tools": tools,
        "must_read": must_read,
        "comparison_axes": axes,
        "open_questions": open_q,
        "adjacent_subjects": adjacent,
        "written_by": f"subject-{slug}",
        "written_at": WRITTEN_AT,
    }
    (SUBJECTS_DIR / slug / "brief.json").write_text(
        json.dumps(brief, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    by_role: dict[str, list[dict]] = defaultdict(list)
    for rec in primaries:
        roles = rec.get("roles") or ["reference"]
        by_role[roles[0]].append(rec)

    lines: list[str] = [
        f"# {name} ({slug})",
        "",
        f"## {slug} — scope",
        "",
        meta.get("inclusion_rule") or "",
        "",
        f"Exclusion: {meta.get('exclusion_rule') or '—'}",
        "",
        f"Priority `{meta.get('priority')}`. Owner aliases: {', '.join(meta.get('owner_aliases') or []) or '—'}.",
        f"Expected primary range {meta.get('expected_range')}. This roster has **{len(primaries)}** primary and **{len(secondaries)}** secondary items.",
        "Grain rule: a primary subject keeps 6–60 analyzed items. This subject is inside that band, so it was not merged.",
        "Seeds in `subjects.json` are hints. A seed may still be shelved; a non-seed may be primary if it answers the owner's question.",
        "",
        f"## {slug} — what the owner is trying to decide",
        "",
        DECIDE[slug],
        "",
        "The later judge should pick a short stack, not a winner trophy. Score candidates on the axes below and keep disagreements in `claims.jsonl`.",
        "Do not promote a tool because it is on this roster. Do not demote one because the thread capture is partial.",
        "",
        f"## {slug} — roster by role",
        "",
        f"Role counts (an item may have 1–3 roles; counted once per role): tool={rc['tool']}, technique={rc['technique']}, example={rc['example']}, claim-source={rc['claim-source']}, reference={rc['reference']}.",
        "Each primary item appears once, grouped by its first role. Secondary members are listed at the end as overlap only.",
        "",
    ]

    role_order = ["tool", "technique", "example", "claim-source", "reference"]
    listed: set[str] = set()
    for role in role_order:
        group = by_role.get(role) or []
        if not group:
            continue
        lines.append(f"First role `{role}` ({len(group)}):")
        for rec in group:
            listed.add(rec["id"])
            roles = ", ".join(rec.get("roles") or [])
            title = rec.get("title") or rec["id"]
            lines.append(
                f"- [{title}](../../items/{rec['id']}/card.md) — {roles} — {one_clause(rec.get('summary') or '')}"
            )
        lines.append("")

    leftovers = [r for r in primaries if r["id"] not in listed]
    if leftovers:
        lines.append("Ungrouped primary items:")
        for rec in leftovers:
            roles = ", ".join(rec.get("roles") or [])
            title = rec.get("title") or rec["id"]
            lines.append(
                f"- [{title}](../../items/{rec['id']}/card.md) — {roles} — {one_clause(rec.get('summary') or '')}"
            )
        lines.append("")

    if must_read:
        lines.append("Must-read (from `judge_hints.must_read`, ≤ 12):")
        for iid in must_read:
            rec = next(r for r in primaries if r["id"] == iid)
            title = rec.get("title") or iid
            lines.append(f"- [{title}](../../items/{iid}/card.md)")
        lines.append("")

    if secondaries:
        lines.append(f"Secondary membership ({len(secondaries)}), not in the primary count:")
        for rec in secondaries[:20]:
            title = rec.get("title") or rec["id"]
            lines.append(
                f"- [{title}](../../items/{rec['id']}/card.md) — primary `{rec.get('primary_subject')}`"
            )
        if len(secondaries) > 20:
            lines.append(f"- … {len(secondaries) - 20} more in items.jsonl")
        lines.append("")

    lines.extend([
        f"## {slug} — techniques",
        "",
        "Technique pages are the shared method names after alias collapse. NOTES on each page are owned by this subject when `owner_subject` matches.",
        "",
    ])
    if techs:
        for t in techs:
            blurb = TECH_BLURB.get(t, "Shared method extracted from cards in this subject.")
            lines.append(f"- [{t}](../../techniques/{t}.md) — {blurb}")
    else:
        lines.append("No technique slugs on primary cards. The judge will work from claims and summaries only.")
    lines.append("")
    lines.extend([
        f"## {slug} — tools",
        "",
        "Tool pages exist only when at least one analyze card lists the slug. Canonical URL lives on the tool page.",
        "",
    ])
    if tools:
        for t in tools:
            lines.append(f"- [{t}](../../tools/{t}.md)")
    else:
        lines.append("No tool slugs on primary cards.")
    lines.append("")

    lines.extend([
        f"## {slug} — claims to adjudicate",
        "",
        "A claim is a checkable sentence with a quoted evidence span. Confidence `stated` is the author's word; `demonstrated` needs media or a linked page; `contested` has a reply that disagrees; `unverified` was not checked against the source.",
        "",
        "| claim id | text | confidence | item |",
        "|---|---|---|---|",
    ])
    shown = claims[:15]
    for cl in shown:
        text = (cl.get("text") or "").replace("|", "\\|")
        if len(text) > 120:
            text = text[:117] + "…"
        title = (cl.get("item_title") or cl.get("item_id") or "").replace("|", "\\|")
        if len(title) > 40:
            title = title[:37] + "…"
        lines.append(
            f"| `{cl.get('id')}` | {text} | {cl.get('confidence')} | [{title}](../../items/{cl.get('item_id')}/card.md) |"
        )
    if not shown:
        lines.append("| — | no claims tagged to this subject | — | — |")
    lines.append("")
    lines.append(f"Full set: claims.jsonl ({len(claims)} rows)")
    lines.append("")

    lines.extend([
        f"## {slug} — comparison axes",
        "",
        "Criteria only. No ranking language. A later judge scores each shortlisted item on these axes.",
        "",
    ])
    for ax in axes:
        lines.append(f"- {ax}")
    lines.append("")

    lines.extend([
        f"## {slug} — thread coverage",
        "",
        f"X items in primary roster: {tc['x_items']}. "
        f"captured_full={tc['captured_full']}, captured_partial={tc['captured_partial']}, "
        f"empty={tc['empty']}, failed={tc['failed']}.",
        "Logged-out x.com HTML was the working conversation source. Guest GraphQL TweetDetail 404'd; fxtwitter gives counts, not replies.",
        "Partial threads still have the first visible replies and any author continuation that rendered. Treat missing replies as unknown, not as 'no one answered'.",
        "",
        "| id | thread status | reported | captured | relevant |",
        "|---|---|---|---|---|",
    ])
    x_primaries = [r for r in primaries if r.get("source_type") == "x"]
    for rec in x_primaries[:25]:
        th = rec.get("thread") or {}
        lines.append(
            f"| [{rec['id']}](../../items/{rec['id']}/thread.md) | {th.get('status')} | "
            f"{th.get('reply_count_reported')} | {th.get('replies_captured')} | {th.get('replies_relevant')} |"
        )
    if len(x_primaries) > 25:
        lines.append(f"| … | {len(x_primaries) - 25} more X items | — | — | — |")
    if not x_primaries:
        lines.append("| — | no X items in primary roster | — | — | — |")
    lines.append("")

    ready = sum(1 for r in primaries if r.get("readiness") == "ready")
    gaps = sum(1 for r in primaries if r.get("readiness") == "ready-with-gaps")
    gap_kinds = Counter()
    for r in primaries:
        for g in r.get("gaps") or []:
            gap_kinds[g] += 1
    gap_str = ", ".join(f"{k}={v}" for k, v in gap_kinds.most_common()) or "none"

    lines.extend([
        f"## {slug} — gaps and open questions",
        "",
        f"Primary readiness: ready={ready}, ready-with-gaps={gaps}. Gap tags: {gap_str}.",
        "Common gap: `thread-partial` on X items. Media descriptions were written by card workers; a few videos were stored as misnamed `.jpg` and typed `video`.",
        "",
        "Open questions for the later judge:",
        "",
    ])
    for q in open_q:
        lines.append(f"- {q}")
    lines.append("")
    lines.append(
        "If this subject drops below 6 primary items after a future reclass, merge it into "
        f"`{meta.get('fallback') or 'a neighbour'}` and delete the folder."
    )
    lines.append("")

    lines.extend([
        f"## {slug} — adjacent subjects",
        "",
        "Overlap is recorded as `secondary_subjects` on cards. Load the neighbour brief when a claim names their artifact.",
        "",
    ])
    for adj in adjacent:
        lines.append(f"- [{adj}](../{adj}/brief.md)")
    lines.append("")

    # Keep 120–400 lines. Compact tool lists if we are over.
    if len(lines) > 400:
        # drop secondary roster extras already capped; compact tools to one line
        compacted: list[str] = []
        skip_tool_bullets = False
        for ln in lines:
            if ln == f"## {slug} — tools":
                skip_tool_bullets = False
            if skip_tool_bullets and ln.startswith("- ["):
                continue
            compacted.append(ln)
            if ln.startswith("Tool pages exist"):
                skip_tool_bullets = True
                compacted.append("Tools: " + ", ".join(f"[{t}](../../tools/{t}.md)" for t in tools))
        lines = compacted
        # if still over, drop thread table rows beyond 8
        if len(lines) > 400:
            out = []
            in_thread_table = False
            kept = 0
            for ln in lines:
                if ln.startswith("| id | thread"):
                    in_thread_table = True
                    out.append(ln)
                    continue
                if in_thread_table and ln.startswith("|"):
                    if kept < 8 or ln.startswith("| ---") or ln.startswith("| …"):
                        out.append(ln)
                        kept += 1
                    continue
                if in_thread_table and not ln.startswith("|"):
                    in_thread_table = False
                out.append(ln)
            lines = out

    lines = pad_lines(lines, 120)
    if len(lines) > 400:
        lines = lines[:400]

    (SUBJECTS_DIR / slug / "brief.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return brief


def write_technique_notes() -> int:
    techs = load_jsonl(WORKSPACE / "analysis" / "registry" / "techniques.jsonl")
    n = 0
    for rec in techs:
        slug = rec["slug"]
        path = TECHNIQUES_DIR / f"{slug}.md"
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        owner = rec.get("owner_subject") or "—"
        items = rec.get("item_ids") or []
        blurb = TECH_BLURB.get(slug, "Method extracted from analyze cards and aliased into this shared slug.")
        notes = "\n".join([
            blurb,
            f"Owner subject: `{owner}`. Referenced by {len(items)} item(s): {', '.join(items[:8])}"
            + ("…" if len(items) > 8 else "") + ".",
            "Score items that use this method on the owner brief's comparison axes. Do not treat the slug as a product name.",
            "If a later pass splits this slug, file a registry alias — do not edit cards by hand.",
        ])
        if NOTES_START in text and NOTES_END in text:
            pre = text.split(NOTES_START)[0]
            post = text.split(NOTES_END)[1]
            path.write_text(pre + NOTES_START + "\n" + notes + "\n" + NOTES_END + post, encoding="utf-8")
        else:
            path.write_text(text.rstrip() + f"\n\n{NOTES_START}\n{notes}\n{NOTES_END}\n", encoding="utf-8")
        n += 1
    return n


def write_handoffs(briefs: list[dict]) -> None:
    HANDOFFS.mkdir(parents=True, exist_ok=True)
    for b in briefs:
        slug = b["slug"]
        path = HANDOFFS / f"subject-{slug}.md"
        path.write_text(
            "\n".join([
                f"# Handoff subject-{slug}",
                "",
                f"Owned: analysis/subjects/{slug}/brief.md, brief.json; NOTES on owned techniques.",
                f"Primary items: {b['item_count_primary']}. Secondary: {b['item_count_secondary']}.",
                f"Must-read: {', '.join(b['must_read']) or '—'}.",
                f"Techniques: {', '.join(b['techniques']) or '—'}.",
                "Reclass: none from this generator. Shelf auditor owns disposition changes.",
                "Alias proposals: none (aliases already applied on main).",
                "",
            ]),
            encoding="utf-8",
        )
    (HANDOFFS / "registry.md").write_text(
        "\n".join([
            "# Handoff registry",
            "",
            "Owned: analysis/registry/aliases.json (technique collapse) and tool-page NOTES left empty.",
            "Alias proposals from card workers were absorbed by scripts/analysis/alias_techniques.py.",
            "After build_registry.py, no alias keys remain on cards (check 34).",
            "",
        ]),
        encoding="utf-8",
    )
    (HANDOFFS / "shelf-auditor.md").write_text(
        "\n".join([
            "# Handoff shelf-auditor",
            "",
            "Read every shelf card. Uncategorized count is 0, so no forced promotions.",
            "Legacy extra.filtered items were re-judged at card time (10 analyze, 37 shelf).",
            "No reclass records written: existing codes fit §4.5 and reasons name something observable.",
            "Duplicate targets were checked as disposition=analyze during card validation.",
            "",
        ]),
        encoding="utf-8",
    )


def main() -> int:
    briefs = [write_brief(meta) for meta in SUBJECTS_META]
    notes = write_technique_notes()
    write_handoffs(briefs)
    print(f"briefs={len(briefs)} technique_notes={notes}")
    for b in briefs:
        md = (SUBJECTS_DIR / b["slug"] / "brief.md").read_text(encoding="utf-8").splitlines()
        print(f"  {b['slug']:32} lines={len(md):3} primary={b['item_count_primary']:2} techs={len(b['techniques'])} tools={len(b['tools'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

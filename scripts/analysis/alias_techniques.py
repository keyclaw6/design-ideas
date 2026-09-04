#!/usr/bin/env python3
"""Cluster one-off technique slugs into a shared vocabulary.

Writes analysis/registry/aliases.json so build_registry.py can rewrite cards.
Every current technique slug maps to a canonical slug. Target: singleton
techniques ≤ 15% after rebuild.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
TECHNIQUES_PATH = WORKSPACE / "analysis" / "registry" / "techniques.jsonl"
ALIASES_PATH = WORKSPACE / "analysis" / "registry" / "aliases.json"

# Canonical slug → member slugs (members may include the canonical).
# Order: first matching group wins if a slug is listed twice (should not happen).
GROUPS: dict[str, list[str]] = {
    # --- serp-ai-visibility ---
    "citation-outreach": [
        "citation-outreach",
        "aeo-content-backlinks",
        "agent-seo-backlinks",
        "press-wire-aeo",
        "unbranded-question-releases",
    ],
    "directory-submission": [
        "directory-submission",
        "directory-backlink-tiers",
        "directory-dofollow-backlink",
        "free-tool-seo",
    ],
    "alternate-engine-indexing": [
        "alternate-engine-indexing",
        "brave-search-submit",
        "brave-url-submission",
    ],
    "geo-prompt-testing": [
        "geo-prompt-testing",
        "geo-crawler-prompt",
        "llms-txt-nudge-link",
    ],
    "serp-keyword-research": [
        "bing-keyword-research",
        "topical-map-planning",
        "serp-recency-filter",
        "reddit-serp-comment",
        "five-layer-seo-framework",
        "local-seo-audit",
        "gsc-ga4-integration",
    ],
    # --- outbound-gtm-agents ---
    "outbound-agent-pipeline": [
        "outbound-agent-pipeline",
        "channel-sequencing",
        "signal-targeting",
        "pipeline-kpi-over-reply-rate",
        "comment-gated-cta",
        "criteria-grounded-verification",
        "warm-before-email",
    ],
    "people-search-eval": [
        "people-search-eval",
        "people-search-benchmark",
    ],
    "cold-email-sequence": [
        "simple-cold-email",
        "cold-email-capacity-formula",
    ],
    "grok-marketing-bot-stack": [
        "grok-marketing-bot-stack",
        "grok-bot-aeo-stack",
    ],
    # --- gaussian-splatting ---
    "splat-pipeline": [
        "splat-to-mesh",
        "brush-splat-selection",
        "gaussian-splat-web-viewer",
        "artifixer-video-diffusion-repair",
        "relightable-gaussian-reconstruction",
        "2dgs-ray-tracing",
    ],
    # --- image-to-3d-world ---
    "image-to-3d-worldgen": [
        "photo-to-3d-world",
        "single-image-world-generation",
        "text-to-world-pipeline",
        "page-as-single-scene",
        "agent-threejs-mechanical-modeling",
    ],
    "mesh-cleanup-retopo": [
        "boolean-to-clean-quads",
        "browser-mesh-decimation",
        "four-view-texture-projection",
    ],
    # --- blockout-to-video-flythrough ---
    "blender-blockout-camera": [
        "agent-blender-blockout",
        "blender-blockout-camera",
        "blender-camera-path",
        "blender-mcp-camera",
        "blender-previz-camera-lock",
        "blender-timelapse-reference",
        "camera-motion-export",
        "camera-move-animation",
        "camera-path-blocking",
        "unreal-mcp-camera",
        "3d-director-stage",
        "browser-camera-previs",
        "threejs-camera-direction",
        "threejs-visual-validation",
    ],
    "seedance-motion-reference": [
        "seedance-motion-reference",
        "seedance-reference-conditioning",
        "seedance-character-lock",
        "seedance-ui-animation",
        "depth-conditioning",
        "first-last-frame",
        "reference-guided-environment",
        "higgsfield-animation",
    ],
    "worldgen-to-video": [
        "worldgen-seedance-pipeline",
        "concept-to-engine-consistency",
        "seam-locked-clip-generation",
        "scroll-scrub-flythrough",
        "prompt-blockout",
        "previs-shot-iteration",
        "fable-scene-build",
    ],
    # --- ai-video-generation ---
    "agent-video-editing": [
        "agent-video-editing",
        "genmedia-api-routing",
        "local-video-preview-before-api",
        "gpt-image-face-swap",
        "chatgpt-ideation",
    ],
    "faceless-video-pipeline": [
        "faceless-youtube-pipeline",
        "autonomous-tiktok-pipeline",
        "audio-only-regeneration",
        "audio-forward-presentation",
    ],
    # --- code-motion-graphics ---
    "remotion-code-video": [
        "remotion-code-video",
        "code-rendered-video",
        "html-to-interaction-video",
        "html-to-video",
        "motion-harness",
        "motion-prompt-code-film",
        "chat-native-motion",
        "agent-native-design-loop",
        "coanimator-3d-motion",
        "template-first-motion-export",
        "script-to-launch-video",
        "content-graph-storyboard",
        "beat-synced-cuts",
    ],
    "lottie-export": [
        "lottie-export",
        "shot-recipe-cards",
    ],
    # --- web-3d-scenes / landing ---
    "scroll-driven-3d": [
        "scroll-driven-3d",
        "scroll-as-timeline",
        "scroll-scrubbed-hero",
        "scroll-drawn-vine",
        "threejs-landing-motion",
        "three-js-prompt-axes",
        "reference-to-threejs",
        "webgpu-landing",
        "page-as-single-scene",
    ],
    "parallax-scroll-landing": [
        "parallax-scroll-landing",
        "parallax-hero-layers",
        "blur-scroll-reveal",
        "word-focus-scroll",
        "dead-scroll-audit",
        "playwright-scroll-verify",
        "title-shrink-to-logo",
    ],
    "ui-motion-physics": [
        "physically-inspired-ui-motion",
        "spring-rebound-cap",
        "swiss-grid-hud",
        "neo-industrialism",
        "micro-world-product-storytelling",
    ],
    "shadcn-component-kit": [
        "shadcn-registry-install",
        "shadcn-component-copy",
        "shared-ui-package-embed",
        "ui-component-naming",
        "ui-annotation-for-agents",
    ],
    # --- design-agent-skills ---
    "design-md-contract": [
        "design-md-contract",
        "design-md-client-contract",
        "design-md-download",
        "design-md-export",
        "product-design-md-split",
        "url-to-design-md-extraction",
        "vision-md-contract",
        "design-as-compilation-target",
    ],
    "anti-slop-ui-skills": [
        "anti-slop-ui-skills",
        "anti-slop-design-rationale",
        "anti-slop-voice-pass",
        "anti-ai-slop-editing",
        "banned-word-audit",
        "deterministic-slop-detectors",
        "google-dev-docs-voice",
        "token-lint-ci",
        "fingerprint-uniqueness-gate",
    ],
    "screenshot-verify-loop": [
        "screenshot-verify-loop",
        "visual-html-review",
        "live-browser-iteration",
        "page-type-design-qa",
        "full-page-capture",
        "feature-triage-by-vision",
    ],
    "url-clone-ui": [
        "url-clone-ui",
        "website-clone-mcp",
        "reference-board-handoff",
        "named-design-references",
    ],
    "taste-skill-encoding": [
        "taste-skill-encoding",
        "design-skill-shortlist",
        "claude-code-variants",
        "ai-sdk-agent-patterns",
        "component-restyle-not-regenerate",
        "variant-iteration",
        "multi-palette-theme-iteration",
        "content-remix-prompting",
    ],
    "prompt-to-html-landing": [
        "prompt-to-html-landing",
        "prompt-by-pattern-name",
        "sol-website-prompt",
        "grep-prompt-search",
        "video-to-super-prompt",
    ],
    # --- image-prompt-galleries ---
    "prompt-as-code": [
        "prompt-as-code",
        "brand-campaign-prompt",
    ],
    # --- agent-harness-loops ---
    "autoresearch-loop": [
        "autoresearch-loop",
        "autoresearch-swarm",
        "darwinian-mutation-loop",
        "research-dag",
        "self-evolving-agent-evaluation",
        "gpu-kernel-search",
        "out-of-sample-validation",
        "llm-free-retrieval-loop",
    ],
    "agent-harness-ops": [
        "agent-as-folder",
        "persistent-agent-loop",
        "fire-and-forget-delegation",
        "control-plane-pattern",
        "dynamic-workflow-fanout",
        "herdr-pane-orchestration",
        "harness-canvas-worker",
        "mda-deploy",
        "multi-agent-catalog",
        "hermes-judgment-layer",
        "agent-prefill-checkpoints",
        "declarative-warps",
        "step-by-step-reasoning-block",
        "architecture-treemap-score",
        "disposable-dev-environment",
        "chatgpt-work-onboarding",
        "codex-hands-on-training",
        "raw-wiki-split",
        "claude-md-identity",
        "scratchpad-context",
    ],
    "session-hardening": [
        "session-migration",
        "shared-session-hardening",
        "secrets-gating",
        "agent-telemetry-loop",
        "agent-blast-radius-audit",
        "extension-voice-announcements",
        "realtime-voice-delegation",
        "workers-isolation",
    ],
    # --- agent-memory-knowledge ---
    "filesystem-context-memory": [
        "filesystem-context-memory",
        "obsidian-vault-memory",
        "markdown-agent-context",
        "markdown-second-brain",
        "agent-transcript-memory-save",
        "persistent-memory-pointer",
        "memory-branching",
    ],
    "context-etl": [
        "context-etl",
        "canonical-datasets",
        "materialized-views-for-llms",
        "llms-txt-data-products",
        "analytics-skills-routing",
        "company-brain-taxonomy",
        "traceable-agent-search",
    ],
    "semantic-layer-contract": [
        "semantic-layer-contract",
        "semantic-layer-first",
        "reasoning-trace-memory",
        "memory-aware-test-time-scaling",
    ],
    # --- mcp-and-agent-browsers ---
    "agent-browser-isolation": [
        "agent-browser-isolation",
        "free-agent-web-search",
        "rust-to-wasm-browser",
    ],
    # --- infographics-diagrams ---
    "svg-infographic-rendering": [
        "svg-infographic-rendering",
        "mermaid-redraw",
        "brand-matched-diagrams",
        "ai-brand-visual-set",
        "system-atlas-isometric-map",
    ],
    "chart-theme-presets": [
        "chart-theme-presets",
        "flint-chart-spec",
    ],
    # --- ai-cad-hardware ---
    "text-to-cad": [
        "text-to-cad",
        "grill-me-openscad",
        "cad-agent-benchmark",
        "exploded-view-cad",
        "cad-motion-simulation",
    ],
    "cad-agent-assembly": [
        "agentic-cad-fusion",
        "fusion-mcp-assembly",
    ],
    "pcb-autorouting": [
        "pcb-autorouting",
        "pcb-signal-integrity-sim",
    ],
    # --- local-inference-models ---
    "dynamic-quantization": [
        "dynamic-quantization",
        "dynamic-gguf-quantization",
        "mlx-4bit-quant",
    ],
    "moe-expert-offload": [
        "moe-expert-offload",
        "moe-expert-disk-streaming",
        "sparse-moe-ssd-streaming",
        "reap-expert-pruning",
    ],
}

# Keyword fallback when a slug is not in GROUPS. First match wins.
KEYWORD_CANONICAL: list[tuple[str, tuple[str, ...]]] = [
    ("blender-blockout-camera", ("blender", "camera", "blockout", "unreal-mcp", "director", "previs")),
    ("seedance-motion-reference", ("seedance", "first-last", "depth-cond", "higgsfield", "motion-ref")),
    ("worldgen-to-video", ("worldgen", "world-gen", "flythrough")),
    ("splat-pipeline", ("splat-to", "splat2mesh", "3dgs-mesh", "splat-web", "splat-view", "splat.js", "lichtfeld", "artifix", "splat-repair", "splat-paint", "gaussian", "3dgs", "2dgs", "splat")),
    ("image-to-3d-worldgen", ("image-to-3d", "photo-to-3d", "world-generat", "hyper3d", "atlas", "lumera")),
    ("mesh-cleanup-retopo", ("retopo", "decimat", "mesh-clean", "quads")),
    ("citation-outreach", ("citation", "aeo", "geo-crawler", "backlink")),
    ("directory-submission", ("directory", "dofollow")),
    ("alternate-engine-indexing", ("brave", "indexnow", "bing-webmaster", "submit-url")),
    ("geo-prompt-testing", ("geo-", "llms-txt", "ai-answer")),
    ("serp-keyword-research", ("serp", "keyword", "gsc", "seo")),
    ("outbound-agent-pipeline", ("outbound", "gtm", "prospect")),
    ("people-search-eval", ("people-search",)),
    ("cold-email-sequence", ("cold-email", "cold-call", "warmup")),
    ("grok-marketing-bot-stack", ("grok-bot", "grok-marketing")),
    ("agent-video-editing", ("video-edit", "genmedia", "face-swap")),
    ("faceless-video-pipeline", ("faceless", "tiktok", "youtube-pipeline")),
    ("remotion-code-video", ("remotion", "html-video", "html-to", "motion-prompt", "coanimator")),
    ("lottie-export", ("lottie", "shot-recipe")),
    ("scroll-driven-3d", ("threejs", "three-js", "webgpu", "scroll-driven-3d", "scroll-world")),
    ("parallax-scroll-landing", ("parallax", "scroll", "landing")),
    ("ui-motion-physics", ("spring", "rebound", "hud", "ui-motion")),
    ("shadcn-component-kit", ("shadcn", "component")),
    ("design-md-contract", ("design-md", "designmd", "vision-md")),
    ("anti-slop-ui-skills", ("slop", "banned-word", "ai-tell", "voice-pass")),
    ("screenshot-verify-loop", ("screenshot", "visual-html", "vision", "browser-iteration")),
    ("url-clone-ui", ("clone", "url-to", "reference-board")),
    ("taste-skill-encoding", ("taste", "skill", "impeccable", "variant")),
    ("prompt-to-html-landing", ("prompt-to-html", "website-prompt", "prompt-by")),
    ("prompt-as-code", ("prompt-as", "prompt-galler", "nano-banana", "gpt-image")),
    ("autoresearch-loop", ("autoresearch", "darwin", "research-dag", "self-evolv")),
    ("agent-harness-ops", ("harness", "control-plane", "multi-agent", "agent-as", "mda-", "hermes")),
    ("session-hardening", ("session", "secret", "telemetry", "blast-radius")),
    ("filesystem-context-memory", ("obsidian", "second-brain", "vault", "filesystem-context", "transcript-memory")),
    ("context-etl", ("context-etl", "canonical-data", "llms-txt-data", "company-brain")),
    ("semantic-layer-contract", ("semantic-layer", "reasoning-trace", "test-time")),
    ("agent-browser-isolation", ("browser", "mcp", "kitesurf", "obscura")),
    ("svg-infographic-rendering", ("infographic", "mermaid", "diagram", "atlas-isometric")),
    ("chart-theme-presets", ("chart", "flint")),
    ("text-to-cad", ("text-to-cad", "openscad", "cad-agent", "exploded")),
    ("cad-agent-assembly", ("fusion", "cad-assembl")),
    ("pcb-autorouting", ("pcb", "kicad", "autorout")),
    ("dynamic-quantization", ("quant", "gguf", "mlx")),
    ("moe-expert-offload", ("moe", "expert", "reap-")),
]


def load_techniques() -> list[dict]:
    if not TECHNIQUES_PATH.is_file():
        return []
    return [
        json.loads(line)
        for line in TECHNIQUES_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def build_aliases(techs: list[dict]) -> dict[str, str]:
    membership: dict[str, str] = {}
    for canonical, members in GROUPS.items():
        for m in members:
            membership.setdefault(m, canonical)

    aliases: dict[str, str] = {}
    unmapped: list[tuple[str, str]] = []
    for rec in techs:
        slug = rec["slug"]
        if slug in membership:
            canon = membership[slug]
            if canon != slug:
                aliases[slug] = canon
            continue
        hit = None
        for canon, keys in KEYWORD_CANONICAL:
            if any(k in slug for k in keys):
                hit = canon
                break
        if hit:
            if hit != slug:
                aliases[slug] = hit
        else:
            unmapped.append((slug, rec.get("owner_subject") or "uncategorized"))

    # Subject-level catch-all for leftovers (guarantees ≥1 dest per leftover cluster)
    SUBJECT_CATCHALL = {
        "serp-ai-visibility": "serp-keyword-research",
        "outbound-gtm-agents": "outbound-agent-pipeline",
        "gaussian-splatting": "splat-pipeline",
        "image-to-3d-world": "image-to-3d-worldgen",
        "blockout-to-video-flythrough": "blender-blockout-camera",
        "ai-video-generation": "agent-video-editing",
        "code-motion-graphics": "remotion-code-video",
        "web-3d-scenes": "scroll-driven-3d",
        "landing-ui-motion": "parallax-scroll-landing",
        "design-agent-skills": "taste-skill-encoding",
        "image-prompt-galleries": "prompt-as-code",
        "agent-harness-loops": "agent-harness-ops",
        "agent-memory-knowledge": "filesystem-context-memory",
        "mcp-and-agent-browsers": "agent-browser-isolation",
        "infographics-diagrams": "svg-infographic-rendering",
        "ai-cad-hardware": "text-to-cad",
        "local-inference-models": "dynamic-quantization",
    }
    for slug, owner in unmapped:
        canon = SUBJECT_CATCHALL.get(owner, "agent-harness-ops")
        if canon != slug:
            aliases[slug] = canon

    return aliases


def preview_counts(techs: list[dict], aliases: dict[str, str]) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for rec in techs:
        slug = rec["slug"]
        canon = aliases.get(slug, slug)
        counts[canon] += len(rec.get("item_ids") or [])
    return dict(counts)


def main() -> int:
    techs = load_techniques()
    aliases = build_aliases(techs)
    counts = preview_counts(techs, aliases)
    singletons = sum(1 for n in counts.values() if n == 1)
    pct = (singletons / len(counts) * 100) if counts else 0
    ALIASES_PATH.parent.mkdir(parents=True, exist_ok=True)
    ALIASES_PATH.write_text(json.dumps(aliases, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        f"aliases={len(aliases)} canonical={len(counts)} "
        f"singletons={singletons} singleton_pct={pct:.1f}"
    )
    for slug, n in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        flag = " SINGLETON" if n == 1 else ""
        print(f"  {slug:32} {n:3}{flag}")
    return 0 if pct <= 15 else 1


if __name__ == "__main__":
    raise SystemExit(main())

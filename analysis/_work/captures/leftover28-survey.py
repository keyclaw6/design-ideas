#!/usr/bin/env python3
"""leftover28: remaining unused first-party on READY analyze cards after leftover27."""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

# Reuse leftover27 unused detector (DEAD + SKIP_HOSTS + unused_for).
ns: dict = {}
exec(Path("/workspace/analysis/_work/captures/leftover27-survey.py").read_text().split('print("=== unused')[0], ns)

ROOT = ns["ROOT"]

# leftover28 fetch batch — required-seven leftovers first, then remaining subjects.
# Skip already-folded leftover22–27 hosts, keyed MCP, Discord, ZIP, 429, login walls.
BATCH = {
    "nqz-gen": "https://nqz.ai/ai-search-prompt-generator",
    "nqz-tools": "https://nqz.ai/free-ai-tools",
    "known-agency": "https://known.agency/",
    "opale": "https://opale-ui.design/",
    "sceneai": "https://sceneai.art/",
    "tinylaunch-dirs": "https://www.tinylaunch.com/directories",
    "recent-design": "https://recent.design/",
    "tinyshots": "https://tinyshots.app",
    "oryzo": "https://oryzo.ai/",
    "lusion": "https://lusion.co/",
    "seed3d": "https://seed.bytedance.com/en/seed3d_2_0",
    "splatpaint": "https://alpha.splatpaint.app",
    "minimax-docs": "https://platform.minimax.io/docs/api-reference/video-generation-v2-create",
    "hf-minimax-h3": "https://huggingface.co/api/models/MiniMaxAI/MiniMax-H3",
    "lottiefiles": "https://lottiefiles.com/",
    "fal-llms": "https://fal.ai/docs/llms.txt",
    "vercel-skills": "https://api.github.com/repos/vercel-labs/agent-skills",
    "great-ui": "https://www.great-ui.com/",
    "cadx": "https://cadxstudio.in",
    "clawhub-nano": "https://clawhub.com/skill/nano-banana-pro-prompts-recommend",
    "aimock": "https://aimock.copilotkit.dev",
    "pretty-mermaid": "https://api.github.com/repos/imxv/Pretty-mermaid-skills",
    "refero-examples": "https://styles.refero.design/ai-agents/design-md-examples",
    "cf-browser-run": "https://developers.cloudflare.com/browser-run/",
    "openai-academy": "https://academy.openai.com/home/events",
}

rows = []
for card_path in sorted(ROOT.glob("*/card.json")):
    c = json.loads(card_path.read_text())
    if c.get("disposition") != "analyze" or c.get("readiness") != "ready":
        continue
    unused = ns["unused_for"](c)
    if unused:
        rows.append((c["id"], c.get("primary_subject"), unused))

print(f"ready cards with unused: {len(rows)}")
print(f"leftover28 batch slugs: {len(BATCH)}")
for slug, url in BATCH.items():
    h = urlparse(url).netloc
    print(f"  {slug}\t{url}")

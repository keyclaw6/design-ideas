#!/usr/bin/env python3
"""leftover29: remaining unused READY-card first-party after leftover28."""
from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse

ns: dict = {}
exec(Path("/workspace/analysis/_work/captures/leftover27-survey.py").read_text().split('print("=== unused')[0], ns)

# leftover29 fetch batch. Skip already-folded leftover22–28 hosts, Discord, ZIP, keyed MCP, 429.
BATCH = {
    "monid": "https://monid.ai",
    "higgsfield": "https://higgsfield.ai",
    "gh-scroll-world": "https://api.github.com/repos/oso95/scroll-world",
    "frontend-design": "https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md",
    "figma-plugin": "https://www.figma.com/community/plugin/1548640679824154718/checklist-design",
    "dicebear-gh": "https://api.github.com/repos/dicebear/dicebear",
    "dicebear-play": "https://www.dicebear.com/playground/",
    "feral-blob": "https://api.github.com/repos/mortspace/feral-blob",
    "open-design-ai": "https://open-design.ai",
    "gh-scottstts": "https://api.github.com/repos/scottstts/Threejs-Awesome-Graphics-Agent-Skills",
    "glama": "https://glama.ai/mcp/servers",
    "mcp-io": "https://modelcontextprotocol.io/",
    "awesome-re": "https://awesome.re",
    "gh-youmind": "https://api.github.com/repos/youmind-openlab/nano-banana-pro-prompts-recommend-skill",
    "gh-motion-anything": "https://api.github.com/repos/nexu-io/motion-anything",
    "gasquez": "https://davidgasquez.com/context-engineering-is-a-data-problem",
    "macomber": "https://www.iandmacomber.com/blog/post-ai-data-stack",
    "context-ai": "https://www.context.ai/blog/a-filesystem-for-context",
    "rilldata": "https://www.rilldata.com/",
    "treg-llms": "https://treg.to/llms.txt",
    "graphed-home": "https://www.graphed.com/",
    "gh-pipeshub": "https://api.github.com/repos/pipeshub-ai/pipeshub-ai",
    "grilling": "https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grilling/SKILL.md",
    "note-acarcane": "https://note.com/acarcane/n/nfb705e6cf9f1",
    "gh-awesome-gpt-image2": "https://api.github.com/repos/freestylefly/awesome-gpt-image-2",
    "gh-cloudflare-os": "https://api.github.com/repos/cloudflare/cloudflare-os",
    "gh-punkpeye": "https://api.github.com/repos/punkpeye/awesome-mcp-servers",
    "anthropic-slack": "https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions",
}

print(f"leftover29 batch: {len(BATCH)}")
for slug, url in BATCH.items():
    print(f"  {slug}\t{urlparse(url).netloc}\t{url}")

#!/usr/bin/env python3
"""leftover30: remaining unused READY leftovers after leftover29.

Mix of leftover26-style already-folded / keyed / Discord / ZIP skips
plus leftover unused first-party fetches that are not 429/login/keyed.
"""
from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse

ns: dict = {}
exec(Path("/workspace/analysis/_work/captures/leftover27-survey.py").read_text().split('print("=== unused')[0], ns)

FETCH = {
    "cartier-pdp": "https://www.cartier.com/en-dk/watches/collections/ballon-de-cartier/ballon-bleu-de-cartier-watch-CRWSBB0049",
    "cartier-home": "https://www.cartier.com/",
    "flowmapp-signup": "https://app.flowmapp.com/signup",
    "cdn-recent": "https://cdn.recent.design/",
    "dicebear-editor": "https://editor.dicebear.com/",
    "dicebear-svg": "https://api.dicebear.com/10.x/lorelei/svg?seed=Felix",
    "gh-arcanamfg": "https://api.github.com/users/ArcanaMfg",
    "gh-mcp-clients": "https://api.github.com/repos/punkpeye/awesome-mcp-clients",
    "gh-open-design": "https://api.github.com/repos/nexu-io/open-design",
    "gh-awesome-llm-apps": "https://api.github.com/repos/Shubhamsaboo/awesome-llm-apps",
    "arxiv-html": "https://arxiv.org/html/2603.27476v3",
    "figma-skill": "https://www.figma.com/community/skill/74536/checklist-design",
    "gh-gpt-image2-skill": "https://api.github.com/repos/wuyoscar/GPT-Image2-Skill",
}

SKIP = {
    "treg.to/people-search": "leftover23 already",
    "github.com/iannuttall/seo": "leftover24 already (self-card leftover)",
    "aura.build": "leftover18 already",
    "discord.gg": "Discord invite — skip",
    "github.com/superdesigndev/treg": "leftover24 already (self-card leftover)",
    "platform.minimax.io/docs": "leftover28 already",
    "arcana-mfg.com/en/splat2mesh": "leftover24 already",
    "Splat2Mesh_v1.0.zip": "ZIP — do not download",
    "flint.data-formulator.ai/mcp": "keyed MCP — do not hammer",
    "mcp.graphed.com/mcp": "keyed MCP — do not hammer",
    "github.com/h4ckf0r0day/obscura": "leftover24/27 already",
    "docs.obscura.sh": "leftover24/27 already",
    "youtube.com seowins": "seowins leftover — do not hammer",
    "nv-tlabs/ArtiFixer": "leftover27 already",
    "neighbor leftover29 essays": "gasquez/macomber/anthropic already leftover29",
}

print(f"leftover30 fetch: {len(FETCH)}")
for slug, url in FETCH.items():
    print(f"  {slug}\t{urlparse(url).netloc}\t{url}")
print(f"leftover30 skip: {len(SKIP)}")
for k, v in SKIP.items():
    print(f"  skip {k}\t{v}")

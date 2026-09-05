#!/usr/bin/env python3
"""Add leftover22 demonstrated claims for unused first-party pages."""
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
        "x-2085006701984698712",
        {
            "id": "x-2085006701984698712#c4",
            "text": "leftover22 unused creatoreconomy.so essay is first-party 207,273 B (Aug 05, 2026). Title Use My /Human-Review Skill to Edit HTML and Markdown Files like A Google Doc. Install is a paste into Codex/Claude Code; editor is local server; agent waits in 10-minute windows; HTML edits autosave; Markdown/localhost need Send. Credits Kun/Lavish. Paid upsell is 12+ more skills. Matches local-loop tweet; not a DESIGN.md library.",
            "kind": "recipe",
            "evidence": "leftover22 creatoreconomy-human-review 207273 B. Quote: Because the whole review loop runs locally, /human-review doesn’t require an account or API key.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/human-review.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://creatoreconomy.so/p/use-my-human-review-skill-to-edit-html-markdown-visually"],
    )
    add_claim(
        "x-2091990178638496195",
        {
            "id": "x-2091990178638496195#c4",
            "text": "leftover22 unused Laude post is first-party 227,836 B (Aug 24, 2026). Official body still says core less than 10K / 9.9K lines in bin/ + thinkers/ — do not collapse with cloc 9,912 code or wc 13,947 already on #c3. $1–2/hour background (GLM or Grok) is first-party. install.sh 25,935 B clones laude-institute/headlong to ~/.headlong/app; BIN_TOOLS 10 + AUX_TOOLS 13; default dash :8080 in Docker path.",
            "kind": "availability",
            "evidence": "leftover22 laude-headlong 227836 B; headlong-install 25935 B. Quote: The core of Headlong is currently less than 10K lines of Bash (9.9K lines in bin/ and thinkers/).",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/headlong.md",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        [
            "https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents",
            "https://headlong.ai/install.sh",
        ],
    )
    add_claim(
        "x-2094864872853119216",
        {
            "id": "x-2094864872853119216#c4",
            "text": "leftover22 unused Spark pages: sparkjs.dev 19,204 B MkDocs (formats ply/sogs/spz/splat/ksplat). worldlabs.ai/blog/spark-2.0 770,998 B first-party LoD + .RAD streaming + 16M-splat GPU page table; example spaceship 6M splats; Starspeed 100,000,000+; captured scenes up to 40M; render budget 500K–2.5M. xrarchitect.xyz 2,689 B title Portfolio - Ian Curtis (visible empty). Do not treat Spark as a mesh exporter.",
            "kind": "capability",
            "evidence": "leftover22 sparkjs 19204 B; spark-20-blog 770998 B; xrarchitect 2689 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/spark-js.md",
            "confidence": "demonstrated",
            "subject": "image-to-3d-world",
        },
        [
            "https://sparkjs.dev",
            "https://www.worldlabs.ai/blog/spark-2.0",
            "https://xrarchitect.xyz",
        ],
    )
    add_claim(
        "x-2093654908322951447",
        {
            "id": "x-2093654908322951447#c3",
            "text": "leftover22 unused how-to-ai.guide 301s to ruben.substack.com 96,312 B. Title How to AI | Ruben Hassid | Substack. Markets Over 925,000 subscribers. Not a skill-pack host and not claude-skills.free. Eleven named /writer skills stay on the tweet + gated library page.",
            "kind": "availability",
            "evidence": "leftover22 how-to-ai 96312 B final ruben.substack.com. Quote: Over 925,000 subscribers.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/claude-skills-free.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["http://how-to-ai.guide", "https://ruben.substack.com/"],
    )
    add_claim(
        "x-2093774183356379560",
        {
            "id": "x-2093774183356379560#c4",
            "text": "leftover22 unused outbid.lol is HTTP 429 / 32,182 B Vercel Security Checkpoint. Top-3 listing for unive.ai stays tweet-only. Do not hammer. unive.ai admissions landing already on #c3.",
            "kind": "availability",
            "evidence": "leftover22 outbid 429 32182 B title Vercel Security Checkpoint.",
            "evidence_source": "note",
            "evidence_ref": "analysis/subjects/landing-ui-motion/worksheet.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        ["https://outbid.lol"],
    )
    add_claim(
        "x-2093986548404428942",
        {
            "id": "x-2093986548404428942#c4",
            "text": "leftover22 unused tapirconvert.com/video-upscaler is HTTP 403 / 5,513 B Cloudflare challenge (Just a moment…). Prior leftover tapir.gg 1,459 B empty body is a different host. Free 2× no-login stays tweet-only. Do not hammer.",
            "kind": "availability",
            "evidence": "leftover22 tapirconvert 403 5513 B. leftover #c3 tapir.gg 1459 B empty.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/video-shotcraft.md",
            "confidence": "demonstrated",
            "subject": "blockout-to-video-flythrough",
        },
        ["http://tapirconvert.com/video-upscaler"],
    )
    add_claim(
        "x-2091689598883934666",
        {
            "id": "x-2091689598883934666#c3",
            "text": "leftover22 unused t.co/KYuOOs0GhP → toolfolio.com/tools/name-that-ui 408,882 B. Listing: UI Visual Dictionary; Freemium; Platforms Web; Last Updated Aug 4, 2026. Product host namethatui.com 602,668 B / 80 H3s already on #c2. Do not collapse Toolfolio listing HTML with the live dictionary.",
            "kind": "availability",
            "evidence": "leftover22 tco-namethatui 200 408882 B final toolfolio.com/tools/name-that-ui.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/name-that-ui.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://t.co/KYuOOs0GhP", "https://toolfolio.com/tools/name-that-ui"],
    )
    add_claim(
        "x-2095055297949610427",
        {
            "id": "x-2095055297949610427#c4",
            "text": "leftover22 unused keep.md 191,347 B: Starter Free; Personal $10/mo; X bookmark sync $5/mo. MCP https://keep.md/mcp; npm i -g keep. ian.is 62,453 B lists Keep + SEO Skill + Swipe/Caffeine/Natter/Portman/Unclaimed/Mailroom/Clockwork/Barkeep/ilo; 6,809 contributions. seoskill.dev 70+ still GitHub-only (#c3). Do not invent keep.md tool file.",
            "kind": "pricing",
            "evidence": "leftover22 keep-md 191347 B; ian-is 62453 B. Quote: Personal $10/month.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/seo-skill-cli.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        ["https://keep.md", "https://ian.is"],
    )
    add_claim(
        "x-2087208634493095978",
        {
            "id": "x-2087208634493095978#c4",
            "text": "leftover22 unused arXiv 2604.03927 abs 41,988 B is Version Control System for Data with MatrixOne (cs.DB; Gou/Tian/Wang/Deng/Xu; 5 Apr 2026; PDF 117 KB). First-party: git-like clone/tag/branch/diff/merge/revert on terabyte tables via MatrixOne MVCC. Not an agent-memory paper — do not collapse with tweet/README “World’s First Git for AI Agent Memory” or GH 593★.",
            "kind": "counter-claim",
            "evidence": "leftover22 memoria-abs 41988 B. Title: Version Control System for Data with MatrixOne.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/memoria.md",
            "confidence": "demonstrated",
            "subject": "agent-memory-knowledge",
        },
        ["https://arxiv.org/abs/2604.03927"],
    )
    add_claim(
        "x-2087714580491370655",
        {
            "id": "x-2087714580491370655#c4",
            "text": "leftover22 unused pi-gippity-control README 3,878 B. Install pi install npm:@howaboua/pi-gippity-control; Pi 0.84.4+ / Node 22.19+; do not install beside pi-codex-conversion. LAN default port 43120; unauthenticated by design; reportRealtimeVoicePrompt is first-party. Matches tweet extension API; not a voice-changelog dump.",
            "kind": "recipe",
            "evidence": "leftover22 pi-gippity-readme 3878 B. Quote: Do not install this alongside @howaboua/pi-codex-conversion.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/pi-shepherdr.md",
            "confidence": "demonstrated",
            "subject": "agent-harness-loops",
        },
        [
            "https://github.com/IgorWarzocha/howaboua-pi-stuff/tree/main/packages/pi-gippity-control"
        ],
    )
    add_claim(
        "x-2087962842985058365",
        {
            "id": "x-2087962842985058365#c4",
            "text": "leftover22 unused GitHub PrismML-Eng/Bonsai-demo Apache-2.0 2,272★ (description Bonsai Demo). Not the HF 1.7B-gguf weights and not tweet 64→90 Android CPU. Do not invent bonsai.md.",
            "kind": "availability",
            "evidence": "leftover22 gh-bonsai-demo 2272 Apache-2.0.",
            "evidence_source": "note",
            "evidence_ref": "analysis/_work/captures/leftover10-bonsai-detail-2026-09-05.json",
            "confidence": "demonstrated",
            "subject": "local-inference-models",
        },
        ["https://github.com/PrismML-Eng/Bonsai-demo"],
    )
    add_claim(
        "x-2094328961522397530",
        {
            "id": "x-2094328961522397530#c5",
            "text": "leftover22 unused tinylaunch.com/directories 106,620 B. Title List of Product Directories (Free). Live list Showing 15 of 691. Paid 110-directory package $279 one-time; 30,000+ makers; Flashcard Buddy DR 7→30 still vendor copy. TinyShots DR 11→46 stays tweet-only. Do not collapse TinyLaunch 691-dir list with TinyShelf 122 outgoing dofollow.",
            "kind": "pricing",
            "evidence": "leftover22 tinylaunch-dirs 106620 B. Quote: Showing 15 of 691; 110 Directories $279.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/tinyshots.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        ["https://www.tinylaunch.com/directories", "https://tinylaunch.com"],
    )
    add_claim(
        "x-2094771557864292784",
        {
            "id": "x-2094771557864292784#c4",
            "text": "leftover22 unused nqz.ai/ai-search-prompt-generator 36,810 B. First-party: 4 topics × 3 intents; no brand names; 10 generations/hour; no login; Immortal Reality PA LLC. Matches the dedicated web card’s stated 4×3 / 10/hour. Not a citation tracker and not Known Agency’s five-layer SEO stack.",
            "kind": "capability",
            "evidence": "leftover22 nqz-generator 36810 B. Quote: Limited to 10 generations/hour per visitor.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/nqz-ai-search-prompt-generator.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        ["https://nqz.ai/ai-search-prompt-generator"],
    )
    add_claim(
        "x-2093129469926215800",
        {
            "id": "x-2093129469926215800#c4",
            "text": "leftover22 unused hyperframes.dev 29,104 B (www). Visible body is Star us / Tools / Loading… — SSR shell, not the launch-composition tree. Official CLI + heygen-com/hyperframes-launches already on #c2. Four replies still unfetched.",
            "kind": "availability",
            "evidence": "leftover22 hyperframes-dev 29104 B title HyperFrames. Visible Star us Tools Loading.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/hyperframes.md",
            "confidence": "demonstrated",
            "subject": "code-motion-graphics",
        },
        ["https://hyperframes.dev"],
    )
    add_claim(
        "x-2094927852399624557",
        {
            "id": "x-2094927852399624557#c4",
            "text": "leftover22 unused b2bfunnel.co 71,788 B is a done-for-you outbound agency (Book 20+ qualified sales calls a month). First-party: 2–3K emails/day/client; $3K+ min LTV; $500+/mo retainer floor; 30K+ addressable. Not Instantly 10k/day / 500 inboxes / 167 domains. Do not invent b2bfunnel.md. Instantly 10k stays tweet-only (#c3).",
            "kind": "counter-claim",
            "evidence": "leftover22 b2bfunnel 71788 B. Quote: 2–3K Emails / day / client.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/mapsdata.md",
            "confidence": "demonstrated",
            "subject": "outbound-gtm-agents",
        },
        ["http://b2bfunnel.co", "https://b2bfunnel.co"],
    )
    add_claim(
        "x-2095123902947090682",
        {
            "id": "x-2095123902947090682#c3",
            "text": "leftover22 unused store.brasshands.com 351,750 B. Title Brass Hands Corp – Gear for the New Industrial Age. Live merch (hoodie Release [01] RE-IND; complimentary US shipping over $100; 10% first-order). Tweet Neo Industrialism Swiss-grid terrain-intel wording is not on the store. Homepage already on #c2.",
            "kind": "availability",
            "evidence": "leftover22 brasshands-store 351750 B.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/motionsites-ai.md",
            "confidence": "demonstrated",
            "subject": "landing-ui-motion",
        },
        ["https://store.brasshands.com/"],
    )
    add_claim(
        "x-2094688982940741816",
        {
            "id": "x-2094688982940741816#c4",
            "text": "leftover22 unused hridoyreh.com 77,652 B. Title Hridoy Reh - An SEO / AI SEO Specialist. Markets 650M+ visitors / $149M+ revenue / 78+ websites / 200+ people. Names seowins.io (already 403 — do not hammer). 1,190 Brave sessions / 1.34% stay on the analytics screenshot. Not a GSC export.",
            "kind": "availability",
            "evidence": "leftover22 hridoyreh 77652 B. Quote: 650M+ visitors and $149M+ in revenue.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/seo-skill-cli.md",
            "confidence": "demonstrated",
            "subject": "serp-ai-visibility",
        },
        ["https://hridoyreh.com/"],
    )
    add_claim(
        "web-designmd-supply",
        {
            "id": "web-designmd-supply#c4",
            "text": "leftover22 unused neighbor github.com/google-labs-code/design.md Apache-2.0 27,737★. Description: format specification for describing a visual identity to coding agents. Not the designmd.supply marketplace (still 429 / 32,184 B — do not hammer).",
            "kind": "availability",
            "evidence": "leftover22 gh-design-md 27737 Apache-2.0.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/getdesign-md.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
        ["https://github.com/google-labs-code/design.md"],
    )
    add_claim(
        "github-google-labs-code-design-md",
        {
            "id": "github-google-labs-code-design-md#c3",
            "text": "leftover22 GitHub API google-labs-code/design.md Apache-2.0 27,737★. Spec + lint/diff CLI claims stay on #c1/#c2 (linked-page). Star count was not previously on-card.",
            "kind": "availability",
            "evidence": "leftover22 gh-design-md 27737 Apache-2.0.",
            "evidence_source": "note",
            "evidence_ref": "analysis/tools/getdesign-md.md",
            "confidence": "demonstrated",
            "subject": "design-agent-skills",
        },
    )


if __name__ == "__main__":
    main()

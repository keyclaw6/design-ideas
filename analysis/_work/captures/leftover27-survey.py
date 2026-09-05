#!/usr/bin/env python3
"""leftover27: unused first-party on ready analyze cards + failed threads + worksheet URLs."""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path("/workspace/analysis/items")
SUBJECTS = Path("/workspace/analysis/subjects")
URL_RE = re.compile(r"https?://[^\s\"'`<>)\]]+")

DEAD = (
    "seowins.io",
    "stackshare.io",
    "calliope.ai",
    "smith.co",
    "fable.com",
    "coreyhaines.com",
    "coreyhaines.co",
    "magnific.com",
    "lichtfeld.io",
    "orca.build",
    "designmd.me",
    "designmd.supply",
    "typeui.com",
    "typeui.sh",
    "cult-ui.com",
    "search.brave.com",
    "brave.com",
    "superhive.com",
    "bqr.gg",
    "cerebras.ai",
    "outbid.lol",
    "tapirconvert.com",
    "npmjs.com",
    "aiautomationsociety.ai",
    "g2.com",
    "producthunt.com",
    "linkedin.com",
    "grok.com",
    "openreview.net",
    "mcp.gojiberry.ai",
    "mcp.crowdreply.io",
    "lottiefiles.com",
)
SKIP_HOSTS = {
    "x.com",
    "twitter.com",
    "pbs.twimg.com",
    "video.twimg.com",
    "abs.twimg.com",
    "t.co",
    "fxtwitter.com",
    "vxtwitter.com",
    "api.fxtwitter.com",
    "fixupx.com",
    "nitter.net",
    "threadreaderapp.com",
}


def host(u: str) -> str:
    return (urlparse(u).netloc or "").lower()


def card_urls(c: dict) -> list[str]:
    urls: list[str] = []
    links = c.get("links") or {}
    for key in ("homepage", "repo", "paper", "docs", "product"):
        v = links.get(key)
        if isinstance(v, str) and v.startswith("http"):
            urls.append(v)
        elif isinstance(v, list):
            urls.extend(u for u in v if isinstance(u, str) and u.startswith("http"))
    for u in links.get("other") or []:
        if isinstance(u, str) and u.startswith("http"):
            urls.append(u)
    seen = set()
    out = []
    for u in urls:
        u = u.rstrip(").,;]")
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def note_blob(c: dict) -> str:
    parts = []
    for cl in c.get("claims") or []:
        if cl.get("evidence_source") == "note":
            parts.append(cl.get("text") or "")
            parts.append(cl.get("evidence") or "")
    return "\n".join(parts).lower()


def unused_for(c: dict) -> list[str]:
    nblob = note_blob(c)
    unused = []
    for u in card_urls(c):
        h = host(u)
        if any(d in h for d in DEAD):
            continue
        if "t.co/" in u or h in SKIP_HOSTS or h.endswith(".twimg.com"):
            continue
        path = urlparse(u).path.strip("/").lower()
        marker = path.split("/")[-1] if path else h
        if u.lower() in nblob or h.replace("www.", "") in nblob:
            continue
        if marker and len(marker) > 4 and marker in nblob:
            continue
        unused.append(u)
    return unused


print("=== unused first-party on READY analyze cards ===")
ready_n = 0
for card_path in sorted(ROOT.glob("*/card.json")):
    c = json.loads(card_path.read_text())
    if c.get("disposition") != "analyze" or c.get("readiness") != "ready":
        continue
    unused = unused_for(c)
    if unused:
        ready_n += 1
        if ready_n <= 40:
            print(f"{c['id']}\t{c.get('primary_subject')}\t{unused[:6]}")
print(f"(ready cards with unused: {ready_n})")

print("\n=== unused on failed-thread analyze ===")
for card_path in sorted(ROOT.glob("*/card.json")):
    c = json.loads(card_path.read_text())
    if c.get("disposition") != "analyze":
        continue
    tpath = card_path.parent / "thread.json"
    if not tpath.exists():
        continue
    t = json.loads(tpath.read_text())
    if t.get("status") != "failed":
        continue
    unused = unused_for(c)
    print(f"{c['id']}\t{c.get('primary_subject')}\t{unused}")

print("\n=== worksheet next-capture http URLs ===")
for ws in sorted(SUBJECTS.glob("*/worksheet.md")):
    text = ws.read_text()
    urls = URL_RE.findall(text)
    # only next-capture section
    if "## " in text and "next capture" in text.lower():
        idx = text.lower().find("next capture")
        text = text[idx:]
        urls = URL_RE.findall(text)
    ext = [
        u
        for u in urls
        if not any(s in u for s in ("x.com", "analysis/", "../../", "github.com"))
        and not any(d in host(u) for d in DEAD)
    ]
    if ext:
        print(ws.parent.name, ext[:12])

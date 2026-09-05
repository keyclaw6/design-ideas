#!/usr/bin/env python3
"""Find unused first-party / t.co links on ready-with-gaps analyze cards."""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path("/workspace/analysis/items")
URL_RE = re.compile(r"https?://[^\s\"'<>]+")
TCO_RE = re.compile(r"https://t\.co/[A-Za-z0-9]+")

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
    "www.orca.build",
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
    "www.npmjs.com",
    "aiautomationsociety.ai",
    "www.aiautomationsociety.ai",
    "g2.com",
    "www.g2.com",
    "producthunt.com",
    "www.producthunt.com",
    "linkedin.com",
    "www.linkedin.com",
)

SKIP_HOSTS = (
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
)


def card_urls(c: dict) -> list[str]:
    urls: list[str] = []
    links = c.get("links") or {}
    for key in ("homepage", "repo", "paper", "docs"):
        v = links.get(key)
        if isinstance(v, str) and v.startswith("http"):
            urls.append(v)
        elif isinstance(v, list):
            urls.extend(u for u in v if isinstance(u, str) and u.startswith("http"))
    for u in links.get("other") or []:
        if isinstance(u, str) and u.startswith("http"):
            urls.append(u)
    blob = json.dumps(c, ensure_ascii=False)
    urls.extend(URL_RE.findall(blob))
    # unique preserve
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
            parts.append(cl.get("evidence_ref") or "")
    return "\n".join(parts).lower()


def host(u: str) -> str:
    return (urlparse(u).netloc or "").lower()


rows = []
for card_path in sorted(ROOT.glob("*/card.json")):
    c = json.loads(card_path.read_text())
    if c.get("disposition") != "analyze":
        continue
    if c.get("readiness") != "ready-with-gaps":
        continue
    must = bool((c.get("judge_hints") or {}).get("must_read"))
    nblob = note_blob(c)
    unused = []
    unused_tco = []
    for u in card_urls(c):
        h = host(u)
        if any(d in h for d in DEAD):
            continue
        if "t.co/" in u:
            token = u.split("t.co/")[-1].split("/")[0]
            if token.lower() not in nblob and u.lower() not in nblob:
                unused_tco.append(u)
            continue
        if h in SKIP_HOSTS or h.endswith(".twimg.com"):
            continue
        # treat as unused if neither URL nor distinctive path in note claims
        path = urlparse(u).path.strip("/").lower()
        marker = path.split("/")[-1] if path else h
        if u.lower() in nblob or h.replace("www.", "") in nblob:
            continue
        if marker and len(marker) > 4 and marker in nblob:
            continue
        unused.append(u)
    if unused or unused_tco:
        rows.append(
            {
                "id": c["id"],
                "subject": c.get("primary_subject"),
                "must_read": must,
                "gaps": c.get("gaps") or [],
                "n_claims": len(c.get("claims") or []),
                "unused": unused[:8],
                "unused_tco": unused_tco[:6],
                "title": (c.get("title") or "")[:80],
            }
        )

print(f"ready-with-gaps cards with unused urls: {len(rows)}")
print(f"  must-read among them: {sum(1 for r in rows if r['must_read'])}")
print("\n=== unused first-party (non-t.co) ===")
n = 0
for r in rows:
    if not r["unused"]:
        continue
    n += 1
    print(
        f"{r['id']}\t{r['subject']}\tmust={r['must_read']}\tgaps={r['gaps']}\t{r['unused']}"
    )
print(f"(shown {n})")
print("\n=== unused t.co (first 40) ===")
shown = 0
for r in rows:
    if not r["unused_tco"]:
        continue
    shown += 1
    if shown > 40:
        break
    print(f"{r['id']}\t{r['subject']}\tmust={r['must_read']}\t{r['unused_tco']}")

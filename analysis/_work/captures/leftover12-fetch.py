#!/usr/bin/env python3
"""leftover12 first-party fetches. No GPU. Skip known 429/403 hosts."""
from __future__ import annotations

import json
import ssl
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

OUT = Path("/workspace/analysis/_work/captures/leftover12-2026-09-05")
OUT.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (compatible; analysis-corpus/1.0; +https://example.invalid)"
CTX = ssl.create_default_context()


class TitleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._in_title = False
        self.title = ""
        self.visible: list[str] = []
        self._skip = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self._in_title = True
        if tag in {"script", "style", "noscript"}:
            self._skip = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in {"script", "style", "noscript"}:
            self._skip = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        elif not self._skip:
            t = " ".join(data.split())
            if t:
                self.visible.append(t)


def fetch(url: str, timeout: int = 25) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=timeout) as resp:
            body = resp.read()
            return {
                "url": url,
                "final": getattr(resp, "url", url),
                "status": getattr(resp, "status", 200),
                "bytes": len(body),
                "ctype": resp.headers.get("Content-Type"),
                "error": None,
                "body": body,
            }
    except urllib.error.HTTPError as e:
        body = e.read() if e.fp else b""
        return {
            "url": url,
            "final": getattr(e, "url", url),
            "status": e.code,
            "bytes": len(body),
            "ctype": e.headers.get("Content-Type") if e.headers else None,
            "error": f"HTTPError {e.code}",
            "body": body,
        }
    except Exception as e:
        return {
            "url": url,
            "final": None,
            "status": None,
            "bytes": 0,
            "ctype": None,
            "error": f"{type(e).__name__}: {e}",
            "body": b"",
        }


def summarize_html(rec: dict, slug: str) -> dict:
    body = rec.pop("body", b"")
    out = {k: rec[k] for k in rec}
    if not body:
        return out
    ctype = (rec.get("ctype") or "").lower()
    if "json" in ctype or (body[:1] in {b"{", b"["}):
        path = OUT / f"{slug}.json"
        try:
            data = json.loads(body.decode("utf-8", "replace"))
            path.write_text(json.dumps(data, indent=2)[:400_000], encoding="utf-8")
            out["saved"] = str(path)
            if isinstance(data, dict):
                out["json_summary"] = {
                    "full_name": data.get("full_name") or data.get("name"),
                    "stars": data.get("stargazers_count") or data.get("stars"),
                    "license": (data.get("license") or {}).get("spdx_id")
                    if isinstance(data.get("license"), dict)
                    else data.get("license"),
                    "desc": data.get("description") or data.get("desc"),
                    "homepage": data.get("homepage"),
                    "total": data.get("total_count"),
                    "items": [
                        {
                            "full_name": i.get("full_name"),
                            "stars": i.get("stargazers_count"),
                            "license": (i.get("license") or {}).get("spdx_id")
                            if isinstance(i.get("license"), dict)
                            else None,
                            "desc": (i.get("description") or "")[:180],
                        }
                        for i in (data.get("items") or [])[:8]
                    ]
                    if data.get("items")
                    else None,
                }
            elif isinstance(data, list):
                out["json_summary"] = {
                    "len": len(data),
                    "head": [
                        {
                            "full_name": i.get("full_name") or i.get("login") or i.get("name"),
                            "stars": i.get("stargazers_count"),
                        }
                        for i in data[:8]
                        if isinstance(i, dict)
                    ],
                }
        except Exception as e:
            path.write_bytes(body[:80_000])
            out["saved"] = str(path)
            out["parse_error"] = str(e)
        return out
    text = body.decode("utf-8", "replace")
    parser = TitleParser()
    try:
        parser.feed(text)
    except Exception:
        pass
    out["title"] = parser.title.strip() or None
    visible = " ".join(parser.visible)
    vis_path = OUT / f"{slug}-visible.txt"
    vis_path.write_text(visible[:40_000], encoding="utf-8")
    out["visible_saved"] = str(vis_path)
    out["visible_len"] = len(visible)
    excerpt = OUT / f"{slug}-excerpt.html"
    excerpt.write_text(text[:20_000], encoding="utf-8")
    out["excerpt_saved"] = str(excerpt)
    return out


URLS = {
    # t.co from leftover11 remaining empty-no-note threads
    "tco-pocock-skill": "https://t.co/UZRe9thSRU",
    "tco-pocock-quoted": "https://t.co/VAfPmyTLLK",
    "tco-hermes-writeup": "https://t.co/YZV33FWmah",
    "tco-lifeos": "https://t.co/nW8O3RWeko",
    "tco-hermes-reply": "https://t.co/7H48QDMSNQ",
    "tco-duckdb": "https://t.co/oJr6WUUGtO",
    "tco-llms-blog": "https://t.co/2dwDI1FuxR",
    "tco-llms-love": "https://t.co/veXnkp2JjU",
    "tco-runway": "https://t.co/5mx6XHOlZj",
    "tco-runway-scam1": "https://t.co/dKY8Rb4a4S",
    "tco-runway-scam2": "https://t.co/qRJ6g5yL6N",
    "tco-h3-plugins": "https://t.co/JlkEPxlSP9",
    "tco-fini-root": "https://t.co/YVWPbF6Ej7",
    "tco-fini-quoted": "https://t.co/K5FnOQbTdA",
    "tco-fini-gh": "https://t.co/o6HgHkP2Vg",
    "tco-hasan-playbook": "https://t.co/HgtgfwfMGj",
    "tco-hasan-agent": "https://t.co/9rrD0MSISr",
    "tco-arcads": "https://t.co/pEEFOquwMA",
    "tco-fable-video": "https://t.co/8ZigK2I1vT",
    "tco-fable-ref1": "https://t.co/spKXHNO8jB",
    "tco-fable-ref2": "https://t.co/CmlrIsbXw5",
    "tco-emil-graphs": "https://t.co/OZkRrENTMb",
    "tco-emil-inspired": "https://t.co/3uzj5lL4Zc",
    "tco-grok-bots": "https://t.co/oAMqQuYEQM",
    "tco-grok-50": "https://t.co/EZax5PplaJ",
    "tco-autoquant-root": "https://t.co/Us3K68iNHr",
    "tco-autoskill": "https://t.co/8tEXz6RIi4",
    "tco-autoquant-curl": "https://t.co/EkgEQAh72T",
    "tco-autoquant-claw": "https://t.co/EB6W9A1qUk",
    "tco-autoquant-commit": "https://t.co/jCaQw495Us",
    "tco-press-wire": "https://t.co/RV7OYxklGQ",
    "tco-aeo-100k": "https://t.co/JiUTuke1cj",
    "tco-hasan-dr": "https://t.co/LbbvsTUrfX",
    "tco-linkedin-seo": "https://t.co/9gZIg87p1C",
    "tco-crawler-ua": "https://t.co/ti2VbZetVW",
    # first-party pages (no 429/403 hosts)
    "runway-home": "https://runwayml.com/",
    "arcads-home": "https://www.arcads.ai/",
    "arcads-apex": "https://arcads.ai/",
    "duckdb-home": "https://duckdb.org/",
    "lifeos-gh": "https://api.github.com/repos/danielmiessler/Personal_AI_Infrastructure",
    "lifeos-search": "https://api.github.com/search/repositories?q=LifeOS+user:danielmiessler",
    "pocock-skill-search": "https://api.github.com/search/repositories?q=improve-codebase-architecture",
    "autoquant-search": "https://api.github.com/search/repositories?q=autoquant",
    "arcads-search": "https://api.github.com/search/repositories?q=arcads+mcp",
    "fini-user": "https://api.github.com/users/0xfini",
}


def main() -> None:
    pages = {}
    for slug, url in URLS.items():
        print(f"GET {slug} {url}", flush=True)
        rec = fetch(url)
        pages[slug] = summarize_html(rec, slug)
        pages[slug].pop("body", None)
        print(
            f"  -> {pages[slug].get('status')} {pages[slug].get('bytes')} {pages[slug].get('final')} {pages[slug].get('error')}",
            flush=True,
        )
        time.sleep(0.35)
    out = {
        "fetched_at": "2026-09-05T06:10:00Z",
        "pages": pages,
    }
    path = Path("/workspace/analysis/_work/captures/leftover12-2026-09-05.json")
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("wrote", path)


if __name__ == "__main__":
    main()

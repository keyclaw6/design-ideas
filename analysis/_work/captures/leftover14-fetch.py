#!/usr/bin/env python3
"""leftover14 first-party + leftover t.co. No GPU/429/403 hammer."""
from __future__ import annotations

import json
import ssl
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

OUT = Path("/workspace/analysis/_work/captures/leftover14-2026-09-05")
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


def summarize(rec: dict, slug: str) -> dict:
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
                    "stars": data.get("stargazers_count"),
                    "forks": data.get("forks_count"),
                    "license": (data.get("license") or {}).get("spdx_id")
                    if isinstance(data.get("license"), dict)
                    else data.get("license"),
                    "desc": (data.get("description") or "")[:240],
                    "homepage": data.get("homepage"),
                    "total": data.get("total_count"),
                    "items": [
                        {
                            "full_name": i.get("full_name"),
                            "stars": i.get("stargazers_count"),
                            "license": (i.get("license") or {}).get("spdx_id")
                            if isinstance(i.get("license"), dict)
                            else None,
                            "desc": (i.get("description") or "")[:160],
                        }
                        for i in (data.get("items") or [])[:8]
                    ]
                    if data.get("items")
                    else None,
                }
                if isinstance(data, list) or (isinstance(data, dict) and isinstance(data.get("tree"), list)):
                    pass
                if isinstance(data, list):
                    out["json_summary"]["list"] = [
                        {
                            "name": i.get("name"),
                            "type": i.get("type"),
                            "path": i.get("path"),
                        }
                        for i in data[:40]
                    ]
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
    (OUT / f"{slug}-visible.txt").write_text(visible[:40_000], encoding="utf-8")
    out["visible_len"] = len(visible)
    (OUT / f"{slug}-excerpt.html").write_text(text[:20_000], encoding="utf-8")
    return out


URLS = {
    "antigravity-google": "https://antigravity.google/",
    "antigravity-www": "https://www.antigravity.google/",
    "antigravity-dev": "https://developers.google.com/antigravity",
    "antigravity-gemini": "https://gemini.google/overview/antigravity/",
    "openscad-org": "https://openscad.org/",
    "openscad-repo": "https://api.github.com/repos/openscad/openscad",
    "openscad-contents": "https://api.github.com/repos/openscad/openscad/contents/",
    "tco-fleeting-hermes": "https://t.co/iRf19az0E7",
    "tco-fleeting-game": "https://t.co/RlQNWV9VfL",
    "tco-fleeting-miho1": "https://t.co/Lr58xVpQrt",
    "tco-fleeting-miho2": "https://t.co/86vU29ZHve",
    "tco-grill-me": "https://t.co/yIPMiN9j4k",
    "tco-openscad-ankush": "https://t.co/NOGx8QjLUO",
    "mattpocock-contents": "https://api.github.com/repos/mattpocock/skills/contents/",
    "mattpocock-productivity": "https://api.github.com/repos/mattpocock/skills/contents/productivity",
    "gh-search-wayfinder": "https://api.github.com/search/repositories?q=wayfinder+skill&per_page=5",
    "gh-search-ask-matt": "https://api.github.com/search/repositories?q=ask-matt+skill&per_page=5",
    "gh-search-ponytail": "https://api.github.com/search/repositories?q=ponytail+skill&per_page=5",
    "gh-search-grilling": "https://api.github.com/search/repositories?q=grilling+SKILL.md&per_page=5",
}


def main() -> None:
    pages = {}
    for slug, url in URLS.items():
        print(f"GET {slug} {url}", flush=True)
        rec = fetch(url)
        pages[slug] = summarize(rec, slug)
        pages[slug].pop("body", None)
        print(
            f"  -> {pages[slug].get('status')} {pages[slug].get('bytes')} {pages[slug].get('final')} {pages[slug].get('error')}",
            flush=True,
        )
        time.sleep(0.4)
    path = Path("/workspace/analysis/_work/captures/leftover14-2026-09-05.json")
    path.write_text(json.dumps({"fetched_at": "2026-09-05T07:10:00Z", "pages": pages}, indent=2), encoding="utf-8")
    print("wrote", path)


if __name__ == "__main__":
    main()

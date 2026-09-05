#!/usr/bin/env python3
"""leftover12 follow-up first-party fetches."""
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
                    "full_name": data.get("full_name") or data.get("login") or data.get("name"),
                    "stars": data.get("stargazers_count") or data.get("public_repos"),
                    "license": (data.get("license") or {}).get("spdx_id")
                    if isinstance(data.get("license"), dict)
                    else data.get("license"),
                    "desc": data.get("description") or data.get("bio"),
                    "homepage": data.get("homepage") or data.get("html_url"),
                    "total": data.get("total_count"),
                    "items": [
                        {
                            "full_name": i.get("full_name") or i.get("name"),
                            "stars": i.get("stargazers_count"),
                            "license": (i.get("license") or {}).get("spdx_id")
                            if isinstance(i.get("license"), dict)
                            else None,
                            "desc": (i.get("description") or "")[:180],
                        }
                        for i in (data.get("items") or data if isinstance(data, list) else [])[:8]
                        if isinstance(i, dict)
                    ]
                    if (data.get("items") or isinstance(data, list))
                    else None,
                }
            elif isinstance(data, list):
                out["json_summary"] = {
                    "len": len(data),
                    "head": [
                        {
                            "full_name": i.get("full_name") or i.get("name"),
                            "stars": i.get("stargazers_count"),
                            "desc": (i.get("description") or "")[:120],
                        }
                        for i in data[:12]
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
    (OUT / f"{slug}-visible.txt").write_text(visible[:40_000], encoding="utf-8")
    out["visible_len"] = len(visible)
    (OUT / f"{slug}-excerpt.html").write_text(text[:20_000], encoding="utf-8")
    return out


URLS = {
    "mattpocock-skills": "https://api.github.com/repos/mattpocock/skills",
    "lifeos-repo": "https://api.github.com/repos/danielmiessler/LifeOS",
    "fini-0xf1n1": "https://api.github.com/users/0xf1n1",
    "fini-repos": "https://api.github.com/users/0xf1n1/repos?per_page=20&sort=updated",
    "ourlifeos": "https://ourlifeos.ai/",
    "hyperspace-agi": "https://api.github.com/repos/hyperspaceai/agi",
    "tco-press-wire": "https://t.co/RV7OYxklGQ",
    "tco-aeo-100k": "https://t.co/JiUTuke1cj",
    "tco-hasan-dr": "https://t.co/LbbvsTUrfX",
    "tco-linkedin-seo": "https://t.co/9gZIg87p1C",
    "tco-crawler-ua": "https://t.co/ti2VbZetVW",
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
        time.sleep(0.35)
    path = Path("/workspace/analysis/_work/captures/leftover12b-2026-09-05.json")
    path.write_text(json.dumps({"fetched_at": "2026-09-05T06:20:00Z", "pages": pages}, indent=2), encoding="utf-8")
    print("wrote", path)


if __name__ == "__main__":
    main()

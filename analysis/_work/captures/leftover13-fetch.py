#!/usr/bin/env python3
"""leftover13 remaining empty-no-note t.co + first-party. No GPU/429/403 hammer."""
from __future__ import annotations

import json
import ssl
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

OUT = Path("/workspace/analysis/_work/captures/leftover13-2026-09-05")
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
                    "license": (data.get("license") or {}).get("spdx_id")
                    if isinstance(data.get("license"), dict)
                    else data.get("license"),
                    "desc": (data.get("description") or "")[:200],
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
    "tco-jeep": "https://t.co/FIqKBvxCeQ",
    "tco-tank": "https://t.co/e52sosOqMo",
    "tco-pi-handoff": "https://t.co/sICsFS7iok",
    "tco-bugatti": "https://t.co/rEYQ9u3OkL",
    "tco-canvas": "https://t.co/kCeD3FdbjQ",
    "tco-hqflow1": "https://t.co/abPVj6fHns",
    "tco-hqflow2": "https://t.co/WZcbOIv0ZQ",
    "tco-saas1": "https://t.co/2w2o3mYt0Z",
    "tco-saas2": "https://t.co/aDdpemWAZq",
    "tco-designertom": "https://t.co/HGmk7r0lca",
    "tco-designertom2": "https://t.co/HB61RYqWwL",
    "tco-imperfect": "https://t.co/7KMjpeWZBU",
    "tco-rl-paint": "https://t.co/4x5B81kjUh",
    "tco-bee": "https://t.co/Q54h0e3zSv",
    "tco-polish": "https://t.co/uCbX29UOlj",
    "tco-polish2": "https://t.co/fcpwDR65ON",
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
    path = Path("/workspace/analysis/_work/captures/leftover13-2026-09-05.json")
    path.write_text(json.dumps({"fetched_at": "2026-09-05T06:45:00Z", "pages": pages}, indent=2), encoding="utf-8")
    print("wrote", path)


if __name__ == "__main__":
    main()

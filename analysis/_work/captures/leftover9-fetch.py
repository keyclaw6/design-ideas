#!/usr/bin/env python3
"""leftover9 first-party fetches. No GPU. Skip known 429/403 hosts."""
from __future__ import annotations

import json
import os
import re
import ssl
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

OUT = Path("/workspace/analysis/_work/captures/leftover9-2026-09-05")
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
                out["json_summary"] = {"len": len(data), "head": data[:5]}
        except Exception as e:
            path.write_bytes(body[:80_000])
            out["saved"] = str(path)
            out["parse_error"] = str(e)
        return out
    # html / text
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
    # keep a small html excerpt, not bulky dump
    excerpt = OUT / f"{slug}-excerpt.html"
    excerpt.write_text(text[:20_000], encoding="utf-8")
    out["excerpt_saved"] = str(excerpt)
    return out


URLS = {
    "tco-sound": "https://t.co/ClE6SOWP5f",
    "tco-template": "https://t.co/KhAZy3E4ZG",
    "tco-range": "https://t.co/zPK69FjkG8",
    "higgsfield-home": "https://higgsfield.ai/",
    "fable-ai": "https://fable.ai/",
    "fable-so": "https://fable.so/",
    "fable-dev": "https://fable.dev/",
    "fable-inc": "https://www.fable.com/",
    "claude-fable": "https://www.anthropic.com/claude",
    "glm-zhipu": "https://z.ai/",
    "glm-open": "https://open.bigmodel.cn/",
    "glm-docs": "https://docs.z.ai/",
    "vanh-design": "https://vanh.design/",
    "vanhdesign-com": "https://vanhdesign.com/",
    "vanhdesign-io": "https://vanhdesign.io/",
    "designbymoein": "https://designbymoein.com/",
    "moeindesign": "https://www.moeindesign.com/",
    "pryne": "https://pryne.com/",
    "lexnlin": "https://lexnlin.com/",
    "raylight": "https://raylight.ai/",
    "raylight-app": "https://www.raylight.app/",
    "cyburns": "https://cyburns.com/",
    "hermes-nous-home": "https://hermes-agent.nousresearch.com/",
    "edge8-gh-search": "https://api.github.com/search/repositories?q=Edge8-35B",
    "edge8-gh-search2": "https://api.github.com/search/repositories?q=edge8+35b",
    "glm-gh-search": "https://api.github.com/search/repositories?q=GLM-5.3-Flash",
    "fable-gh-search": "https://api.github.com/search/repositories?q=fable+5.1+cad",
    "vanh-gh": "https://api.github.com/users/VanhDesign/repos?per_page=20",
    "hf-glm": "https://huggingface.co/api/models?search=GLM-5.3-Flash&limit=8",
    "hf-edge8": "https://huggingface.co/api/models?search=Edge8-35B&limit=8",
}


def main() -> None:
    pages = {}
    for slug, url in URLS.items():
        print(f"GET {slug} {url}", flush=True)
        rec = fetch(url)
        pages[slug] = summarize_html(rec, slug)
        # drop body leftovers
        pages[slug].pop("body", None)
        print(
            f"  -> {pages[slug].get('status')} {pages[slug].get('bytes')} {pages[slug].get('final')} {pages[slug].get('error')}",
            flush=True,
        )
        time.sleep(0.4)
    out = {
        "fetched_at": "2026-09-05T05:20:00Z",
        "pages": pages,
    }
    path = Path("/workspace/analysis/_work/captures/leftover9-2026-09-05.json")
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("wrote", path)


if __name__ == "__main__":
    main()

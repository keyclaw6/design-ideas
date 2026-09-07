#!/usr/bin/env python3
"""Parse `tnr create --json`. Prints KEY=value lines for eval."""
from __future__ import annotations

import json
import re
import sys


def parse(raw: str) -> dict[str, str]:
    m = re.search(r"(\{.*\}|\[.*\])", raw, re.S)
    id_ = uuid = key = ""
    if m:
        try:
            d = json.loads(m.group(1))
            it = d[0] if isinstance(d, list) else d
            if isinstance(it, dict):
                ident = it.get("identifier", it.get("id", ""))
                id_ = str(ident) if ident is not None and ident != "" else ""
                uuid = str(it.get("uuid") or "")
                key = str(it.get("key") or "")
        except json.JSONDecodeError:
            pass
    if id_ and ("-" in id_ or len(id_) > 20):
        # accidentally grabbed a UUID as id
        if not uuid:
            uuid = id_
        id_ = ""
    if not id_ and uuid.isdigit():
        id_ = uuid
    return {
        "INSTANCE_ID": id_ or uuid,
        "INSTANCE_UUID": uuid,
        "TNR_INDEX": id_ if id_ and len(id_) <= 20 else "0",
        "HAS_KEY": "1" if key.strip() else "0",
        "KEY_PEM": key,
    }


def main() -> None:
    raw = sys.stdin.read()
    d = parse(raw)
    pem = d.pop("KEY_PEM")
    for k, v in d.items():
        print(f"{k}={v}")
    if pem.strip():
        out = sys.argv[1] if len(sys.argv) > 1 else ""
        if out:
            Path = __import__("pathlib").Path
            p = Path(out)
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(pem if pem.endswith("\n") else pem + "\n")
            p.chmod(0o600)


if __name__ == "__main__":
    main()

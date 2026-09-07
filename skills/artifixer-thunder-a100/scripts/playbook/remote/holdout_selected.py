#!/usr/bin/env python3
"""Hold out every 3rd still as ArtiFixer3D target (issue #13). Rest are GT anchors."""
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--images", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--exclude-re", default="")
    p.add_argument("--wide-json", type=Path, default=None)
    args = p.parse_args()
    names = sorted(x.name for x in args.images.glob("*.jpg"))
    if args.wide_json and args.wide_json.is_file():
        import json

        wide = json.loads(args.wide_json.read_text())
        if isinstance(wide, dict):
            wide = list(wide)
        names = [n for n in names if n in set(wide)]
    elif args.exclude_re:
        import re

        rx = re.compile(args.exclude_re)
        names = [n for n in names if not rx.search(n)]
    selected = [n for i, n in enumerate(names) if i % 3 != 2]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(selected) + ("\n" if selected else ""))
    print(f"images={len(list(args.images.glob('*.jpg')))} eligible={len(names)} anchors={len(selected)} -> {args.out}")


if __name__ == "__main__":
    main()

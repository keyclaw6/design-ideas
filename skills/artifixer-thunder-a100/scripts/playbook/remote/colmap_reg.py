#!/usr/bin/env python3
"""Registered-image fraction from COLMAP sparse/0 (TXT or BIN)."""
from __future__ import annotations

import struct
import sys
from pathlib import Path


def count_images_bin(path: Path) -> int:
    data = path.read_bytes()
    n = struct.unpack_from("<Q", data, 0)[0]
    return int(n)


def count_images_txt(path: Path) -> int:
    n = 0
    lines = path.read_text(errors="replace").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.startswith("#"):
            i += 1
            continue
        n += 1
        i += 2
    return n


def main() -> None:
    sparse = Path(sys.argv[1])
    n_jpg = int(sys.argv[2])
    min_pct = float(sys.argv[3]) if len(sys.argv) > 3 else 30.0
    n_reg = 0
    txt = sparse / "images.txt"
    binf = sparse / "images.bin"
    if txt.is_file():
        n_reg = count_images_txt(txt)
    elif binf.is_file():
        n_reg = count_images_bin(binf)
    pct = 100.0 * n_reg / max(n_jpg, 1)
    print(f"registered={n_reg}/{n_jpg} ({pct:.1f}%) min={min_pct}")
    sys.exit(0 if pct + 1e-6 >= min_pct else 3)


if __name__ == "__main__":
    main()

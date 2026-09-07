#!/usr/bin/env python3
"""Kill-gate: recon_results PNGs + 30k ckpt + issue #13 selected != 100%."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    root = Path(sys.argv[1])
    recon = root / "recon_results"
    pngs = list(recon.rglob("*.png")) if recon.is_dir() else []
    ckpts = list(root.rglob("ckpt_30000.pt")) + list(root.rglob("ckpt_last.pt"))
    sel_p = root / "selected_indices.json"
    n_sel = 0
    if sel_p.is_file():
        sel = json.loads(sel_p.read_text())
        n_sel = len(sel) if isinstance(sel, list) else len(sel.get("selected", sel))
    n_img = len(list((root / "3dgrut_input").rglob("*.jpg"))) + len(
        list((root / "3dgrut_input").rglob("*.png"))
    )
    print(f"gate {root} pngs={len(pngs)} ckpts={len(ckpts)} selected={n_sel} images={n_img}")
    if not recon.is_dir() or len(pngs) < 8:
        print("FAIL: recon_results missing or too few PNGs (needle-soup / empty recon)", file=sys.stderr)
        sys.exit(1)
    if not ckpts:
        print("FAIL: no ckpt_30000.pt", file=sys.stderr)
        sys.exit(1)
    if n_img and n_sel and n_sel >= n_img:
        print("FAIL: issue #13 — selected covers every frame (3D becomes a no-op)", file=sys.stderr)
        sys.exit(1)
    print("PASS")


if __name__ == "__main__":
    main()

#!/usr/bin/env bash
# Pack per-object stills + C4 COLMAP. Longest edge 1600. No C8, no Woshixing.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=00_env.sh
source "$SCRIPT_DIR/00_env.sh"

SRC="${SPLAT_OBJECTS:-$HOME/Downloads/splat-objects}"
C4_COLMAP="${HOME}/.cache/bess-splat-plan/scene-zip5/colmap"
STAGING="${ROOT}/upload/staging"
TAR="${ROOT}/upload/scenes.tar"

if [[ -f "${ROOT}/upload/scenes.tar.gz" && "${FORCE_PACK:-0}" != "1" ]]; then
  echo "scenes archive exists $(du -h "${ROOT}/upload/scenes.tar.gz" | awk '{print $1}')"
  exit 0
fi

rm -rf "$STAGING"
mkdir -p "$STAGING"

map_copy() {
  local name="$1" dest="$2"
  mkdir -p "$STAGING/$dest/images"
  find "$SRC/$name" -maxdepth 2 -iname '*.jpg' ! -path '*_previews*' \
    -exec cp -n {} "$STAGING/$dest/images/" \;
}

map_copy 05-envicool-lcu-closed c5-lcu-closed
map_copy 06-envicool-lcu-open c6-lcu-open
map_copy 01-pcs-inverter-open c1-pcs
map_copy 02-bcu-b30-chassis c2-bcu
map_copy 07-zg-mod-52-face c7-module-face
C4_IMG="${HOME}/.cache/bess-splat-plan/scene-zip5/images-1600"
mkdir -p "$STAGING/c4-cabinet/images"
if [[ -d "$C4_IMG" ]]; then
  find "$C4_IMG" -maxdepth 1 -iname '*.jpg' -exec cp -n {} "$STAGING/c4-cabinet/images/" \;
else
  map_copy 04-assembled-open-cabinet c4-cabinet
fi
rm -f "$STAGING/c6-lcu-open/images/20260610_140213.jpg" || true

python3 - <<RESIZE
from pathlib import Path
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
root = Path(r"""$STAGING""")
n_ok = n_skip = 0
for jpg in root.rglob("*.jpg"):
    try:
        im = Image.open(jpg)
        im.load()
        im = im.convert("RGB")
        w, h = im.size
        long = max(w, h)
        if long > 1600:
            s = 1600 / long
            im = im.resize((max(1, int(w * s)), max(1, int(h * s))), Image.LANCZOS)
            im.save(jpg, quality=92, optimize=True)
        n_ok += 1
    except Exception as e:
        print("skip", jpg, e)
        n_skip += 1
print(f"resized ok={n_ok} skip={n_skip}")
RESIZE

if [[ -d "$C4_COLMAP/sparse/0" ]]; then
  mkdir -p "$STAGING/c4-cabinet/sparse/0"
  cp -a "$C4_COLMAP/sparse/0/"*.bin "$STAGING/c4-cabinet/sparse/0/"
  [[ -f "$C4_COLMAP/wide.json" ]] && cp -a "$C4_COLMAP/wide.json" "$STAGING/c4-cabinet/"
  [[ -f "$C4_COLMAP/registered.json" ]] && cp -a "$C4_COLMAP/registered.json" "$STAGING/c4-cabinet/"
fi

python3 "$SCRIPT_DIR/holdout_selected.py" --images "$STAGING/c4-cabinet/images" \
  --out "$STAGING/c4-cabinet/selected.txt" \
  --wide-json "$STAGING/c4-cabinet/wide.json"

tar -C "$STAGING" -cf "$TAR" .
gzip -f "$TAR"
echo "Wrote ${TAR}.gz"
du -h "${TAR}.gz"

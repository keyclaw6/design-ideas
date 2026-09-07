#!/usr/bin/env python3
"""Render posed RGB-D from a 3DGRUT checkpoint for local Open3D TSDF.

T_to_world is camera-to-world, OpenCV RDF (right-down-front), same as Open3D pinhole.
pred_dist[..., 0] is the first-hit distance; low-opacity pixels are written as 0.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import torch
import torchvision


def load_scale(path: Path | None) -> float:
    if path is None or not path.is_file():
        return 1.0
    for line in path.read_text().splitlines():
        if ":" in line:
            try:
                return float(line.split(":")[-1].strip())
            except ValueError:
                continue
    return 1.0


def rgb_key(outputs: dict) -> torch.Tensor:
    for k in ("pred_features", "pred_rgb"):
        if k in outputs:
            return outputs[k]
    raise KeyError(list(outputs))


def fx_fy_cx_cy(gpu_batch, h: int, w: int) -> tuple[float, float, float, float]:
    intr = getattr(gpu_batch, "intrinsics", None)
    if isinstance(intr, (list, tuple)) and len(intr) == 4:
        return float(intr[0]), float(intr[1]), float(intr[2]), float(intr[3])
    for name in dir(gpu_batch):
        if not name.startswith("intrinsics_"):
            continue
        d = getattr(gpu_batch, name)
        if isinstance(d, dict) and "focal_length" in d:
            fl = np.asarray(d["focal_length"]).reshape(-1)
            pp = np.asarray(d.get("principal_point", [w / 2, h / 2])).reshape(-1)
            return float(fl[0]), float(fl[min(1, len(fl) - 1)]), float(pp[0]), float(pp[min(1, len(pp) - 1)])
    return float(w), float(w), w / 2.0, h / 2.0


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--checkpoint", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--colmap-dir", type=Path, default=None)
    p.add_argument("--scale-file", type=Path, default=None)
    p.add_argument("--max-frames", type=int, default=0)
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    from threedgrut.datasets import make_test
    from threedgrut.model.model import MixtureOfGaussians
    from threedgrut.utils.render import apply_background, apply_feature_decoder, apply_post_processing

    ckpt = torch.load(str(args.checkpoint), weights_only=False, map_location="cpu")
    conf = ckpt["config"]
    if args.colmap_dir is not None:
        conf.path = str(args.colmap_dir)
    # non-positive interval = dump every camera (3DGRUT ColmapDataset)
    if hasattr(conf, "dataset"):
        conf.dataset.test_split_interval = 0
    model = MixtureOfGaussians(conf)
    model.init_from_checkpoint(ckpt, setup_optimizer=False)
    model.build_acc()
    model.eval()

    dataset = make_test(name=conf.dataset.type, config=conf)
    loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, num_workers=0)

    scale = load_scale(args.scale_file)
    n = 0
    k_written = False
    with torch.no_grad():
        for i, batch in enumerate(loader):
            if args.max_frames and i >= args.max_frames:
                break
            gpu_batch = dataset.get_gpu_batch_with_intrinsics(batch)
            outputs = model(gpu_batch)
            outputs = apply_background(model.background, outputs, gpu_batch, training=False)
            rgb = rgb_key(outputs)
            dist = outputs.get("pred_dist")
            opac = outputs.get("pred_opacity")
            if dist is None:
                raise RuntimeError("checkpoint renderer has no pred_dist — cannot dump TSDF depth")
            rgb_np = rgb.squeeze(0).clamp(0, 1).detach().float().cpu()
            if rgb_np.ndim == 3 and rgb_np.shape[-1] == 3:
                rgb_chw = rgb_np.permute(2, 0, 1)
            else:
                rgb_chw = rgb_np
            torchvision.utils.save_image(rgb_chw, str(args.out / f"frame_{i:04d}.color.png"))
            depth = dist.squeeze(0)[..., 0].detach().float().cpu().numpy().astype(np.float32)
            if opac is not None:
                a = opac.squeeze(0)[..., 0].detach().float().cpu().numpy()
                depth = np.where(a >= 0.15, depth, 0.0).astype(np.float32)
            if scale != 1.0:
                depth = depth * scale
            np.save(args.out / f"frame_{i:04d}.depth.npy", depth)
            pose = gpu_batch.T_to_world.squeeze(0).detach().float().cpu().numpy()
            if scale != 1.0:
                pose = pose.copy()
                pose[:3, 3] *= scale
            np.savetxt(args.out / f"frame_{i:04d}.pose.txt", pose)
            h, w = depth.shape[:2]
            fx, fy, cx, cy = fx_fy_cx_cy(gpu_batch, h, w)
            if not k_written:
                K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]], dtype=np.float64)
                np.savetxt(args.out / "K.txt", K)
                k_written = True
            n += 1
    meta = {"frames": n, "scale": scale, "checkpoint": str(args.checkpoint)}
    (args.out / "dump_meta.json").write_text(json.dumps(meta, indent=2))
    print(f"dumped {n} RGB-D frames -> {args.out}")
    if n == 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

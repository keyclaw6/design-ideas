#!/usr/bin/env python3
"""Fuse posed RGB-D frames with Open3D TSDF."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--depth-dir", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--voxel", type=float, default=0.005)
    p.add_argument("--fx", type=float, default=0.0)
    p.add_argument("--fy", type=float, default=0.0)
    p.add_argument("--cx", type=float, default=0.0)
    p.add_argument("--cy", type=float, default=0.0)
    args = p.parse_args()
    try:
        import open3d as o3d
    except ImportError:
        print("Install: python3 -m pip install open3d", file=sys.stderr)
        sys.exit(2)

    colors = sorted(args.depth_dir.glob("*.color.png"))
    if not colors:
        print(f"No *.color.png in {args.depth_dir}", file=sys.stderr)
        sys.exit(1)

    kpath = args.depth_dir / "K.txt"
    if kpath.is_file():
        K = np.loadtxt(kpath)
        fx, fy, cx, cy = float(K[0, 0]), float(K[1, 1]), float(K[0, 2]), float(K[1, 2])
    else:
        fx, fy, cx, cy = args.fx, args.fy, args.cx, args.cy
        if not fx:
            print("Need K.txt or --fx --fy --cx --cy", file=sys.stderr)
            sys.exit(1)

    volume = o3d.pipelines.integration.ScalableTSDFVolume(
        voxel_length=args.voxel,
        sdf_trunc=max(args.voxel * 4, 0.02),
        color_type=o3d.pipelines.integration.TSDFVolumeColorType.RGB8,
    )
    n = 0
    for color_p in colors:
        stem = color_p.name.replace(".color.png", "")
        depth_p = args.depth_dir / f"{stem}.depth.npy"
        pose_p = args.depth_dir / f"{stem}.pose.txt"
        if not depth_p.is_file() or not pose_p.is_file():
            continue
        color = o3d.io.read_image(str(color_p))
        depth_np = np.load(depth_p).astype(np.float32)
        depth = o3d.geometry.Image(depth_np)
        h, w = depth_np.shape[:2]
        intrinsic = o3d.camera.PinholeCameraIntrinsic(w, h, fx, fy, cx, cy)
        pose = np.loadtxt(pose_p)
        rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(
            color, depth, depth_scale=1.0, depth_trunc=8.0, convert_rgb_to_intensity=False
        )
        volume.integrate(rgbd, intrinsic, np.linalg.inv(pose))
        n += 1
    if n == 0:
        print("No complete color/depth/pose triples", file=sys.stderr)
        sys.exit(1)
    mesh = volume.extract_triangle_mesh()
    mesh.compute_vertex_normals()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    o3d.io.write_triangle_mesh(str(args.out), mesh)
    print(f"wrote {args.out} frames={n} verts={len(mesh.vertices)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Check that the complete internal coordinate census leaves a quadratic reservoir."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} EXAMPLE.json")

    data = json.loads(Path(sys.argv[1]).read_text())
    m = int(data["m"])
    M = int(data["M"])
    R = int(data["R"])
    W = int(data["W"])
    slab_reserved = int(data["slab_reserved"])
    small_reserved = int(data["small_reserved"])
    marked_size = int(data["marked_size"])
    helper_constant = int(data["helper_constant"])

    if slab_reserved >= m:
        raise AssertionError("slab reservation is already a complete cover")
    if marked_size > W:
        raise AssertionError("marked block exceeds the target scale")

    total_reserved = slab_reserved + small_reserved + marked_size
    available = m - total_reserved
    helper_demand = helper_constant * marked_size * marked_size

    if helper_demand > helper_constant * R:
        raise AssertionError("quadratic helper demand exceeds the stored R-scale bound")
    if available < helper_demand:
        raise AssertionError("internal reservation census does not leave the required reservoir")

    slab_density = slab_reserved / m
    available_density = available / m
    demand_to_available = helper_demand / available

    print("m", m)
    print("M", M)
    print("R", R)
    print("W", W)
    print("slab reserved", slab_reserved)
    print("slab reserved density", slab_density)
    print("small reserved", small_reserved)
    print("marked size", marked_size)
    print("total reserved", total_reserved)
    print("available coordinates", available)
    print("available density", available_density)
    print("quadratic helper demand", helper_demand)
    print("helper demand to available ratio", demand_to_available)
    print("outcome internal_reservation_leaves_automatic_helper_reservoir")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite diagnostic for PP3ali--PP3alm."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main(path: str) -> None:
    data = json.loads(Path(path).read_text())

    W = int(data["W"])
    R = int(data["R"])
    blocks = int(data["blocks"])
    side = int(data["block_side"])
    column_mass_factor = float(data["column_mass_factor"])

    if not (1 <= side < W):
        raise ValueError("block_side must lie in [1,W)")

    column_mass = blocks * side * side
    column_threshold = column_mass_factor * R
    maximum_source_degree = side
    exact_endpoint_matching = blocks * side
    theorem_matching_lower_bound = column_mass / (2 * W)
    one_layer_anchor_bank = min(W, exact_endpoint_matching // 2)
    batch_puncture_ratio = one_layer_anchor_bank / R

    if (
        column_mass > column_threshold
        and maximum_source_degree < W
        and one_layer_anchor_bank >= W
    ):
        outcome = "fixed_label_anchor_endpoint_bank"
    elif maximum_source_degree >= W:
        outcome = "fixed_label_anchor_source_star"
    else:
        outcome = "fixed_label_anchor_threshold_not_met"

    print(f"W {W}")
    print(f"R {R}")
    print(f"fixed-label anchor column mass {column_mass}")
    print(f"column threshold {column_threshold}")
    print(f"maximum source degree {maximum_source_degree}")
    print(f"exact endpoint matching {exact_endpoint_matching}")
    print(f"matching lower bound {theorem_matching_lower_bound}")
    print(f"one-layer anchor bank {one_layer_anchor_bank}")
    print(f"batch puncture ratio {batch_puncture_ratio}")
    print(f"outcome {outcome}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} INSTANCE.json")
    main(sys.argv[1])

#!/usr/bin/env python3
"""Finite diagnostic for PP3alc--PP3alh."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main(path: str) -> None:
    data = json.loads(Path(path).read_text())

    W = int(data["W"])
    R = int(data["R"])
    delta = float(data["delta"])
    blocks = int(data["blocks"])
    side = int(data["block_side"])

    if not (1 <= side < W):
        raise ValueError("block_side must lie in [1,W)")

    bad_entries = blocks * side * side
    maximum_blocker_degree = side
    exact_resource_matching = blocks * side
    greedy_resource_lower_bound = bad_entries / (3 * (W + 1))
    one_layer_endpoint_bank = min(W, exact_resource_matching // 2)
    batch_puncture_ratio = one_layer_endpoint_bank / R
    fibre_threshold = delta * R

    if (
        bad_entries > fibre_threshold
        and maximum_blocker_degree < W
        and one_layer_endpoint_bank >= W
    ):
        outcome = "fixed_label_resource_bank"
    elif maximum_blocker_degree >= W:
        outcome = "fixed_label_blocker_star"
    else:
        outcome = "fixed_label_threshold_not_met"

    print(f"W {W}")
    print(f"R {R}")
    print(f"bad fixed-label entries {bad_entries}")
    print(f"delta R threshold {fibre_threshold}")
    print(f"maximum blocker degree {maximum_blocker_degree}")
    print(f"exact resource matching {exact_resource_matching}")
    print(f"greedy resource lower bound {greedy_resource_lower_bound}")
    print(f"one-layer endpoint bank {one_layer_endpoint_bank}")
    print(f"batch puncture ratio {batch_puncture_ratio}")
    print(f"outcome {outcome}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} INSTANCE.json")
    main(sys.argv[1])

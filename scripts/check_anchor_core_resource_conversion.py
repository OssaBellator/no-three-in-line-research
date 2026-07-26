#!/usr/bin/env python3
"""Finite diagnostic for PP3akv--PP3alb."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main(path: str) -> None:
    data = json.loads(Path(path).read_text())

    W = int(data["W"])
    D_m = int(data["D_m"])
    R = int(data["R"])
    blocks = int(data["blocks"])
    side = int(data["block_side"])
    pair_multiplicity = int(data["pair_multiplicity"])
    domain_lower = int(data["domain_lower"])

    if not (1 <= side < W):
        raise ValueError("block_side must lie in [1,W)")

    physical_pairs = blocks * side * side
    slot_energy = physical_pairs * pair_multiplicity
    physical_multiplicity_cap = W * D_m
    if pair_multiplicity > physical_multiplicity_cap:
        raise AssertionError("physical pair multiplicity exceeds W*D_m")

    pair_lower_bound = slot_energy / physical_multiplicity_cap
    maximum_source_degree = side
    exact_matching_size = blocks * side
    theorem_matching_lower_bound = pair_lower_bound / (2 * W)
    core_threshold = 2 * D_m * W**3

    # After the graph matching, pigeonhole the anchor endpoints between two source
    # layers and retain any W of the resulting common-layer bank.
    one_layer_anchor_bank = min(W, exact_matching_size // 2)
    post_puncture_domain_lower = domain_lower - one_layer_anchor_bank

    threshold_met = slot_energy > core_threshold
    matching_branch = maximum_source_degree < W
    bank_complete = one_layer_anchor_bank >= W

    if threshold_met and matching_branch and bank_complete:
        outcome = "batch_punctured_anchor_endpoint_bank"
    elif maximum_source_degree >= W:
        outcome = "target_size_anchor_source_star"
    else:
        outcome = "anchor_core_threshold_not_met"

    print(f"W {W}")
    print(f"D_m {D_m}")
    print(f"distinct pair count {physical_pairs}")
    print(f"slot-expanded energy {slot_energy}")
    print(f"core threshold {core_threshold}")
    print(f"pair lower bound {pair_lower_bound}")
    print(f"maximum source degree {maximum_source_degree}")
    print(f"exact matching size {exact_matching_size}")
    print(f"matching lower bound {theorem_matching_lower_bound}")
    print(f"one-layer anchor bank {one_layer_anchor_bank}")
    print(f"post-puncture domain lower bound {post_puncture_domain_lower}")
    print(f"puncture/domain ratio {one_layer_anchor_bank / R}")
    print(f"outcome {outcome}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} INSTANCE.json")
    main(sys.argv[1])

#!/usr/bin/env python3
"""Check the weighted unary/binary activation localization thresholds."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()

    data = json.loads(args.input.read_text())
    s = int(data["marked_size"])
    n = int(data["helper_reservoir"])
    credit = int(data["removal_credit"])
    singleton_weights = [int(value) for value in data["singleton_weights"]]
    clique_vertices = int(data["binary_clique_vertices"])
    edge_weight = int(data["binary_edge_weight"])

    if not (2 <= s <= n):
        raise AssertionError("invalid marked/helper sizes")
    if credit <= 0 or edge_weight <= 0:
        raise AssertionError("credit and edge weight must be positive")
    if clique_vertices > n:
        raise AssertionError("binary clique exceeds helper reservoir")

    w1 = sum(singleton_weights)
    w2 = clique_vertices * (clique_vertices - 1) // 2 * edge_weight
    threshold1 = credit * n / (2 * s)
    threshold2 = credit * n * (n - 1) / (2 * s * (s - 1))
    expected_upper = (s / n) * w1 + (s * (s - 1) / (n * (n - 1))) * w2

    if w1 < threshold1:
        raise AssertionError("stored unary mass does not reach the failure threshold")
    if w2 < threshold2:
        raise AssertionError("stored binary mass does not reach the failure threshold")

    max_singleton = max(singleton_weights, default=0)
    positive_singletons = sum(1 for value in singleton_weights if value > 0)
    if max_singleton >= credit:
        unary_outcome = "heavy_singleton"
    elif positive_singletons >= s:
        unary_outcome = "target_singleton_bank"
    else:
        raise AssertionError("unary localization produced neither endpoint")

    max_weighted_degree = (clique_vertices - 1) * edge_weight
    matching_size = clique_vertices // 2
    if edge_weight >= credit:
        binary_outcome = "heavy_pair"
    elif matching_size >= s:
        binary_outcome = "target_binary_matching"
    elif max_weighted_degree >= credit * s:
        binary_outcome = "weighted_helper_star"
    else:
        raise AssertionError("binary localization produced no target endpoint")

    if expected_upper < credit:
        raise AssertionError("stored combined mass does not model activation failure")

    print("marked size", s)
    print("helper reservoir", n)
    print("removal credit", credit)
    print("unary threshold", threshold1)
    print("binary threshold", threshold2)
    print("unary mass", w1)
    print("maximum singleton weight", max_singleton)
    print("positive singleton supports", positive_singletons)
    print("unary outcome", unary_outcome)
    print("binary mass", w2)
    print("maximum weighted degree", max_weighted_degree)
    print("binary matching size", matching_size)
    print("binary outcome", binary_outcome)
    print("activation expectation upper bound", expected_upper)
    print("outcome", "same_slot_anchor_activation_localization")


if __name__ == "__main__":
    main()

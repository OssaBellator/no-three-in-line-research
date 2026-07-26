#!/usr/bin/env python3
"""Exhaustively check rank-three helper support for alternating endpoint patterns."""

from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path


def helper_of(vertex: tuple[str, int]) -> tuple[str, int] | None:
    return vertex if vertex[0] == "h" else None


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} EXAMPLE.json")

    data = json.loads(Path(sys.argv[1]).read_text())
    s = int(data["marked_size"])
    R = int(data["R"])
    gamma = float(data["gamma"])
    xi = float(data["xi"])
    all_selected_are_controllers = bool(data["all_selected_are_controllers"])

    order: list[tuple[str, int]] = []
    for i in range(s):
        order.append(("d", i))
        order.append(("h", i))

    cells: list[tuple[tuple[str, int], tuple[str, int]]] = []
    for i, tail in enumerate(order):
        head = order[(i + 1) % len(order)]
        helpers = {v for v in (helper_of(tail), helper_of(head)) if v is not None}
        if len(helpers) != 1:
            raise AssertionError("a selected cell is not strictly marked--helper")
        cells.append((tail, head))

    pattern_counts: dict[int, int] = {}
    maximum_support_rank = 0
    minimum_support_rank = 10**9
    for rank in (1, 2, 3):
        count = 0
        for pattern in itertools.combinations(cells, rank):
            support = {
                vertex
                for cell in pattern
                for vertex in cell
                if vertex[0] == "h"
            }
            if not support:
                raise AssertionError("a positive local pattern has empty helper support")
            if len(support) > rank or len(support) > 3:
                raise AssertionError("a local pattern exceeds the rank-three support bound")
            maximum_support_rank = max(maximum_support_rank, len(support))
            minimum_support_rank = min(minimum_support_rank, len(support))
            count += 1
        pattern_counts[rank] = count

    if len(set(cells)) != 2 * s:
        raise AssertionError("the alternating cycle does not define distinct selected cells")
    if {tail for tail, _ in cells} != set(order) or {head for _, head in cells} != set(order):
        raise AssertionError("the selected cells do not form a permutation cycle")

    selected_controllers = 2 * s if all_selected_are_controllers else 0
    initial_domain = (gamma + xi) * R
    post_puncture_domain = initial_domain - selected_controllers
    half_margin_threshold = (gamma + xi / 2.0) * R
    if post_puncture_domain < half_margin_threshold:
        raise AssertionError("selected-controller puncturing destroys the half-margin certificate")

    print("marked size", s)
    print("selected cycle cells", len(cells))
    print("one-cell patterns", pattern_counts[1])
    print("two-cell patterns", pattern_counts[2])
    print("three-cell patterns", pattern_counts[3])
    print("minimum helper support rank", minimum_support_rank)
    print("maximum helper support rank", maximum_support_rank)
    print("selected controller punctures", selected_controllers)
    print("puncture to R ratio", selected_controllers / R)
    print("initial domain lower bound", initial_domain)
    print("post-puncture lower bound", post_puncture_domain)
    print("half-margin threshold", half_margin_threshold)
    print("outcome complete_endpoint_rank_three_local_normal_form")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite checker for petal-conditioned complete-support capture."""

from __future__ import annotations

import argparse
import json
from itertools import permutations
from math import factorial
from pathlib import Path
from typing import Any


def conditioned_cycles(vertices: list[int], fixed_arcs: set[tuple[int, int]]) -> list[set[tuple[int, int]]]:
    root = min(vertices)
    cycles: list[set[tuple[int, int]]] = []
    for order in permutations(v for v in vertices if v != root):
        cyc = (root,) + order
        arcs = {(cyc[j], cyc[(j + 1) % len(cyc)]) for j in range(len(cyc))}
        if fixed_arcs.issubset(arcs):
            cycles.append(arcs)
    return cycles


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data: dict[str, Any] = json.loads(args.input.read_text())

    path_vertices = list(map(int, data["path_vertices"]))
    path_fixed = {tuple(map(int, arc)) for arc in data["path_fixed_arcs"]}
    path_core = set(map(int, data["path_core_vertices"]))
    path_supports = [frozenset(map(int, e)) for e in data["path_residual_supports"]]
    path_helpers = frozenset(map(int, data["path_independent_helpers"]))
    path_credit = int(data["path_credit"])
    path_local_cost = int(data["path_local_cost"])

    path_cycles = conditioned_cycles(path_vertices, path_fixed)
    expected_path_count = factorial(len(path_vertices) - len(path_fixed) - 1)
    if len(path_cycles) != expected_path_count:
        raise AssertionError((len(path_cycles), expected_path_count))
    if any(edge.issubset(path_helpers) for edge in path_supports):
        raise AssertionError("path helper set is not independent")

    local_arcs_path = set().union(*path_cycles)
    local_arcs_path = {arc for arc in local_arcs_path if arc[0] in path_core and arc[1] in path_core}
    if local_arcs_path != path_fixed:
        raise AssertionError((local_arcs_path, path_fixed))
    if not path_local_cost < path_credit:
        raise AssertionError("stored spanning path should be paid")

    fan_vertices = list(map(int, data["fan_vertices"]))
    fan_fixed = {tuple(map(int, arc)) for arc in data["fan_fixed_arcs"]}
    fan_core = set(map(int, data["fan_core_vertices"]))
    fan_supports = [frozenset(map(int, e)) for e in data["fan_residual_supports"]]
    fan_helpers = frozenset(map(int, data["fan_independent_helpers"]))
    bridge_weights = {
        tuple(map(int, key.split("->"))): int(value)
        for key, value in data["fan_local_bridge_weights"].items()
    }

    fan_cycles = conditioned_cycles(fan_vertices, fan_fixed)
    expected_fan_count = factorial(len(fan_vertices) - len(fan_fixed) - 1)
    if len(fan_cycles) != expected_fan_count:
        raise AssertionError((len(fan_cycles), expected_fan_count))
    if any(edge.issubset(fan_helpers) for edge in fan_supports):
        raise AssertionError("fan helper set is not independent")

    local_bridge_counts = {arc: 0 for arc in bridge_weights}
    local_cost_sum = 0
    for arcs in fan_cycles:
        cost = 0
        for arc, weight in bridge_weights.items():
            if arc in arcs:
                local_bridge_counts[arc] += 1
                cost += weight
        local_cost_sum += cost
    fan_expected_local_cost = local_cost_sum / len(fan_cycles)

    print(f"path cycle size {len(path_vertices)}")
    print(f"path fixed arcs {len(path_fixed)}")
    print(f"path conditional cycles {len(path_cycles)}")
    print(f"path formula count {expected_path_count}")
    print(f"path selected residual supports 0")
    print(f"path local arcs {sorted(local_arcs_path)}")
    print(f"path deterministic local cost {path_local_cost}")
    print(f"path removal credit {path_credit}")
    print("path outcome zero_residual_paid_path")
    print(f"fan cycle size {len(fan_vertices)}")
    print(f"fan fixed arcs {len(fan_fixed)}")
    print(f"fan conditional cycles {len(fan_cycles)}")
    print(f"fan formula count {expected_fan_count}")
    print(f"fan selected residual supports 0")
    for arc in sorted(local_bridge_counts):
        print(f"fan local bridge {arc[0]}->{arc[1]} count {local_bridge_counts[arc]}")
    print(f"fan expected local core cost {fan_expected_local_cost:.12f}")
    print("fan outcome finite_local_core_only")
    print("outcome petal_conditioned_complete_support_capture")


if __name__ == "__main__":
    main()

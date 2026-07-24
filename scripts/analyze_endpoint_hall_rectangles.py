#!/usr/bin/env python3
"""Extract PP3jz Hall rectangles from endpoint-safe hosts.

The current certificate diagnostic reports maximum matching sizes.  This script
adds an exact Hall witness whenever a full or PP3is-pruned endpoint host has no
perfect matching.  It also reports every complementary-degree violation of the
bipartite Ore criterion PP3kc.
"""
from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path
from typing import Any

from analyze_endpoint_trade_hosts import build_safe_graph, prune_indices
from analyze_random_matching_block_preparation import load_certificates, matching_layers

Point = tuple[int, int]
Graph = tuple[frozenset[int], ...]


def maximum_matching(
    graph: Graph, active: set[int]
) -> tuple[dict[int, int], dict[int, int]]:
    """Return left-to-right and right-to-left maps for a maximum matching."""
    right_owner: dict[int, int] = {}

    def augment(left: int, seen: set[int]) -> bool:
        for right in sorted(graph[left] & active):
            if right in seen:
                continue
            seen.add(right)
            owner = right_owner.get(right)
            if owner is None or augment(owner, seen):
                right_owner[right] = left
                return True
        return False

    for left in sorted(active, key=lambda item: len(graph[item] & active)):
        augment(left, set())

    left_partner = {left: right for right, left in right_owner.items()}
    return left_partner, right_owner


def hall_witness(graph: Graph, active: set[int]) -> dict[str, Any] | None:
    """Return an exact PP3jz deficient set and forbidden rectangle."""
    left_partner, right_owner = maximum_matching(graph, active)
    if len(left_partner) == len(active):
        return None

    reachable_left = set(active) - set(left_partner)
    reachable_right: set[int] = set()
    queue: deque[int] = deque(sorted(reachable_left))

    while queue:
        left = queue.popleft()
        matched_right = left_partner.get(left)
        for right in graph[left] & active:
            if right == matched_right or right in reachable_right:
                continue
            reachable_right.add(right)
            owner = right_owner.get(right)
            if owner is not None and owner not in reachable_left:
                reachable_left.add(owner)
                queue.append(owner)

    neighbors = set().union(
        *(graph[left] & active for left in reachable_left)
    ) if reachable_left else set()
    forbidden_right = active - neighbors

    if len(neighbors) >= len(reachable_left):
        raise RuntimeError("alternating search did not produce a Hall-deficient set")

    rectangle_cells = [
        [left, right]
        for left in sorted(reachable_left)
        for right in sorted(forbidden_right)
    ]
    return {
        "matching_size": len(left_partner),
        "left_set": sorted(reachable_left),
        "neighbor_set": sorted(neighbors),
        "right_forbidden_set": sorted(forbidden_right),
        "left_size": len(reachable_left),
        "neighbor_size": len(neighbors),
        "right_forbidden_size": len(forbidden_right),
        "hall_deficiency": len(reachable_left) - len(neighbors),
        "size_sum": len(reachable_left) + len(forbidden_right),
        "rectangle_area": len(reachable_left) * len(forbidden_right),
        "rectangle_cells": rectangle_cells,
    }


def ore_diagnostics(graph: Graph, active: set[int]) -> dict[str, Any]:
    size = len(active)
    left_degree = {left: len(graph[left] & active) for left in active}
    right_degree = {
        right: sum(right in graph[left] for left in active) for right in active
    }
    violations: list[dict[str, int]] = []
    minimum_sum = 2 * size
    minimum_nonedge: list[int] | None = None

    for left in sorted(active):
        for right in sorted(active):
            if right in graph[left]:
                continue
            degree_sum = left_degree[left] + right_degree[right]
            if degree_sum < minimum_sum:
                minimum_sum = degree_sum
                minimum_nonedge = [left, right]
            if degree_sum < size:
                violations.append(
                    {
                        "left": left,
                        "right": right,
                        "left_degree": left_degree[left],
                        "right_degree": right_degree[right],
                        "degree_sum": degree_sum,
                    }
                )

    return {
        "active_size": size,
        "minimum_nonedge_degree_sum": (
            minimum_sum if minimum_nonedge is not None else None
        ),
        "minimum_nonedge": minimum_nonedge,
        "ore_condition": not violations,
        "ore_violation_count": len(violations),
        "ore_violations": violations,
    }


def analyze_host(graph: Graph, active: set[int]) -> dict[str, Any]:
    left_partner, _ = maximum_matching(graph, active)
    return {
        "active_indices": sorted(active),
        "active_size": len(active),
        "edge_count": sum(len(graph[left] & active) for left in active),
        "maximum_matching_size": len(left_partner),
        "perfect_matching": len(left_partner) == len(active),
        "hall_witness": hall_witness(graph, active),
        "ore": ore_diagnostics(graph, active),
    }


def analyze_layer(
    n: int,
    points: tuple[Point, ...],
    layer_number: int,
    layer_indices: tuple[int, ...],
) -> dict[str, Any]:
    layer_set = set(layer_indices)
    endpoints = tuple(points[index] for index in layer_indices)
    fixed = tuple(point for index, point in enumerate(points) if index not in layer_set)
    graph, _ = build_safe_graph(endpoints, fixed)
    full = set(range(n))
    pruned, theta, threshold = prune_indices(graph)
    return {
        "n": n,
        "layer": layer_number,
        "unary_forbidden_density": theta,
        "PP3is_threshold": threshold,
        "full": analyze_host(graph, full),
        "pruned": analyze_host(graph, pruned),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificates", type=Path)
    parser.add_argument("--n", type=int, action="append", dest="side_lengths")
    parser.add_argument("--layer", type=int, choices=(0, 1), action="append")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    requested_sides = set(args.side_lengths or [])
    requested_layers = set(args.layer or (0, 1))
    rows: list[dict[str, Any]] = []
    try:
        for n, points in load_certificates(args.certificates):
            if requested_sides and n not in requested_sides:
                continue
            layers = matching_layers(points)
            for layer_number in sorted(requested_layers):
                rows.append(analyze_layer(n, points, layer_number, layers[layer_number]))
    except (OSError, ValueError, json.JSONDecodeError, RuntimeError) as exc:
        raise SystemExit(f"analysis failed: {exc}") from exc

    text = json.dumps({"results": rows}, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

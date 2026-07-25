#!/usr/bin/env python3
"""Verify PP3um--PP3ur by exact perfect-matching enumeration."""

from __future__ import annotations

import argparse
import json
from itertools import permutations
from pathlib import Path
from typing import Any

Edge = tuple[int, int]
Matching = tuple[int, ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--enumeration-limit", type=int, default=10)
    return parser.parse_args()


def parse_edge(raw: Any, label: str, n: int) -> Edge:
    if (
        not isinstance(raw, list)
        or len(raw) != 2
        or any(isinstance(value, bool) or not isinstance(value, int) for value in raw)
    ):
        raise ValueError(f"{label}: expected [left,right] integers")
    left, right = raw
    if not (0 <= left < n and 0 <= right < n):
        raise ValueError(f"{label}: edge outside [0,n)^2")
    return left, right


def enumerate_matchings(n: int, edges: set[Edge], limit: int) -> list[Matching]:
    if n > limit:
        raise ValueError(f"n={n} exceeds enumeration limit {limit}")
    return [
        permutation
        for permutation in permutations(range(n))
        if all((left, permutation[left]) in edges for left in range(n))
    ]


def permutation_cycles(matching: Matching) -> list[list[int]]:
    n = len(matching)
    seen = [False] * n
    cycles: list[list[int]] = []
    for start in range(n):
        if seen[start]:
            continue
        current = start
        cycle: list[int] = []
        while not seen[current]:
            seen[current] = True
            cycle.append(current)
            current = matching[current]
        if len(cycle) > 1:
            cycles.append(cycle)
    return cycles


def has_nontrivial_directed_cycle(adjacency: list[list[int]], deleted: set[int]) -> bool:
    n = len(adjacency)
    colour = [0] * n

    def visit(vertex: int) -> bool:
        colour[vertex] = 1
        for target in adjacency[vertex]:
            if target == vertex or target in deleted:
                continue
            if colour[target] == 1:
                return True
            if colour[target] == 0 and visit(target):
                return True
        colour[vertex] = 2
        return False

    for vertex in range(n):
        if vertex in deleted or colour[vertex] != 0:
            continue
        if visit(vertex):
            return True
    return False


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        n = payload.get("n")
        if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
            raise ValueError("n must be a positive integer")
        raw_edges = payload.get("edges")
        if not isinstance(raw_edges, list):
            raise ValueError("edges must be a list")
        edges = {
            parse_edge(raw, f"edges[{index}]", n)
            for index, raw in enumerate(raw_edges)
        }
        if len(edges) != len(raw_edges):
            raise ValueError("edges contains duplicates")
        if any((index, index) not in edges for index in range(n)):
            raise ValueError("the identity reference matching must be present")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    matchings = enumerate_matchings(n, edges, args.enumeration_limit)
    if not matchings:
        raise SystemExit("check failed: host has no perfect matching")

    moved_sets = [
        {index for index, image in enumerate(matching) if image != index}
        for matching in matchings
    ]
    maximum_mobility = max(len(moved) for moved in moved_sets)
    maximizer_index = min(
        index
        for index, moved in enumerate(moved_sets)
        if len(moved) == maximum_mobility
    )
    maximizer = matchings[maximizer_index]
    hub = moved_sets[maximizer_index]
    maximizer_cycles = permutation_cycles(maximizer)

    adjacency = [
        sorted(target for source, target in edges if source == vertex)
        for vertex in range(n)
    ]
    hub_is_feedback_set = not has_nontrivial_directed_cycle(adjacency, hub)

    all_matching_cycles_hit_hub = True
    maximum_cycle_count = 0
    matching_records: list[dict[str, Any]] = []
    for matching, moved in zip(matchings, moved_sets):
        cycles = permutation_cycles(matching)
        maximum_cycle_count = max(maximum_cycle_count, len(cycles))
        if any(hub.isdisjoint(cycle) for cycle in cycles):
            all_matching_cycles_hit_hub = False
        matching_records.append(
            {
                "matching": list(matching),
                "moved_vertices": sorted(moved),
                "cycles": cycles,
            }
        )

    result = {
        "n": n,
        "perfect_matching_count": len(matchings),
        "maximum_mobility": maximum_mobility,
        "maximum_mobility_matching": list(maximizer),
        "maximum_mobility_cycles": maximizer_cycles,
        "mobility_hub": sorted(hub),
        "hub_is_feedback_set": hub_is_feedback_set,
        "all_matching_cycles_hit_hub": all_matching_cycles_hit_hub,
        "maximum_nontrivial_cycle_count_in_a_matching": maximum_cycle_count,
        "cycle_count_at_most_hub_size": maximum_cycle_count <= len(hub),
        "matchings": matching_records,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

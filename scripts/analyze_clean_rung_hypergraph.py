#!/usr/bin/env python3
"""Analyze the clean four-edge rung hypergraph of matching layers."""
from __future__ import annotations

import argparse
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path
from typing import Any

from analyze_matching_first_reservoirs import alternating_decomposition, load_cases
from analyze_matching_first_width_two import canonical_state, certificate_counts

Point = tuple[int, int]


def clean_edge_masks(layer: tuple[Point, ...], n: int) -> tuple[int, ...]:
    masks = []
    for selected in combinations(range(len(layer)), 4):
        selected_set = set(selected)
        deleted = tuple(layer[index] for index in selected)
        retained = tuple(
            point for index, point in enumerate(layer) if index not in selected_set
        )
        inserted = canonical_state(deleted, n)
        blocked, anchored, internal = certificate_counts(retained, inserted)
        if blocked + anchored + internal == 0:
            masks.append(sum(1 << index for index in selected))
    return tuple(masks)


def maximum_matching(
    masks: tuple[int, ...], vertex_count: int
) -> tuple[int, tuple[int, ...]]:
    incident: list[list[int]] = [[] for _ in range(vertex_count)]
    for edge_index, mask in enumerate(masks):
        for vertex in range(vertex_count):
            if mask & (1 << vertex):
                incident[vertex].append(edge_index)

    @lru_cache(maxsize=None)
    def solve(available: int) -> tuple[int, tuple[int, ...]]:
        if not available:
            return 0, ()
        vertex = (available & -available).bit_length() - 1
        best = solve(available & ~(1 << vertex))
        for edge_index in incident[vertex]:
            mask = masks[edge_index]
            if mask & available != mask:
                continue
            count, chosen = solve(available & ~mask)
            candidate = count + 1, chosen + (edge_index,)
            if candidate[0] > best[0]:
                best = candidate
        return best

    return solve((1 << vertex_count) - 1)


def minimum_transversal(masks: tuple[int, ...], vertex_count: int) -> tuple[int, ...]:
    if not masks:
        return ()
    for size in range(1, vertex_count + 1):
        for vertices in combinations(range(vertex_count), size):
            hit_mask = sum(1 << vertex for vertex in vertices)
            if all(mask & hit_mask for mask in masks):
                return vertices
    raise AssertionError("the full vertex set should hit every nonempty edge")


def analyze_layer(n: int, layer_index: int, layer: tuple[Point, ...]) -> dict[str, Any]:
    masks = clean_edge_masks(layer, n)
    degrees = [
        sum(bool(mask & (1 << vertex)) for mask in masks)
        for vertex in range(n)
    ]
    matching_size, matching_indices = maximum_matching(masks, n)
    transversal = minimum_transversal(masks, n)
    maximum_degree = max(degrees, default=0)
    return {
        "layer": layer_index,
        "edge_count": n,
        "clean_state_count": len(masks),
        "maximum_vertex_degree": maximum_degree,
        "minimum_vertex_degree": min(degrees, default=0),
        "degree_sequence": degrees,
        "greedy_lower_bound": (
            0
            if not masks
            else (len(masks) + 4 * maximum_degree - 1) // (4 * maximum_degree)
        ),
        "maximum_matching_size": matching_size,
        "maximum_matching_states": [
            [vertex for vertex in range(n) if masks[index] & (1 << vertex)]
            for index in matching_indices
        ],
        "minimum_transversal_size": len(transversal),
        "minimum_transversal_vertices": list(transversal),
        "common_vertices": [
            vertex
            for vertex in range(n)
            if masks and all(mask & (1 << vertex) for mask in masks)
        ],
        "layer_points": [list(point) for point in layer],
    }


def analyze_case(n: int, core: tuple[Point, ...]) -> dict[str, Any]:
    if n < 4:
        return {"source_n": n, "layers": [], "status": "fewer-than-four-edges"}
    layer_zero, layer_one, cycle_lengths = alternating_decomposition(n, core)
    return {
        "source_n": n,
        "cycle_edge_lengths": list(cycle_lengths),
        "layers": [
            analyze_layer(n, index, layer)
            for index, layer in enumerate((layer_zero, layer_one))
        ],
        "status": "searched",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        cases = load_cases(args.certificate, args.n)
        result = {"cases": [analyze_case(n, core) for n, core in cases]}
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

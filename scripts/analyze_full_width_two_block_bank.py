#!/usr/bin/env python3
"""Analyze all 36 width-two geometries for matching-block states."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable

from analyze_matching_first_reservoirs import alternating_decomposition, load_cases

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def no_three(points: Iterable[Point]) -> bool:
    ordered = tuple(points)
    return all(determinant(*triple) != 0 for triple in combinations(ordered, 3))


def ordered_pair_partitions(
    values: tuple[int, ...]
) -> tuple[tuple[tuple[int, int], tuple[int, int]], ...]:
    if len(values) != 4:
        raise ValueError("ordered pair partitions require four values")
    out = []
    for first_indices in combinations(range(4), 2):
        first_index_set = set(first_indices)
        first = tuple(values[index] for index in first_indices)
        second = tuple(
            values[index]
            for index in range(4)
            if index not in first_index_set
        )
        out.append((tuple(sorted(first)), tuple(sorted(second))))
    return tuple(out)


def patch_states(deleted: tuple[Point, ...], n: int) -> Iterable[tuple[Point, ...]]:
    columns = tuple(sorted(x for x, _ in deleted))
    rows = tuple(sorted(y for _, y in deleted))
    a, b = n + 1, n + 2
    new_values = (a, b)
    for column_partition in ordered_pair_partitions(columns):
        movement = tuple(
            (column, new_values[index])
            for index, pair in enumerate(column_partition)
            for column in pair
        )
        for row_partition in ordered_pair_partitions(rows):
            refill = tuple(
                (new_values[index], row)
                for index, pair in enumerate(row_partition)
                for row in pair
            )
            yield tuple(sorted(movement + refill))


def maximum_matching(masks: tuple[int, ...], vertex_count: int) -> int:
    incident: list[list[int]] = [[] for _ in range(vertex_count)]
    for edge_index, mask in enumerate(masks):
        for vertex in range(vertex_count):
            if mask & (1 << vertex):
                incident[vertex].append(edge_index)

    @lru_cache(maxsize=None)
    def solve(available: int) -> int:
        if not available:
            return 0
        vertex = (available & -available).bit_length() - 1
        best = solve(available & ~(1 << vertex))
        for edge_index in incident[vertex]:
            mask = masks[edge_index]
            if mask & available == mask:
                best = max(best, 1 + solve(available & ~mask))
        return best

    return solve((1 << vertex_count) - 1)


def minimum_transversal_size(masks: tuple[int, ...], vertex_count: int) -> int:
    if not masks:
        return 0
    for size in range(1, vertex_count + 1):
        for vertices in combinations(range(vertex_count), size):
            hit_mask = sum(1 << vertex for vertex in vertices)
            if all(mask & hit_mask for mask in masks):
                return size
    raise AssertionError("full vertex set should hit every clean deletion")


def analyze_layer(n: int, layer_index: int, layer: tuple[Point, ...]) -> dict[str, Any]:
    clean_geometry_count = 0
    clean_geometry_histogram: Counter[int] = Counter()
    clean_deletion_masks: list[int] = []
    maximum_geometry_multiplicity = 0
    deletion_count = 0

    for selected in combinations(range(n), 4):
        deletion_count += 1
        selected_set = set(selected)
        deleted = tuple(layer[index] for index in selected)
        retained = tuple(
            point for index, point in enumerate(layer) if index not in selected_set
        )
        clean_for_deletion = 0
        for patch in patch_states(deleted, n):
            if no_three(retained + patch):
                clean_for_deletion += 1
        clean_geometry_count += clean_for_deletion
        clean_geometry_histogram[clean_for_deletion] += 1
        maximum_geometry_multiplicity = max(
            maximum_geometry_multiplicity, clean_for_deletion
        )
        if clean_for_deletion:
            clean_deletion_masks.append(sum(1 << index for index in selected))

    masks = tuple(clean_deletion_masks)
    total_states = 36 * deletion_count
    return {
        "layer": layer_index,
        "edge_count": n,
        "total_state_count": total_states,
        "clean_state_count": clean_geometry_count,
        "clean_state_fraction": f"{clean_geometry_count}/{total_states}",
        "clean_deletion_count": len(masks),
        "clean_geometry_multiplicity_histogram": {
            str(multiplicity): count
            for multiplicity, count in sorted(clean_geometry_histogram.items())
        },
        "maximum_clean_geometries_for_one_deletion": maximum_geometry_multiplicity,
        "maximum_clean_deletion_matching_size": maximum_matching(masks, n),
        "minimum_clean_deletion_transversal_size": minimum_transversal_size(masks, n),
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

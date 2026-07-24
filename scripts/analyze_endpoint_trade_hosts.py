#!/usr/bin/env python3
"""Analyze PP3in--PP3jb endpoint-trade hosts on stored certificates.

For each deterministic perfect-matching layer, remove the complete layer and use
its columns and rows as tied endpoint indices. The opposite layer is the fixed
source. The script constructs the unary source-safe endpoint graph, applies the
PP3is high-degree pruning, counts anchored-pair and inserted-triple patterns by
endpoint-index support rank, computes the exact PP3ix canonical-event resource
mass, and searches exactly for a source-admissible perfect matching.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any

from analyze_random_matching_block_preparation import (
    determinant,
    load_certificates,
    matching_layers,
)

Point = tuple[int, int]
Edge = tuple[int, int]


def falling(value: int, rank: int) -> int:
    result = 1
    for offset in range(rank):
        result *= value - offset
    return result


def fraction_object(value: Fraction) -> dict[str, Any]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": str(value),
        "decimal": float(value),
    }


def blocker_free(cell: Point, fixed: tuple[Point, ...]) -> bool:
    return all(
        determinant(first, second, cell) != 0
        for first, second in itertools.combinations(fixed, 2)
    )


def build_safe_graph(
    endpoints: tuple[Point, ...], fixed: tuple[Point, ...]
) -> tuple[tuple[frozenset[int], ...], tuple[tuple[Point, ...], ...]]:
    occupied = set(fixed)
    rows: list[frozenset[int]] = []
    cells: list[tuple[Point, ...]] = []
    for left, (x, _) in enumerate(endpoints):
        allowed: set[int] = set()
        row_cells: list[Point] = []
        for right, (_, y) in enumerate(endpoints):
            cell = (x, y)
            row_cells.append(cell)
            if left == right:
                continue
            if cell in occupied:
                continue
            if not blocker_free(cell, fixed):
                continue
            allowed.add(right)
        rows.append(frozenset(allowed))
        cells.append(tuple(row_cells))
    return tuple(rows), tuple(cells)


def maximum_matching_size(graph: tuple[frozenset[int], ...], active: set[int]) -> int:
    right_owner: dict[int, int] = {}

    def augment(left: int, seen: set[int]) -> bool:
        for right in graph[left]:
            if right not in active or right in seen:
                continue
            seen.add(right)
            owner = right_owner.get(right)
            if owner is None or augment(owner, seen):
                right_owner[right] = left
                return True
        return False

    matched = 0
    for left in sorted(active, key=lambda item: len(graph[item] & active)):
        if augment(left, set()):
            matched += 1
    return matched


def prune_indices(graph: tuple[frozenset[int], ...]) -> tuple[set[int], float, float]:
    q = len(graph)
    safe_edges = sum(len(row) for row in graph)
    forbidden_edges = q * q - safe_edges
    theta = forbidden_edges / (q * q)
    threshold = math.sqrt(theta) * q
    forbidden_left = [q - len(graph[left]) for left in range(q)]
    forbidden_right = [
        q - sum(right in graph[left] for left in range(q)) for right in range(q)
    ]
    removed = {
        index
        for index in range(q)
        if forbidden_left[index] > threshold or forbidden_right[index] > threshold
    }
    return set(range(q)) - removed, theta, threshold


def compatible(first: Edge, second: Edge) -> bool:
    return first[0] != second[0] and first[1] != second[1]


def support_rank(*edges: Edge) -> int:
    return len({index for edge in edges for index in edge})


def safe_edges(
    graph: tuple[frozenset[int], ...], active: set[int]
) -> list[Edge]:
    return [
        (left, right)
        for left in active
        for right in graph[left]
        if right in active
    ]


def anchored_pair(
    first: Edge,
    second: Edge,
    cells: tuple[tuple[Point, ...], ...],
    fixed: tuple[Point, ...],
) -> bool:
    first_cell = cells[first[0]][first[1]]
    second_cell = cells[second[0]][second[1]]
    return any(determinant(first_cell, second_cell, anchor) == 0 for anchor in fixed)


def inserted_triple(
    first: Edge,
    second: Edge,
    third: Edge,
    cells: tuple[tuple[Point, ...], ...],
) -> bool:
    return (
        determinant(
            cells[first[0]][first[1]],
            cells[second[0]][second[1]],
            cells[third[0]][third[1]],
        )
        == 0
    )


def count_patterns(
    graph: tuple[frozenset[int], ...],
    cells: tuple[tuple[Point, ...], ...],
    fixed: tuple[Point, ...],
    active: set[int],
) -> tuple[Counter[int], Counter[int]]:
    edges = safe_edges(graph, active)
    pair_counts: Counter[int] = Counter()
    triple_counts: Counter[int] = Counter()

    for first, second in itertools.combinations(edges, 2):
        if compatible(first, second) and anchored_pair(first, second, cells, fixed):
            pair_counts[support_rank(first, second)] += 1

    for first, second, third in itertools.combinations(edges, 3):
        if not (
            compatible(first, second)
            and compatible(first, third)
            and compatible(second, third)
        ):
            continue
        if inserted_triple(first, second, third, cells):
            triple_counts[support_rank(first, second, third)] += 1

    return pair_counts, triple_counts


def low_support_metrics(
    graph: tuple[frozenset[int], ...],
    cells: tuple[tuple[Point, ...], ...],
    fixed: tuple[Point, ...],
    active: set[int],
) -> dict[str, Any]:
    q = len(active)
    left_mass = {index: Fraction(0) for index in active}
    right_mass = {index: Fraction(0) for index in active}
    low_counts: Counter[str] = Counter()

    def add_event(edges: tuple[Edge, ...], probability: Fraction, label: str) -> None:
        low_counts[label] += 1
        for left in {edge[0] for edge in edges}:
            left_mass[left] += probability
        for right in {edge[1] for edge in edges}:
            right_mass[right] += probability

    unary_probability = Fraction(1, q)
    for left in active:
        for right in active:
            if right not in graph[left]:
                add_event(((left, right),), unary_probability, "unary")

    edges = safe_edges(graph, active)
    pair_probability = Fraction(1, falling(q, 2)) if q >= 2 else Fraction(0)
    for first, second in itertools.combinations(edges, 2):
        if not compatible(first, second):
            continue
        rank = support_rank(first, second)
        if rank <= 3 and anchored_pair(first, second, cells, fixed):
            add_event((first, second), pair_probability, f"anchored_pair_rank_{rank}")

    triple_probability = Fraction(1, falling(q, 3)) if q >= 3 else Fraction(0)
    for first, second, third in itertools.combinations(edges, 3):
        if not (
            compatible(first, second)
            and compatible(first, third)
            and compatible(second, third)
        ):
            continue
        if support_rank(first, second, third) == 3 and inserted_triple(
            first, second, third, cells
        ):
            add_event(
                (first, second, third),
                triple_probability,
                "inserted_triple_rank_3",
            )

    maximum_mass = max(
        list(left_mass.values()) + list(right_mass.values()),
        default=Fraction(0),
    )
    pair_counts, triple_counts = count_patterns(graph, cells, fixed, active)
    high_source_bound = Fraction(9 * pair_counts[4], q * q)
    high_source_bound += Fraction(
        27 * sum(count for rank, count in triple_counts.items() if rank >= 4),
        q * q * q,
    )
    return {
        "low_event_counts": dict(sorted(low_counts.items())),
        "maximum_low_event_resource_mass": fraction_object(maximum_mass),
        "PP3ix_mass_condition": maximum_mass <= Fraction(1, 24),
        "PP3ja_high_support_source_bound": fraction_object(high_source_bound),
    }


def source_admissible_matching(
    graph: tuple[frozenset[int], ...],
    cells: tuple[tuple[Point, ...], ...],
    fixed: tuple[Point, ...],
    active: set[int],
) -> tuple[Edge, ...] | None:
    order = sorted(active, key=lambda left: len(graph[left] & active))
    fixed_set = set(fixed)

    def valid_extension(chosen_cells: list[Point], cell: Point) -> bool:
        if cell in fixed_set or cell in chosen_cells:
            return False
        for previous in chosen_cells:
            if any(determinant(previous, cell, anchor) == 0 for anchor in fixed):
                return False
        for first, second in itertools.combinations(chosen_cells, 2):
            if determinant(first, second, cell) == 0:
                return False
        return True

    def search(
        position: int,
        used_right: set[int],
        chosen_edges: list[Edge],
        chosen_cells: list[Point],
    ) -> tuple[Edge, ...] | None:
        if position == len(order):
            return tuple(chosen_edges)
        left = order[position]
        for right in sorted(graph[left] & active):
            if right in used_right:
                continue
            cell = cells[left][right]
            if not valid_extension(chosen_cells, cell):
                continue
            used_right.add(right)
            chosen_edges.append((left, right))
            chosen_cells.append(cell)
            result = search(position + 1, used_right, chosen_edges, chosen_cells)
            if result is not None:
                return result
            chosen_cells.pop()
            chosen_edges.pop()
            used_right.remove(right)
        return None

    return search(0, set(), [], [])


def histogram_object(counter: Counter[int]) -> dict[str, int]:
    return {str(rank): counter[rank] for rank in sorted(counter)}


def analyze_layer(
    n: int,
    points: tuple[Point, ...],
    layer_number: int,
    layer_indices: tuple[int, ...],
) -> dict[str, Any]:
    layer_set = set(layer_indices)
    endpoints = tuple(points[index] for index in layer_indices)
    fixed = tuple(point for index, point in enumerate(points) if index not in layer_set)
    graph, cells = build_safe_graph(endpoints, fixed)
    full = set(range(n))
    pruned, theta, threshold = prune_indices(graph)

    full_pairs, full_triples = count_patterns(graph, cells, fixed, full)
    pruned_pairs, pruned_triples = count_patterns(graph, cells, fixed, pruned)
    full_solution = source_admissible_matching(graph, cells, fixed, full)
    pruned_solution = source_admissible_matching(graph, cells, fixed, pruned)

    forbidden_left = [n - len(graph[left]) for left in range(n)]
    forbidden_right = [
        n - sum(right in graph[left] for left in range(n)) for right in range(n)
    ]

    return {
        "n": n,
        "layer": layer_number,
        "endpoint_count": n,
        "safe_host_edges": sum(len(row) for row in graph),
        "unary_forbidden_edges": n * n - sum(len(row) for row in graph),
        "unary_forbidden_density": theta,
        "maximum_forbidden_left_degree": max(forbidden_left, default=0),
        "maximum_forbidden_right_degree": max(forbidden_right, default=0),
        "PP3is_threshold": threshold,
        "PP3is_retained_indices": len(pruned),
        "full_maximum_matching": maximum_matching_size(graph, full),
        "pruned_maximum_matching": maximum_matching_size(graph, pruned),
        "full_anchored_pair_support_ranks": histogram_object(full_pairs),
        "full_inserted_triple_support_ranks": histogram_object(full_triples),
        "pruned_anchored_pair_support_ranks": histogram_object(pruned_pairs),
        "pruned_inserted_triple_support_ranks": histogram_object(pruned_triples),
        "full_low_support_metrics": low_support_metrics(graph, cells, fixed, full),
        "pruned_low_support_metrics": low_support_metrics(graph, cells, fixed, pruned),
        "full_source_admissible_matching_exists": full_solution is not None,
        "pruned_source_admissible_matching_exists": pruned_solution is not None,
        "full_source_admissible_matching": full_solution,
        "pruned_source_admissible_matching": pruned_solution,
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
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"analysis failed: {exc}") from exc

    text = json.dumps({"results": rows}, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

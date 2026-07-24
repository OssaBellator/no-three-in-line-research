#!/usr/bin/env python3
"""Analyze PP3hm--PP3hq controller-aware domains on stored certificates.

For each perfect-matching layer, use that layer as the controller pool and test
candidate movement/refill cells against the full saturated source.  A value is
controller-safe exactly when every source blocker pair through its candidate
cell contains the controller point.  The analyzer also removes same-slot source
anchors, builds the exact label compatibility graph, computes maximum matching,
and reports blocker-star/resource statistics.

This is a finite diagnostic.  It does not certify the asymptotic density theorem.
"""
from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path
from typing import Any

from analyze_random_matching_block_preparation import (
    determinant,
    load_certificates,
    matching_layers,
)

Point = tuple[int, int]
Witness = tuple[int, int]


def parse_fraction(text: str) -> tuple[int, int]:
    try:
        numerator_text, denominator_text = (
            text.split("/", 1) if "/" in text else (text, "1")
        )
        numerator = int(numerator_text)
        denominator = int(denominator_text)
    except (TypeError, ValueError) as exc:
        raise argparse.ArgumentTypeError(f"invalid fraction: {text}") from exc
    if denominator <= 0 or numerator <= 0 or numerator > denominator:
        raise argparse.ArgumentTypeError("fraction must lie in (0,1]")
    return numerator, denominator


def blocker_pairs(points: tuple[Point, ...], candidate: Point) -> tuple[Witness, ...]:
    pairs = tuple(
        (first, second)
        for first, second in itertools.combinations(range(len(points)), 2)
        if determinant(points[first], points[second], candidate) == 0
    )
    endpoints = [endpoint for pair in pairs for endpoint in pair]
    if len(set(endpoints)) != len(endpoints):
        raise AssertionError("external-point blocker pairs are not endpoint-disjoint")
    return pairs


def controller_safe(
    points: tuple[Point, ...], controller: int, candidate: Point
) -> tuple[bool, tuple[Witness, ...]]:
    pairs = blocker_pairs(points, candidate)
    additional = tuple(pair for pair in pairs if controller not in pair)
    return not additional, additional


def same_slot_anchor_bad(
    points: tuple[Point, ...], controller: int, movement: Point, refill: Point
) -> bool:
    return any(
        anchor != controller
        and determinant(movement, refill, points[anchor]) == 0
        for anchor in range(len(points))
    )


def maximum_bipartite_matching(adjacency: list[list[int]], right_size: int) -> int:
    match_right = [-1] * right_size

    def augment(left: int, seen: set[int]) -> bool:
        for right in adjacency[left]:
            if right in seen:
                continue
            seen.add(right)
            owner = match_right[right]
            if owner == -1 or augment(owner, seen):
                match_right[right] = left
                return True
        return False

    matched = 0
    for left in range(len(adjacency)):
        if augment(left, set()):
            matched += 1
    return matched


def exact_graph_matching_number(vertex_count: int, edges: set[Witness]) -> int:
    """Exact maximum matching for the small stored source graphs by bitmask DP."""

    neighbours = [0] * vertex_count
    for first, second in edges:
        neighbours[first] |= 1 << second
        neighbours[second] |= 1 << first

    memo: dict[int, int] = {0: 0}

    def solve(mask: int) -> int:
        cached = memo.get(mask)
        if cached is not None:
            return cached
        first_bit = mask & -mask
        first = first_bit.bit_length() - 1
        remaining = mask ^ first_bit
        best = solve(remaining)
        options = neighbours[first] & remaining
        while options:
            second_bit = options & -options
            best = max(best, 1 + solve(remaining ^ second_bit))
            options ^= second_bit
        memo[mask] = best
        return best

    return solve((1 << vertex_count) - 1)


def analyze_layer(
    n: int,
    points: tuple[Point, ...],
    layer_number: int,
    layer_tuple: tuple[int, ...],
    label_count: int,
    gamma: tuple[int, int],
) -> dict[str, Any]:
    labels = tuple(range(n + 1, n + label_count + 1))
    numerator, denominator = gamma
    pool_size = len(layer_tuple)

    movement_safe: dict[tuple[int, int], bool] = {}
    refill_safe: dict[tuple[int, int], bool] = {}
    movement_witnesses: dict[tuple[int, int], tuple[Witness, ...]] = {}
    refill_witnesses: dict[tuple[int, int], tuple[Witness, ...]] = {}

    witness_entries: Counter[Witness] = Counter()
    endpoint_entry_degree: Counter[int] = Counter()
    controller_safe_movement_entries = 0
    controller_safe_refill_entries = 0

    for label in labels:
        for controller in layer_tuple:
            x, y = points[controller]
            safe_m, witnesses_m = controller_safe(points, controller, (x, label))
            safe_f, witnesses_f = controller_safe(points, controller, (label, y))
            movement_safe[label, controller] = safe_m
            refill_safe[label, controller] = safe_f
            movement_witnesses[label, controller] = witnesses_m
            refill_witnesses[label, controller] = witnesses_f
            controller_safe_movement_entries += int(safe_m)
            controller_safe_refill_entries += int(safe_f)
            for witness in witnesses_m + witnesses_f:
                normalized = tuple(sorted(witness))
                witness_entries[normalized] += 1
                endpoint_entry_degree[normalized[0]] += 1
                endpoint_entry_degree[normalized[1]] += 1

    domain_sizes: dict[tuple[int, int], int] = {}
    same_slot_bad_counts: dict[tuple[int, int], int] = {}
    adjacency: list[list[int]] = [[] for _ in labels]
    for left_index, movement_label in enumerate(labels):
        for right_index, refill_label in enumerate(labels):
            domain_size = 0
            anchor_bad = 0
            for controller in layer_tuple:
                if not movement_safe[movement_label, controller]:
                    continue
                if not refill_safe[refill_label, controller]:
                    continue
                x, y = points[controller]
                if same_slot_anchor_bad(
                    points,
                    controller,
                    (x, movement_label),
                    (refill_label, y),
                ):
                    anchor_bad += 1
                    continue
                domain_size += 1
            domain_sizes[movement_label, refill_label] = domain_size
            same_slot_bad_counts[movement_label, refill_label] = anchor_bad
            if domain_size * denominator >= numerator * pool_size:
                adjacency[left_index].append(right_index)

    left_degrees = [len(row) for row in adjacency]
    right_degrees = [
        sum(right in row for row in adjacency) for right in range(label_count)
    ]
    matching_size = maximum_bipartite_matching(adjacency, label_count)

    distinct_witnesses = set(witness_entries)
    blocker_matching_number = exact_graph_matching_number(len(points), distinct_witnesses)
    maximum_witness_multiplicity = max(witness_entries.values(), default=0)
    maximum_endpoint_entry_degree = max(endpoint_entry_degree.values(), default=0)

    domain_histogram = Counter(domain_sizes.values())
    anchor_bad_histogram = Counter(same_slot_bad_counts.values())
    total_entries = 2 * label_count * pool_size
    bad_cell_entries = (
        total_entries
        - controller_safe_movement_entries
        - controller_safe_refill_entries
    )

    return {
        "source_n": n,
        "layer": layer_number,
        "pool_size": pool_size,
        "label_count": label_count,
        "gamma": f"{numerator}/{denominator}",
        "movement_entry_count": label_count * pool_size,
        "refill_entry_count": label_count * pool_size,
        "controller_safe_movement_entries": controller_safe_movement_entries,
        "controller_safe_refill_entries": controller_safe_refill_entries,
        "bad_cell_entries": bad_cell_entries,
        "bad_cell_fraction": {
            "numerator": bad_cell_entries,
            "denominator": total_entries,
        },
        "distinct_noncontroller_blocker_pairs": len(distinct_witnesses),
        "maximum_blocker_pair_entry_multiplicity": maximum_witness_multiplicity,
        "maximum_blocker_endpoint_entry_degree": maximum_endpoint_entry_degree,
        "exact_blocker_graph_matching_number": blocker_matching_number,
        "controller_aware_domain_size_histogram": {
            str(size): count for size, count in sorted(domain_histogram.items())
        },
        "same_slot_anchor_bad_count_histogram": {
            str(size): count for size, count in sorted(anchor_bad_histogram.items())
        },
        "compatibility_graph_edges": sum(left_degrees),
        "minimum_left_degree": min(left_degrees, default=0),
        "minimum_right_degree": min(right_degrees, default=0),
        "maximum_label_matching": matching_size,
        "has_full_label_matching": matching_size == label_count,
        "minimum_positive_domain_size": min(
            (size for size in domain_sizes.values() if size > 0), default=0
        ),
        "maximum_domain_size": max(domain_sizes.values(), default=0),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificates", type=Path)
    parser.add_argument("--n", type=int, action="append", dest="side_lengths")
    parser.add_argument("--layer", type=int, choices=(0, 1), action="append")
    parser.add_argument("--labels", type=int, default=4)
    parser.add_argument("--gamma", type=parse_fraction, default=(1, 2))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.labels < 1:
        raise SystemExit("--labels must be positive")

    requested_sides = set(args.side_lengths or [])
    requested_layers = set(args.layer or (0, 1))
    rows: list[dict[str, Any]] = []
    try:
        for n, points in load_certificates(args.certificates):
            if requested_sides and n not in requested_sides:
                continue
            layers = matching_layers(points)
            for layer_number in sorted(requested_layers):
                rows.append(
                    analyze_layer(
                        n,
                        points,
                        layer_number,
                        layers[layer_number],
                        args.labels,
                        args.gamma,
                    )
                )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"analysis failed: {exc}") from exc

    text = json.dumps({"results": rows}, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Analyze PP3ff refined movement/refill label domains on stored certificates.

For each perfect-matching layer, use that layer as the source-edge pool and the
opposite layer as the fixed retained source.  Candidate movement rows and refill
columns are consecutive new labels.  The analyzer computes fixed-pair safe edge
sets, same-edge anchor-bad sets, the refined compatibility graph
J_{gamma,epsilon}, its maximum matching, and the widths certified by PP3ff and
PP3fg.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

from analyze_matching_first_reservoirs import alternating_decomposition, load_cases

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def parse_fraction(text: str) -> Fraction:
    try:
        value = Fraction(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError(f"invalid fraction: {text}") from exc
    if value <= 0 or value > 1:
        raise argparse.ArgumentTypeError("fraction must lie in (0,1]")
    return value


def divisor_count(value: int) -> int:
    value = abs(value)
    if value == 0:
        return 0
    result = 1
    factor = 2
    while factor * factor <= value:
        exponent = 0
        while value % factor == 0:
            value //= factor
            exponent += 1
        if exponent:
            result *= exponent + 1
        factor += 1 if factor == 2 else 2
    if value > 1:
        result *= 2
    return result


def is_blocked(cell: Point, fixed: tuple[Point, ...]) -> bool:
    return any(
        determinant(first, second, cell) == 0
        for first, second in itertools.combinations(fixed, 2)
    )


def maximum_bipartite_matching(adjacency: list[list[int]], right_size: int) -> int:
    match_right = [-1] * right_size

    def augment(left: int, seen: set[int]) -> bool:
        for right in adjacency[left]:
            if right in seen:
                continue
            seen.add(right)
            if match_right[right] == -1 or augment(match_right[right], seen):
                match_right[right] = left
                return True
        return False

    matched = 0
    for left in range(len(adjacency)):
        if augment(left, set()):
            matched += 1
    return matched


def certified_width(
    maximum_matching: int,
    pool_size: int,
    density: Fraction,
    spread_version: bool,
) -> int:
    best = 0
    for width in range(1, maximum_matching + 1):
        if spread_version:
            left = 24 * (2 * (2 * width) ** 2 + 1)
        else:
            left = 48 * (2 * width) ** 2
        if Fraction(left, 1) <= density * density * pool_size:
            best = width
    return best


def analyze_layer(
    n: int,
    layer_index: int,
    pool: tuple[Point, ...],
    fixed: tuple[Point, ...],
    label_count: int,
    gamma: Fraction,
    epsilon: Fraction,
) -> dict[str, Any]:
    labels = tuple(range(n + 1, n + label_count + 1))
    pool_size = len(pool)

    movement_safe: dict[int, set[int]] = {}
    refill_safe: dict[int, set[int]] = {}
    for label in labels:
        movement_safe[label] = {
            edge_index
            for edge_index, (x, _) in enumerate(pool)
            if not is_blocked((x, label), fixed)
        }
        refill_safe[label] = {
            edge_index
            for edge_index, (_, y) in enumerate(pool)
            if not is_blocked((label, y), fixed)
        }

    bad_sets: dict[tuple[int, int], set[int]] = {}
    divisor_energy = 0
    for edge in pool:
        x, y = edge
        for u, v in fixed:
            product = (x - u) * (y - v)
            if product > 0:
                divisor_energy += divisor_count(product)

    adjacency: list[list[int]] = [[] for _ in labels]
    refined_domain_sizes: list[int] = []
    bad_pair_count = 0
    bad_incidence_sum = 0
    for left_index, movement_label in enumerate(labels):
        for right_index, refill_label in enumerate(labels):
            bad_edges = {
                edge_index
                for edge_index, (x, y) in enumerate(pool)
                if any(
                    determinant(
                        (x, movement_label),
                        (refill_label, y),
                        anchor,
                    )
                    == 0
                    for anchor in fixed
                )
            }
            bad_sets[movement_label, refill_label] = bad_edges
            bad_incidence_sum += len(bad_edges)
            if len(bad_edges) > epsilon * pool_size:
                bad_pair_count += 1

            safe_intersection = (
                movement_safe[movement_label] & refill_safe[refill_label]
            )
            refined_domain = safe_intersection - bad_edges
            if (
                len(safe_intersection) >= gamma * pool_size
                and len(bad_edges) <= epsilon * pool_size
            ):
                adjacency[left_index].append(right_index)
                refined_domain_sizes.append(len(refined_domain))

    maximum_matching = maximum_bipartite_matching(adjacency, len(labels))
    left_degrees = [len(neighbors) for neighbors in adjacency]
    right_degrees = [
        sum(right in neighbors for neighbors in adjacency)
        for right in range(len(labels))
    ]
    refined_density = gamma - epsilon

    return {
        "source_n": n,
        "layer": layer_index,
        "pool_size": pool_size,
        "fixed_source_size": len(fixed),
        "candidate_labels": list(labels),
        "gamma": str(gamma),
        "epsilon": str(epsilon),
        "refined_density_lower_bound": str(refined_density),
        "movement_safe_sizes": {
            str(label): len(movement_safe[label]) for label in labels
        },
        "refill_safe_sizes": {
            str(label): len(refill_safe[label]) for label in labels
        },
        "same_edge_bad_incidence_sum": bad_incidence_sum,
        "pool_anchor_divisor_energy": divisor_energy,
        "PP3fe_energy_bound_holds": bad_incidence_sum <= divisor_energy,
        "label_pairs_above_epsilon": bad_pair_count,
        "refined_graph_edge_count": sum(left_degrees),
        "refined_graph_min_left_degree": min(left_degrees, default=0),
        "refined_graph_min_right_degree": min(right_degrees, default=0),
        "refined_graph_maximum_matching": maximum_matching,
        "refined_graph_has_full_matching": maximum_matching == len(labels),
        "minimum_refined_domain_size_on_graph": min(
            refined_domain_sizes, default=0
        ),
        "maximum_refined_domain_size_on_graph": max(
            refined_domain_sizes, default=0
        ),
        "PP3ff_certified_width": certified_width(
            maximum_matching, pool_size, refined_density, False
        ),
        "PP3fg_spread_certified_width": certified_width(
            maximum_matching, pool_size, refined_density, True
        ),
    }


def analyze_case(
    n: int,
    core: tuple[Point, ...],
    label_count: int,
    gamma: Fraction,
    epsilon: Fraction,
) -> dict[str, Any]:
    layer_zero, layer_one, cycle_lengths = alternating_decomposition(n, core)
    return {
        "source_n": n,
        "cycle_edge_lengths": list(cycle_lengths),
        "layers": [
            analyze_layer(
                n,
                0,
                layer_zero,
                layer_one,
                label_count,
                gamma,
                epsilon,
            ),
            analyze_layer(
                n,
                1,
                layer_one,
                layer_zero,
                label_count,
                gamma,
                epsilon,
            ),
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--labels", type=int, default=4)
    parser.add_argument("--gamma", type=parse_fraction, default=Fraction(1, 2))
    parser.add_argument("--epsilon", type=parse_fraction, default=Fraction(1, 4))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.labels < 1:
        raise SystemExit("--labels must be positive")
    if args.epsilon >= args.gamma:
        raise SystemExit("require epsilon < gamma")

    try:
        cases = load_cases(args.certificate, args.n)
        result = {
            "cases": [
                analyze_case(
                    n,
                    core,
                    args.labels,
                    args.gamma,
                    args.epsilon,
                )
                for n, core in cases
                if n >= 2
            ]
        }
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

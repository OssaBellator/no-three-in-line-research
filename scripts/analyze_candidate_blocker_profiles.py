#!/usr/bin/env python3
"""Analyze PP3cs blocker-cover profiles for every labeled candidate cell.

For a chosen matching layer and block size r, reserve K=floor(m/r) width-two
intervals.  For every source edge, block label, component, and new line, compute
the external source blocker matching through the candidate cell, remove the
automatic controller axis pair, classify the remaining pairs by their number of
endpoints in the deletable layer, and evaluate the exact PP3cs cover probability.
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
    Candidate,
    build_candidates,
    determinant,
    fraction_object,
    load_certificates,
    matching_layers,
)

Point = tuple[int, int]


def safe_comb(n: int, k: int) -> int:
    if n < 0 or k < 0 or k > n:
        return 0
    return math.comb(n, k)


def blocker_pairs(points: tuple[Point, ...], candidate: Point) -> tuple[tuple[int, int], ...]:
    pairs = tuple(
        (first, second)
        for first, second in itertools.combinations(range(len(points)), 2)
        if determinant(points[first], points[second], candidate) == 0
    )
    endpoints = [edge for pair in pairs for edge in pair]
    if len(set(endpoints)) != len(endpoints):
        raise AssertionError("external-point blocker pairs are not a matching")
    return pairs


def cover_probability(
    layer_size: int,
    deleted_count: int,
    one_endpoint_pairs: int,
    two_endpoint_pairs: int,
    zero_endpoint_pairs: int,
) -> Fraction:
    if zero_endpoint_pairs:
        return Fraction(0)
    denominator = safe_comb(layer_size - 1, deleted_count - 1)
    if denominator == 0:
        return Fraction(0)
    numerator = 0
    for missed in range(two_endpoint_pairs + 1):
        numerator += (
            (-1) ** missed
            * safe_comb(two_endpoint_pairs, missed)
            * safe_comb(
                layer_size - 1 - one_endpoint_pairs - 2 * missed,
                deleted_count - 1 - one_endpoint_pairs,
            )
        )
    return Fraction(numerator, denominator)


def candidate_profile(
    points: tuple[Point, ...], layer: set[int], candidate: Candidate, deleted_count: int
) -> tuple[int, int, int, int, Fraction]:
    controller = candidate[1]
    pairs = blocker_pairs(points, candidate[4])
    controller_pairs = [pair for pair in pairs if controller in pair]
    if len(controller_pairs) != 1:
        raise AssertionError("candidate does not have one automatic controller blocker")

    additional = [pair for pair in pairs if controller not in pair]
    endpoint_ranks = [int(first in layer) + int(second in layer) for first, second in additional]
    zero = endpoint_ranks.count(0)
    one = endpoint_ranks.count(1)
    two = endpoint_ranks.count(2)
    probability = cover_probability(len(layer), deleted_count, one, two, zero)
    return len(additional), one, two, zero, probability


def analyze_layer(
    n: int,
    points: tuple[Point, ...],
    layer_number: int,
    layer_tuple: tuple[int, ...],
    block_size: int,
) -> dict[str, Any]:
    block_count = n // block_size
    if block_count == 0:
        raise ValueError(f"n={n}: block size exceeds matching layer size")
    deleted_count = 4 * block_count
    _, all_candidates = build_candidates(n, layer_tuple, points, block_count)
    layer = set(layer_tuple)

    additional_histogram: Counter[int] = Counter()
    profile_histogram: Counter[tuple[int, int, int]] = Counter()
    probability_histogram: Counter[str] = Counter()
    axis_clean = 0
    impossible = 0
    expected_safe = Fraction(0)

    for candidate in all_candidates:
        additional, one, two, zero, probability = candidate_profile(
            points, layer, candidate, deleted_count
        )
        additional_histogram[additional] += 1
        profile_histogram[one, two, zero] += 1
        probability_histogram[str(probability)] += 1
        if additional == 0:
            axis_clean += 1
        if zero:
            impossible += 1
        expected_safe += Fraction(2, n) * probability

    total_candidates = len(all_candidates)
    expected_selected = Fraction(2 * total_candidates, n)
    expected_unsafe = expected_selected - expected_safe
    nontrivial_upper = min(Fraction(1), Fraction(2 * (deleted_count - 1), n - 1))
    lower_bound = Fraction(2 * (total_candidates - axis_clean), n) * (1 - nontrivial_upper)

    return {
        "n": n,
        "layer": layer_number,
        "block_size": block_size,
        "block_count": block_count,
        "deleted_layer_edges": deleted_count,
        "candidate_entry_count": total_candidates,
        "axis_clean_candidate_entries": axis_clean,
        "impossible_candidate_entries": impossible,
        "additional_blocker_histogram": {
            str(rank): count for rank, count in sorted(additional_histogram.items())
        },
        "layer_endpoint_profile_histogram": {
            f"one={one},two={two},zero={zero}": count
            for (one, two, zero), count in sorted(profile_histogram.items())
        },
        "cover_probability_histogram": dict(sorted(probability_histogram.items())),
        "expected_selected_candidates": fraction_object(expected_selected),
        "expected_blocker_safe_selected_candidates": fraction_object(expected_safe),
        "expected_unsafe_selected_candidates": fraction_object(expected_unsafe),
        "PP3cu_simple_lower_bound": fraction_object(lower_bound),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificates", type=Path)
    parser.add_argument("--n", type=int, action="append", dest="side_lengths")
    parser.add_argument("--layer", type=int, choices=(0, 1), action="append")
    parser.add_argument("--block-size", type=int, default=4)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.block_size < 4:
        raise SystemExit("block size must be at least four")

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
                        args.block_size,
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

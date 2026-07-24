#!/usr/bin/env python3
"""Enumerate random-block PP3ca loads and verify the PP3cl average bound."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

from analyze_matching_block_loads import determinant, patch_with_owners
from analyze_matching_first_reservoirs import alternating_decomposition, load_cases

Point = tuple[int, int]


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def theorem_bound(m: int, r: int) -> Fraction:
    if not 4 <= r <= m:
        raise ValueError("block size must satisfy 4 <= r <= m")
    return (
        Fraction(8 * m * (r - 1) * (r - 2), (m - 1) * (m - 2))
        + Fraction(32 * (r - 1), m - 1)
        + Fraction(192 * m * (r - 2), (m - 1) * (m - 2))
    )


def block_statistics(block: tuple[Point, ...], n: int) -> tuple[Fraction, Fraction, int]:
    r = len(block)
    blockers: set[tuple[int, int, Point]] = set()
    same_edge_anchors: set[tuple[int, Point, Point]] = set()
    two_edge_anchors: set[tuple[int, Point, Point]] = set()
    clean_states = 0
    state_count = 0

    for selected in combinations(range(r), 4):
        state_count += 1
        selected_set = set(selected)
        retained = tuple(index for index in range(r) if index not in selected_set)
        patch = patch_with_owners(block, selected, n)
        bad = False

        for first, second in combinations(retained, 2):
            for point, _, _ in patch:
                if determinant(block[first], block[second], point) == 0:
                    blockers.add((first, second, point))
                    bad = True

        for anchor in retained:
            for left, right in combinations(patch, 2):
                left_point, left_owner, _ = left
                right_point, right_owner, _ = right
                if determinant(block[anchor], left_point, right_point) != 0:
                    continue
                signature = (
                    anchor,
                    min(left_point, right_point),
                    max(left_point, right_point),
                )
                if left_owner == right_owner:
                    same_edge_anchors.add(signature)
                else:
                    two_edge_anchors.add(signature)
                bad = True

        if not bad:
            clean_states += 1

    load = (
        Fraction(4 * len(blockers), r)
        + Fraction(4 * len(same_edge_anchors), r)
        + Fraction(12 * len(two_edge_anchors), r * (r - 1))
    )
    clean_fraction = Fraction(clean_states, state_count)
    return load, clean_fraction, state_count


def analyze_layer(
    n: int, layer_index: int, layer: tuple[Point, ...], r: int
) -> dict[str, Any]:
    loads: list[Fraction] = []
    clean_fractions: list[Fraction] = []
    state_count = 0

    for indices in combinations(range(n), r):
        block = tuple(layer[index] for index in indices)
        load, clean_fraction, state_count = block_statistics(block, n)
        loads.append(load)
        clean_fractions.append(clean_fraction)

    average_load = sum(loads, Fraction()) / len(loads)
    average_clean_fraction = sum(clean_fractions, Fraction()) / len(clean_fractions)
    bound = theorem_bound(n, r)
    if average_load > bound:
        raise AssertionError("exact average exceeds PP3cl theorem bound")

    thresholds = (Fraction(1, 1), Fraction(1, 2), Fraction(1, 4))
    return {
        "layer": layer_index,
        "edge_count": n,
        "block_size": r,
        "block_count": len(loads),
        "canonical_states_per_block": state_count,
        "average_pp3ca_load": fraction_text(average_load),
        "theorem_pp3cl_bound": fraction_text(bound),
        "maximum_pp3ca_load": fraction_text(max(loads)),
        "minimum_pp3ca_load": fraction_text(min(loads)),
        "average_exact_clean_fraction": fraction_text(average_clean_fraction),
        "blocks_below_load_threshold": {
            fraction_text(threshold): sum(load <= threshold for load in loads)
            for threshold in thresholds
        },
    }


def analyze_case(
    n: int, core: tuple[Point, ...], requested_r: int | None
) -> dict[str, Any]:
    if n < 4:
        return {"source_n": n, "layers": [], "status": "fewer-than-four-edges"}
    r = requested_r if requested_r is not None else min(n, 4)
    if not 4 <= r <= n:
        raise ValueError(f"n={n}: block size must satisfy 4 <= r <= n")
    layer_zero, layer_one, cycle_lengths = alternating_decomposition(n, core)
    return {
        "source_n": n,
        "cycle_edge_lengths": list(cycle_lengths),
        "layers": [
            analyze_layer(n, index, layer, r)
            for index, layer in enumerate((layer_zero, layer_one))
        ],
        "status": "searched",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--r", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        cases = load_cases(args.certificate, args.n)
        result = {
            "cases": [analyze_case(n, core, args.r) for n, core in cases]
        }
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

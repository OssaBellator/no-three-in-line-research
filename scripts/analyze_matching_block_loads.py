#!/usr/bin/env python3
"""Compute PP3ca signature loads for full perfect-matching source blocks."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

from analyze_matching_first_reservoirs import alternating_decomposition, load_cases

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def patch_with_owners(
    layer: tuple[Point, ...], selected: tuple[int, ...], n: int
) -> tuple[tuple[Point, int, str], ...]:
    by_column = sorted(selected, key=lambda index: layer[index][0])
    by_row = sorted(selected, key=lambda index: layer[index][1])
    a, b = n + 1, n + 2
    patch: list[tuple[Point, int, str]] = []
    for rank, edge_index in enumerate(by_column):
        x, _ = layer[edge_index]
        patch.append(((x, a if rank < 2 else b), edge_index, "M"))
    for rank, edge_index in enumerate(by_row):
        _, y = layer[edge_index]
        patch.append(((a if rank < 2 else b, y), edge_index, "F"))
    return tuple(patch)


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def analyze_layer(
    n: int, layer_index: int, layer: tuple[Point, ...]
) -> dict[str, Any]:
    r = len(layer)
    blocker_signatures: set[tuple[int, int, Point]] = set()
    same_edge_anchor_signatures: set[tuple[int, Point, Point]] = set()
    two_edge_anchor_signatures: set[tuple[int, Point, Point]] = set()
    total_local_triples = 0
    locally_clean_states = 0
    state_count = 0

    for selected in combinations(range(r), 4):
        state_count += 1
        selected_set = set(selected)
        retained = tuple(index for index in range(r) if index not in selected_set)
        patch = patch_with_owners(layer, selected, n)
        state_triples = 0

        for first, second in combinations(retained, 2):
            for point, _, _ in patch:
                if determinant(layer[first], layer[second], point) == 0:
                    blocker_signatures.add((first, second, point))
                    state_triples += 1

        for anchor in retained:
            for left, right in combinations(patch, 2):
                left_point, left_owner, _ = left
                right_point, right_owner, _ = right
                if determinant(layer[anchor], left_point, right_point) != 0:
                    continue
                signature = (
                    anchor,
                    min(left_point, right_point),
                    max(left_point, right_point),
                )
                if left_owner == right_owner:
                    same_edge_anchor_signatures.add(signature)
                else:
                    two_edge_anchor_signatures.add(signature)
                state_triples += 1

        total_local_triples += state_triples
        locally_clean_states += state_triples == 0

    b_count = len(blocker_signatures)
    a1_count = len(same_edge_anchor_signatures)
    a2_count = len(two_edge_anchor_signatures)
    bound = (
        Fraction(4 * b_count, r)
        + Fraction(4 * a1_count, r)
        + Fraction(12 * a2_count, r * (r - 1))
    )
    exact_average = Fraction(total_local_triples, state_count)
    return {
        "layer": layer_index,
        "edge_count": r,
        "state_count": state_count,
        "locally_clean_state_count": locally_clean_states,
        "blocker_signature_count_B": b_count,
        "same_edge_anchor_signature_count_A1": a1_count,
        "two_edge_anchor_signature_count_A2": a2_count,
        "pp3ca_upper_bound": fraction_text(bound),
        "exact_average_local_triples": fraction_text(exact_average),
        "criterion_passes": bound < 1,
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

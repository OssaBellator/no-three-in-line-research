#!/usr/bin/env python3
"""Check that only final-state shadow matters along a source-valid trade path."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


Point = tuple[int, int]
Entry = tuple[str, int, int, int]


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (
        c[0] - a[0]
    )


def row_intersection(a: Point, b: Point, row: int) -> int | None:
    if a[1] == b[1]:
        return None
    t = Fraction(row - a[1], b[1] - a[1])
    x = Fraction(a[0]) + t * (b[0] - a[0])
    return int(x) if x.denominator == 1 else None


def column_intersection(a: Point, b: Point, column: int) -> int | None:
    if a[0] == b[0]:
        return None
    t = Fraction(column - a[0], b[0] - a[0])
    y = Fraction(a[1]) + t * (b[1] - a[1])
    return int(y) if y.denominator == 1 else None


def assert_no_three(points: set[Point], stage: int) -> None:
    for triple in itertools.combinations(points, 3):
        if collinear(*triple):
            raise ValueError(f"stage {stage} is not no-three-in-line: {triple}")


def state_shadow(
    initial: set[Point],
    current: set[Point],
    movement_labels: list[int],
    refill_labels: list[int],
    old_max: int,
    macro_modulus: int,
) -> dict[str, Any]:
    new_points = sorted(current - initial)
    retained_old = sorted(current & initial)
    unary_support: set[Entry] = set()
    binary_support: set[Entry] = set()
    unary_incidence_weight = 0
    unary_fibres: dict[tuple[int, str, int, int], set[tuple[int, int]]] = (
        defaultdict(set)
    )

    for new_index, a in enumerate(new_points):
        for old_index, p in enumerate(retained_old):
            for label in movement_labels:
                x = row_intersection(a, p, label)
                if x is not None and 0 <= x <= old_max:
                    entry = ("M", label, x, x % macro_modulus)
                    unary_support.add(entry)
                    unary_incidence_weight += 1
                    unary_fibres[(new_index, "M", label, x % macro_modulus)].add(
                        (x, old_index)
                    )
            for label in refill_labels:
                y = column_intersection(a, p, label)
                if y is not None and 0 <= y <= old_max:
                    entry = ("F", label, y, y % macro_modulus)
                    unary_support.add(entry)
                    unary_incidence_weight += 1
                    unary_fibres[(new_index, "F", label, y % macro_modulus)].add(
                        (y, old_index)
                    )

    for a, b in itertools.combinations(new_points, 2):
        for label in movement_labels:
            x = row_intersection(a, b, label)
            if x is not None and 0 <= x <= old_max:
                binary_support.add(("M", label, x, x % macro_modulus))
        for label in refill_labels:
            y = column_intersection(a, b, label)
            if y is not None and 0 <= y <= old_max:
                binary_support.add(("F", label, y, y % macro_modulus))

    best_fibre: dict[str, Any] | None = None
    if unary_fibres:
        key, entries = max(unary_fibres.items(), key=lambda item: len(item[1]))
        best_fibre = {
            "new_point_index": key[0],
            "type": key[1],
            "label": key[2],
            "macro": key[3],
            "degree": len({edge for edge, _ in entries}),
            "distinct_old_partners": len({old for _, old in entries}),
        }

    return {
        "new_points": new_points,
        "retained_old": retained_old,
        "unary_support": unary_support,
        "binary_support": binary_support,
        "unary_incidence_weight": unary_incidence_weight,
        "best_unary_fibre": best_fibre,
    }


def maximum_domain_loss(
    support: set[Entry],
    movement_labels: list[int],
    refill_labels: list[int],
    macro_modulus: int,
) -> tuple[int, tuple[int, int, int] | None]:
    movement: dict[tuple[int, int], set[int]] = defaultdict(set)
    refill: dict[tuple[int, int], set[int]] = defaultdict(set)
    for kind, label, edge, macro in support:
        target = movement if kind == "M" else refill
        target[(macro, label)].add(edge)

    best = 0
    witness: tuple[int, int, int] | None = None
    for macro in range(macro_modulus):
        for movement_label in movement_labels:
            for refill_label in refill_labels:
                loss = len(
                    movement[(macro, movement_label)]
                    | refill[(macro, refill_label)]
                )
                if loss > best:
                    best = loss
                    witness = (macro, movement_label, refill_label)
    return best, witness


def analyse(data: dict[str, Any]) -> dict[str, Any]:
    initial = {tuple(map(int, p)) for p in data["initial_points"]}
    movement_labels = list(map(int, data["movement_labels"]))
    refill_labels = list(map(int, data["refill_labels"]))
    old_max = int(data["old_coordinate_max"])
    macro_modulus = int(data["macro_modulus"])
    R = float(data["R"])
    gamma = float(data["gamma"])
    xi = float(data["xi"])
    base_domain_size = int(data["base_domain_size"])

    current = set(initial)
    assert_no_three(current, 0)
    stage_shadows: list[dict[str, Any]] = []
    union_support: set[Entry] = set()

    for stage_index, stage in enumerate(data["stages"], start=1):
        removals = {tuple(map(int, p)) for p in stage.get("remove", [])}
        insertions = {tuple(map(int, p)) for p in stage.get("insert", [])}
        missing = removals - current
        if missing:
            raise ValueError(f"stage {stage_index} removes absent points: {missing}")
        duplicate = insertions & (current - removals)
        if duplicate:
            raise ValueError(f"stage {stage_index} reinserts present points: {duplicate}")
        current = (current - removals) | insertions
        assert_no_three(current, stage_index)
        shadow = state_shadow(
            initial,
            current,
            movement_labels,
            refill_labels,
            old_max,
            macro_modulus,
        )
        support = shadow["unary_support"] | shadow["binary_support"]
        union_support |= support
        stage_shadows.append(
            {
                "stage": stage_index,
                "source_size": len(current),
                "new_point_count": len(shadow["new_points"]),
                "unary_support_size": len(shadow["unary_support"]),
                "binary_support_size": len(shadow["binary_support"]),
                "total_support_size": len(support),
            }
        )

    final_shadow = state_shadow(
        initial,
        current,
        movement_labels,
        refill_labels,
        old_max,
        macro_modulus,
    )
    final_support = final_shadow["unary_support"] | final_shadow["binary_support"]
    transient_only = union_support - final_support
    final_new_count = len(final_shadow["new_points"])
    binary_general_bound = final_new_count * max(0, final_new_count - 1)
    combined_general_bound = (
        final_shadow["unary_incidence_weight"] + binary_general_bound
    )
    exact_domain_loss, domain_witness = maximum_domain_loss(
        final_support, movement_labels, refill_labels, macro_modulus
    )
    post_shadow_lower_bound = base_domain_size - exact_domain_loss
    margin_budget = xi * R

    best_fibre = final_shadow["best_unary_fibre"]
    star_threshold = (
        xi * R / (2 * final_new_count) if final_new_count else float("inf")
    )
    star_degree = best_fibre["degree"] if best_fibre else 0

    direct = (
        combined_general_bound <= margin_budget
        and post_shadow_lower_bound >= gamma * R
    )
    star = star_degree > star_threshold
    if direct:
        outcome = "final_state_direct_allocation"
    elif star:
        outcome = "next_generation_unary_star"
    else:
        outcome = "base_margin_or_global_allocation_failure"

    return {
        "stage_count": len(stage_shadows),
        "stage_shadows": stage_shadows,
        "union_intermediate_support_size": len(union_support),
        "final_support_size": len(final_support),
        "transient_only_support_size": len(transient_only),
        "final_new_point_count": final_new_count,
        "final_unary_incidence_weight": final_shadow["unary_incidence_weight"],
        "final_unary_support_size": len(final_shadow["unary_support"]),
        "final_binary_support_size": len(final_shadow["binary_support"]),
        "binary_general_domain_bound": binary_general_bound,
        "combined_general_domain_bound": combined_general_bound,
        "exact_maximum_domain_loss": exact_domain_loss,
        "domain_witness": domain_witness,
        "base_domain_size": base_domain_size,
        "post_shadow_lower_bound": post_shadow_lower_bound,
        "allocation_threshold": gamma * R,
        "margin_budget": margin_budget,
        "largest_final_unary_fibre": best_fibre,
        "next_star_threshold": star_threshold,
        "outcome": outcome,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    with args.input.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    print(json.dumps(analyse(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

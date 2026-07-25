#!/usr/bin/env python3
"""Check unary and binary candidate support against a controller-domain margin."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


def collinear(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (
        c[0] - a[0]
    )


def row_intersection(
    a: tuple[int, int], b: tuple[int, int], row: int
) -> int | None:
    if a[1] == b[1]:
        return None
    t = Fraction(row - a[1], b[1] - a[1])
    x = Fraction(a[0]) + t * (b[0] - a[0])
    return int(x) if x.denominator == 1 else None


def column_intersection(
    a: tuple[int, int], b: tuple[int, int], column: int
) -> int | None:
    if a[0] == b[0]:
        return None
    t = Fraction(column - a[0], b[0] - a[0])
    y = Fraction(a[1]) + t * (b[1] - a[1])
    return int(y) if y.denominator == 1 else None


def analyse(data: dict[str, Any]) -> dict[str, Any]:
    inserted = [tuple(map(int, p)) for p in data["inserted_points"]]
    retained = [tuple(map(int, p)) for p in data["retained_points"]]
    movement_labels = list(map(int, data["movement_labels"]))
    refill_labels = list(map(int, data["refill_labels"]))
    old_max = int(data["old_coordinate_max"])
    controller_rows = list(map(int, data["controller_rows_by_column"]))
    macro_modulus = int(data["macro_modulus"])
    R = int(data["R"])
    gamma = float(data["gamma"])
    xi = float(data["xi"])
    base_domain_size = int(data["base_domain_size"])

    complete = inserted + retained
    if len({x for x, _ in complete}) != len(complete):
        raise ValueError("complete state must use distinct old columns in this diagnostic")
    if len({y for _, y in complete}) != len(complete):
        raise ValueError("complete state must use distinct old rows in this diagnostic")
    for triple in itertools.combinations(complete, 3):
        if collinear(*triple):
            raise ValueError("complete state is not no-three-in-line")

    if sorted(controller_rows) != list(range(len(controller_rows))):
        raise ValueError("controller_rows_by_column must be a coordinate permutation")
    if len(controller_rows) != old_max + 1:
        raise ValueError("controller matching must cover every old coordinate")
    row_to_edge = {row: col for col, row in enumerate(controller_rows)}

    unary_incidences: list[tuple[int, int, str, int, int]] = []
    unary_support: set[tuple[str, int, int]] = set()

    for inserted_index, a in enumerate(inserted):
        for retained_index, p in enumerate(retained):
            for label in movement_labels:
                x = row_intersection(a, p, label)
                if x is None or not (0 <= x <= old_max):
                    continue
                unary_incidences.append(
                    (inserted_index, retained_index, "M", label, x)
                )
                unary_support.add(("M", label, x))
            for label in refill_labels:
                y = column_intersection(a, p, label)
                if y is None or not (0 <= y <= old_max):
                    continue
                edge = row_to_edge[y]
                unary_incidences.append(
                    (inserted_index, retained_index, "F", label, edge)
                )
                unary_support.add(("F", label, edge))

    fixed_inserted_candidate_multiplicity = Counter(
        (inserted_index, kind, label, edge)
        for inserted_index, _, kind, label, edge in unary_incidences
    )
    candidate_multiplicity = Counter(
        (kind, label, edge)
        for _, _, kind, label, edge in unary_incidences
    )

    binary_support: set[tuple[str, int, int]] = set()
    for a, b in itertools.combinations(inserted, 2):
        for label in movement_labels:
            x = row_intersection(a, b, label)
            if x is not None and 0 <= x <= old_max:
                binary_support.add(("M", label, x))
        for label in refill_labels:
            y = column_intersection(a, b, label)
            if y is not None and 0 <= y <= old_max:
                binary_support.add(("F", label, row_to_edge[y]))

    combined_support = unary_support | binary_support
    max_domain_loss = 0
    max_domain_loss_state: dict[str, Any] | None = None
    for movement_label in movement_labels:
        for refill_label in refill_labels:
            for macro in range(macro_modulus):
                removed = {
                    edge
                    for kind, label, edge in combined_support
                    if kind == "M"
                    and label == movement_label
                    and edge % macro_modulus == macro
                }
                removed.update(
                    edge
                    for kind, label, edge in combined_support
                    if kind == "F"
                    and label == refill_label
                    and edge % macro_modulus == macro
                )
                if len(removed) > max_domain_loss:
                    max_domain_loss = len(removed)
                    max_domain_loss_state = {
                        "movement_label": movement_label,
                        "refill_label": refill_label,
                        "macro": macro,
                        "controller_edges": sorted(removed),
                    }

    s = len(inserted)
    unary_weight = len(unary_incidences)
    binary_bound = s * (s - 1)
    crude_domain_bound = unary_weight + binary_bound
    witness_uniqueness = max(
        fixed_inserted_candidate_multiplicity.values(), default=0
    ) <= 1
    candidate_multiplicity_bound = max(
        candidate_multiplicity.values(), default=0
    ) <= s
    margin_ok = crude_domain_bound <= xi * R
    post_domain_lower_bound = base_domain_size - max_domain_loss
    allocation_threshold = gamma * R
    bypass_ok = (
        witness_uniqueness
        and candidate_multiplicity_bound
        and max_domain_loss <= crude_domain_bound
        and margin_ok
        and post_domain_lower_bound >= allocation_threshold
    )

    return {
        "inserted_state_size": s,
        "retained_state_size": len(retained),
        "unary_incidence_weight": unary_weight,
        "simple_unary_candidate_entries": len(unary_support),
        "max_fixed_inserted_candidate_witnesses": max(
            fixed_inserted_candidate_multiplicity.values(), default=0
        ),
        "max_candidate_unary_multiplicity": max(
            candidate_multiplicity.values(), default=0
        ),
        "binary_candidate_entries": len(binary_support),
        "binary_domain_bound": binary_bound,
        "crude_combined_domain_bound": crude_domain_bound,
        "max_domain_loss": max_domain_loss,
        "max_domain_loss_state": max_domain_loss_state,
        "base_domain_size": base_domain_size,
        "post_shadow_lower_bound": post_domain_lower_bound,
        "allocation_threshold": allocation_threshold,
        "margin_condition": margin_ok,
        "outcome": (
            "direct_unary_binary_shadow_bypass"
            if bypass_ok
            else "unary_domain_core_or_margin_failure"
        ),
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

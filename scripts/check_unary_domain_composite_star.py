#!/usr/bin/env python3
"""Check the unary-domain-failure to composite source-star reduction."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
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
    labels = list(map(int, data["labels"]))
    old_max = int(data["old_coordinate_max"])
    macro_modulus = int(data["macro_modulus"])
    R = float(data["R"])
    xi = float(data["xi"])
    initial_credit = float(data["initial_credit"])
    first_other_cost = float(data["first_other_cost"])
    second_foreign_cost = float(data["second_foreign_cost"])
    star_ambient_size = int(data["star_ambient_size"])
    star_subbank_size = int(data["star_subbank_size"])
    marked_distortion = float(data["marked_distortion"])

    complete = inserted + retained
    for triple in itertools.combinations(complete, 3):
        if collinear(*triple):
            raise ValueError("complete state is not no-three-in-line")

    fibres: dict[tuple[int, str, int, int], set[tuple[int, int]]] = defaultdict(set)
    for inserted_index, a in enumerate(inserted):
        for retained_index, p in enumerate(retained):
            for label in labels:
                x = row_intersection(a, p, label)
                if x is not None and 0 <= x <= old_max:
                    fibres[(inserted_index, "M", label, x % macro_modulus)].add(
                        (x, retained_index)
                    )
                y = column_intersection(a, p, label)
                if y is not None and 0 <= y <= old_max:
                    fibres[(inserted_index, "F", label, y % macro_modulus)].add(
                        (y, retained_index)
                    )

    if not fibres:
        raise ValueError("stored state has no unary candidate fibres")
    best_key, best_entries = max(fibres.items(), key=lambda item: len(item[1]))
    star_degree = len({edge for edge, _ in best_entries})
    distinct_partner_count = len(
        {retained_index for _, retained_index in best_entries}
    )
    threshold = xi * R / (2 * len(inserted))

    if star_subbank_size < 3 or star_ambient_size <= 2:
        raise ValueError("marked sizes must make the recapture formula meaningful")
    self_recapture_bound = (
        marked_distortion
        * star_degree
        * (star_subbank_size - 2)
        / (star_ambient_size - 2)
    )
    composite_change_upper = (
        first_other_cost
        + self_recapture_bound
        + second_foreign_cost
        - initial_credit
    )

    star_ok = star_degree >= threshold and distinct_partner_count == star_degree
    outcome = (
        "composite_paid_improvement"
        if star_ok and composite_change_upper < 0
        else "foreign_cost_or_marked_host_failure"
    )

    return {
        "inserted_state_size": len(inserted),
        "largest_fibre": {
            "inserted_index": best_key[0],
            "type": best_key[1],
            "label": best_key[2],
            "macro": best_key[3],
            "controller_edges": sorted(edge for edge, _ in best_entries),
            "retained_partner_indices": sorted(
                retained_index for _, retained_index in best_entries
            ),
        },
        "star_degree": star_degree,
        "distinct_star_partners": distinct_partner_count,
        "pigeonhole_threshold": threshold,
        "initial_credit": initial_credit,
        "first_other_cost": first_other_cost,
        "self_recapture_bound": self_recapture_bound,
        "second_foreign_cost": second_foreign_cost,
        "composite_change_upper": composite_change_upper,
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

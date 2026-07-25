#!/usr/bin/env python3
"""Check domain congestion from all binary secants of an endpoint trade."""

from __future__ import annotations

import argparse
import itertools
import json
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
    ax, ay = a
    bx, by = b
    if ay == by:
        return None
    t = Fraction(row - ay, by - ay)
    x = Fraction(ax) + t * (bx - ax)
    return int(x) if x.denominator == 1 else None


def column_intersection(
    a: tuple[int, int], b: tuple[int, int], column: int
) -> int | None:
    ax, ay = a
    bx, by = b
    if ax == bx:
        return None
    t = Fraction(column - ax, bx - ax)
    y = Fraction(ay) + t * (by - ay)
    return int(y) if y.denominator == 1 else None


def analyse(data: dict[str, Any]) -> dict[str, Any]:
    points = [tuple(map(int, p)) for p in data["inserted_points"]]
    movement_labels = list(map(int, data["movement_labels"]))
    refill_labels = list(map(int, data["refill_labels"]))
    old_max = int(data["old_coordinate_max"])
    controller_rows = list(map(int, data["controller_rows_by_column"]))
    macro_modulus = int(data["macro_modulus"])
    R = int(data["R"])
    gamma = float(data["gamma"])
    xi = float(data["xi"])
    base_domain_size = int(data["base_domain_size"])

    if len({x for x, _ in points}) != len(points):
        raise ValueError("inserted points must use distinct old columns")
    if len({y for _, y in points}) != len(points):
        raise ValueError("inserted points must use distinct old rows")
    for triple in itertools.combinations(points, 3):
        if collinear(*triple):
            raise ValueError("inserted state is not no-three-in-line")

    if sorted(controller_rows) != list(range(len(controller_rows))):
        raise ValueError("controller_rows_by_column must be a coordinate permutation")
    if len(controller_rows) != old_max + 1:
        raise ValueError("controller matching must cover every old coordinate")
    row_to_edge = {row: col for col, row in enumerate(controller_rows)}

    secants = list(itertools.combinations(points, 2))
    line_bound = len(secants)
    movement: dict[int, set[tuple[int, int]]] = {
        label: set() for label in movement_labels
    }
    refill: dict[int, set[tuple[int, int]]] = {
        label: set() for label in refill_labels
    }

    for line_index, (a, b) in enumerate(secants):
        for label in movement_labels:
            x = row_intersection(a, b, label)
            if x is None or not (0 <= x <= old_max):
                continue
            movement[label].add((line_index, x))
        for label in refill_labels:
            y = column_intersection(a, b, label)
            if y is None or not (0 <= y <= old_max):
                continue
            refill[label].add((line_index, row_to_edge[y]))

    max_movement_label_load = max((len(v) for v in movement.values()), default=0)
    max_refill_label_load = max((len(v) for v in refill.values()), default=0)

    movement_edge_load: dict[int, int] = {}
    refill_edge_load: dict[int, int] = {}
    for entries in movement.values():
        for _, edge in entries:
            movement_edge_load[edge] = movement_edge_load.get(edge, 0) + 1
    for entries in refill.values():
        for _, edge in entries:
            refill_edge_load[edge] = refill_edge_load.get(edge, 0) + 1

    max_movement_edge_load = max(movement_edge_load.values(), default=0)
    max_refill_edge_load = max(refill_edge_load.values(), default=0)

    max_domain_loss = 0
    max_domain_loss_state: dict[str, Any] | None = None
    for movement_label in movement_labels:
        for refill_label in refill_labels:
            for macro in range(macro_modulus):
                removed = {
                    edge
                    for _, edge in movement[movement_label]
                    if edge % macro_modulus == macro
                }
                removed.update(
                    edge
                    for _, edge in refill[refill_label]
                    if edge % macro_modulus == macro
                )
                if len(removed) > max_domain_loss:
                    max_domain_loss = len(removed)
                    max_domain_loss_state = {
                        "movement_label": movement_label,
                        "refill_label": refill_label,
                        "macro": macro,
                        "controller_edges": sorted(removed),
                    }

    trace_bound_ok = all(
        load <= line_bound
        for load in (
            max_movement_label_load,
            max_refill_label_load,
            max_movement_edge_load,
            max_refill_edge_load,
        )
    )
    domain_loss_bound = 2 * line_bound
    domain_bound_ok = max_domain_loss <= domain_loss_bound
    margin_ok = domain_loss_bound <= xi * R
    post_domain_lower_bound = base_domain_size - max_domain_loss
    allocation_threshold = gamma * R
    bypass_ok = (
        trace_bound_ok
        and domain_bound_ok
        and margin_ok
        and post_domain_lower_bound >= allocation_threshold
    )

    return {
        "inserted_state_size": len(points),
        "secant_lines": line_bound,
        "movement_candidate_entries": sum(map(len, movement.values())),
        "refill_candidate_entries": sum(map(len, refill.values())),
        "max_movement_label_load": max_movement_label_load,
        "max_refill_label_load": max_refill_label_load,
        "max_movement_controller_load": max_movement_edge_load,
        "max_refill_controller_load": max_refill_edge_load,
        "line_union_degree_bound": line_bound,
        "max_domain_loss": max_domain_loss,
        "domain_loss_bound": domain_loss_bound,
        "max_domain_loss_state": max_domain_loss_state,
        "base_domain_size": base_domain_size,
        "post_domain_lower_bound": post_domain_lower_bound,
        "allocation_threshold": allocation_threshold,
        "margin_condition": margin_ok,
        "outcome": (
            "direct_binary_shadow_bypass"
            if bypass_ok
            else "domain_margin_or_host_failure"
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

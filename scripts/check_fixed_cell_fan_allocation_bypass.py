#!/usr/bin/env python3
"""Check the allocation-domain congestion bound for a fixed-cell binary fan."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd
from pathlib import Path
from typing import Any


def integer_intersection_on_row(
    a: tuple[int, int], b: tuple[int, int], row: int
) -> int | None:
    ax, ay = a
    bx, by = b
    if by == ay:
        return None
    t = Fraction(row - ay, by - ay)
    x = Fraction(ax) + t * (bx - ax)
    return int(x) if x.denominator == 1 else None


def integer_intersection_on_column(
    a: tuple[int, int], b: tuple[int, int], column: int
) -> int | None:
    ax, ay = a
    bx, by = b
    if bx == ax:
        return None
    t = Fraction(column - ax, bx - ax)
    y = Fraction(ay) + t * (by - ay)
    return int(y) if y.denominator == 1 else None


def analyse(data: dict[str, Any]) -> dict[str, Any]:
    centre = tuple(map(int, data["centre"]))
    partners = [tuple(map(int, p)) for p in data["partners"]]
    movement_labels = list(map(int, data["movement_labels"]))
    refill_labels = list(map(int, data["refill_labels"]))
    old_max = int(data["old_coordinate_max"])
    controller_rows = list(map(int, data["controller_rows_by_column"]))
    macro_modulus = int(data["macro_modulus"])
    R = int(data["R"])
    gamma = float(data["gamma"])
    xi = float(data["xi"])
    base_domain_size = int(data["base_domain_size"])

    if sorted(controller_rows) != list(range(len(controller_rows))):
        raise ValueError(
            "controller_rows_by_column must be a permutation of 0..old_coordinate_max"
        )
    if len(controller_rows) != old_max + 1:
        raise ValueError("controller matching must cover every old coordinate")
    row_to_edge = {row: col for col, row in enumerate(controller_rows)}

    cx, cy = centre
    seen_x: set[int] = set()
    seen_y: set[int] = set()
    line_directions: set[tuple[int, int]] = set()
    for bx, by in partners:
        if bx == cx or by == cy:
            raise ValueError("every fan partner must be compatible with the fixed centre")
        if bx in seen_x or by in seen_y:
            raise ValueError("partners must form a matching")
        seen_x.add(bx)
        seen_y.add(by)
        dx, dy = bx - cx, by - cy
        common = gcd(abs(dx), abs(dy))
        direction = (dx // common, dy // common)
        if direction[0] < 0:
            direction = (-direction[0], -direction[1])
        if direction in line_directions:
            raise ValueError("two partners lie on the same line through the centre")
        line_directions.add(direction)

    movement: dict[int, list[dict[str, int]]] = {
        label: [] for label in movement_labels
    }
    refill: dict[int, list[dict[str, int]]] = {
        label: [] for label in refill_labels
    }

    for partner_index, partner in enumerate(partners):
        for label in movement_labels:
            x = integer_intersection_on_row(centre, partner, label)
            if x is None or not (0 <= x <= old_max):
                continue
            edge_id = x
            movement[label].append(
                {
                    "partner": partner_index,
                    "controller_edge": edge_id,
                    "macro": edge_id % macro_modulus,
                }
            )
        for label in refill_labels:
            y = integer_intersection_on_column(centre, partner, label)
            if y is None or not (0 <= y <= old_max):
                continue
            edge_id = row_to_edge[y]
            refill[label].append(
                {
                    "partner": partner_index,
                    "controller_edge": edge_id,
                    "macro": edge_id % macro_modulus,
                }
            )

    n = len(partners)
    max_movement_label_load = max((len(v) for v in movement.values()), default=0)
    max_refill_label_load = max((len(v) for v in refill.values()), default=0)

    movement_edge_load: dict[int, int] = {}
    refill_edge_load: dict[int, int] = {}
    for entries in movement.values():
        for entry in entries:
            edge = entry["controller_edge"]
            movement_edge_load[edge] = movement_edge_load.get(edge, 0) + 1
    for entries in refill.values():
        for entry in entries:
            edge = entry["controller_edge"]
            refill_edge_load[edge] = refill_edge_load.get(edge, 0) + 1

    max_movement_edge_load = max(movement_edge_load.values(), default=0)
    max_refill_edge_load = max(refill_edge_load.values(), default=0)

    max_domain_loss = 0
    max_domain_loss_state: dict[str, Any] | None = None
    for movement_label in movement_labels:
        for refill_label in refill_labels:
            for macro in range(macro_modulus):
                removed = {
                    entry["controller_edge"]
                    for entry in movement[movement_label]
                    if entry["macro"] == macro
                }
                removed.update(
                    entry["controller_edge"]
                    for entry in refill[refill_label]
                    if entry["macro"] == macro
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
        value <= n
        for value in (
            max_movement_label_load,
            max_refill_label_load,
            max_movement_edge_load,
            max_refill_edge_load,
        )
    )
    domain_bound_ok = max_domain_loss <= 2 * n
    margin_ok = 2 * n <= xi * R
    post_domain_lower_bound = base_domain_size - max_domain_loss
    allocation_threshold = gamma * R
    bypass_ok = (
        trace_bound_ok
        and domain_bound_ok
        and margin_ok
        and post_domain_lower_bound >= allocation_threshold
    )

    return {
        "residual_matching_size": n,
        "movement_candidate_entries": sum(map(len, movement.values())),
        "refill_candidate_entries": sum(map(len, refill.values())),
        "max_movement_label_load": max_movement_label_load,
        "max_refill_label_load": max_refill_label_load,
        "max_movement_controller_load": max_movement_edge_load,
        "max_refill_controller_load": max_refill_edge_load,
        "trace_degree_bound": n,
        "max_domain_loss": max_domain_loss,
        "domain_loss_bound": 2 * n,
        "max_domain_loss_state": max_domain_loss_state,
        "base_domain_size": base_domain_size,
        "post_domain_lower_bound": post_domain_lower_bound,
        "allocation_threshold": allocation_threshold,
        "margin_condition": margin_ok,
        "outcome": (
            "direct_allocation_bypass"
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

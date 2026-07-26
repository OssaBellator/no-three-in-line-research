#!/usr/bin/env python3
"""Check multiplicity-blind domain loss for current-row fixed states."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd
from pathlib import Path
from typing import Any


def canonical_line(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int, int]:
    x1, y1 = a
    x2, y2 = b
    if x1 == x2 or y1 == y2:
        raise ValueError("fixed-state lines must be nonvertical and nonhorizontal")
    A = y2 - y1
    B = x1 - x2
    C = -(A * x1 + B * y1)
    d = gcd(gcd(abs(A), abs(B)), abs(C)) or 1
    A, B, C = A // d, B // d, C // d
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def row_intersection(line: tuple[int, int, int], row: int) -> int | None:
    A, B, C = line
    x = Fraction(-(B * row + C), A)
    return int(x) if x.denominator == 1 else None


def column_intersection(line: tuple[int, int, int], column: int) -> int | None:
    A, B, C = line
    y = Fraction(-(A * column + C), B)
    return int(y) if y.denominator == 1 else None


def require_point(value: Any, label: str) -> tuple[int, int]:
    if not isinstance(value, list) or len(value) != 2:
        raise ValueError(f"{label}: expected [x,y]")
    x, y = value
    if isinstance(x, bool) or isinstance(y, bool) or not isinstance(x, int) or not isinstance(y, int):
        raise ValueError(f"{label}: coordinates must be integers")
    return x, y


def analyse_case(data: dict[str, Any]) -> dict[str, Any]:
    fixed = [require_point(v, "fixed_cells") for v in data["fixed_cells"]]
    partners = [require_point(v, "partners") for v in data["partners"]]
    if len(fixed) not in (1, 2):
        raise ValueError("fixed_cells must contain one or two cells")
    if not partners:
        raise ValueError("partners must be nonempty")

    movement_labels = [int(v) for v in data["movement_labels"]]
    refill_labels = [int(v) for v in data["refill_labels"]]
    old_max = int(data["old_coordinate_max"])
    controller_rows = [int(v) for v in data["controller_rows_by_column"]]
    macro_modulus = int(data["macro_modulus"])
    R = int(data["R"])
    gamma = float(data["gamma"])
    xi = float(data["xi"])
    base_domain_size = int(data["base_domain_size"])

    if len(controller_rows) != old_max + 1 or sorted(controller_rows) != list(range(old_max + 1)):
        raise ValueError("controller_rows_by_column must be a permutation of 0..old_coordinate_max")
    row_to_edge = {row: col for col, row in enumerate(controller_rows)}

    lines: set[tuple[int, int, int]] = set()
    for a in fixed:
        for b in partners:
            lines.add(canonical_line(a, b))
    for i, a in enumerate(fixed):
        for b in fixed[i + 1 :]:
            lines.add(canonical_line(a, b))

    k = len(fixed)
    n = len(partners)
    line_bound = k * n + k * (k - 1) // 2
    if len(lines) > line_bound:
        raise ValueError("distinct line count exceeds combinatorial bound")

    movement: dict[int, list[tuple[int, int]]] = {label: [] for label in movement_labels}
    refill: dict[int, list[tuple[int, int]]] = {label: [] for label in refill_labels}
    for line in lines:
        for label in movement_labels:
            x = row_intersection(line, label)
            if x is not None and 0 <= x <= old_max:
                movement[label].append((x, x % macro_modulus))
        for label in refill_labels:
            y = column_intersection(line, label)
            if y is not None and 0 <= y <= old_max:
                edge = row_to_edge[y]
                refill[label].append((edge, edge % macro_modulus))

    max_movement_label_load = max((len(set(v)) for v in movement.values()), default=0)
    max_refill_label_load = max((len(set(v)) for v in refill.values()), default=0)

    movement_edge_load: dict[int, int] = {}
    refill_edge_load: dict[int, int] = {}
    for entries in movement.values():
        for edge, _ in set(entries):
            movement_edge_load[edge] = movement_edge_load.get(edge, 0) + 1
    for entries in refill.values():
        for edge, _ in set(entries):
            refill_edge_load[edge] = refill_edge_load.get(edge, 0) + 1
    max_movement_edge_load = max(movement_edge_load.values(), default=0)
    max_refill_edge_load = max(refill_edge_load.values(), default=0)

    loads = [
        max_movement_label_load,
        max_refill_label_load,
        max_movement_edge_load,
        max_refill_edge_load,
    ]
    if any(load > line_bound for load in loads):
        raise ValueError("controller-edge--label load exceeds line bound")

    max_domain_loss = 0
    for A in movement_labels:
        for B in refill_labels:
            for macro in range(macro_modulus):
                removed = {edge for edge, m in movement[A] if m == macro}
                removed.update(edge for edge, m in refill[B] if m == macro)
                max_domain_loss = max(max_domain_loss, len(removed))

    domain_loss_bound = 2 * line_bound
    if max_domain_loss > domain_loss_bound:
        raise ValueError("paired-domain loss exceeds twice the line bound")

    post_domain_lower_bound = base_domain_size - max_domain_loss
    allocation_threshold = gamma * R
    margin_condition = domain_loss_bound <= xi * R
    bypass = margin_condition and post_domain_lower_bound >= allocation_threshold
    if not bypass:
        raise ValueError("stored case does not preserve the allocation margin")

    return {
        "name": str(data.get("name", "case")),
        "fixed_cell_count": k,
        "residual_matching_size": n,
        "distinct_line_count": len(lines),
        "line_count_bound": line_bound,
        "max_movement_label_load": max_movement_label_load,
        "max_refill_label_load": max_refill_label_load,
        "max_movement_controller_load": max_movement_edge_load,
        "max_refill_controller_load": max_refill_edge_load,
        "max_domain_loss": max_domain_loss,
        "domain_loss_bound": domain_loss_bound,
        "base_domain_size": base_domain_size,
        "post_domain_lower_bound": post_domain_lower_bound,
        "allocation_threshold": allocation_threshold,
        "margin_condition": margin_condition,
        "outcome": "direct_allocation_bypass",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        cases = payload.get("cases")
        if not isinstance(cases, list) or not cases:
            raise ValueError("cases must be a nonempty list")
        results = [analyse_case(case) for case in cases]
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc
    print(json.dumps({"outcome": "current_row_multiplicity_bypassed", "cases": results}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

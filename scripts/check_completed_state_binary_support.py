#!/usr/bin/env python3
"""Check simple binary secant support for one completed endpoint state."""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

Point = tuple[int, int]
Line = tuple[int, int, int]


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def normalize_line(a: Point, b: Point) -> Line:
    x1, y1 = a
    x2, y2 = b
    A = y2 - y1
    B = x1 - x2
    C = -(A * x1 + B * y1)
    common = math.gcd(math.gcd(abs(A), abs(B)), abs(C))
    if common:
        A //= common
        B //= common
        C //= common
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def row_intersection(line: Line, row: int) -> int | None:
    A, B, C = line
    if A == 0:
        return None
    x = Fraction(-(B * row + C), A)
    return int(x) if x.denominator == 1 else None


def column_intersection(line: Line, column: int) -> int | None:
    A, B, C = line
    if B == 0:
        return None
    y = Fraction(-(A * column + C), B)
    return int(y) if y.denominator == 1 else None


def analyse(data: dict[str, Any]) -> dict[str, Any]:
    old_max = require_int(data.get("old_coordinate_max"), "old_coordinate_max", 1)
    raw_points = data.get("selected_points")
    if not isinstance(raw_points, list) or len(raw_points) < 2:
        raise ValueError("selected_points: expected at least two points")
    points: list[Point] = []
    for i, raw in enumerate(raw_points):
        if not isinstance(raw, list) or len(raw) != 2:
            raise ValueError(f"selected_points[{i}]: expected [x,y]")
        x = require_int(raw[0], f"selected_points[{i}][0]")
        y = require_int(raw[1], f"selected_points[{i}][1]")
        points.append((x, y))
    if len(set(points)) != len(points):
        raise ValueError("selected_points: duplicates are not allowed")

    movement_labels = [require_int(v, "movement label") for v in data.get("movement_labels", [])]
    refill_labels = [require_int(v, "refill label") for v in data.get("refill_labels", [])]
    if not movement_labels or not refill_labels:
        raise ValueError("movement_labels and refill_labels must be nonempty")

    controller_rows = data.get("controller_rows_by_column")
    if not isinstance(controller_rows, list):
        raise ValueError("controller_rows_by_column: expected list")
    controller_rows = [require_int(v, "controller row") for v in controller_rows]
    if len(controller_rows) != old_max + 1:
        raise ValueError("controller_rows_by_column has wrong length")
    if sorted(controller_rows) != list(range(old_max + 1)):
        raise ValueError("controller_rows_by_column must be a permutation of 0..old_coordinate_max")
    row_to_edge = {row: column for column, row in enumerate(controller_rows)}

    macro_modulus = require_int(data.get("macro_modulus"), "macro_modulus", 1)
    R = require_int(data.get("R"), "R", 1)
    base_domain_size = require_int(data.get("base_domain_size"), "base_domain_size")
    gamma = float(data.get("gamma"))
    xi = float(data.get("xi"))
    if not (0 < gamma < 1 and 0 < xi < 1):
        raise ValueError("gamma and xi must lie in (0,1)")

    pair_line_bound = math.comb(len(points), 2)
    lines: set[Line] = set()
    axis_pair_count = 0
    for a, b in combinations(points, 2):
        if a[0] == b[0] or a[1] == b[1]:
            axis_pair_count += 1
            continue
        lines.add(normalize_line(a, b))
    if len(lines) > pair_line_bound:
        raise ValueError("distinct nonaxis line count exceeds pair bound")

    movement: dict[int, set[int]] = {label: set() for label in movement_labels}
    refill: dict[int, set[int]] = {label: set() for label in refill_labels}
    line_edge_load_movement: dict[int, int] = {}
    line_edge_load_refill: dict[int, int] = {}

    for line in lines:
        for label in movement_labels:
            x = row_intersection(line, label)
            if x is None or not (0 <= x <= old_max):
                continue
            movement[label].add(x)
            line_edge_load_movement[x] = line_edge_load_movement.get(x, 0) + 1
        for label in refill_labels:
            y = column_intersection(line, label)
            if y is None or not (0 <= y <= old_max):
                continue
            edge = row_to_edge[y]
            refill[label].add(edge)
            line_edge_load_refill[edge] = line_edge_load_refill.get(edge, 0) + 1

    max_movement_label_load = max(map(len, movement.values()), default=0)
    max_refill_label_load = max(map(len, refill.values()), default=0)
    max_movement_edge_load = max(line_edge_load_movement.values(), default=0)
    max_refill_edge_load = max(line_edge_load_refill.values(), default=0)

    line_trace_ok = all(
        value <= len(lines)
        for value in (
            max_movement_label_load,
            max_refill_label_load,
            max_movement_edge_load,
            max_refill_edge_load,
        )
    )
    if not line_trace_ok:
        raise ValueError("one simple line union exceeds the distinct-line degree bound")

    max_domain_loss = 0
    witness: dict[str, Any] | None = None
    for A in movement_labels:
        for B in refill_labels:
            for macro in range(macro_modulus):
                removed = {e for e in movement[A] if e % macro_modulus == macro}
                removed.update(e for e in refill[B] if e % macro_modulus == macro)
                if len(removed) > max_domain_loss:
                    max_domain_loss = len(removed)
                    witness = {
                        "movement_label": A,
                        "refill_label": B,
                        "macro": macro,
                        "controller_edges": sorted(removed),
                    }

    domain_loss_bound = 2 * len(lines)
    if max_domain_loss > domain_loss_bound:
        raise ValueError("paired domain loss exceeds twice the distinct-line count")

    margin_allowance = xi * R
    post_domain_lower_bound = base_domain_size - max_domain_loss
    threshold = gamma * R
    margin_survives = max_domain_loss <= margin_allowance and post_domain_lower_bound >= threshold

    return {
        "selected_state_size": len(points),
        "unordered_pair_bound": pair_line_bound,
        "axis_pair_count": axis_pair_count,
        "distinct_nonaxis_lines": len(lines),
        "movement_candidate_entries": sum(map(len, movement.values())),
        "refill_candidate_entries": sum(map(len, refill.values())),
        "max_movement_label_load": max_movement_label_load,
        "max_refill_label_load": max_refill_label_load,
        "max_movement_controller_load": max_movement_edge_load,
        "max_refill_controller_load": max_refill_edge_load,
        "simple_line_degree_bound": len(lines),
        "max_paired_domain_loss": max_domain_loss,
        "paired_domain_loss_bound": domain_loss_bound,
        "max_domain_loss_state": witness,
        "R": R,
        "base_domain_size": base_domain_size,
        "post_domain_lower_bound": post_domain_lower_bound,
        "allocation_threshold": threshold,
        "margin_allowance": margin_allowance,
        "outcome": "binary_pair_shadow_absorbed" if margin_survives else "explicit_domain_concentration",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        result = analyse(payload)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

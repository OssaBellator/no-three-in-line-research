#!/usr/bin/env python3
"""Check sparse-host preservation versus typed heavy-pencil extraction."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Any, Iterable


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def require_number(value: Any, label: str, minimum: float = 0.0) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label}: expected number")
    result = float(value)
    if not math.isfinite(result) or result < minimum:
        raise ValueError(f"{label}: expected finite number >= {minimum}")
    return result


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def subsets(items: list[int], minimum_size: int) -> Iterable[tuple[int, ...]]:
    for size in range(minimum_size, len(items) + 1):
        yield from itertools.combinations(items, size)


def graph_density(matrix: list[list[int]], left: tuple[int, ...], right: tuple[int, ...]) -> float:
    return sum(matrix[i][j] for i in left for j in right) / (len(left) * len(right))


def superregular_summary(
    matrix: list[list[int]], epsilon: float, delta: float, label: str
) -> dict[str, Any]:
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError(f"{label}: matrix must be nonempty and square")
    degrees = [sum(row) for row in matrix]
    degrees += [sum(matrix[i][j] for i in range(n)) for j in range(n)]
    minimum_degree = min(degrees)
    if minimum_degree + 1e-12 < delta * n:
        raise ValueError(f"{label}: minimum degree below delta*n")
    whole = graph_density(matrix, tuple(range(n)), tuple(range(n)))
    minimum_size = max(1, math.ceil(epsilon * n))
    maximum_discrepancy = 0.0
    checked = 0
    vertices = list(range(n))
    for left in subsets(vertices, minimum_size):
        for right in subsets(vertices, minimum_size):
            discrepancy = abs(graph_density(matrix, left, right) - whole)
            maximum_discrepancy = max(maximum_discrepancy, discrepancy)
            checked += 1
            if discrepancy > epsilon + 1e-12:
                raise ValueError(
                    f"{label}: discrepancy {discrepancy:.6g} exceeds epsilon"
                )
    return {
        "order": n,
        "density": whole,
        "minimum_degree": minimum_degree,
        "maximum_density_discrepancy": maximum_discrepancy,
        "checked_subset_pairs": checked,
    }


def parse_edges(value: Any, n: int, label: str) -> list[tuple[int, int, float]]:
    if not isinstance(value, list):
        raise ValueError(f"{label}: expected list")
    edges: list[tuple[int, int, float]] = []
    seen: set[tuple[int, int]] = set()
    for pos, raw in enumerate(value):
        if not isinstance(raw, list) or len(raw) not in (2, 3):
            raise ValueError(f"{label}[{pos}]: expected [left,right] or [left,right,weight]")
        i = require_int(raw[0], f"{label}[{pos}][0]")
        j = require_int(raw[1], f"{label}[{pos}][1]")
        if i >= n or j >= n:
            raise ValueError(f"{label}[{pos}]: endpoint out of range")
        if (i, j) in seen:
            raise ValueError(f"{label}[{pos}]: duplicate edge")
        seen.add((i, j))
        weight = require_number(raw[2], f"{label}[{pos}][2]") if len(raw) == 3 else 1.0
        edges.append((i, j, weight))
    return edges


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        matrix = payload.get("adjacency")
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise ValueError("adjacency: expected matrix")
        n = len(matrix)
        max_order = require_int(payload.get("max_exhaustive_order", 10), "max_exhaustive_order", 1)
        if n > max_order:
            raise ValueError("adjacency order exceeds max_exhaustive_order")
        if any(len(row) != n or any(x not in (0, 1) for x in row) for row in matrix):
            raise ValueError("adjacency: expected square 0/1 matrix")

        parent_epsilon = require_number(payload.get("parent_epsilon"), "parent_epsilon")
        parent_delta = require_number(payload.get("parent_delta"), "parent_delta")
        residual_epsilon = require_number(payload.get("residual_epsilon"), "residual_epsilon")
        residual_delta = require_number(payload.get("residual_delta"), "residual_delta")
        parent = superregular_summary(matrix, parent_epsilon, parent_delta, "parent")

        cases = payload.get("cases")
        if not isinstance(cases, list) or not cases:
            raise ValueError("cases: expected nonempty list")
        results: list[dict[str, Any]] = []
        seen_outcomes: set[str] = set()
        for pos, case in enumerate(cases):
            if not isinstance(case, dict):
                raise ValueError(f"cases[{pos}]: expected object")
            name = case.get("name")
            if not isinstance(name, str) or not name:
                raise ValueError(f"cases[{pos}].name: expected nonempty string")
            eta = require_number(case.get("eta"), f"cases[{pos}].eta")
            threshold = eta * n
            edges = parse_edges(case.get("heavy_edges"), n, f"cases[{pos}].heavy_edges")
            left_degree = [0] * n
            right_degree = [0] * n
            total_weight = 0.0
            for i, j, weight in edges:
                if matrix[i][j] != 1:
                    raise ValueError(f"cases[{pos}]: heavy edge is absent from parent host")
                left_degree[i] += 1
                right_degree[j] += 1
                total_weight += weight
            max_left = max(left_degree, default=0)
            max_right = max(right_degree, default=0)
            maximum_degree = max(max_left, max_right)

            if maximum_degree <= threshold + 1e-12:
                residual = [row[:] for row in matrix]
                for i, j, _ in edges:
                    residual[i][j] = 0
                residual_summary = superregular_summary(
                    residual, residual_epsilon, residual_delta, f"cases[{pos}].residual"
                )
                outcome = "uniform_superregular_residual"
                entry: dict[str, Any] = {
                    "name": name,
                    "outcome": outcome,
                    "eta_degree_threshold": threshold,
                    "maximum_heavy_degree": maximum_degree,
                    "residual": residual_summary,
                    "common_spread_parameter_class": True,
                }
            else:
                if max_left >= max_right:
                    side = "left"
                    resource = left_degree.index(max_left)
                    pencil_size = max_left
                else:
                    side = "right"
                    resource = right_degree.index(max_right)
                    pencil_size = max_right
                outcome = "typed_heavy_partner_pencil"
                entry = {
                    "name": name,
                    "outcome": outcome,
                    "eta_degree_threshold": threshold,
                    "maximum_heavy_degree": maximum_degree,
                    "pencil_side": side,
                    "pencil_resource": resource,
                    "pencil_size": pencil_size,
                    "total_heavy_weight": total_weight,
                }
            seen_outcomes.add(outcome)
            results.append(entry)

        require_both = payload.get("require_both_outcomes", False)
        if not isinstance(require_both, bool):
            raise ValueError("require_both_outcomes: expected boolean")
        expected = {"uniform_superregular_residual", "typed_heavy_partner_pencil"}
        if require_both and seen_outcomes != expected:
            raise ValueError(f"missing outcomes: {sorted(expected - seen_outcomes)}")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    result = {
        "outcome": "fixed_cell_fan_host_leaf_eliminated",
        "parent": parent,
        "cases": results,
        "seen_outcomes": sorted(seen_outcomes),
        "untyped_host_failure_allowed": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

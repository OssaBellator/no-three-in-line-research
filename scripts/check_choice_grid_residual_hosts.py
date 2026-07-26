#!/usr/bin/env python3
"""Check uniform residual superregularity after fixing choice-grid local pairs."""

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


def all_subsets(items: list[int], minimum_size: int) -> Iterable[tuple[int, ...]]:
    for size in range(minimum_size, len(items) + 1):
        yield from itertools.combinations(items, size)


def density(matrix: list[list[int]], left: tuple[int, ...], right: tuple[int, ...]) -> float:
    edges = sum(matrix[i][j] for i in left for j in right)
    return edges / (len(left) * len(right))


def check_superregular(
    matrix: list[list[int]], epsilon: float, delta: float, label: str
) -> dict[str, Any]:
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError(f"{label}: matrix must be nonempty and square")
    if any(value not in (0, 1) for row in matrix for value in row):
        raise ValueError(f"{label}: matrix entries must be 0 or 1")

    left_degrees = [sum(row) for row in matrix]
    right_degrees = [sum(matrix[i][j] for i in range(n)) for j in range(n)]
    minimum_degree = min(left_degrees + right_degrees)
    if minimum_degree + 1e-12 < delta * n:
        raise ValueError(f"{label}: minimum degree is below delta*n")

    whole = density(matrix, tuple(range(n)), tuple(range(n)))
    minimum_size = max(1, math.ceil(epsilon * n))
    maximum_discrepancy = 0.0
    checked_pairs = 0
    vertices = list(range(n))
    for left in all_subsets(vertices, minimum_size):
        for right in all_subsets(vertices, minimum_size):
            discrepancy = abs(density(matrix, left, right) - whole)
            maximum_discrepancy = max(maximum_discrepancy, discrepancy)
            checked_pairs += 1
            if discrepancy > epsilon + 1e-12:
                raise ValueError(
                    f"{label}: density discrepancy {discrepancy:.6g} exceeds epsilon"
                )

    return {
        "order": n,
        "density": whole,
        "minimum_degree": minimum_degree,
        "minimum_large_subset_size": minimum_size,
        "maximum_density_discrepancy": maximum_discrepancy,
        "checked_subset_pairs": checked_pairs,
    }


def residual_matrix(
    matrix: list[list[int]], state: list[list[int]], label: str
) -> tuple[list[list[int]], list[int], list[int]]:
    if len(state) != 2:
        raise ValueError(f"{label}: expected exactly two selected cells")
    cells: list[tuple[int, int]] = []
    n = len(matrix)
    for pos, cell in enumerate(state):
        if not isinstance(cell, list) or len(cell) != 2:
            raise ValueError(f"{label}[{pos}]: expected [left,right]")
        i = require_int(cell[0], f"{label}[{pos}][0]")
        j = require_int(cell[1], f"{label}[{pos}][1]")
        if i >= n or j >= n:
            raise ValueError(f"{label}[{pos}]: endpoint out of range")
        if matrix[i][j] != 1:
            raise ValueError(f"{label}[{pos}]: selected cell is not an edge")
        cells.append((i, j))
    left_deleted = sorted({i for i, _ in cells})
    right_deleted = sorted({j for _, j in cells})
    if len(left_deleted) != 2 or len(right_deleted) != 2:
        raise ValueError(f"{label}: selected cells are not compatible")
    left_keep = [i for i in range(n) if i not in left_deleted]
    right_keep = [j for j in range(n) if j not in right_deleted]
    residual = [[matrix[i][j] for j in right_keep] for i in left_keep]
    return residual, left_deleted, right_deleted


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        matrix = payload.get("adjacency")
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise ValueError("adjacency: expected square list matrix")

        parent_epsilon = require_number(payload.get("parent_epsilon"), "parent_epsilon")
        parent_delta = require_number(payload.get("parent_delta"), "parent_delta")
        residual_epsilon = require_number(
            payload.get("residual_epsilon"), "residual_epsilon"
        )
        residual_delta = require_number(payload.get("residual_delta"), "residual_delta")
        max_order = require_int(payload.get("max_exhaustive_order", 10), "max_exhaustive_order", 1)
        if len(matrix) > max_order:
            raise ValueError("adjacency order exceeds max_exhaustive_order")

        parent = check_superregular(matrix, parent_epsilon, parent_delta, "parent")
        states = payload.get("states")
        if not isinstance(states, list) or not states:
            raise ValueError("states: expected nonempty list")

        checked_states: list[dict[str, Any]] = []
        for pos, state in enumerate(states):
            if not isinstance(state, list):
                raise ValueError(f"states[{pos}]: expected list")
            residual, left_deleted, right_deleted = residual_matrix(
                matrix, state, f"states[{pos}]"
            )
            summary = check_superregular(
                residual, residual_epsilon, residual_delta, f"states[{pos}].residual"
            )
            summary.update(
                {
                    "left_deleted": left_deleted,
                    "right_deleted": right_deleted,
                }
            )
            checked_states.append(summary)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    result = {
        "outcome": "choice_grid_residual_hosts_uniform",
        "parent": parent,
        "residual_parameter_class": {
            "epsilon": residual_epsilon,
            "delta": residual_delta,
        },
        "state_count": len(checked_states),
        "states": checked_states,
        "residual_host_failure_allowed": False,
        "common_spread_parameter_class": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

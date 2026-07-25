#!/usr/bin/env python3
"""Check the PP3lg--PP3lk rich-line endpoint energy on a finite instance."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

Point = tuple[int, int]
Edge = tuple[int, int]


def parse_point(raw: Any, label: str) -> Point:
    if (
        not isinstance(raw, list)
        or len(raw) != 2
        or isinstance(raw[0], bool)
        or isinstance(raw[1], bool)
        or not isinstance(raw[0], int)
        or not isinstance(raw[1], int)
    ):
        raise ValueError(f"{label}: expected an integer point [x,y]")
    return raw[0], raw[1]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def parse_fraction(raw: Any, label: str) -> Fraction:
    if isinstance(raw, bool):
        raise ValueError(f"{label}: invalid rational")
    try:
        value = Fraction(str(raw))
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"{label}: invalid rational") from exc
    if value <= 0:
        raise ValueError(f"{label}: must be positive")
    return value


def maximum_matching(q: int, edges: set[Edge]) -> tuple[dict[int, int], dict[int, int]]:
    adjacency = [[] for _ in range(q)]
    for left, right in sorted(edges):
        adjacency[left].append(right)
    left_to_right: dict[int, int] = {}
    right_to_left: dict[int, int] = {}

    def augment(left: int, seen: set[int]) -> bool:
        for right in adjacency[left]:
            if right in seen:
                continue
            seen.add(right)
            owner = right_to_left.get(right)
            if owner is None or augment(owner, seen):
                right_to_left[right] = left
                left_to_right[left] = right
                return True
        return False

    for left in range(q):
        augment(left, set())
    return left_to_right, right_to_left


def minimum_cost_assignment(
    q: int, edges: set[Edge], costs: list[list[int]], limit: int
) -> tuple[int, list[int]] | None:
    if q > limit:
        return None
    infinity = 10**30
    dp = [infinity] * (1 << q)
    parent: list[tuple[int, int] | None] = [None] * (1 << q)
    dp[0] = 0
    for mask in range(1 << q):
        left = mask.bit_count()
        if left >= q or dp[mask] == infinity:
            continue
        for right in range(q):
            if mask & (1 << right) or (left, right) not in edges:
                continue
            following = mask | (1 << right)
            value = dp[mask] + costs[left][right]
            if value < dp[following]:
                dp[following] = value
                parent[following] = (mask, right)
    full = (1 << q) - 1
    if dp[full] == infinity:
        return None
    permutation = [0] * q
    mask = full
    for left in range(q - 1, -1, -1):
        previous = parent[mask]
        assert previous is not None
        old_mask, right = previous
        permutation[left] = right
        mask = old_mask
    return dp[full], permutation


def encode_fraction(value: Fraction) -> dict[str, Any]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": str(value),
        "decimal": float(value),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--assignment-limit", type=int, default=18)
    args = parser.parse_args()

    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        x_raw = payload.get("x_coordinates")
        y_raw = payload.get("y_coordinates")
        candidates_raw = payload.get("candidates")
        targets_raw = payload.get("target_cells")
        if not isinstance(x_raw, list) or not isinstance(y_raw, list):
            raise ValueError("x_coordinates and y_coordinates must be lists")
        if len(x_raw) != len(y_raw) or not x_raw:
            raise ValueError("coordinate lists must have the same positive length")
        if any(
            isinstance(value, bool) or not isinstance(value, int)
            for value in x_raw + y_raw
        ):
            raise ValueError("coordinates must be integers")
        if len(set(x_raw)) != len(x_raw) or len(set(y_raw)) != len(y_raw):
            raise ValueError("x_coordinates and y_coordinates must be distinct")
        q = len(x_raw)
        if not isinstance(candidates_raw, list) or len(candidates_raw) != q:
            raise ValueError("candidates must contain q points")
        if not isinstance(targets_raw, list):
            raise ValueError("target_cells must be a list")
        candidates = [
            parse_point(raw, f"candidates[{index}]")
            for index, raw in enumerate(candidates_raw)
        ]
        targets = {
            parse_point(raw, f"target_cells[{index}]")
            for index, raw in enumerate(targets_raw)
        }
        if len(targets) != len(targets_raw):
            raise ValueError("target_cells contains duplicates")

        permitted_raw = payload.get("permitted_edges")
        if permitted_raw is None:
            permitted = {(i, j) for i in range(q) for j in range(q)}
        else:
            if not isinstance(permitted_raw, list):
                raise ValueError("permitted_edges must be a list")
            permitted: set[Edge] = set()
            for index, raw in enumerate(permitted_raw):
                edge = parse_point(raw, f"permitted_edges[{index}]")
                if not (0 <= edge[0] < q and 0 <= edge[1] < q):
                    raise ValueError(f"permitted_edges[{index}] outside [0,q)^2")
                permitted.add(edge)
            if len(permitted) != len(permitted_raw):
                raise ValueError("permitted_edges contains duplicates")

        current_raw = payload.get("current_permutation", list(range(q)))
        if (
            not isinstance(current_raw, list)
            or len(current_raw) != q
            or any(
                isinstance(value, bool) or not isinstance(value, int)
                for value in current_raw
            )
            or set(current_raw) != set(range(q))
        ):
            raise ValueError("current_permutation must be a permutation of [0,q)")
        current = list(current_raw)
        k_value = parse_fraction(payload.get("K", "1"), "K")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    loads: list[list[int]] = []
    for i, x_value in enumerate(x_raw):
        row: list[int] = []
        for y_value in y_raw:
            replacement = (x_value, y_value)
            row.append(
                sum(
                    target != replacement
                    and determinant(candidates[i], replacement, target) == 0
                    for target in targets
                )
            )
        loads.append(row)

    current_load = sum(loads[i][current[i]] for i in range(q))
    permitted_energy = sum(loads[i][j] for i, j in permitted)
    expected_upper = k_value * permitted_energy / q
    matching, _ = maximum_matching(q, permitted)

    minimum = minimum_cost_assignment(q, permitted, loads, args.assignment_limit)
    minimum_object: dict[str, Any] | None
    if minimum is None:
        minimum_object = None
    else:
        minimum_object = {
            "load": minimum[0],
            "permutation": minimum[1],
            "strictly_improves_current": minimum[0] < current_load,
        }

    minimum_current_load = min(loads[i][current[i]] for i in range(q))
    c_ratio = Fraction(minimum_current_load, q)
    alpha = min(Fraction(1), c_ratio / k_value)
    threshold = alpha * q / 2
    rich_edges = {
        (i, j)
        for i, j in permitted
        if Fraction(loads[i][j]) >= threshold
    }
    rich_matching, _ = maximum_matching(q, rich_edges)
    guaranteed_rich_count = (
        Fraction(alpha, 2 - alpha) * q * q if alpha else Fraction(0)
    )
    guaranteed_matching = guaranteed_rich_count / (2 * q)

    output = {
        "q": q,
        "target_cell_count": len(targets),
        "permitted_edge_count": len(permitted),
        "current_permutation": current,
        "current_line_load": current_load,
        "permitted_assignment_energy": permitted_energy,
        "K": encode_fraction(k_value),
        "PP3lh_expected_upper": encode_fraction(expected_upper),
        "PP3lh_strict_improvement_certified": expected_upper < current_load,
        "permitted_perfect_matching_exists": len(matching) == q,
        "one_permitted_matching": [[i, matching[i]] for i in sorted(matching)],
        "exact_minimum_assignment": minimum_object,
        "minimum_current_owner_load": minimum_current_load,
        "c_ratio": encode_fraction(c_ratio),
        "alpha": encode_fraction(alpha),
        "rich_threshold": encode_fraction(threshold),
        "rich_edge_count": len(rich_edges),
        "rich_matching_size": len(rich_matching),
        "PP3lj_guaranteed_rich_edge_count_if_energy_fails": encode_fraction(
            guaranteed_rich_count
        ),
        "PP3lk_guaranteed_matching_size_if_energy_fails": encode_fraction(
            guaranteed_matching
        ),
        "load_matrix": loads,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

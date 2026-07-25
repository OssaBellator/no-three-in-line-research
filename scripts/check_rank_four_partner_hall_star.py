#!/usr/bin/env python3
"""Check robust Hall localization for a rank-four partner-support deletion."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any


Edge = tuple[int, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def require_fraction(value: Any, label: str) -> Fraction:
    if isinstance(value, int) and not isinstance(value, bool):
        return Fraction(value, 1)
    if not isinstance(value, str):
        raise ValueError(f"{label}: expected integer or rational string")
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"{label}: invalid rational") from exc
    return result


def parse_edges(raw: Any, label: str, q: int) -> set[Edge]:
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected list")
    result: set[Edge] = set()
    for pos, item in enumerate(raw):
        if not isinstance(item, list) or len(item) != 2:
            raise ValueError(f"{label}[{pos}]: expected [left,right]")
        left = require_int(item[0], f"{label}[{pos}][0]")
        right = require_int(item[1], f"{label}[{pos}][1]")
        if left >= q or right >= q:
            raise ValueError(f"{label}[{pos}]: endpoint outside [0,q)")
        edge = (left, right)
        if edge in result:
            raise ValueError(f"{label}: duplicate edge {edge}")
        result.add(edge)
    return result


def powerset_of_size_at_least(q: int, threshold: Fraction):
    vertices = range(q)
    for size in range(q + 1):
        if Fraction(size, 1) < threshold:
            continue
        for subset in combinations(vertices, size):
            yield set(subset)


def neighbours(edges: set[Edge], left_set: set[int]) -> set[int]:
    return {right for left, right in edges if left in left_set}


def max_matching(q: int, edges: set[Edge]) -> tuple[int, dict[int, int]]:
    adjacency = {left: [] for left in range(q)}
    for left, right in sorted(edges):
        adjacency[left].append(right)

    match_right: dict[int, int] = {}

    def augment(left: int, seen: set[int]) -> bool:
        for right in adjacency[left]:
            if right in seen:
                continue
            seen.add(right)
            owner = match_right.get(right)
            if owner is None or augment(owner, seen):
                match_right[right] = left
                return True
        return False

    size = 0
    for left in range(q):
        if augment(left, set()):
            size += 1
    return size, match_right


def find_hall_witness(q: int, edges: set[Edge]) -> tuple[set[int], set[int]]:
    for size in range(1, q + 1):
        for subset in combinations(range(q), size):
            left_set = set(subset)
            neighbour_set = neighbours(edges, left_set)
            if len(neighbour_set) < len(left_set):
                return left_set, neighbour_set
    raise ValueError("no Hall witness found despite deficient matching")


def degree_data(q: int, edges: set[Edge]) -> tuple[list[int], list[int]]:
    left = [0] * q
    right = [0] * q
    for u, v in edges:
        left[u] += 1
        right[v] += 1
    return left, right


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        q = require_int(payload.get("q"), "q", minimum=2)
        epsilon = require_fraction(payload.get("epsilon"), "epsilon")
        delta = require_fraction(payload.get("delta"), "delta")
        if not (0 < epsilon < delta < 1):
            raise ValueError("require 0 < epsilon < delta < 1")
        if payload.get("complete_host", False):
            host = {(u, v) for u in range(q) for v in range(q)}
        else:
            host = parse_edges(payload.get("host_edges"), "host_edges", q)
        support = parse_edges(payload.get("support_edges"), "support_edges", q)
        if not support <= host:
            raise ValueError("support_edges must be a subset of the host")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    host_left, host_right = degree_data(q, host)
    min_degree = min(host_left + host_right)
    if Fraction(min_degree, q) < delta:
        raise SystemExit("check failed: host minimum degree is below delta*q")

    threshold = epsilon * q
    alpha = delta - epsilon
    lower_regular_checked_pairs = 0
    left_subsets = list(powerset_of_size_at_least(q, threshold))
    right_subsets = list(powerset_of_size_at_least(q, threshold))
    for x_set in left_subsets:
        for y_set in right_subsets:
            edge_count = sum((u, v) in host for u in x_set for v in y_set)
            if Fraction(edge_count, len(x_set) * len(y_set)) < alpha:
                raise SystemExit(
                    "check failed: lower-regularity inequality fails "
                    f"for |X|={len(x_set)}, |Y|={len(y_set)}"
                )
            lower_regular_checked_pairs += 1

    residual = host - support
    matching_size, _ = max_matching(q, residual)
    support_left, support_right = degree_data(q, support)
    max_support_degree = max(support_left + support_right)

    result: dict[str, Any] = {
        "q": q,
        "epsilon": str(epsilon),
        "delta": str(delta),
        "host_edge_count": len(host),
        "support_edge_count": len(support),
        "residual_edge_count": len(residual),
        "host_min_degree": min_degree,
        "lower_regular_checked_pairs": lower_regular_checked_pairs,
        "max_support_degree": max_support_degree,
        "residual_matching_size": matching_size,
    }

    if matching_size == q:
        result["outcome"] = "support_avoiding_perfect_matching"
    else:
        x_set, n_set = find_hall_witness(q, residual)
        y_set = set(range(q)) - n_set
        missing_rectangle = {
            (u, v) for u in x_set for v in y_set if (u, v) in host
        }
        if not missing_rectangle <= support:
            raise SystemExit("check failed: Hall rectangle is not covered by support")

        linear_bound = epsilon * alpha * q
        if Fraction(max_support_degree, 1) < linear_bound:
            raise SystemExit(
                "check failed: robust Hall linear-degree conclusion violated"
            )

        result.update({
            "outcome": "linear_partner_resource_star",
            "hall_left_set": sorted(x_set),
            "hall_neighbour_set": sorted(n_set),
            "hall_opposite_set": sorted(y_set),
            "hall_deleted_rectangle_edges": len(missing_rectangle),
            "linear_degree_lower_bound": str(linear_bound),
        })

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

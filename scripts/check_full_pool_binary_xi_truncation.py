#!/usr/bin/env python3
"""Check full-pool binary-Xi truncation to fixed-centre support cores."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path
from typing import Any


Path3 = tuple[int, int, int]
Arc = tuple[int, int]
Pattern4 = tuple[Arc, Arc]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def require_number(value: Any, label: str, minimum: float = 0.0) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label}: expected number")
    result = float(value)
    if result < minimum:
        raise ValueError(f"{label}: expected number >= {minimum}")
    return result


def canonical_pattern4(first: Arc, second: Arc) -> Pattern4:
    return tuple(sorted((first, second)))  # type: ignore[return-value]


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")

        n = require_int(payload.get("n"), "n", minimum=6)
        b = require_int(payload.get("block_size"), "block_size", minimum=5)
        if b > n:
            raise ValueError("block_size must be at most n")
        centre = require_int(payload.get("centre"), "centre")
        if centre >= n:
            raise ValueError("centre must lie in [0,n)")

        threshold3 = require_int(
            payload.get("rank3_heavy_threshold"),
            "rank3_heavy_threshold",
            minimum=1,
        )
        threshold4 = require_int(
            payload.get("rank4_heavy_threshold"),
            "rank4_heavy_threshold",
            minimum=1,
        )
        default3 = require_int(
            payload.get("default_rank3_weight"),
            "default_rank3_weight",
            minimum=0,
        )
        default4 = require_int(
            payload.get("default_rank4_weight"),
            "default_rank4_weight",
            minimum=0,
        )
        removal_credit = require_number(
            payload.get("removal_credit"), "removal_credit", minimum=1e-15
        )
        residual = require_number(
            payload.get("residual_objective"), "residual_objective"
        )
        tau = require_number(payload.get("tau"), "tau", minimum=1e-15)
        if tau >= 1:
            raise ValueError("tau must be less than one")

        overrides3: dict[Path3, int] = {}
        raw3 = payload.get("rank3_weight_overrides", [])
        if not isinstance(raw3, list):
            raise ValueError("rank3_weight_overrides: expected list")
        for pos, item in enumerate(raw3):
            if not isinstance(item, list) or len(item) != 4:
                raise ValueError(
                    f"rank3_weight_overrides[{pos}]: expected [u,v,w,weight]"
                )
            u, v, w = (
                require_int(item[k], f"rank3_weight_overrides[{pos}][{k}]")
                for k in range(3)
            )
            weight = require_int(
                item[3], f"rank3_weight_overrides[{pos}][3]", minimum=0
            )
            if max(u, v, w) >= n or len({u, v, w}) != 3:
                raise ValueError(
                    f"rank3_weight_overrides[{pos}]: expected three distinct indices"
                )
            pattern = (u, v, w)
            if pattern in overrides3:
                raise ValueError(
                    f"rank3_weight_overrides: duplicate pattern {pattern}"
                )
            overrides3[pattern] = weight

        overrides4: dict[Pattern4, int] = {}
        raw4 = payload.get("rank4_weight_overrides", [])
        if not isinstance(raw4, list):
            raise ValueError("rank4_weight_overrides: expected list")
        for pos, item in enumerate(raw4):
            if not isinstance(item, list) or len(item) != 5:
                raise ValueError(
                    f"rank4_weight_overrides[{pos}]: expected [i,j,k,l,weight]"
                )
            i, j, k, ell = (
                require_int(item[t], f"rank4_weight_overrides[{pos}][{t}]")
                for t in range(4)
            )
            weight = require_int(
                item[4], f"rank4_weight_overrides[{pos}][4]", minimum=0
            )
            if max(i, j, k, ell) >= n or len({i, j, k, ell}) != 4:
                raise ValueError(
                    f"rank4_weight_overrides[{pos}]: expected four distinct indices"
                )
            pattern = canonical_pattern4((i, j), (k, ell))
            if pattern in overrides4:
                raise ValueError(
                    f"rank4_weight_overrides: duplicate pattern {pattern}"
                )
            overrides4[pattern] = weight
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    allowed3 = tau * removal_credit / (8.0 * b)
    allowed4 = tau * removal_credit / (4.0 * b * b)
    if threshold3 > allowed3 + 1e-12:
        raise SystemExit("check failed: rank3 threshold exceeds tau*R/(8b)")
    if threshold4 > allowed4 + 1e-12:
        raise SystemExit("check failed: rank4 threshold exceeds tau*R/(4b^2)")
    if residual > 1.0 - tau + 1e-12:
        raise SystemExit("check failed: residual_objective exceeds 1-tau")

    paths3 = [
        (u, v, w)
        for u in range(n)
        for v in range(n)
        for w in range(n)
        if len({u, v, w}) == 3
    ]
    arcs = [(i, j) for i in range(n) for j in range(n) if i != j]
    patterns4: list[Pattern4] = []
    seen4: set[Pattern4] = set()
    for first, second in combinations(arcs, 2):
        support = {first[0], first[1], second[0], second[1]}
        if len(support) != 4:
            continue
        pattern = canonical_pattern4(first, second)
        if pattern not in seen4:
            seen4.add(pattern)
            patterns4.append(pattern)

    def weight3(pattern: Path3) -> int:
        return overrides3.get(pattern, default3)

    def weight4(pattern: Pattern4) -> int:
        return overrides4.get(pattern, default4)

    heavy3 = [pattern for pattern in paths3 if weight3(pattern) >= threshold3]
    heavy4 = [
        pattern for pattern in patterns4 if weight4(pattern) >= threshold4
    ]

    incident3 = [pattern for pattern in heavy3 if centre in pattern]
    incident4 = [
        pattern
        for pattern in heavy4
        if centre in {x for arc in pattern for x in arc}
    ]
    nonincident3 = [pattern for pattern in heavy3 if centre not in pattern]
    nonincident4 = [
        pattern
        for pattern in heavy4
        if centre not in {x for arc in pattern for x in arc}
    ]

    expected3 = (
        len(incident3) / ((n - 1) * (n - 2))
        + len(nonincident3)
        * (b - 3)
        / ((n - 1) * (n - 2) * (n - 3))
    )
    expected4 = (
        len(incident4)
        * (b - 3)
        / ((n - 1) * (n - 2) * (n - 3))
        + len(nonincident4)
        * (b - 3)
        * (b - 4)
        / ((n - 1) * (n - 2) * (n - 3) * (n - 4))
    )

    degree3 = [0] * n
    for pattern in heavy3:
        for vertex in pattern:
            degree3[vertex] += 1

    degree4 = [0] * n
    for pattern in heavy4:
        for arc in pattern:
            for vertex in arc:
                degree4[vertex] += 1

    vertex3 = max(range(n), key=lambda v: (degree3[v], -v))
    vertex4 = max(range(n), key=lambda v: (degree4[v], -v))
    delta3 = degree3[vertex3]
    delta4 = degree4[vertex4]

    coefficient3 = (
        1.0 / ((n - 1) * (n - 2))
        + n * (b - 3) / (3.0 * (n - 1) * (n - 2) * (n - 3))
    )
    coefficient4 = (
        (b - 3) / ((n - 1) * (n - 2) * (n - 3))
        + n
        * (b - 3)
        * (b - 4)
        / (4.0 * (n - 1) * (n - 2) * (n - 3) * (n - 4))
    )
    if expected3 > coefficient3 * delta3 + 1e-12:
        raise SystemExit("check failed: rank3 expectation degree bound violated")
    if expected4 > coefficient4 * delta4 + 1e-12:
        raise SystemExit("check failed: rank4 expectation degree bound violated")

    low_fraction = (
        b * threshold3 / removal_credit
        + b * (b - 3) * threshold4 / (2.0 * removal_credit)
    )
    objective = expected3 + expected4 + low_fraction + residual

    if objective < 1.0:
        outcome = "paid_heavy_binary_avoidance"
        selected_rank = None
        selected_vertex = None
        selected_degree = 0
    elif expected3 >= expected4:
        outcome = "rank3_fixed_centre_core"
        selected_rank = 3
        selected_vertex = vertex3
        selected_degree = delta3
    else:
        outcome = "rank4_fixed_centre_core"
        selected_rank = 4
        selected_vertex = vertex4
        selected_degree = delta4

    result = {
        "outcome": outcome,
        "n": n,
        "block_size": b,
        "centre": centre,
        "rank3_heavy_threshold": threshold3,
        "rank4_heavy_threshold": threshold4,
        "rank3_allowed_threshold_upper_bound": allowed3,
        "rank4_allowed_threshold_upper_bound": allowed4,
        "rank3_heavy_pattern_count": len(heavy3),
        "rank4_heavy_pattern_count": len(heavy4),
        "rank3_expected_selected_heavy": expected3,
        "rank4_expected_selected_heavy": expected4,
        "rank3_maximum_vertex_degree": delta3,
        "rank3_maximum_degree_vertex": vertex3,
        "rank4_maximum_vertex_degree": delta4,
        "rank4_maximum_degree_vertex": vertex4,
        "rank3_degree_bound_coefficient": coefficient3,
        "rank4_degree_bound_coefficient": coefficient4,
        "low_binary_fraction_upper_bound": low_fraction,
        "residual_objective": residual,
        "combined_objective": objective,
        "selected_core_rank": selected_rank,
        "selected_core_vertex": selected_vertex,
        "selected_core_degree": selected_degree,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

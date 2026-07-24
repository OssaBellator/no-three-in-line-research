#!/usr/bin/env python3
"""Evaluate deletion-aware type-two one-strip certificate masses.

For each saturated no-three certificate on [m]^2, enumerate every deletion pair
in distinct rows and columns, form the forced boundary-only type-two patch, and
count exact collinear triples in the final configuration. The script also
computes the coarse nonaxis-blocker bound from Proposition PP3d.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def no_three(points: Iterable[Point]) -> bool:
    pts = tuple(points)
    return all(determinant(a, b, c) != 0 for a, b, c in combinations(pts, 3))


def saturated(points: Iterable[Point], n: int) -> bool:
    pts = tuple(points)
    return (
        len(pts) == 2 * n
        and len(set(pts)) == len(pts)
        and all(sum(x == col for x, _ in pts) == 2 for col in range(1, n + 1))
        and all(sum(y == row for _, y in pts) == 2 for row in range(1, n + 1))
    )


def load_cases(path: Path) -> list[tuple[int, tuple[Point, ...]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw_cases = payload if isinstance(payload, list) else [payload]
    cases: list[tuple[int, tuple[Point, ...]]] = []
    for ordinal, raw in enumerate(raw_cases, 1):
        if not isinstance(raw, dict):
            raise ValueError(f"case {ordinal}: expected an object")
        n = raw.get("n")
        raw_points = raw.get("points")
        if isinstance(n, bool) or not isinstance(n, int) or n < 2:
            raise ValueError(f"case {ordinal}: invalid n")
        if not isinstance(raw_points, list):
            raise ValueError(f"case {ordinal}: points must be a list")
        points: list[Point] = []
        for index, raw_point in enumerate(raw_points):
            if not isinstance(raw_point, list) or len(raw_point) != 2:
                raise ValueError(f"case {ordinal}: malformed point {index}")
            x, y = raw_point
            if (
                isinstance(x, bool)
                or isinstance(y, bool)
                or not isinstance(x, int)
                or not isinstance(y, int)
            ):
                raise ValueError(f"case {ordinal}: nonintegral point {index}")
            points.append((x, y))
        if not saturated(points, n) or not no_three(points):
            raise ValueError(f"case {ordinal}: not a saturated no-three certificate")
        cases.append((n, tuple(sorted(points))))
    return cases


def triple_count(points: tuple[Point, ...]) -> int:
    return sum(determinant(a, b, c) == 0 for a, b, c in combinations(points, 3))


def analyze(m: int, core: tuple[Point, ...]) -> dict[str, Any]:
    q = m + 1
    states: list[dict[str, Any]] = []
    histogram: Counter[int] = Counter()

    for first, second in combinations(core, 2):
        if first[0] == second[0] or first[1] == second[1]:
            continue
        deleted = {first, second}
        inserted = {
            (first[0], q),
            (second[0], q),
            (q, first[1]),
            (q, second[1]),
        }
        final = tuple(sorted(point for point in core if point not in deleted) + sorted(inserted))
        assert saturated(final, q)
        defects = triple_count(final)
        histogram[defects] += 1
        states.append(
            {
                "deleted": [list(point) for point in sorted(deleted)],
                "defect_count": defects,
                "points": [list(point) for point in final],
            }
        )

    state_count = len(states)
    total_defects = sum(state["defect_count"] for state in states)
    exact_average = Fraction(total_defects, state_count)

    boundary = [(x, q) for x in range(1, m + 1)] + [(q, y) for y in range(1, m + 1)]
    nonaxis_blocker_incidences = 0
    for z in boundary:
        for first, second in combinations(core, 2):
            if determinant(first, second, z) != 0:
                continue
            axis = (
                z[1] == q and first[0] == second[0] == z[0]
            ) or (
                z[0] == q and first[1] == second[1] == z[1]
            )
            if not axis:
                nonaxis_blocker_incidences += 1

    core_set = set(core)
    occupied_anchor_incidences = 0
    empty_anchor_incidences = 0
    for x in range(1, m + 1):
        for y in range(1, m + 1):
            first = (x, q)
            second = (q, y)
            anchors = sum(determinant(first, second, anchor) == 0 for anchor in core)
            if (x, y) in core_set:
                occupied_anchor_incidences += anchors
            else:
                empty_anchor_incidences += anchors

    K = m * (2 * m - 3)
    coarse = (
        Fraction(2 * nonaxis_blocker_incidences, m)
        + Fraction(
            occupied_anchor_incidences + 4 * empty_anchor_incidences,
            K,
        )
    )
    clean_states = [state for state in states if state["defect_count"] == 0]
    return {
        "source_n": m,
        "target_n": q,
        "state_count": state_count,
        "clean_state_count": len(clean_states),
        "minimum_defect_count": min(state["defect_count"] for state in states),
        "maximum_defect_count": max(state["defect_count"] for state in states),
        "exact_average_defects_fraction": (
            f"{exact_average.numerator}/{exact_average.denominator}"
        ),
        "exact_average_criterion_passes": exact_average < 1,
        "nonaxis_boundary_blocker_incidences": nonaxis_blocker_incidences,
        "occupied_mixed_pair_anchor_incidences": occupied_anchor_incidences,
        "empty_mixed_pair_anchor_incidences": empty_anchor_incidences,
        "coarse_bound_fraction": f"{coarse.numerator}/{coarse.denominator}",
        "coarse_criterion_passes": coarse < 1,
        "defect_histogram": {str(key): histogram[key] for key in sorted(histogram)},
        "clean_states": clean_states,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        cases = load_cases(args.certificate)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc
    if args.n is not None:
        cases = [case for case in cases if case[0] == args.n]
        if not cases:
            raise SystemExit(f"no certificate with n={args.n}")

    results = [analyze(n, points) for n, points in cases]
    payload: Any = results[0] if len(results) == 1 else results
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

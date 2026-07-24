#!/usr/bin/env python3
"""Analyze every boundary-only one-strip extension of certified configurations.

For a saturated configuration on [m]^2, a patch to [m+1]^2 whose inserted
points all lie in the new row or new column has one of exactly two degree forms:

* delete one old point and insert its top/right cells plus the new corner;
* delete two old points in distinct rows and columns and insert the four
  corresponding top/right cells, without the new corner.

The program enumerates these forced candidates and verifies them using exact
integer determinant tests. Input may be one certificate object or a list.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
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


def parse_cases(path: Path) -> list[tuple[int, tuple[Point, ...]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw_cases = payload if isinstance(payload, list) else [payload]
    cases: list[tuple[int, tuple[Point, ...]]] = []
    for ordinal, raw in enumerate(raw_cases, 1):
        if not isinstance(raw, dict):
            raise ValueError(f"case {ordinal}: expected a JSON object")
        n = raw.get("n")
        raw_points = raw.get("points")
        if isinstance(n, bool) or not isinstance(n, int) or n < 2:
            raise ValueError(f"case {ordinal}: n must be an integer at least 2")
        if not isinstance(raw_points, list):
            raise ValueError(f"case {ordinal}: points must be a list")
        points: list[Point] = []
        for index, raw_point in enumerate(raw_points):
            if not isinstance(raw_point, list) or len(raw_point) != 2:
                raise ValueError(f"case {ordinal}: point {index} is malformed")
            x, y = raw_point
            if (
                isinstance(x, bool)
                or isinstance(y, bool)
                or not isinstance(x, int)
                or not isinstance(y, int)
            ):
                raise ValueError(f"case {ordinal}: point {index} is not integral")
            points.append((x, y))
        if not saturated(points, n) or not no_three(points):
            raise ValueError(f"case {ordinal}: input is not a saturated no-three certificate")
        cases.append((n, tuple(sorted(points))))
    return cases


def first_collinear_triple(points: tuple[Point, ...]) -> tuple[Point, Point, Point] | None:
    for triple in combinations(points, 3):
        if determinant(*triple) == 0:
            return triple
    return None


def type_one(core: tuple[Point, ...], m: int, edge: Point) -> tuple[Point, ...]:
    q = m + 1
    x, y = edge
    retained = tuple(point for point in core if point != edge)
    return tuple(sorted(retained + ((x, q), (q, y), (q, q))))


def type_two(core: tuple[Point, ...], m: int, first: Point, second: Point) -> tuple[Point, ...]:
    q = m + 1
    retained = tuple(point for point in core if point not in (first, second))
    added = ((first[0], q), (second[0], q), (q, first[1]), (q, second[1]))
    return tuple(sorted(retained + added))


def analyze(core: tuple[Point, ...], m: int) -> dict[str, Any]:
    valid: list[dict[str, Any]] = []
    type_one_failures: Counter[str] = Counter()
    type_two_failures: Counter[str] = Counter()

    for edge in core:
        points = type_one(core, m, edge)
        assert saturated(points, m + 1)
        bad = first_collinear_triple(points)
        if bad is None:
            valid.append(
                {
                    "type": 1,
                    "deleted": [list(edge)],
                    "points": [list(point) for point in points],
                }
            )
        else:
            type_one_failures[str([list(point) for point in bad])] += 1

    type_two_candidates = 0
    for first, second in combinations(core, 2):
        if first[0] == second[0] or first[1] == second[1]:
            continue
        type_two_candidates += 1
        points = type_two(core, m, first, second)
        assert saturated(points, m + 1)
        bad = first_collinear_triple(points)
        if bad is None:
            valid.append(
                {
                    "type": 2,
                    "deleted": [list(first), list(second)],
                    "points": [list(point) for point in points],
                }
            )
        else:
            type_two_failures[str([list(point) for point in bad])] += 1

    return {
        "source_n": m,
        "target_n": m + 1,
        "type_one_candidates": len(core),
        "type_two_candidates": type_two_candidates,
        "valid_count": len(valid),
        "valid_extensions": valid,
        "type_one_distinct_first_obstructions": len(type_one_failures),
        "type_two_distinct_first_obstructions": len(type_two_failures),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int, help="analyze only this side length from a list")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        cases = parse_cases(args.certificate)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    if args.n is not None:
        cases = [case for case in cases if case[0] == args.n]
        if not cases:
            raise SystemExit(f"no certificate with n={args.n}")

    results = [analyze(core, n) for n, core in cases]
    payload: Any = results[0] if len(results) == 1 else results
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

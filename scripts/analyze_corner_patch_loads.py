#!/usr/bin/env python3
"""Compute exact local loads for a corner-only prime patch.

Given a saturated no-three core on [m]^2 and t>=2, the candidate region is the
new t by t corner. Cells on old-pair secants are unavailable. Among remaining
cells the program counts old-anchor forbidden pairs and internal collinear
triples, then evaluates the pair-aware clone-space local-lemma inequality.

The computation is exhaustive and intended for modest t.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import gcd
from pathlib import Path
from typing import Any, Iterable

Point = tuple[int, int]
Line = tuple[int, int, int]


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


def line_key(a: Point, b: Point) -> Line:
    x1, y1 = a
    x2, y2 = b
    A = y2 - y1
    B = x1 - x2
    C = A * x1 + B * y1
    common = gcd(gcd(abs(A), abs(B)), abs(C))
    if common:
        A, B, C = A // common, B // common, C // common
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def choose2(n: int) -> int:
    return n * (n - 1) // 2


def choose3(n: int) -> int:
    return n * (n - 1) * (n - 2) // 6


def load_case(path: Path, selected_n: int | None) -> tuple[int, tuple[Point, ...]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw_cases = payload if isinstance(payload, list) else [payload]
    parsed: list[tuple[int, tuple[Point, ...]]] = []
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
        parsed.append((n, tuple(sorted(points))))

    if selected_n is not None:
        parsed = [case for case in parsed if case[0] == selected_n]
    if len(parsed) != 1:
        raise ValueError("select exactly one certificate, using --n for a list")
    return parsed[0]


def analyze(core: tuple[Point, ...], m: int, t: int) -> dict[str, Any]:
    boundary = range(m + 1, m + t + 1)
    cells = tuple((x, y) for x in boundary for y in boundary)
    old_pairs = tuple(combinations(core, 2))

    unavailable = {
        cell
        for cell in cells
        if any(determinant(first, second, cell) == 0 for first, second in old_pairs)
    }
    allowed = tuple(cell for cell in cells if cell not in unavailable)

    missing_rows: dict[int, int] = defaultdict(int)
    missing_columns: dict[int, int] = defaultdict(int)
    for x, y in unavailable:
        missing_columns[x] += 1
        missing_rows[y] += 1

    pair_rows: dict[int, int] = defaultdict(int)
    pair_columns: dict[int, int] = defaultdict(int)
    forbidden_pairs = 0
    line_points: dict[Line, set[Point]] = defaultdict(set)

    for first, second in combinations(allowed, 2):
        if first[0] == second[0] or first[1] == second[1]:
            continue
        key = line_key(first, second)
        line_points[key].add(first)
        line_points[key].add(second)
        if any(determinant(first, second, anchor) == 0 for anchor in core):
            forbidden_pairs += 1
            pair_columns[first[0]] += 1
            pair_columns[second[0]] += 1
            pair_rows[first[1]] += 1
            pair_rows[second[1]] += 1

    triple_rows: dict[int, int] = defaultdict(int)
    triple_columns: dict[int, int] = defaultdict(int)
    internal_triples = 0
    for points_on_line in line_points.values():
        count = len(points_on_line)
        if count < 3:
            continue
        internal_triples += choose3(count)
        through_point = choose2(count - 1)
        for x, y in points_on_line:
            triple_columns[x] += through_point
            triple_rows[y] += through_point

    m_star = max([0, *missing_rows.values(), *missing_columns.values()])
    pi_star = max([0, *pair_rows.values(), *pair_columns.values()])
    tau_star = max([0, *triple_rows.values(), *triple_columns.values()])

    N = 2 * t
    load = (
        Fraction(m_star, t)
        + Fraction(1, 2 * t - 1)
        + Fraction(8 * pi_star, N * (N - 1))
        + Fraction(32 * tau_star, N * (N - 1) * (N - 2))
    )

    return {
        "source_n": m,
        "t": t,
        "candidate_cells": len(cells),
        "allowed_cells": len(allowed),
        "unavailable_cells": len(unavailable),
        "forbidden_old_anchor_pairs": forbidden_pairs,
        "internal_candidate_triples": internal_triples,
        "m_star": m_star,
        "pi_star": pi_star,
        "tau_star": tau_star,
        "local_load_fraction": f"{load.numerator}/{load.denominator}",
        "local_load_decimal": float(load),
        "threshold_fraction": "1/24",
        "criterion_passes": load <= Fraction(1, 24),
        "robust_bounds_pass": (
            t >= 100
            and m_star <= t / 100
            and pi_star <= t * t / 400
            and tau_star <= t * t * t / 400
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int, help="select one side length from a certificate list")
    parser.add_argument("--t", type=int, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.t < 2:
        raise SystemExit("t must be at least 2; use analyze_one_strip_extensions.py for t=1")

    try:
        m, core = load_case(args.certificate, args.n)
        result = analyze(core, m, args.t)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

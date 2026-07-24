#!/usr/bin/env python3
"""Verify exact no-three-in-line certificates for finite side lengths.

Input is JSON containing either one object or a list of objects. Each object has

    {"n": 7, "points": [[1, 1], [1, 3], ...]}

Coordinates are one-based. A valid certificate has exactly 2n distinct points,
exactly two in every row and column, and no collinear triple. All geometry is
checked with exact integer determinants.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Any

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    """Twice the signed area of triangle abc."""
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def parse_point(raw: Any, case_label: str, index: int) -> Point:
    if not isinstance(raw, list) or len(raw) != 2:
        raise ValueError(f"{case_label}: point {index} is not a two-entry JSON list")
    x, y = raw
    if isinstance(x, bool) or isinstance(y, bool) or not isinstance(x, int) or not isinstance(y, int):
        raise ValueError(f"{case_label}: point {index} does not have integer coordinates")
    return x, y


def verify_case(raw: Any, ordinal: int) -> tuple[int, list[Point]]:
    if not isinstance(raw, dict):
        raise ValueError(f"case {ordinal}: expected a JSON object")
    n = raw.get("n")
    if isinstance(n, bool) or not isinstance(n, int) or n < 2:
        raise ValueError(f"case {ordinal}: n must be an integer at least 2")
    label = str(raw.get("label", f"n={n}"))
    raw_points = raw.get("points")
    if not isinstance(raw_points, list):
        raise ValueError(f"{label}: points must be a JSON list")
    points = [parse_point(p, label, i) for i, p in enumerate(raw_points)]

    if len(points) != 2 * n:
        raise ValueError(f"{label}: expected {2*n} points, found {len(points)}")
    if len(set(points)) != len(points):
        duplicates = [p for p, count in Counter(points).items() if count > 1]
        raise ValueError(f"{label}: duplicate points {duplicates}")

    outside = [p for p in points if not (1 <= p[0] <= n and 1 <= p[1] <= n)]
    if outside:
        raise ValueError(f"{label}: points outside [1,{n}]^2: {outside}")

    columns = Counter(x for x, _ in points)
    rows = Counter(y for _, y in points)
    bad_columns = {x: columns[x] for x in range(1, n + 1) if columns[x] != 2}
    bad_rows = {y: rows[y] for y in range(1, n + 1) if rows[y] != 2}
    if bad_columns or bad_rows:
        raise ValueError(
            f"{label}: saturation failure; columns={bad_columns or 'ok'}, rows={bad_rows or 'ok'}"
        )

    for a, b, c in combinations(points, 3):
        if determinant(a, b, c) == 0:
            raise ValueError(f"{label}: collinear triple {a}, {b}, {c}")

    return n, points


def load_cases(path: Path) -> list[Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc
    return payload if isinstance(payload, list) else [payload]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path, help="JSON certificate file")
    args = parser.parse_args()

    try:
        cases = load_cases(args.certificate)
        verified = [verify_case(case, i + 1) for i, case in enumerate(cases)]
    except (OSError, ValueError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    for n, points in verified:
        triples = len(points) * (len(points) - 1) * (len(points) - 2) // 6
        print(f"verified n={n}: {len(points)} points, {triples} exact determinant checks")


if __name__ == "__main__":
    main()

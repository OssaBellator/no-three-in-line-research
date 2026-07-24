#!/usr/bin/env python3
"""Exhaustively verify the adjacent-pair width-two rung on bounded coordinates."""
from __future__ import annotations

import argparse
import json
from itertools import combinations
from typing import Iterable

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def no_three(points: Iterable[Point]) -> bool:
    ordered = tuple(points)
    return all(determinant(*triple) != 0 for triple in combinations(ordered, 3))


def adjacent_state(
    columns: tuple[int, ...], rows: tuple[int, ...], old_side: int
) -> tuple[Point, ...]:
    if len(columns) != 4 or len(rows) != 4:
        raise ValueError("exactly four columns and rows are required")
    c1, c2, c3, c4 = sorted(columns)
    y1, y2, y3, y4 = sorted(rows)
    a, b = old_side + 1, old_side + 2
    return (
        (c1, a),
        (c2, a),
        (c3, b),
        (c4, b),
        (a, y1),
        (a, y2),
        (b, y3),
        (b, y4),
    )


def analyze(max_side: int) -> dict[str, object]:
    if max_side < 4:
        raise ValueError("max side must be at least four")
    total_pairs = 0
    cases = []
    for m in range(4, max_side + 1):
        coordinate_sets = tuple(combinations(range(1, m + 1), 4))
        checked = 0
        for columns in coordinate_sets:
            for rows in coordinate_sets:
                checked += 1
                state = adjacent_state(columns, rows, m)
                if not no_three(state):
                    raise AssertionError(
                        f"counterexample at m={m}, columns={columns}, rows={rows}"
                    )
        total_pairs += checked
        cases.append(
            {
                "m": m,
                "four_coordinate_sets": len(coordinate_sets),
                "column_row_pairs_checked": checked,
                "counterexamples": 0,
            }
        )
    return {
        "max_side": max_side,
        "total_pairs_checked": total_pairs,
        "cases": cases,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-side", type=int, default=12)
    args = parser.parse_args()
    try:
        result = analyze(args.max_side)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

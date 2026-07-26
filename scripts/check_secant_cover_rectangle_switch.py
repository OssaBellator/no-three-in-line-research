#!/usr/bin/env python3
"""Check complete secant-cover extraction and the two-by-two cross switch."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path
from typing import Iterable

Point = tuple[int, int]


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def no_three(points: Iterable[Point]) -> bool:
    pts = list(points)
    return len(set(pts)) == len(pts) and all(
        not collinear(a, b, c) for a, b, c in itertools.combinations(pts, 3)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()

    data = json.loads(args.input.read_text())
    q = int(data["q"])
    template = [tuple(point) for point in data["template"]]
    pivot_cell = tuple(data["pivot_cell"])

    assert no_three(template)
    assert len({x for x, _ in template}) == len(template)
    assert len({y for _, y in template}) == len(template)

    rectangle = [(x, y) for x in range(q) for y in range(q)]
    records: dict[Point, tuple[Point, Point]] = {}
    for z in rectangle:
        witnesses = [
            (a, b)
            for a, b in itertools.combinations(template, 2)
            if collinear(a, b, z)
        ]
        assert witnesses, f"uncovered endpoint cell {z}"
        records[z] = witnesses[0]

    degree = Counter(point for pair in records.values() for point in pair)
    centre, centre_degree = max(degree.items(), key=lambda item: item[1])

    assert pivot_cell in records
    pair = records[pivot_cell]
    assert centre in pair
    partner = pair[0] if pair[1] == centre else pair[1]
    assert collinear(centre, partner, pivot_cell)

    a = centre
    z = pivot_cell
    cross = ((a[0], z[1]), (z[0], a[1]))

    state0_columns = sorted([a[0], z[0]])
    state0_rows = sorted([a[1], z[1]])
    state1_columns = sorted([cross[0][0], cross[1][0]])
    state1_rows = sorted([cross[0][1], cross[1][1]])
    assert state0_columns == state1_columns
    assert state0_rows == state1_rows
    assert a not in cross and z not in cross

    print("endpoint side", q)
    print("template size", len(template))
    print("covered endpoint cells", len(records))
    print("template resource degrees", sorted(degree.values(), reverse=True))
    print("fixed centre", list(centre))
    print("fixed-centre degree", centre_degree)
    print("pivot covered cell", list(z))
    print("pivot partner", list(partner))
    print("state-zero diagonal", [list(a), list(z)])
    print("state-one cross diagonal", [list(cross[0]), list(cross[1])])
    print("same column resources", state0_columns == state1_columns)
    print("same row resources", state0_rows == state1_rows)
    print("target triple omitted", a not in cross and z not in cross)
    print("outcome secant_cover_rectangle_switch")


if __name__ == "__main__":
    main()

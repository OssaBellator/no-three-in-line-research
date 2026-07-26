#!/usr/bin/env python3
"""Check the old-grid endpoint-shadow potential and exact trade identity."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Iterable, Sequence

Point = tuple[int, int]


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def source_from_layers(layers: Sequence[Sequence[int]]) -> set[Point]:
    return {(column, row) for layer in layers for column, row in enumerate(layer)}


def no_three(points: Iterable[Point]) -> bool:
    pts = list(points)
    return len(set(pts)) == len(pts) and all(
        not collinear(a, b, c) for a, b, c in itertools.combinations(pts, 3)
    )


def blocker_count(source: set[Point], z: Point) -> int:
    others = sorted(source - {z})
    return sum(collinear(a, b, z) for a, b in itertools.combinations(others, 2))


def endpoint_potential(source: set[Point], n: int) -> int:
    return sum(
        blocker_count(source, (x, y)) - 2 * ((x, y) not in source)
        for x in range(n)
        for y in range(n)
    )


def pair_weight(a: Point, b: Point, n: int) -> int:
    return sum(
        collinear(a, b, (x, y))
        for x in range(n)
        for y in range(n)
        if (x, y) not in {a, b}
    )


def trade_terms(before: set[Point], after: set[Point], n: int) -> tuple[int, int]:
    removed = before - after
    inserted = after - before
    unchanged = before & after

    removal = sum(pair_weight(d, p, n) for d in removed for p in unchanged)
    removal += sum(pair_weight(d, e, n) for d, e in itertools.combinations(removed, 2))

    insertion = sum(pair_weight(a, p, n) for a in inserted for p in unchanged)
    insertion += sum(pair_weight(a, b, n) for a, b in itertools.combinations(inserted, 2))
    return removal, insertion


def positive_cells(source: set[Point], n: int) -> list[tuple[list[int], int]]:
    result: list[tuple[list[int], int]] = []
    for x in range(n):
        for y in range(n):
            z = (x, y)
            excess = blocker_count(source, z) - 2 * (z not in source)
            if excess > 0:
                result.append(([x, y], excess))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()

    data = json.loads(args.input.read_text())
    n = int(data["n"])
    before = source_from_layers([data["selected_layer"], data["opposite_layer"]])
    after = source_from_layers([data["replacement_layer"], data["opposite_layer"]])

    assert no_three(before), "initial source is not no-three"
    assert no_three(after), "replacement source is not no-three"
    assert len(before) == len(after) == 2 * n

    initial = endpoint_potential(before, n)
    final = endpoint_potential(after, n)
    removal, insertion = trade_terms(before, after, n)
    assert final - initial == insertion - removal

    positives = positive_cells(before, n)
    print("grid side", n)
    print("initial source size", len(before))
    print("final source size", len(after))
    print("initial endpoint potential", initial)
    print("final endpoint potential", final)
    print("positive old-grid cells", len(positives))
    print("positive-cell multiplicity", sum(weight for _, weight in positives))
    print("removed source points", len(before - after))
    print("inserted source points", len(after - before))
    print("removal term", removal)
    print("insertion term", insertion)
    print("exact potential change", final - initial)
    print("identity insertion-minus-removal", insertion - removal)
    print("outcome old_grid_endpoint_shadow_potential")


if __name__ == "__main__":
    main()

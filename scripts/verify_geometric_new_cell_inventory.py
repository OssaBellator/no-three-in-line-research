#!/usr/bin/env python3
"""Finite checks for GC2b and GC3e--GC3f."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from math import gcd

Point = tuple[int, int]


def primitive_height(a: Point, b: Point) -> int:
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    divisor = gcd(abs(dx), abs(dy))
    if divisor == 0:
        return 0
    return max(abs(dx) // divisor, abs(dy) // divisor)


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (
        b[1] - a[1]
    ) * (c[0] - a[0])


def pair_shadow(anchor: Point, cells: set[Point], height: int) -> int:
    return sum(
        1
        for first, second in combinations(cells, 2)
        if collinear(anchor, first, second)
        and primitive_height(anchor, first) >= height
    )


def cross_shadow(
    anchor: Point, old: set[Point], new: set[Point], height: int
) -> int:
    return sum(
        1
        for first in old
        for second in new
        if collinear(anchor, first, second)
        and primitive_height(anchor, second) >= height
    )


def verify_line_length(counts: Counter[str]) -> None:
    for size in range(2, 8):
        points = [(row, column) for row in range(size) for column in range(size)]
        for anchor in points:
            for other in points:
                if anchor == other:
                    continue
                height = primitive_height(anchor, other)
                line = [point for point in points if collinear(anchor, other, point)]
                ceiling = 1 + (size - 1) // height
                assert len(line) <= ceiling
                counts["line-length checks"] += 1


def verify_new_cell_bounds(counts: Counter[str]) -> None:
    for size in range(2, 4):
        points = [(row, column) for row in range(size) for column in range(size)]
        for anchor in points:
            available = [point for point in points if point != anchor]
            for height in range(1, size + 1):
                line_ceiling = 1 + (size - 1) // height
                residual = max(0, line_ceiling - 2)
                # Label every nonanchor cell as old, new or absent.
                for labels in product((0, 1, 2), repeat=len(available)):
                    old = {
                        point
                        for point, label in zip(available, labels, strict=True)
                        if label == 1
                    }
                    new = {
                        point
                        for point, label in zip(available, labels, strict=True)
                        if label == 2
                    }

                    cross = cross_shadow(anchor, old, new, height)
                    internal = pair_shadow(anchor, new, height)
                    increment = pair_shadow(anchor, old | new, height) - pair_shadow(
                        anchor, old, height
                    )

                    assert increment == cross + internal
                    assert cross <= len(new) * residual
                    assert 2 * internal <= len(new) * residual
                    assert 2 * increment <= 3 * len(new) * residual

                    # Any k new rectangle assignments contribute at most 2k cells.
                    assignment_count = (len(new) + 1) // 2
                    assert increment <= 3 * assignment_count * residual
                    counts["old/new inventories"] += 1


def verify_margin_and_crossing_bounds(counts: Counter[str]) -> None:
    for anchor_count in range(1, 13):
        for assignment_count in range(0, 8):
            for residual in range(0, 7):
                per_anchor = 3 * assignment_count * residual
                total = anchor_count * per_anchor
                for margin in range(1, 10):
                    crossings = total // (margin + 1)
                    assert crossings * (margin + 1) <= total
                    assert crossings < total / margin if total else crossings == 0
                    counts["margin budgets"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_line_length(counts)
    verify_new_cell_bounds(counts)
    verify_margin_and_crossing_bounds(counts)

    print("GC2b and GC3e--GC3f new-cell inventory audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the direction-stratified rectangle conflict bounds PX70--PX73."""
from __future__ import annotations

from itertools import product
from math import gcd
import random

Point = tuple[int, int]
Edge = tuple[int, int, int, int]
ORIENTATIONS = ("cc", "cf", "fc", "ff")


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def compatible(first: Edge, second: Edge) -> bool:
    return all(a != b for a, b in zip(first, second))


def flatten(n: int, coarse: int, fine: int, mode: str) -> int:
    return n * coarse + fine if mode == "c" else 2 * fine + coarse


def corners(n: int, edge: Edge, orientation: str) -> tuple[Point, ...]:
    u, p, t, r = edge
    return (
        (flatten(n, 0, u, orientation[0]), flatten(n, 0, t, orientation[1])),
        (flatten(n, 0, u, orientation[0]), flatten(n, 1, r, orientation[1])),
        (flatten(n, 1, p, orientation[0]), flatten(n, 0, t, orientation[1])),
        (flatten(n, 1, p, orientation[0]), flatten(n, 1, r, orientation[1])),
    )


def primitive_height(first: Point, second: Point) -> int:
    dx = second[0] - first[0]
    dy = second[1] - first[1]
    divisor = gcd(abs(dx), abs(dy))
    assert divisor > 0
    return max(abs(dx) // divisor, abs(dy) // divisor)


def pair_height(n: int, first: Edge, second: Edge, orientation: str) -> int:
    return min(
        primitive_height(a, b)
        for a in corners(n, first, orientation)
        for b in corners(n, second, orientation)
    )


def transversal_conflict(
    n: int,
    first: Edge,
    second: Edge,
    third: Edge,
    orientation: str,
) -> bool:
    return any(
        determinant(a, b, c) == 0
        for a in corners(n, first, orientation)
        for b in corners(n, second, orientation)
        for c in corners(n, third, orientation)
    )


def completion_count(n: int, first: Edge, second: Edge, orientation: str) -> int:
    return sum(
        compatible(first, third)
        and compatible(second, third)
        and transversal_conflict(n, first, second, third, orientation)
        for third in product(range(n), repeat=4)
    )


def verify_line_intersections() -> None:
    for n in range(2, 9):
        side = 2 * n
        grid = tuple((x, y) for x in range(side) for y in range(side))
        for first_index, first in enumerate(grid):
            for second in grid[first_index + 1 :]:
                height = primitive_height(first, second)
                line = [point for point in grid if determinant(first, second, point) == 0]
                assert len(line) <= 1 + (2 * n - 1) // height + 1
    print("PX70 line-intersection bound checked through base eight")


def verify_canonical_lower_bound() -> None:
    expected_exact_cc = {3: 1, 4: 14, 5: 63, 6: 172, 7: 365}
    for n in range(3, 8):
        first = (0, 0, 0, 0)
        second = (1, 1, 1, 1)
        family = tuple(
            (w, p, w, r)
            for w in range(2, n)
            for p in range(2, n)
            for r in range(2, n)
        )
        assert len(family) == (n - 2) ** 3
        for orientation in ORIENTATIONS:
            first_corner = corners(n, first, orientation)[0]
            second_corner = corners(n, second, orientation)[0]
            assert all(
                compatible(first, third)
                and compatible(second, third)
                and determinant(
                    first_corner,
                    second_corner,
                    corners(n, third, orientation)[0],
                )
                == 0
                for third in family
            )
        exact = completion_count(n, first, second, "cc")
        assert exact == expected_exact_cc[n]
        assert exact >= (n - 2) ** 3
        print(
            f"n={n}: canonical family={(n - 2) ** 3}, exact cc completions={exact}"
        )


def verify_completion_upper_bound() -> None:
    rng = random.Random(20260725)
    for n in range(3, 7):
        edges = tuple(product(range(n), repeat=4))
        for orientation in ORIENTATIONS:
            for _ in range(80):
                while True:
                    first = rng.choice(edges)
                    second = rng.choice(edges)
                    if compatible(first, second):
                        break
                height = pair_height(n, first, second, orientation)
                exact = completion_count(n, first, second, orientation)
                bound = 64 * n * n * (1 + 2 * n / height)
                assert exact <= bound, (
                    n,
                    orientation,
                    first,
                    second,
                    height,
                    exact,
                    bound,
                )
            print(f"PX71 sampled completion bound: n={n}, orientation={orientation}")


def verify_low_height_partner_bound() -> None:
    rng = random.Random(1451)
    for n in range(3, 7):
        edges = tuple(product(range(n), repeat=4))
        for orientation in ORIENTATIONS:
            for cutoff in range(2, min(n + 1, 5)):
                first = rng.choice(edges)
                exact = sum(
                    compatible(first, second)
                    and pair_height(n, first, second, orientation) < cutoff
                    for second in edges
                )
                bound = 256 * cutoff * n**3
                assert exact <= bound
            print(f"PX73 low-height partner bound: n={n}, orientation={orientation}")


def main() -> None:
    verify_line_intersections()
    verify_canonical_lower_bound()
    verify_completion_upper_bound()
    verify_low_height_partner_bound()
    print("direction-stratified conflict bounds verified")


if __name__ == "__main__":
    main()

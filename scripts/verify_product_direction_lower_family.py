#!/usr/bin/env python3
"""Verify PX174--PX175 explicit low-direction completion families."""
from __future__ import annotations

from itertools import product
from math import gcd

Point = tuple[int, int]
Edge = tuple[int, int, int, int]
ORIENTATIONS = ("cc", "cf", "fc", "ff")


def flatten(n: int, coarse: int, fine: int, mode: str) -> int:
    return n * coarse + fine if mode == "c" else 2 * fine + coarse


def corners(n: int, item: Edge, orientation: str) -> tuple[Point, ...]:
    u, p, t, r = item
    return (
        (flatten(n, 0, u, orientation[0]), flatten(n, 0, t, orientation[1])),
        (flatten(n, 0, u, orientation[0]), flatten(n, 1, r, orientation[1])),
        (flatten(n, 1, p, orientation[0]), flatten(n, 0, t, orientation[1])),
        (flatten(n, 1, p, orientation[0]), flatten(n, 1, r, orientation[1])),
    )


def determinant(first: Point, second: Point, third: Point) -> int:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        - (second[1] - first[1]) * (third[0] - first[0])
    )


def compatible(first: Edge, second: Edge) -> bool:
    return all(left != right for left, right in zip(first, second))


def primitive_direction(first: Point, second: Point) -> tuple[int, int]:
    dx = second[0] - first[0]
    dy = second[1] - first[1]
    divisor = gcd(abs(dx), abs(dy))
    dx //= divisor
    dy //= divisor
    if dx < 0 or (dx == 0 and dy < 0):
        dx, dy = -dx, -dy
    return dx, dy


def explicit_family(n: int, a: int, b: int) -> tuple[Edge, Edge, tuple[Edge, ...]]:
    height = max(a, b)
    first = (0, 0, 0, 0)
    second = (a, 1, b, 1)
    maximum_multiplier = (n - 1) // height
    family = tuple(
        (multiplier * a, p, multiplier * b, r)
        for multiplier in range(2, maximum_multiplier + 1)
        for p in range(2, n)
        for r in range(2, n)
    )
    return first, second, family


def verify_prime_side(n: int) -> None:
    for a in range(1, n):
        for b in range(1, n):
            if gcd(a, b) != 1 or 2 * max(a, b) > n - 1:
                continue
            first, second, family = explicit_family(n, a, b)
            expected = (((n - 1) // max(a, b)) - 1) * (n - 2) ** 2
            assert len(family) == expected
            assert compatible(first, second)
            assert all(
                compatible(first, third) and compatible(second, third)
                for third in family
            )

            for orientation in ORIENTATIONS:
                first_corner = corners(n, first, orientation)[0]
                second_corner = corners(n, second, orientation)[0]
                direction = primitive_direction(first_corner, second_corner)
                scale_x = 1 if orientation[0] == "c" else 2
                scale_y = 1 if orientation[1] == "c" else 2
                divisor = gcd(scale_x * a, scale_y * b)
                assert direction == (
                    scale_x * a // divisor,
                    scale_y * b // divisor,
                )
                assert all(
                    determinant(
                        first_corner,
                        second_corner,
                        corners(n, third, orientation)[0],
                    )
                    == 0
                    for third in family
                )

    print(f"n={n}: explicit primitive-direction families verified")


def verify_direction_count(cutoff: int) -> None:
    primitive = sum(
        gcd(a, b) == 1
        for a in range(1, cutoff + 1)
        for b in range(1, cutoff + 1)
    )
    # A crude elementary lower bound sufficient for the asymptotic theorem:
    # pairs with a odd and b even are coprime often enough in the tested range.
    assert primitive >= cutoff * cutoff // 4
    print(f"H={cutoff}: primitive positive directions={primitive}")


def main() -> None:
    for n in range(5, 16):
        verify_prime_side(n)
    for cutoff in (4, 8, 16, 32, 64):
        verify_direction_count(cutoff)
    print("PX174--PX175 low-direction lower families verified")


if __name__ == "__main__":
    main()

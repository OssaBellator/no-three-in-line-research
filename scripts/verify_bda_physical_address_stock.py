#!/usr/bin/env python3
"""Finite checks for BDA5av--BDA5ay.

The program verifies the physical direction normalization, determinant ceiling,
reduced-denominator ceiling, and ambient profile-count inequalities for small
boards. It is a regression check, not a proof for arbitrary n.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd


def normalize(dx: int, dy: int) -> tuple[int, int]:
    if dx == 0 and dy == 0:
        raise ValueError("zero direction")
    g = gcd(abs(dx), abs(dy))
    x, y = dx // g, dy // g
    if x < 0 or (x == 0 and y < 0):
        x, y = -x, -y
    return x, y


def directions(n: int) -> set[tuple[int, int]]:
    out: set[tuple[int, int]] = set()
    for x1 in range(n):
        for y1 in range(n):
            for x2 in range(n):
                for y2 in range(n):
                    if (x1, y1) != (x2, y2):
                        out.add(normalize(x2 - x1, y2 - y1))
    return out


def det(u: tuple[int, int], v: tuple[int, int]) -> int:
    return u[0] * v[1] - u[1] * v[0]


def check(n: int) -> None:
    m = n - 1
    dirs = directions(n)
    ambient = m * (2 * m + 1) + 1
    assert len(dirs) <= ambient
    assert all((x == 0 and y == 1) or (1 <= x <= m and abs(y) <= m) for x, y in dirs)

    determinants = {det(u, v) for u in dirs for v in dirs}
    assert all(abs(value) <= 2 * m * m for value in determinants)

    nonzero = [value for value in determinants if value]
    q_det = 2 * m * m
    denominators: set[int] = set()
    for numerator in nonzero:
        for denominator in nonzero:
            value = Fraction(numerator, denominator)
            denominators.add(value.denominator)
            assert value.denominator <= q_det
            assert abs(value.numerator) <= q_det

    exact_profile_count = len(dirs) ** 2 * sum(range(2, q_det + 1))
    ambient_profile_count = ambient**2 * q_det * (q_det + 1) // 2
    assert exact_profile_count <= ambient_profile_count

    print(
        f"n={n}: directions={len(dirs)}, determinants={len(determinants)}, "
        f"reduced_denominators={len(denominators)}, Q_det={q_det}"
    )


def main() -> None:
    for n in range(2, 9):
        check(n)
    print("BDA physical address-stock checks passed")


if __name__ == "__main__":
    main()

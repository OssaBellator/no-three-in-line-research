#!/usr/bin/env python3
"""Verify CMR38--CMR39 on finite completed-reciprocal instances."""
from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import combinations
from math import gcd, isqrt, sqrt

Point = tuple[int, int]


def valuation(value: int, p: int) -> int:
    out = 0
    while value % p == 0:
        value //= p
        out += 1
    return out


def completed_reciprocal(p: int, k: int) -> list[Point]:
    n = p**k
    points: list[Point] = []
    for x in range(n):
        if x == 0:
            y = 0
        else:
            r = valuation(x, p)
            modulus = p ** (k - r)
            unit = x // (p**r)
            y = p**r * pow(unit, -1, modulus)
        points.append((x, y))
    return points


def line_key(a: Point, b: Point) -> tuple[int, int, int]:
    x1, y1 = a
    x2, y2 = b
    A = y2 - y1
    B = x1 - x2
    C = A * x1 + B * y1
    common = gcd(gcd(abs(A), abs(B)), abs(C))
    if common:
        A //= common
        B //= common
        C //= common
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def direction_height(a: Point, b: Point) -> int:
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    common = gcd(abs(dx), abs(dy))
    return max(abs(dx), abs(dy)) // common


def verify_instance(p: int, k: int) -> tuple[int, float, float, int, float]:
    points = completed_reciprocal(p, k)
    n = len(points)
    energy = 0.0
    lines: dict[tuple[int, int, int], set[Point]] = defaultdict(set)
    for first, second in combinations(points, 2):
        energy += 1.0 / direction_height(first, second)
        lines[line_key(first, second)].update((first, second))

    triples = sum(
        len(points_on_line)
        * (len(points_on_line) - 1)
        * (len(points_on_line) - 2)
        // 6
        for points_on_line in lines.values()
    )

    cutoff = max(1, isqrt(n))
    harmonic = sum(1.0 / height for height in range(1, cutoff + 1))
    energy_bound = (
        2 * n * (2 * k + 1) * cutoff
        + 4 * n * sqrt(n) * harmonic
        + (n * (n - 1) / 2) / cutoff
    )
    syndrome_bound = (
        (2 * k / 3) * (n * (n - 1) / 2)
        + (2 * sqrt(n) / 3) * energy_bound
    )

    assert energy <= energy_bound + 1e-9, (p, k, energy, energy_bound)
    assert triples <= syndrome_bound + 1e-9, (p, k, triples, syndrome_bound)
    return n, energy, energy_bound, triples, syndrome_bound


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=243)
    args = parser.parse_args()

    instances = 0
    for p in (3, 5, 7):
        k = 2
        while p**k <= args.max_modulus:
            n, energy, energy_bound, triples, syndrome_bound = verify_instance(p, k)
            print(
                f"N={n}: energy={energy:.6f}/{energy_bound:.3f}; "
                f"triples={triples}/{syndrome_bound:.3f}"
            )
            instances += 1
            k += 1
    print(f"verified global-energy instances={instances}")


if __name__ == "__main__":
    main()

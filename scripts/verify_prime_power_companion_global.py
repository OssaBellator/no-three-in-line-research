#!/usr/bin/env python3
"""Verify CMR40--CMR42 on finite odd-prime companion hosts."""
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


def completed_reciprocal(p: int, k: int) -> list[int]:
    n = p**k
    values: list[int] = []
    for x in range(n):
        if x == 0:
            y = 0
        else:
            r = valuation(x, p)
            modulus = p ** (k - r)
            unit = x // (p**r)
            y = p**r * pow(unit, -1, modulus)
        values.append(y)
    return values


def companion(y: int, p: int, n: int) -> int:
    return ((1 + p) * y + 1) % n


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
    n = p**k
    first_values = completed_reciprocal(p, k)
    points: list[Point] = (
        [(x, first_values[x]) for x in range(n)]
        + [(x, companion(first_values[x], p, n)) for x in range(n)]
    )
    assert len(set(points)) == 2 * n

    lines: dict[tuple[int, int, int], set[Point]] = defaultdict(set)
    energy = 0.0
    for first, second in combinations(points, 2):
        lines[line_key(first, second)].update((first, second))
        energy += 1.0 / direction_height(first, second)

    A0 = (p + 2) * (2 * k + 2)
    B0 = 2 * ((p + 1) ** 2 + 1) * sqrt(n)
    for line, occupants in lines.items():
        A, B, _ = line
        height = max(abs(A), abs(B))
        assert len(occupants) <= A0 + B0 / height + 1e-9, (
            p,
            k,
            line,
            len(occupants),
            A0 + B0 / height,
        )

    cutoff = max(1, isqrt(n))
    harmonic = sum(1.0 / height for height in range(1, cutoff + 1))
    energy_bound = (
        4 * n * (A0 - 1) * cutoff
        + 4 * n * B0 * harmonic
        + ((2 * n) * (2 * n - 1) / 2) / cutoff
    )
    assert energy <= energy_bound + 1e-9, (p, k, energy, energy_bound)

    triples = sum(
        len(occupants) * (len(occupants) - 1) * (len(occupants) - 2) // 6
        for occupants in lines.values()
    )
    syndrome_bound = (
        ((A0 - 2) / 3) * ((2 * n) * (2 * n - 1) / 2)
        + (B0 / 3) * energy_bound
    )
    assert triples <= syndrome_bound + 1e-9, (p, k, triples, syndrome_bound)
    return n, energy, energy_bound, triples, syndrome_bound


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=125)
    args = parser.parse_args()

    instances = 0
    for p in (3, 5, 7):
        k = 2
        while p**k <= args.max_modulus:
            n, energy, energy_bound, triples, syndrome_bound = verify_instance(p, k)
            print(
                f"N={n}: union-energy={energy:.6f}/{energy_bound:.3f}; "
                f"union-triples={triples}/{syndrome_bound:.3f}"
            )
            instances += 1
            k += 1
    print(f"verified companion-global instances={instances}")


if __name__ == "__main__":
    main()

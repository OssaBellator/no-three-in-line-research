#!/usr/bin/env python3
"""Compute harmonic direction energy and verify CMR32."""
from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import combinations
from math import gcd, log, sqrt


def valuation(value: int, p: int) -> int:
    out = 0
    while value % p == 0:
        value //= p
        out += 1
    return out


def completed_reciprocal(p: int, k: int):
    n = p**k
    points = []
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


def line_key(a, b):
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


def direction_height(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    common = gcd(abs(dx), abs(dy))
    return max(abs(dx) // common, abs(dy) // common)


def verify_instance(p: int, k: int):
    points = completed_reciprocal(p, k)
    n = len(points)
    lines = defaultdict(set)
    energy = 0.0
    for a, b in combinations(points, 2):
        lines[line_key(a, b)].update((a, b))
        energy += 1.0 / direction_height(a, b)

    triples = 0
    for occupants in lines.values():
        s = len(occupants)
        triples += s * (s - 1) * (s - 2) // 6

    bound = (2 * k / 3) * (n * (n - 1) / 2) + (2 * sqrt(n) / 3) * energy
    assert triples <= bound + 1e-9, (p, k, triples, bound)
    return n, energy, triples, bound


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=243)
    args = parser.parse_args()

    instances = 0
    for p in (3, 5, 7):
        k = 2
        while p**k <= args.max_modulus:
            n, energy, triples, bound = verify_instance(p, k)
            print(
                f"N={n}: energy={energy:.6f}; energy/N={energy/n:.6f}; "
                f"energy/(N log N)={energy/(n*log(n)):.6f}; "
                f"triples={triples}; bound={bound:.3f}"
            )
            instances += 1
            k += 1
    print(f"verified harmonic-energy instances={instances}")


if __name__ == "__main__":
    main()

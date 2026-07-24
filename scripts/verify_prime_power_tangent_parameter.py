#!/usr/bin/env python3
"""Verify CMR30 for uniform completed reciprocals on small odd prime powers."""
from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import combinations
from math import gcd


def valuation(value: int, p: int) -> int:
    value = abs(value)
    out = 0
    while value % p == 0:
        value //= p
        out += 1
    return out


def determinant(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])


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


def tangent_bound(A: int, B: int, C: int, p: int, k: int) -> int:
    h = valuation(C, p)
    m = k - h
    modulus = p**m
    reduced = C // (p**h)
    delta = (reduced * reduced - 4 * A * B) % modulus
    height = max(abs(A), abs(B))
    if delta == 0:
        spacing = p ** ((m + 1) // 2)
        return 1 + (modulus - 1) // (height * spacing)
    nu = valuation(delta, p)
    if nu % 2:
        return 0
    t = nu // 2
    unit = delta // (p ** (2 * t))
    if pow(unit % p, (p - 1) // 2, p) != 1:
        return 0
    spacing = p ** (m - t)
    return 2 * (1 + (modulus - 1) // (height * spacing))


def verify_instance(p: int, k: int) -> int:
    points = completed_reciprocal(p, k)
    lines = defaultdict(set)
    for a, b in combinations(points, 2):
        key = line_key(a, b)
        lines[key].add(a)
        lines[key].add(b)

    checks = 0
    for (A, B, C), occupants in lines.items():
        if C == 0:
            continue
        h = valuation(C, p)
        if h >= k or A % p == 0 or B % p == 0:
            continue
        top = [
            point for point in occupants
            if point[0] != 0 and valuation(point[0], p) == h
        ]
        bound = tangent_bound(A, B, C, p, k)
        assert len(top) <= bound, (p, k, (A, B, C), len(top), bound)
        checks += 1
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=243)
    args = parser.parse_args()

    instances = 0
    checks = 0
    for p in (3, 5, 7):
        k = 2
        while p**k <= args.max_modulus:
            checks += verify_instance(p, k)
            instances += 1
            k += 1
    print(f"verified tangent parameter instances={instances}; cells={checks}")


if __name__ == "__main__":
    main()

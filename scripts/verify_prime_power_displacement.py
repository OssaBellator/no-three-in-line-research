#!/usr/bin/env python3
"""Verify completed-reciprocal displacement and syndrome claims.

This script checks Theorems CMR6--CMR8 and prints exact finite data for the
uniform parameter choice c_r=1.  It uses exact integer arithmetic only.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import combinations
from math import comb, gcd

Point = tuple[int, int]


def valuation(value: int, p: int) -> int:
    if value == 0:
        raise ValueError("zero valuation is handled separately")
    value = abs(value)
    result = 0
    while value % p == 0:
        value //= p
        result += 1
    return result


def completed_reciprocal(p: int, k: int, parameters: tuple[int, ...]) -> list[Point]:
    n = p**k
    points: list[Point] = []
    for x in range(n):
        if x == 0:
            y = 0
        else:
            r = valuation(x, p)
            modulus = p ** (k - r)
            unit = x // (p**r)
            c = parameters[r] % modulus
            assert gcd(c, p) == 1
            y = p**r * ((c * pow(unit, -1, modulus)) % modulus)
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


def line_statistics(points: list[Point]) -> tuple[int, int]:
    lines: dict[tuple[int, int, int], set[Point]] = defaultdict(set)
    for a, b in combinations(points, 2):
        key = line_key(a, b)
        lines[key].add(a)
        lines[key].add(b)
    maximum = max((len(occupants) for occupants in lines.values()), default=1)
    triples = sum(comb(len(occupants), 3) for occupants in lines.values())
    return maximum, triples


def verify_displacement_signatures(p: int, k: int, points: list[Point]) -> int:
    checks = 0
    for first, second in combinations(points, 2):
        x, y = first
        xp, yp = second
        a = xp - x
        b = yp - y
        assert a and b
        t = valuation(a, p)
        assert valuation(b, p) == t

        r = k if x == 0 else valuation(x, p)
        s = k if xp == 0 else valuation(xp, p)
        if r == s and r < k:
            alpha = a // (p**t)
            beta = b // (p**t)
            modulus = p ** (k - t)
            u = x // (p**r)
            v = xp // (p**r)
            c = 1
            assert (u * v + c * alpha * pow(beta, -1, modulus)) % modulus == 0
            assert (
                u * (u + p ** (t - r) * alpha)
                + c * alpha * pow(beta, -1, modulus)
            ) % modulus == 0
        checks += 1
    return checks


def verify_syndrome_bound(p: int, k: int, maximum: int, triples: int) -> None:
    n = p**k
    theoretical_cap = 2 * k + 2 * p ** (k // 2) + 1
    assert maximum <= theoretical_cap
    bound_numerator = (theoretical_cap - 2) * comb(n, 2)
    assert 3 * triples <= bound_numerator


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=243)
    args = parser.parse_args()
    if args.max_modulus < 25:
        parser.error("--max-modulus must be at least 25")

    total_checks = 0
    rows: list[tuple[int, int, int]] = []
    for p in (3, 5, 7):
        k = 1
        while p**k <= args.max_modulus:
            points = completed_reciprocal(p, k, tuple(1 for _ in range(k)))
            total_checks += verify_displacement_signatures(p, k, points)
            maximum, triples = line_statistics(points)
            verify_syndrome_bound(p, k, maximum, triples)
            rows.append((p**k, maximum, triples))
            k += 1

    print(f"verified displacement pairs={total_checks}")
    for n, maximum, triples in rows:
        print(f"N={n}: max-line={maximum}; triples={triples}")


if __name__ == "__main__":
    main()

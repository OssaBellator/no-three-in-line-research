#!/usr/bin/env python3
"""Verify CMR28 on exhaustive small prime-power grids."""
from __future__ import annotations

import argparse
from itertools import combinations


def determinant(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])


def components(points, a):
    lower = [(x % a, y % a) for x, y in points]
    digits = [(x // a, y // a) for x, y in points]
    d0 = determinant(*lower)
    d1 = determinant(*digits)
    (x1, y1), (x2, y2), (x3, y3) = lower
    (u1, v1), (u2, v2), (u3, v3) = digits
    mixed = (
        (u2 - u1) * (y3 - y1)
        + (x2 - x1) * (v3 - v1)
        - (u3 - u1) * (y2 - y1)
        - (x3 - x1) * (v2 - v1)
    )
    return d0, mixed, d1


def verify_grid(p: int, k: int, max_triples: int) -> int:
    n = p**k
    a = p ** (k - 1)
    points = [(x, y) for x in range(n) for y in range(n)]
    checks = 0
    for triple in combinations(points, 3):
        full = determinant(*triple)
        d0, mixed, d1 = components(triple, a)
        assert full == d0 + a * mixed + a * a * d1
        if full == 0:
            assert d0 % a == 0
            assert d0 // a + mixed + a * d1 == 0
        checks += 1
        if checks >= max_triples:
            break
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-triples", type=int, default=250000)
    args = parser.parse_args()

    checks = 0
    instances = 0
    for p, k in ((2, 3), (3, 2), (2, 4), (5, 2)):
        checks += verify_grid(p, k, args.max_triples)
        instances += 1
    print(f"verified recursive determinant instances={instances}; triples={checks}")


if __name__ == "__main__":
    main()

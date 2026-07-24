#!/usr/bin/env python3
"""Verify the terminal-block mass lower bound CMR23."""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations


def determinant(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])


def exact_one_layer_mass(p: int) -> Fraction:
    cells = [(x, y) for x in range(p) for y in range(p)]
    mass = Fraction(0, 1)
    falling = p * (p - 1) * (p - 2)
    for triple in combinations(cells, 3):
        if len({x for x, _ in triple}) < 3:
            continue
        if len({y for _, y in triple}) < 3:
            continue
        if determinant(*triple) == 0:
            mass += Fraction(1, falling)
    return mass


def slope_bound(p: int) -> Fraction:
    choose3 = p * (p - 1) * (p - 2) // 6
    choose4 = p * (p - 1) * (p - 2) * (p - 3) // 24
    falling = p * (p - 1) * (p - 2)
    return Fraction(2 * (choose3 + 2 * choose4), falling)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=13)
    args = parser.parse_args()

    checked = 0
    for p in (3, 5, 7, 11, 13):
        if p > args.max_prime:
            continue
        exact = exact_one_layer_mass(p)
        lower = slope_bound(p)
        assert lower == Fraction(p - 1, 6)
        assert exact >= lower
        assert 2 * exact >= Fraction(p - 1, 3)
        print(
            f"p={p}: one-layer exact={exact}; slope lower={lower}; "
            f"two-layer lower={2 * lower}"
        )
        checked += 1
    print(f"verified terminal mass primes={checked}")


if __name__ == "__main__":
    main()

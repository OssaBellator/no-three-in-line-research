#!/usr/bin/env python3
"""Verify the finite inequalities in CMR50--CMR51."""
from __future__ import annotations

import argparse
from collections import Counter
from math import gcd, sqrt


def valuation(value: int, p: int, cap: int) -> int:
    if value == 0:
        return cap
    value = abs(value)
    out = 0
    while value % p == 0:
        value //= p
        out += 1
    return out


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def completed_reciprocal(p: int, k: int) -> list[int]:
    n = p**k
    values = []
    for x in range(n):
        if x == 0:
            values.append(0)
            continue
        r = valuation(x, p, k)
        modulus = p ** (k - r)
        unit = x // (p**r)
        values.append(p**r * pow(unit, -1, modulus))
    return values


def square_root_count(p: int, exponent: int, delta: int) -> int:
    modulus = p**exponent
    delta %= modulus
    if delta == 0:
        return p ** (exponent // 2)
    nu = valuation(delta, p, exponent)
    if nu % 2:
        return 0
    half = nu // 2
    unit = delta // (p ** (2 * half))
    if pow(unit % p, (p - 1) // 2, p) != 1:
        return 0
    return 2 * p**half


def verify_instance(p: int, k: int) -> tuple[int, int]:
    n = p**k
    values = completed_reciprocal(p, k)
    critical_counts: Counter[tuple[int, int]] = Counter()
    same_counts: Counter[tuple[int, int]] = Counter()
    root_sums: dict[tuple[int, int], int] = {}

    for a in range(1, n):
        t = valuation(a, p, k)
        reduced = a // (p**t)
        modulus = p ** (k - t)
        exponent = k - t

        for d in divisors(reduced):
            roots = 0
            for m in range(-(modulus // d + 1), modulus // d + 1):
                if m == 0 or abs(m) * d >= modulus or m % p == 0:
                    continue
                delta = (
                    reduced * reduced
                    - 4 * reduced * pow((d * m) % modulus, -1, modulus)
                ) % modulus
                roots += square_root_count(p, exponent, delta)
            root_sums[(a, d)] = roots
            assert roots < 6 * modulus / d + 2 * sqrt(modulus) + 1e-12

        for x in range(n - a):
            row_difference = values[x + a] - values[x]
            reduced_row = abs(row_difference) // (p**t)
            r = valuation(x, p, k)
            s = valuation(x + a, p, k)
            if r != s:
                continue
            for d in divisors(reduced):
                if reduced_row % d:
                    continue
                same_counts[(a, d)] += 1
                if r == t:
                    critical_counts[(a, d)] += 1

    for key, count in critical_counts.items():
        a, d = key
        t = valuation(a, p, k)
        modulus = p ** (k - t)
        assert count <= root_sums[key]
        assert count < 6 * modulus / d + 2 * sqrt(modulus) + 1e-12

    for (a, d), count in same_counts.items():
        assert count < 12 * n / d + 2 * sqrt(n) + 1e-12

    return len(root_sums), sum(critical_counts.values())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=125)
    args = parser.parse_args()

    cells = 0
    collisions = 0
    instances = 0
    for p in (3, 5, 7, 11):
        k = 2
        while p**k <= args.max_modulus:
            c, q = verify_instance(p, k)
            cells += c
            collisions += q
            instances += 1
            k += 1

    print(
        f"verified singular sums instances={instances}; "
        f"carry-cells={cells}; critical-collisions={collisions}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify CMR45 and compute finite divisor-collision constants."""
from __future__ import annotations

import argparse
from fractions import Fraction
from math import gcd, log


def valuation(value: int, p: int) -> int:
    value = abs(value)
    out = 0
    while value % p == 0:
        value //= p
        out += 1
    return out


def totient(n: int) -> int:
    result = n
    value = n
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            while value % divisor == 0:
                value //= divisor
            result -= result // divisor
        divisor += 1
    if value > 1:
        result -= result // value
    return result


def divisors(n: int) -> list[int]:
    small: list[int] = []
    large: list[int] = []
    divisor = 1
    while divisor * divisor <= n:
        if n % divisor == 0:
            small.append(divisor)
            if divisor * divisor != n:
                large.append(n // divisor)
        divisor += 1
    return small + list(reversed(large))


def completed_reciprocal(p: int, k: int) -> list[int]:
    n = p**k
    values = []
    for x in range(n):
        if x == 0:
            values.append(0)
            continue
        r = valuation(x, p)
        modulus = p ** (k - r)
        unit = x // (p**r)
        values.append(p**r * pow(unit, -1, modulus))
    return values


def verify_instance(p: int, k: int):
    n = p**k
    values = completed_reciprocal(p, k)
    energy = Fraction(0)
    divisor_bound = Fraction(0)
    collision_constant = Fraction(0)
    witness = None

    for difference in range(1, n):
        t = valuation(difference, p)
        reduced = difference // (p**t)
        reduced_divisors = divisors(reduced)
        counts = {d: 0 for d in reduced_divisors}

        for x in range(n - difference):
            row_difference = abs(values[x + difference] - values[x])
            assert row_difference != 0
            assert valuation(row_difference, p) == t
            reduced_row = row_difference // (p**t)

            energy += Fraction(
                gcd(reduced, reduced_row),
                max(reduced, reduced_row),
            )
            for d in reduced_divisors:
                if reduced_row % d == 0:
                    counts[d] += 1

        for d, count in counts.items():
            divisor_bound += Fraction(totient(d) * count, reduced)
            ratio = Fraction(d * count, n)
            if ratio > collision_constant:
                collision_constant = ratio
                witness = (difference, reduced, d, count)

    assert energy <= divisor_bound
    return n, energy, divisor_bound, collision_constant, witness


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=243)
    args = parser.parse_args()

    instances = 0
    for p in (3, 5, 7, 11):
        k = 2
        while p**k <= args.max_modulus:
            n, energy, bound, constant, witness = verify_instance(p, k)
            print(
                f"N={n}: energy={float(energy):.6f}; "
                f"divisor-bound={float(bound):.6f}; "
                f"K={float(constant):.6f}; "
                f"K/logN={float(constant)/log(n):.6f}; witness={witness}"
            )
            instances += 1
            k += 1

    print(f"verified divisor-collision instances={instances}")


if __name__ == "__main__":
    main()

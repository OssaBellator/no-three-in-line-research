#!/usr/bin/env python3
"""Verify the cross-stratum bounds CMR52--CMR55 in finite cases."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
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


def harmonic_number(n: int) -> Fraction:
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction())


def verify_instance(p: int, k: int) -> tuple[int, int]:
    n = p**k
    values = completed_reciprocal(p, k)
    actual: Counter[tuple[int, int, int]] = Counter()

    for a in range(1, n):
        t = valuation(a, p, k)
        reduced = a // (p**t)
        for x in range(n - a):
            row_difference = values[x + a] - values[x]
            reduced_row = abs(row_difference) // (p**t)
            r = valuation(x, p, k)
            s = valuation(x + a, p, k)
            if r == s:
                continue
            high = max(r, s)
            for d in divisors(reduced):
                if reduced_row % d:
                    continue
                m = row_difference // (p**t * d)
                h = high - t
                assert (d * m * reduced - 1) % (p**h) == 0
                actual[(a, d, high)] += 1

    for (a, d, r), count in actual.items():
        t = valuation(a, p, k)
        h = r - t
        reduced = a // (p**t)
        modulus = p ** (k - t)
        local_modulus = p ** (k - r)
        exponent = k - r

        roots = 0
        possible_carries = 0
        limit = (modulus - 1) // d
        for m in range(-limit, limit + 1):
            if m == 0 or abs(m) * d >= modulus or m % p == 0:
                continue
            if (d * m * reduced - 1) % (p**h):
                continue
            possible_carries += 1
            z = (d * m * reduced - 1) // (p**h)
            delta = ((z - p**h) ** 2 - 4) % local_modulus
            roots += square_root_count(p, exponent, delta)

        assert possible_carries <= 1 + 2 * local_modulus / d
        assert count <= 2 * roots
        assert count < 8 + 16 * local_modulus / d + 8 * sqrt(local_modulus)

    totals: Counter[tuple[int, int]] = Counter()
    for (a, d, _), count in actual.items():
        totals[(a, d)] += count

    for (a, d), count in totals.items():
        t = valuation(a, p, k)
        modulus = p ** (k - t)
        assert count < 8 * modulus / d + 11 * sqrt(modulus) + 8 * k

    # Check the unconditional CMR55 energy bound itself.
    energy = Fraction()
    for x in range(n):
        for xp in range(x + 1, n):
            dx = xp - x
            dy = abs(values[xp] - values[x])
            energy += Fraction(gcd(dx, dy), max(dx, dy))

    h_n = harmonic_number(n)
    energy_bound = 20 * n * k * h_n * h_n
    energy_bound += (n - 1) * (13 * sqrt(n) + 8 * k)
    assert float(energy) <= float(energy_bound)

    return len(actual), sum(actual.values())


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
        f"verified cross-stratum sums instances={instances}; "
        f"critical-cells={cells}; cross-collisions={collisions}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the critical divisor-collision identities CMR47--CMR49."""
from __future__ import annotations

import argparse
from collections import Counter
from math import gcd


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


def completed_reciprocal(p: int, k: int, parameters: tuple[int, ...]) -> list[int]:
    n = p**k
    values = []
    for x in range(n):
        if x == 0:
            values.append(0)
            continue
        r = valuation(x, p, k)
        modulus = p ** (k - r)
        unit = x // (p**r)
        c = parameters[r] % modulus
        assert gcd(c, p) == 1
        values.append(p**r * ((c * pow(unit, -1, modulus)) % modulus))
    return values


def verify_instance(p: int, k: int) -> tuple[int, int, int]:
    n = p**k
    parameters = tuple(1 for _ in range(k))
    values = completed_reciprocal(p, k, parameters)
    identity_checks = 0
    regular_counts: Counter[tuple[int, int, int]] = Counter()
    critical_checks = 0

    for a in range(1, n):
        t = valuation(a, p, k)
        reduced_a = a // (p**t)
        modulus = p ** (k - t)

        for x in range(n - a):
            row_difference = values[x + a] - values[x]
            assert valuation(row_difference, p, k) == t
            reduced_row = abs(row_difference) // (p**t)
            r = valuation(x, p, k)
            s = valuation(x + a, p, k)

            for d in divisors(reduced_a):
                if reduced_row % d:
                    continue
                m = row_difference // (p**t * d)
                assert m and m % p
                assert abs(m) < modulus / d

                if r == s:
                    assert r <= t
                    u = x // (p**r)
                    v = (x + a) // (p**r)
                    c = parameters[r]
                    assert (d * m * u * v + reduced_a * c) % modulus == 0

                    shift = (p ** (t - r) * reduced_a) % modulus
                    discriminant = (
                        shift * shift
                        - 4 * reduced_a * c * pow((d * m) % modulus, -1, modulus)
                    ) % modulus

                    if r < t:
                        assert discriminant % p != 0
                        regular_counts[(a, d, r)] += 1
                    elif discriminant % p != 0:
                        regular_counts[(a, d, r)] += 1
                    else:
                        assert (d * m * reduced_a - 4 * parameters[t]) % p == 0
                        critical_checks += 1
                else:
                    assert min(r, s) == t
                    assert (d * m * reduced_a - parameters[t]) % p == 0
                    critical_checks += 1

                identity_checks += 1

    for (a, d, r), count in regular_counts.items():
        t = valuation(a, p, k)
        if r < t:
            assert count < 4 * (p ** (k - r)) / d
        else:
            assert r == t
            assert count < 4 * (p ** (k - t)) / d

    return identity_checks, len(regular_counts), critical_checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=125)
    args = parser.parse_args()

    identities = 0
    regular_cells = 0
    critical = 0
    instances = 0
    for p in (3, 5, 7, 11):
        k = 2
        while p**k <= args.max_modulus:
            i, r, c = verify_instance(p, k)
            identities += i
            regular_cells += r
            critical += c
            instances += 1
            k += 1

    print(
        f"verified critical collisions instances={instances}; "
        f"identities={identities}; regular-cells={regular_cells}; "
        f"critical-collisions={critical}"
    )


if __name__ == "__main__":
    main()

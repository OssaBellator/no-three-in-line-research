#!/usr/bin/env python3
"""Verify Theorem CMR14 for finite odd prime powers."""
from __future__ import annotations

import argparse
from collections import Counter
from math import gcd


def valuation(value: int, p: int) -> int:
    out = 0
    while value % p == 0:
        value //= p
        out += 1
    return out


def completed_reciprocal_values(p: int, k: int, c0: int) -> list[int]:
    n = p**k
    values: list[int] = []
    for x in range(n):
        if x == 0:
            values.append(0)
            continue
        r = valuation(x, p)
        modulus = p ** (k - r)
        c = c0 if r == 0 else 1
        unit = x // (p**r)
        values.append(p**r * ((c * pow(unit, -1, modulus)) % modulus))
    return values


def verify_instance(p: int, k: int, c0: int) -> tuple[int, int]:
    n = p**k
    a = p ** (k - 1)
    values = completed_reciprocal_values(p, k, c0)
    exact = Counter()
    residue_counts = Counter()

    for x in range(n - a):
        if x % p == 0:
            continue
        q = (c0 * pow((x * x) % p, -1, p)) % p
        dy = values[x + a] - values[x]
        assert dy in (-q * a, (p - q) * a)
        exact[(a, dy)] += 1
        residue_counts[q] += 1

    expected_per_q = 2 * (p - 1) * p ** (k - 2)
    assert set(residue_counts.values()) == {expected_per_q}
    lower_bound = (p - 1) * p ** (k - 2)
    maximum = max(exact.values())
    assert maximum >= lower_bound
    return maximum, lower_bound


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=343)
    args = parser.parse_args()
    if args.max_modulus < 9:
        parser.error("--max-modulus must be at least 9")

    checks = 0
    weakest_ratio = None
    for p in (3, 5, 7, 11):
        k = 2
        while p**k <= args.max_modulus:
            n = p**k
            parameters = list(range(1, p))
            parameters.extend(c + p for c in range(1, p) if c + p < n)
            for c0 in parameters:
                if gcd(c0, p) != 1:
                    continue
                maximum, lower = verify_instance(p, k, c0)
                ratio = maximum / lower
                weakest_ratio = ratio if weakest_ratio is None else min(weakest_ratio, ratio)
                checks += 1
            k += 1

    print(
        f"verified displacement obstruction instances={checks}; "
        f"minimum observed maximum/lower-bound ratio={weakest_ratio:.3f}"
    )


if __name__ == "__main__":
    main()

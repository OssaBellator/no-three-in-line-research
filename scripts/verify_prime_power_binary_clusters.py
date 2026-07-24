#!/usr/bin/env python3
"""Verify CMR73--CMR74 clustering identities and local coefficients."""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, product


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def valuation(n: int, p: int) -> int:
    assert n != 0
    n = abs(n)
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value


def prime_power_data(n: int) -> tuple[int, int] | None:
    for p in range(3, n + 1, 2):
        if not is_prime(p):
            continue
        value = p
        k = 1
        while value < n:
            value *= p
            k += 1
        if value == n:
            return p, k
    return None


def tau(x: int, p: int) -> int:
    return 0 if x == 0 else pow(x, -1, p)


def verify_instance(p: int, k: int) -> tuple[int, int, int]:
    n = p**k
    equilateral: Counter[int] = Counter()
    binary_pairs: Counter[int] = Counter()
    binary_triples: Counter[int] = Counter()
    coefficient_checks = 0

    for x1, x2 in combinations(range(n), 2):
        binary_pairs[valuation(x1 - x2, p)] += 1

    for columns in combinations(range(n), 3):
        pairs = ((0, 1), (0, 2), (1, 2))
        values = [valuation(columns[i] - columns[j], p) for i, j in pairs]
        r = min(values)
        s = max(values)
        if r == s:
            equilateral[s] += 1
            continue

        closest = pairs[values.index(s)]
        binary_triples[s] += 1

        # Check the separation-node coefficient used in CMR73.
        i, j = closest
        xi = (columns[i] // (p**s)) % p
        xj = (columns[j] // (p**s)) % p
        assert xi != xj
        assert (tau(xi, p) - tau(xj, p)) % p != 0

        # Exactly four layer assignments align the closest pair.
        aligned = 0
        for layers in product((0, 1), repeat=3):
            if layers[i] == layers[j]:
                aligned += 1
        assert aligned == 4
        coefficient_checks += 1

    for s in range(k):
        length = p ** (k - s - 1)
        expected_equilateral = p**s * (p * (p - 1) * (p - 2) // 6) * length**3
        expected_pairs = p**s * (p * (p - 1) // 2) * length**2
        assert equilateral[s] == expected_equilateral
        assert binary_pairs[s] == expected_pairs
        assert binary_triples[s] <= expected_pairs * n

    return sum(equilateral.values()), sum(binary_triples.values()), coefficient_checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=125)
    args = parser.parse_args()

    instances = 0
    equilateral = 0
    binary = 0
    checks = 0
    for n in range(9, args.max_modulus + 1):
        data = prime_power_data(n)
        if data is None:
            continue
        p, k = data
        if k < 2 or p % 4 != 1:
            continue
        a, b, c = verify_instance(p, k)
        instances += 1
        equilateral += a
        binary += b
        checks += c

    print(
        "verified binary-cluster sum "
        f"instances={instances}; equilateral={equilateral}; "
        f"binary={binary}; coefficient-checks={checks}"
    )


if __name__ == "__main__":
    main()

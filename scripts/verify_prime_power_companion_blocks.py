#!/usr/bin/env python3
"""Verify Theorem CMR17 on finite prime powers."""
from __future__ import annotations

import argparse
from itertools import permutations
from math import gcd


def valuation(value: int, p: int) -> int:
    out = 0
    while value % p == 0:
        value //= p
        out += 1
    return out


def completed_reciprocal_values(p: int, k: int, c0: int) -> list[int]:
    n = p**k
    values = []
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


def companion(y: int, p: int, k: int) -> int:
    n = p**k
    increment = p if p % 2 else 4
    return ((1 + increment) * y + 1) % n


def verify_instance(p: int, k: int, c0: int) -> tuple[int, int]:
    n = p**k
    a = p ** (k - 1)
    first = completed_reciprocal_values(p, k, c0)
    blocks = 0
    states = 0

    for xi in range(a):
        if xi % p == 0:
            continue
        columns = [xi + j * a for j in range(p)]
        rows = [first[x] for x in columns]
        assert len({row % a for row in rows}) == 1
        assert all(companion(row, p, k) % a != row % a for row in rows)
        assert all(companion(row, p, k) not in set(rows) for row in rows)

        # Exhaust every local state for small p and verify companion disjointness.
        for pi in permutations(range(p)):
            state = [rows[pi[j]] for j in range(p)]
            assert set(state) == set(rows)
            assert all(state[j] != companion(first[columns[j]], p, k) for j in range(p))
            states += 1
        blocks += 1

    assert blocks == (p - 1) * p ** (k - 2)
    return blocks, states


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=125)
    args = parser.parse_args()
    if args.max_modulus < 8:
        parser.error("--max-modulus must be at least 8")

    instances = 0
    blocks = 0
    states = 0
    for p in (2, 3, 5, 7):
        k = 2 if p % 2 else 3
        while p**k <= args.max_modulus:
            for c0 in range(1, p):
                if gcd(c0, p) != 1:
                    continue
                b, s = verify_instance(p, k, c0)
                blocks += b
                states += s
                instances += 1
            k += 1

    print(
        f"verified companion block instances={instances}; "
        f"blocks={blocks}; executable local states={states}"
    )


if __name__ == "__main__":
    main()

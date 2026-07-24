#!/usr/bin/env python3
"""Verify CMR25 and finite instances of the CMR26 lift."""
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


def completed_reciprocal_values(p: int, k: int, parameters: tuple[int, ...]) -> list[int]:
    n = p**k
    values = []
    for x in range(n):
        if x == 0:
            values.append(0)
            continue
        r = valuation(x, p)
        modulus = p ** (k - r)
        unit = x // (p**r)
        values.append(p**r * ((parameters[r] * pow(unit, -1, modulus)) % modulus))
    return values


def companion_values(first: list[int], p: int, k: int) -> list[int]:
    n = p**k
    increment = p if p % 2 else 4
    return [((1 + increment) * y + 1) % n for y in first]


def verify_quotient(p: int, k: int) -> int:
    n = p**k
    a = p ** (k - 1)
    parameters = tuple(1 + p * r for r in range(k))
    parameters = tuple(c if gcd(c, p) == 1 else 1 for c in parameters)
    first = completed_reciprocal_values(p, k, parameters)
    small = completed_reciprocal_values(p, k - 1, parameters[:-1])
    second = companion_values(first, p, k)
    small_second = companion_values(small, p, k - 1)

    for x in range(n):
        assert first[x] % a == small[x % a]
        assert second[x] % a == small_second[x % a]

    for xbar in range(a):
        columns = [xbar + j * a for j in range(p)]
        first_rows = {first[x] for x in columns}
        second_rows = {second[x] for x in columns}
        assert first_rows == {small[xbar] + j * a for j in range(p)}
        assert second_rows == {small_second[xbar] + j * a for j in range(p)}
    return n


def verify_lift(p: int, k: int) -> int:
    n = p**k
    a = p ** (k - 1)
    # Use two cyclic quotient permutations with distinct images in every column.
    first_q = list(range(a))
    second_q = [(x + 1) % a for x in range(a)]
    reverse = tuple(reversed(range(p)))
    identity = tuple(range(p))

    layer0 = []
    layer1 = []
    for xbar in range(a):
        columns = [xbar + j * a for j in range(p)]
        rows0 = [first_q[xbar] + j * a for j in range(p)]
        rows1 = [second_q[xbar] + j * a for j in range(p)]
        pi = identity if xbar % 2 == 0 else reverse
        tau = reverse if xbar % 2 == 0 else identity
        layer0.extend((columns[j], rows0[pi[j]]) for j in range(p))
        layer1.extend((columns[j], rows1[tau[j]]) for j in range(p))

    assert sorted(y for _, y in layer0) == list(range(n))
    assert sorted(y for _, y in layer1) == list(range(n))
    assert all(layer0[x][0] == layer1[x][0] for x in range(n))
    assert all(layer0[x][1] != layer1[x][1] for x in range(n))
    return 2 * n


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=125)
    args = parser.parse_args()
    if args.max_modulus < 8:
        parser.error("--max-modulus must be at least 8")

    quotient_points = 0
    lift_points = 0
    instances = 0
    for p in (2, 3, 5, 7):
        k = 2
        while p**k <= args.max_modulus:
            quotient_points += verify_quotient(p, k)
            lift_points += verify_lift(p, k)
            instances += 1
            k += 1

    print(
        f"verified recursive quotient instances={instances}; "
        f"quotient points={quotient_points}; lifted points={lift_points}"
    )


if __name__ == "__main__":
    main()

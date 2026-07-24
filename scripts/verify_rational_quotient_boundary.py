#!/usr/bin/env python3
"""Verify RI2f quotient symmetry and exact boundary/image identities."""

from __future__ import annotations

from itertools import combinations


def primes_through(limit: int) -> list[int]:
    return [
        value
        for value in range(3, limit + 1, 2)
        if all(
            value % divisor
            for divisor in range(2, int(value**0.5) + 1)
        )
    ]


def prime_factors(number: int) -> set[int]:
    factors: set[int] = set()
    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        divisor += 1
    if number > 1:
        factors.add(number)
    return factors


def primitive_root(p: int) -> int:
    factors = prime_factors(p - 1)
    return next(
        candidate
        for candidate in range(2, p)
        if all(
            pow(candidate, (p - 1) // factor, p) != 1
            for factor in factors
        )
    )


def divisors(number: int) -> list[int]:
    return [value for value in range(1, number + 1) if number % value == 0]


def image(x: int, r: int, p: int) -> int:
    return x * (1 - x) * pow(r - x, -1, p) % p


def partner(x: int, r: int, p: int) -> int:
    return r * (x - 1) * pow(x - r, -1, p) % p


def quotient_subsets(index: int) -> set[frozenset[int]]:
    labels = set(range(index))
    if index <= 8:
        return {
            frozenset(
                label for label in range(index) if mask & (1 << label)
            )
            for mask in range(1 << index)
        }

    selected: set[frozenset[int]] = set()
    for size in range(4):
        for subset in combinations(range(index), size):
            frozen = frozenset(subset)
            selected.add(frozen)
            selected.add(frozenset(labels - set(frozen)))
    return selected


def verify(limit: int = 31) -> None:
    for p in primes_through(limit):
        generator = primitive_root(p)
        logarithm = {
            pow(generator, exponent, p): exponent
            for exponent in range(p - 1)
        }
        for order in divisors(p - 1):
            index = (p - 1) // order
            label_of = {
                value: exponent % index
                for value, exponent in logarithm.items()
            }
            cosets = [
                {value for value, label in label_of.items() if label == index_}
                for index_ in range(index)
            ]

            for r in range(2, p):
                domain = set(range(1, p)) - {1, r}
                matrix = [[0 for _ in range(index)] for _ in range(index)]
                for x in domain:
                    z = partner(x, r, p)
                    assert z in domain
                    assert partner(z, r, p) == x
                    assert image(z, r, p) == image(x, r, p)
                    matrix[label_of[x]][label_of[z]] += 1

                assert all(
                    matrix[left][right] == matrix[right][left]
                    for left in range(index)
                    for right in range(index)
                )
                assert all(
                    sum(matrix[label]) == len(cosets[label] & domain)
                    for label in range(index)
                )

                for labels in quotient_subsets(index):
                    selected = {
                        x for x in domain if label_of[x] in labels
                    }
                    fixed = sum(partner(x, r, p) == x for x in selected)
                    boundary = sum(
                        partner(x, r, p) not in selected for x in selected
                    )
                    matrix_boundary = sum(
                        matrix[left][right]
                        for left in labels
                        for right in range(index)
                        if right not in labels
                    )
                    assert matrix_boundary == boundary

                    internal_pairs = {
                        tuple(sorted((x, partner(x, r, p))))
                        for x in selected
                        if partner(x, r, p) in selected
                        and partner(x, r, p) != x
                    }
                    pair_count = len(internal_pairs)
                    outputs = {image(x, r, p) for x in selected}
                    assert len(selected) == 2 * pair_count + fixed + boundary
                    assert len(outputs) == pair_count + fixed + boundary
                    assert 2 * len(outputs) - len(selected) == fixed + boundary


def main() -> None:
    verify()
    print("rational quotient boundary identities: verified through prime 31")


if __name__ == "__main__":
    main()

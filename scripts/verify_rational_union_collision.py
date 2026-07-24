#!/usr/bin/env python3
"""Verify RI2b--RI2c on unions of small subgroup cosets."""

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


def verify(limit: int = 31) -> None:
    for p in primes_through(limit):
        generator = primitive_root(p)
        logarithm = {
            pow(generator, exponent, p): exponent
            for exponent in range(p - 1)
        }
        for order in divisors(p - 1):
            index = (p - 1) // order
            subgroup = {
                pow(generator, index * exponent, p)
                for exponent in range(order)
            }
            cosets = [
                {pow(generator, label, p) * value % p for value in subgroup}
                for label in range(index)
            ]
            maximum_union = min(3, index)
            for union_size in range(1, maximum_union + 1):
                for labels in combinations(range(index), union_size):
                    full = set().union(*(cosets[label] for label in labels))
                    for r in range(2, p):
                        domain = full - {1, r}
                        outputs = {image(x, r, p) for x in domain}
                        target_labels = {
                            logarithm[value] % index for value in outputs
                        }
                        target_count = len(target_labels)
                        exceptional = len(full - domain)

                        pairs: set[tuple[int, int]] = set()
                        by_type: dict[tuple[int, int], int] = {}
                        for x in domain:
                            z = partner(x, r, p)
                            if z not in domain or z == x:
                                continue
                            pair = tuple(sorted((x, z)))
                            if pair in pairs:
                                continue
                            pairs.add(pair)
                            pair_type = tuple(
                                sorted(
                                    (
                                        logarithm[x] % index,
                                        logarithm[z] % index,
                                    )
                                )
                            )
                            by_type[pair_type] = by_type.get(pair_type, 0) + 1

                        assert len(pairs) == len(domain) - len(outputs)
                        assert 2 * order * target_count >= len(domain)
                        lower = (
                            (union_size - target_count) * order
                            - exceptional
                        )
                        assert len(pairs) >= lower
                        if lower > 0:
                            type_count = union_size * (union_size + 1) // 2
                            assert max(by_type.values()) * type_count >= lower


def main() -> None:
    verify()
    print("rational union collision localization: verified through prime 31")


if __name__ == "__main__":
    main()

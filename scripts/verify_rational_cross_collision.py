#!/usr/bin/env python3
"""Verify RI2d--RI2e cross-coset collision caps."""

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


def collision_pairs(domain: set[int], r: int, p: int) -> int:
    pairs: set[tuple[int, int]] = set()
    for x in domain:
        other = partner(x, r, p)
        if other in domain and other != x:
            pairs.add(tuple(sorted((x, other))))
    return len(pairs)


def verify(limit: int = 31) -> None:
    for p in primes_through(limit):
        generator = primitive_root(p)
        logarithm = {
            pow(generator, exponent, p): exponent
            for exponent in range(p - 1)
        }
        for order in divisors(p - 1):
            index = (p - 1) // order
            cosets = [
                {
                    pow(generator, label + index * exponent, p)
                    for exponent in range(order)
                }
                for label in range(index)
            ]
            for r in range(2, p):
                for source in cosets:
                    for target in cosets:
                        overlap = sum(
                            x not in {1, r}
                            and partner(x, r, p) in target
                            for x in source
                        )
                        scaled_error = (
                            index * index * overlap - (p - 3)
                        )
                        assert scaled_error * scaled_error <= (
                            9
                            * (index * index - 1) ** 2
                            * p
                        )

                for union_size in range(1, min(3, index) + 1):
                    for labels in combinations(range(index), union_size):
                        full = set().union(
                            *(cosets[label] for label in labels)
                        )
                        domain = full - {1, r}
                        exceptional = len(full - domain)
                        pair_count = collision_pairs(domain, r, p)
                        output_labels = {
                            logarithm[image(x, r, p)] % index
                            for x in domain
                        }
                        target_count = len(output_labels)

                        # RI2d, multiplied by 2m^2 and squared when the
                        # square-root error is needed.
                        cap_excess = (
                            2 * index * index * pair_count
                            - union_size * union_size * (p - 3)
                        )
                        if cap_excess > 0:
                            assert cap_excess * cap_excess <= (
                                9
                                * union_size**4
                                * (index * index - 1) ** 2
                                * p
                            )

                        assert (
                            (union_size - target_count) * order
                            <= exceptional + pair_count
                        )

                        # Exact squared test for
                        # e + s^2 A_m(p)/2 < h.
                        coverage_margin = (
                            2
                            * index
                            * index
                            * (order - exceptional)
                            - union_size * union_size * (p - 3)
                        )
                        error_square = (
                            9
                            * union_size**4
                            * (index * index - 1) ** 2
                            * p
                        )
                        if (
                            coverage_margin > 0
                            and coverage_margin * coverage_margin
                            > error_square
                        ):
                            assert target_count >= union_size


def main() -> None:
    verify()
    print("rational cross-coset collision caps: verified through prime 31")


if __name__ == "__main__":
    main()

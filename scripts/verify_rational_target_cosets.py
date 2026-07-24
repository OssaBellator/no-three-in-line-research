#!/usr/bin/env python3
"""Verify target-coset equidistribution for the rational inverse map."""

from __future__ import annotations


def primes_through(limit: int) -> list[int]:
    return [
        n
        for n in range(3, limit + 1, 2)
        if all(n % divisor for divisor in range(2, int(n**0.5) + 1))
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
        if all(pow(candidate, (p - 1) // factor, p) != 1 for factor in factors)
    )


def divisors(number: int) -> list[int]:
    return [value for value in range(1, number + 1) if number % value == 0]


def image(x: int, r: int, p: int) -> int:
    return x * (1 - x) * pow(r - x, -1, p) % p


def verify(limit: int = 43) -> None:
    for p in primes_through(limit):
        generator = primitive_root(p)
        logarithm = {
            pow(generator, exponent, p): exponent for exponent in range(p - 1)
        }
        for order in divisors(p - 1):
            index = (p - 1) // order
            subgroup = {
                pow(generator, index * exponent, p) for exponent in range(order)
            }
            for source_index in range(index):
                x0 = pow(generator, source_index, p)
                source_coset = {x0 * value % p for value in subgroup}
                for r in range(2, p):
                    source = source_coset - {1, r}
                    counts = [0] * index
                    for value in source:
                        target = image(value, r, p)
                        counts[logarithm[target] % index] += 1
                    assert sum(counts) == len(source)
                    for count in counts:
                        difference = abs(index * index * count - (p - 3))
                        assert difference * difference <= (
                            9 * (index * index - 1) ** 2 * p
                        )
                    if (p - 3) ** 2 > (
                        9 * (index * index - 1) ** 2 * p
                    ):
                        assert all(count > 0 for count in counts)


def main() -> None:
    verify()
    print("rational target-coset distribution: verified through prime 43")


if __name__ == "__main__":
    main()

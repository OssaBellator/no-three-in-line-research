#!/usr/bin/env python3
"""Verify the RI1d subgroup-overlap inequality on small finite fields."""

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


def tau(x: int, r: int, p: int) -> int:
    return r * (x - 1) * pow(x - r, -1, p) % p


def image(x: int, r: int, p: int) -> int:
    return x * (1 - x) * pow(r - x, -1, p) % p


def verify(limit: int = 43) -> None:
    for p in primes_through(limit):
        generator = primitive_root(p)
        for order in divisors(p - 1):
            index = (p - 1) // order
            subgroup = {
                pow(generator, index * exponent, p) for exponent in range(order)
            }
            for coset_index in range(index):
                x0 = pow(generator, coset_index, p)
                coset = {x0 * value % p for value in subgroup}
                for r in range(2, p):
                    source = coset - {1, r}
                    partner_points = {
                        value for value in source if tau(value, r, p) in source
                    }
                    overlap = len(partner_points)
                    difference = abs(index * index * overlap - (p - 3))
                    assert difference * difference <= (
                        9 * (index * index - 1) ** 2 * p
                    )

                    fixed = {
                        value
                        for value in partner_points
                        if tau(value, r, p) == value
                    }
                    pairs = {
                        tuple(sorted((value, tau(value, r, p))))
                        for value in partner_points - fixed
                    }
                    assert 2 * len(pairs) == overlap - len(fixed)
                    outputs = {image(value, r, p) for value in source}
                    assert len(outputs) == len(source) - len(pairs)


def main() -> None:
    verify()
    print("rational Weil overlap bound: verified through prime 43")


if __name__ == "__main__":
    main()

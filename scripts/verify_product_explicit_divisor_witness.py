#!/usr/bin/env python3
"""Exact arithmetic checks for PX466--PX470 divisor and exponent witnesses."""

from __future__ import annotations

from fractions import Fraction
from math import isqrt


def primes_below(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * limit
    if limit:
        sieve[0] = 0
    if limit > 1:
        sieve[1] = 0
    for prime in range(2, isqrt(limit - 1) + 1):
        if sieve[prime]:
            start = prime * prime
            count = (limit - 1 - start) // prime + 1
            sieve[start:limit:prime] = b"\x00" * count
    return [value for value in range(2, limit) if sieve[value]]


def maximizing_exponent(prime: int) -> int:
    """First a for which f(a+1) <= f(a), compared after 12th powers."""
    exponent = 0
    while (exponent + 2) ** 12 > prime * (exponent + 1) ** 12:
        exponent += 1
    return exponent


def check_local_maxima() -> tuple[int, int]:
    primes = primes_below(4096)
    assert len(primes) == 564

    numerator = 1
    denominator = 1
    largest_exponent = 0

    for prime in primes:
        exponent = maximizing_exponent(prime)
        largest_exponent = max(largest_exponent, exponent)

        # The sequence increases up to exponent and is nonincreasing after it.
        assert (exponent + 2) ** 12 <= prime * (exponent + 1) ** 12
        if exponent:
            assert (exponent + 1) ** 12 > prime * exponent**12

        # Check a generous finite window around the exact ratio-change point.
        local_numerator = (exponent + 1) ** 12
        local_denominator = prime**exponent
        for candidate in range(0, exponent + 20):
            assert (
                (candidate + 1) ** 12 * local_denominator
                <= local_numerator * prime**candidate
            )

        numerator *= local_numerator
        denominator *= local_denominator

    assert largest_exponent == 16
    assert numerator < 10**324 * denominator
    return numerator, denominator


def divisor_counts(limit: int) -> list[int]:
    counts = [0] * (limit + 1)
    for divisor in range(1, limit + 1):
        for multiple in range(divisor, limit + 1, divisor):
            counts[multiple] += 1
    return counts


def check_finite_divisor_range() -> None:
    # Exact twelfth-power form of tau(m) <= 10^27 m^(1/12).
    limit = 100_000
    counts = divisor_counts(limit)
    constant_power = 10**324
    for value in range(1, limit + 1):
        assert counts[value] ** 12 <= constant_power * value


def check_large_prime_local_factors() -> None:
    # For p >= 2^12, (a+1)^12 <= 2^(12a) <= p^a.
    for exponent in range(0, 1000):
        assert (exponent + 1) <= 2**exponent
        assert (exponent + 1) ** 12 <= 4096**exponent


def check_effective_exponents() -> None:
    epsilon = Fraction(1, 10)
    divisor_exponent = Fraction(1, 6)
    assert 2 * epsilon > divisor_exponent
    assert 2 * epsilon - divisor_exponent == Fraction(1, 30)

    fourth_destruction = Fraction(15, 16)
    line_cap = Fraction(1, 3)
    star = fourth_destruction - line_cap
    threshold = Fraction(3, 5)
    assert star == Fraction(29, 48)
    assert star - threshold == Fraction(1, 240)
    assert Fraction(2, 3) > threshold


def main() -> None:
    check_local_maxima()
    check_large_prime_local_factors()
    check_finite_divisor_range()
    check_effective_exponents()
    print("PX466--PX470 explicit divisor-witness verifier: PASS")


if __name__ == "__main__":
    main()

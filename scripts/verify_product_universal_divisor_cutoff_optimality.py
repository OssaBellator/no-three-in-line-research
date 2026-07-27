#!/usr/bin/env python3
"""Proves that no universal Euler-product exponent certifies cutoff 10^2873."""

from __future__ import annotations

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext


PRECISION = 100
PIVOT_PRIME = 13033
DECIMAL_POWER = 2873
TARGET_POWER = 2 * DECIMAL_POWER
FIXED_DENOMINATOR = 32768 * 256
FIXED_EXPONENTIAL_LOG = 6 * 33


def primes_below(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * limit
    sieve[:2] = b"\x00\x00"
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            start = prime * prime
            count = (limit - 1 - start) // prime + 1
            sieve[start:limit:prime] = b"\x00" * count
    return [value for value in range(2, limit) if sieve[value]]


def log_bounds(value: int) -> tuple[Decimal, Decimal]:
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_FLOOR
        lower = Decimal(value).ln()
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        upper = Decimal(value).ln()
    return lower, upper


def positive_division_bounds(
    numerator: tuple[Decimal, Decimal],
    denominator: tuple[Decimal, Decimal],
) -> tuple[Decimal, Decimal]:
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_FLOOR
        lower = numerator[0] / denominator[1]
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        upper = numerator[1] / denominator[0]
    return lower, upper


def positive_product_bounds(
    first: tuple[Decimal, Decimal],
    second: tuple[Decimal, Decimal],
) -> tuple[Decimal, Decimal]:
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_FLOOR
        lower = first[0] * second[0]
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        upper = first[1] * second[1]
    return lower, upper


def difference_bounds(
    first: tuple[Decimal, Decimal],
    second: tuple[Decimal, Decimal],
) -> tuple[Decimal, Decimal]:
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_FLOOR
        lower = first[0] - second[1]
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        upper = first[1] - second[0]
    return lower, upper


def exponent_at_pivot(
    prime: int,
    alpha: tuple[Decimal, Decimal],
) -> tuple[int, Decimal]:
    right = positive_product_bounds(alpha, log_bounds(prime))
    exponent = 0
    minimum_separation: Decimal | None = None
    while True:
        left = difference_bounds(
            log_bounds(exponent + 2),
            log_bounds(exponent + 1),
        )
        if left[0] > right[1]:
            separation = left[0] - right[1]
            minimum_separation = (
                separation
                if minimum_separation is None
                else min(minimum_separation, separation)
            )
            exponent += 1
            continue
        if left[1] < right[0]:
            separation = right[0] - left[1]
            minimum_separation = (
                separation
                if minimum_separation is None
                else min(minimum_separation, separation)
            )
            assert minimum_separation is not None
            return exponent, minimum_separation
        raise AssertionError((prime, exponent, left, right))


def margin_upper_bound(
    alpha: tuple[Decimal, Decimal],
    numerator_product: int,
    prime_product: int,
) -> Decimal:
    log_12 = log_bounds(12)
    log_fixed = log_bounds(FIXED_DENOMINATOR)
    log_10 = log_bounds(10)
    log_numerator = log_bounds(numerator_product)
    log_prime_product = log_bounds(prime_product)
    alpha_times_prime = positive_product_bounds(alpha, log_prime_product)
    alpha_times_ten = positive_product_bounds(alpha, log_10)

    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        return (
            -log_12[0]
            - log_fixed[0]
            - Decimal(FIXED_EXPONENTIAL_LOG)
            + (Decimal(DECIMAL_POWER) / Decimal(5)) * log_10[1]
            - log_numerator[0]
            + alpha_times_prime[1]
            - Decimal(2 * DECIMAL_POWER) * alpha_times_ten[0]
        )


def main() -> None:
    primes = primes_below(PIVOT_PRIME + 1)
    assert primes[-1] == PIVOT_PRIME
    lower_primes = primes[:-1]
    assert lower_primes[-1] == 13009

    alpha = positive_division_bounds(
        log_bounds(2),
        log_bounds(PIVOT_PRIME),
    )
    assert Decimal("0.07315352320641910") < alpha[0]
    assert alpha[1] < Decimal("0.07315352320641911")

    numerator_product = 1
    prime_product = 1
    exponents: list[int] = []
    minimum_separation: Decimal | None = None
    for prime in lower_primes:
        exponent, separation = exponent_at_pivot(prime, alpha)
        exponents.append(exponent)
        numerator_product *= exponent + 1
        prime_product *= prime**exponent
        minimum_separation = (
            separation
            if minimum_separation is None
            else min(minimum_separation, separation)
        )

    assert len(lower_primes) == 1551
    assert min(exponents) == 1
    assert max(exponents) == 19
    assert minimum_separation is not None
    assert minimum_separation > Decimal("0.000046")

    target = 10**TARGET_POWER
    assert prime_product < target
    assert prime_product * PIVOT_PRIME > target

    upper = margin_upper_bound(alpha, numerator_product, prime_product)
    assert upper < Decimal("-0.0934")

    print(
        "PX966--PX969 universal divisor cutoff optimality verifier: PASS",
        f"margin_upper={upper}",
    )


if __name__ == "__main__":
    main()

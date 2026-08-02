#!/usr/bin/env python3
"""Bracket the divisor-bound improvement needed at decimal order 2873."""
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


def log_bounds(value: int | Decimal) -> tuple[Decimal, Decimal]:
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
) -> int:
    right = positive_product_bounds(alpha, log_bounds(prime))
    exponent = 0
    while True:
        left = difference_bounds(
            log_bounds(exponent + 2),
            log_bounds(exponent + 1),
        )
        if left[0] > right[1]:
            exponent += 1
            continue
        if left[1] < right[0]:
            return exponent
        raise AssertionError((prime, exponent, left, right))


def margin_bounds(
    alpha: tuple[Decimal, Decimal],
    numerator_product: int,
    prime_product: int,
) -> tuple[Decimal, Decimal]:
    log_12 = log_bounds(12)
    log_fixed = log_bounds(FIXED_DENOMINATOR)
    log_10 = log_bounds(10)
    log_numerator = log_bounds(numerator_product)
    log_prime_product = log_bounds(prime_product)
    alpha_times_prime = positive_product_bounds(alpha, log_prime_product)
    alpha_times_ten = positive_product_bounds(alpha, log_10)

    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_FLOOR
        lower = (
            -log_12[1]
            - log_fixed[1]
            - Decimal(FIXED_EXPONENTIAL_LOG)
            + (Decimal(DECIMAL_POWER) / Decimal(5)) * log_10[0]
            - log_numerator[1]
            + alpha_times_prime[0]
            - Decimal(TARGET_POWER) * alpha_times_ten[1]
        )
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        upper = (
            -log_12[0]
            - log_fixed[0]
            - Decimal(FIXED_EXPONENTIAL_LOG)
            + (Decimal(DECIMAL_POWER) / Decimal(5)) * log_10[1]
            - log_numerator[0]
            + alpha_times_prime[1]
            - Decimal(TARGET_POWER) * alpha_times_ten[0]
        )
    return lower, upper


def main() -> None:
    primes = primes_below(PIVOT_PRIME + 1)
    alpha = positive_division_bounds(log_bounds(2), log_bounds(PIVOT_PRIME))

    numerator_product = 1
    prime_product = 1
    for prime in primes[:-1]:
        exponent = exponent_at_pivot(prime, alpha)
        numerator_product *= exponent + 1
        prime_product *= prime**exponent

    target = 10**TARGET_POWER
    assert prime_product < target < prime_product * PIVOT_PRIME

    lower, upper = margin_bounds(alpha, numerator_product, prime_product)
    assert Decimal("-0.093413") < lower
    assert upper < Decimal("-0.093412")

    log_109 = log_bounds(Decimal(109) / Decimal(100))
    log_110 = log_bounds(Decimal(11) / Decimal(10))
    assert upper + log_109[1] < Decimal("-0.0072")
    assert lower + log_110[0] > Decimal("0.0018")

    # The fixed-pivot power-law margin is increasing throughout the decimal slab.
    log_n = Decimal(DECIMAL_POWER) * log_bounds(10)[0]
    delta_derivative_upper = Decimal(2) / (
        log_bounds(2)[0] * (log_n + Decimal(2) * log_bounds(2)[0])
    )
    derivative_lower = (
        Decimal(1) / Decimal(5)
        - Decimal(2) * alpha[1]
        - Decimal(6) * delta_derivative_upper
    )
    assert derivative_lower > Decimal("0.051")

    print("PX1016--PX1018 decimal-2873 divisor improvement target: PASS")
    print(
        f"margin=[{lower},{upper}] "
        f"nine_percent_upper={upper + log_109[1]} "
        f"ten_percent_lower={lower + log_110[0]} "
        f"derivative_lower={derivative_lower}"
    )


if __name__ == "__main__":
    main()

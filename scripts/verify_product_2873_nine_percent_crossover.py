#!/usr/bin/env python3
"""Bracket where a nine-percent divisor improvement becomes sufficient."""
from __future__ import annotations

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext

from verify_product_2873_divisor_improvement_target import (
    DECIMAL_POWER,
    PIVOT_PRIME,
    PRECISION,
    TARGET_POWER,
    exponent_at_pivot,
    log_bounds,
    margin_bounds,
    positive_division_bounds,
    primes_below,
)


def mul_lower(first: Decimal, second: Decimal, third: Decimal) -> Decimal:
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_FLOOR
        return first * second * third


def mul_upper(first: Decimal, second: Decimal, third: Decimal) -> Decimal:
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        return first * second * third


def main() -> None:
    primes = primes_below(PIVOT_PRIME + 1)
    log_2 = log_bounds(2)
    log_10 = log_bounds(10)
    alpha = positive_division_bounds(log_2, log_bounds(PIVOT_PRIME))

    numerator_product = 1
    prime_product = 1
    for prime in primes[:-1]:
        exponent = exponent_at_pivot(prime, alpha)
        numerator_product *= exponent + 1
        prime_product *= prime**exponent

    assert prime_product < 10**TARGET_POWER < prime_product * PIVOT_PRIME
    margin_lower, margin_upper = margin_bounds(
        alpha, numerator_product, prime_product
    )
    log_109 = log_bounds(Decimal(109) / Decimal(100))
    endpoint_lower = margin_lower + log_109[0]
    endpoint_upper = margin_upper + log_109[1]
    assert endpoint_upper < 0

    # The exact derivative used by the fixed-pivot margin is
    # 1/5 - 2 alpha - 6 delta'(log N), with delta' positive and decreasing.
    # The lower bound uses the maximum delta' at the slab's left endpoint.
    log_n_lower = Decimal(DECIMAL_POWER) * log_10[0]
    delta_derivative_upper = Decimal(2) / (
        log_2[0] * (log_n_lower + Decimal(2) * log_2[0])
    )
    derivative_lower = (
        Decimal(1) / Decimal(5)
        - Decimal(2) * alpha[1]
        - Decimal(6) * delta_derivative_upper
    )
    # Dropping the negative delta' term gives a uniform derivative upper bound.
    derivative_upper = Decimal(1) / Decimal(5) - Decimal(2) * alpha[0]
    assert derivative_lower > Decimal("0.051")
    assert derivative_upper < Decimal("0.054")

    insufficient_offset = Decimal("0.0585")
    sufficient_offset = Decimal("0.0616")
    insufficient_upper = endpoint_upper + mul_upper(
        derivative_upper, insufficient_offset, log_10[1]
    )
    sufficient_lower = endpoint_lower + mul_lower(
        derivative_lower, sufficient_offset, log_10[0]
    )
    assert insufficient_upper < Decimal("-0.0000025")
    assert sufficient_lower > Decimal("0.0000095")

    assert sufficient_offset - insufficient_offset == Decimal("0.0031")
    print("PX1143--PX1145 decimal-2873 nine-percent crossover: PASS")
    print(
        f"endpoint_nine_percent=[{endpoint_lower},{endpoint_upper}] "
        f"derivative=[{derivative_lower},{derivative_upper}] "
        f"insufficient_at={insufficient_offset} upper={insufficient_upper} "
        f"sufficient_at={sufficient_offset} lower={sufficient_lower}"
    )


if __name__ == "__main__":
    main()

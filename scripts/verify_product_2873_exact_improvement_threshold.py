#!/usr/bin/env python3
"""Bracket the exact multiplicative divisor improvement required at 10^2873."""
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


def exp_bounds(value: tuple[Decimal, Decimal]) -> tuple[Decimal, Decimal]:
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_FLOOR
        lower = value[0].exp()
    with localcontext() as context:
        context.prec = PRECISION
        context.rounding = ROUND_CEILING
        upper = value[1].exp()
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
    margin_lower, margin_upper = margin_bounds(
        alpha, numerator_product, prime_product
    )

    # The unique unchanged-inequality threshold is rho_* = exp(-M_*).
    threshold_lower, threshold_upper = exp_bounds(
        (-margin_upper, -margin_lower)
    )
    assert Decimal("1.0979139") < threshold_lower
    assert threshold_upper < Decimal("1.0979151")
    assert threshold_upper - threshold_lower < Decimal("0.0000012")

    insufficient = Decimal("1.097913")
    sufficient = Decimal("1.097916")
    insufficient_log = log_bounds(insufficient)
    sufficient_log = log_bounds(sufficient)
    assert margin_upper + insufficient_log[1] < 0
    assert margin_lower + sufficient_log[0] > 0

    print("PX1098--PX1100 exact decimal-2873 improvement threshold: PASS")
    print(
        f"margin=[{margin_lower},{margin_upper}] "
        f"rho_threshold=[{threshold_lower},{threshold_upper}] "
        f"width={threshold_upper-threshold_lower} "
        f"insufficient={insufficient} sufficient={sufficient}"
    )


if __name__ == "__main__":
    main()

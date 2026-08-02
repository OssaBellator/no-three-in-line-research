#!/usr/bin/env python3
"""Checks the sharpened alpha=8/109 divisor certificate and 10^2875 cutoff."""

from __future__ import annotations

import math


ETA = 1.0 / 12.0
LOG10 = math.log(10.0)
LOG2 = math.log(2.0)
LOG_N4 = 2875.0 * LOG10
DELTA = 33.0
PRODUCT_EXPONENT = 6425
PRODUCT_ROOT = 109
DIVISOR_LOG10_BOUND = PRODUCT_EXPONENT / PRODUCT_ROOT


def primes_below(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * limit
    sieve[:2] = b"\x00\x00"
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            start = prime * prime
            count = (limit - 1 - start) // prime + 1
            sieve[start:limit:prime] = b"\x00" * count
    return [value for value in range(2, limit) if sieve[value]]


def peak_exponent(prime: int) -> int:
    exponent = 0
    while (exponent + 2) ** 109 > prime**8 * (exponent + 1) ** 109:
        exponent += 1
    return exponent


def check_sharp_product_certificate() -> None:
    primes = [
        prime for prime in primes_below(1 << 14)
        if prime**8 < 2**109
    ]
    assert len(primes) == 1508
    assert primes[-1] == 12619

    numerator = 1
    denominator = 1
    exponents: list[int] = []
    for prime in primes:
        exponent = peak_exponent(prime)
        exponents.append(exponent)
        numerator *= (exponent + 1) ** 109
        denominator *= prime ** (8 * exponent)
        if exponent:
            assert (exponent + 1) ** 109 > prime**8 * exponent**109
        assert (exponent + 2) ** 109 <= prime**8 * (exponent + 1) ** 109

    assert min(exponents) == 1
    assert max(exponents) == 19
    assert numerator < 10**PRODUCT_EXPONENT * denominator
    assert numerator >= 10**(PRODUCT_EXPONENT - 1) * denominator


def logaddexp(first: float, second: float) -> float:
    high = max(first, second)
    return high + math.log(math.exp(first - high) + math.exp(second - high))


def delta_bar(log_n: float) -> float:
    return 7.0 + 2.0 * math.log2(log_n / LOG2 + 2.0)


def delta_bar_derivative(log_n: float) -> float:
    return 2.0 / (LOG2 * (log_n + 2.0 * LOG2))


def divisor_retained_margin(decimal_power: float) -> float:
    log_n = decimal_power * LOG10
    log_t = 0.6 * log_n
    log_b = math.log(256.0) + 2.0 * DELTA
    log_q2 = (
        math.log(ETA)
        + log_t
        - math.log(32768.0)
        - DIVISOR_LOG10_BOUND * LOG10
        - 4.0 * DELTA
        - (1.0 + 16.0 / 109.0) * log_n
    )
    return log_q2 + log_t - log_b


def check_cutoff() -> None:
    margin = 1.0 / 5.0 - 16.0 / 109.0
    assert abs(margin - 29.0 / 545.0) < 1e-15
    assert margin > 0.0

    depth = 1 + math.ceil(math.log2(LOG_N4 / LOG2 + 2.0))
    assert depth == 15
    assert 3 + 2 * depth == 33

    log_t = 0.6 * LOG_N4
    log_b = math.log(256.0) + 2.0 * DELTA
    log_q1 = (
        math.log(ETA)
        - math.log(16.0 * 1_310_720.0)
        - 2.0 * DELTA
        - math.log(math.log(4.0) + log_t)
    )

    assert log_q1 + log_t - log_b > 3800.0
    assert divisor_retained_margin(2875.0) > 0.09
    assert divisor_retained_margin(2874.0) < -0.02

    log_d_seed = (
        math.log(32780.0)
        + LOG_N4
        + math.log(1.0 + math.log(2.0) + LOG_N4)
    )
    log_k = logaddexp(math.log(2.0), (math.log(6.0) + log_d_seed) / 3.0)
    log_four_return = (
        (15.0 / 16.0) * (LOG_N4 - math.log(96.0))
        - math.log(48.0)
        - log_k
        - log_t
    )
    log_two_variable = LOG_N4 - math.log(64.0 * 48.0) - log_k - log_t
    log_partner = LOG_N4 - math.log(2.0 * DELTA + 2.0)

    assert log_four_return > 12.0
    assert log_two_variable > 420.0
    assert log_partner > 6600.0

    assert margin - 6.0 * delta_bar_derivative(9000.0) > 0.0
    smooth_handoff = (
        math.log(ETA)
        + margin * 9000.0
        - math.log(32768.0 * 256.0)
        - DIVISOR_LOG10_BOUND * LOG10
        - 6.0 * delta_bar(9000.0)
    )
    assert smooth_handoff > 118.0


def main() -> None:
    check_sharp_product_certificate()
    check_cutoff()
    print("PX952--PX955 sharp rational divisor cutoff verifier: PASS")


if __name__ == "__main__":
    main()

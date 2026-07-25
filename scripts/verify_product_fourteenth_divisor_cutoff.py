#!/usr/bin/env python3
"""Checks for PX483--PX487 fourteenth-power divisor cutoff."""

from __future__ import annotations

import math


ETA = 1.0 / 12.0
LOG10 = math.log(10.0)
LOG2 = math.log(2.0)
LOG_N2 = 2950.0 * LOG10
DELTA = 33.0


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
    while (exponent + 2) ** 14 > prime * (exponent + 1) ** 14:
        exponent += 1
    return exponent


def check_exact_product_certificate() -> None:
    primes = primes_below(1 << 14)
    assert len(primes) == 1900
    assert primes[-1] == 16381

    numerator = 1
    denominator = 1
    exponents: list[int] = []
    for prime in primes:
        exponent = peak_exponent(prime)
        exponents.append(exponent)
        numerator *= (exponent + 1) ** 14
        denominator *= prime**exponent

        # Verify the local sequence changes from increasing to nonincreasing.
        if exponent:
            assert (exponent + 1) ** 14 > prime * exponent**14
        assert (exponent + 2) ** 14 <= prime * (exponent + 1) ** 14

    assert min(exponents) == 1
    assert max(exponents) == 19
    assert numerator < 10 ** (72 * 14) * denominator


def check_effective_exponent() -> None:
    assert abs((6.0 / 5.0 - 1.0 - 1.0 / 7.0) - 2.0 / 35.0) < 1e-15
    assert 2.0 / 35.0 > 0.0


def logaddexp(first: float, second: float) -> float:
    high = max(first, second)
    return high + math.log(math.exp(first - high) + math.exp(second - high))


def delta_bar(log_n: float) -> float:
    return 7.0 + 2.0 * math.log2(log_n / LOG2 + 2.0)


def delta_bar_derivative(log_n: float) -> float:
    return 2.0 / (LOG2 * (log_n + 2.0 * LOG2))


def check_cutoff_start() -> None:
    depth = 1 + math.ceil(math.log2(LOG_N2 / LOG2 + 2.0))
    assert depth == 15
    assert 3 + 2 * depth == 33

    log_t = 0.6 * LOG_N2
    log_b = math.log(256.0) + 2.0 * DELTA
    log_q1 = (
        math.log(ETA)
        - math.log(16.0 * 1_310_720.0)
        - 2.0 * DELTA
        - math.log(math.log(4.0) + log_t)
    )
    log_q2 = (
        math.log(ETA)
        + log_t
        - math.log(32768.0)
        - 72.0 * LOG10
        - 4.0 * DELTA
        - (8.0 / 7.0) * LOG_N2
    )

    assert log_q1 + log_t - log_b > 3900.0
    assert log_q2 + log_t - log_b > 5.9

    log_d_seed = (
        math.log(32780.0)
        + LOG_N2
        + math.log(1.0 + math.log(2.0) + LOG_N2)
    )
    log_k = logaddexp(math.log(2.0), (math.log(6.0) + log_d_seed) / 3.0)
    log_four_return = (
        (15.0 / 16.0) * (LOG_N2 - math.log(96.0))
        - math.log(48.0)
        - log_k
        - log_t
    )
    log_two_variable = LOG_N2 - math.log(64.0 * 48.0) - log_k - log_t
    log_partner = LOG_N2 - math.log(2.0 * DELTA + 2.0)

    assert log_four_return > 13.0
    assert log_two_variable > 430.0
    assert log_partner > 6700.0


def check_monotonicity() -> None:
    for log_n in (LOG_N2, 8000.0, 9000.0):
        assert 0.6 - 0.6 / (math.log(4.0) + 0.6 * log_n) > 0.0
        assert 2.0 / 35.0 > 0.0
        assert 1.0 / 240.0 - 1.0 / (3.0 * log_n) > 0.0

    handoff = 9000.0
    derivative = delta_bar_derivative(handoff)
    assert 2.0 / 35.0 - 6.0 * derivative > 0.0

    smooth_q2_log_ratio = (
        math.log(ETA)
        + (2.0 / 35.0) * handoff
        - math.log(32768.0 * 256.0)
        - 72.0 * LOG10
        - 6.0 * delta_bar(handoff)
    )
    assert smooth_q2_log_ratio > 120.0


def main() -> None:
    check_exact_product_certificate()
    check_effective_exponent()
    check_cutoff_start()
    check_monotonicity()
    print("PX483--PX487 fourteenth-power divisor cutoff verifier: PASS")


if __name__ == "__main__":
    main()

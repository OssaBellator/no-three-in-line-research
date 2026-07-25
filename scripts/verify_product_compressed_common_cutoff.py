#!/usr/bin/env python3
"""Checks for PX479--PX482 compressed cutoff N1=10^3650."""

from __future__ import annotations

import math


LOG10 = math.log(10.0)
LOG2 = math.log(2.0)
LOG_N1 = 3650.0 * LOG10
UPPER_HANDOFF = 9000.0
ETA = 1.0 / 12.0
DELTA = 33.0


def delta_bar(log_n: float) -> float:
    return 7.0 + 2.0 * math.log2(log_n / LOG2 + 2.0)


def delta_bar_derivative(log_n: float) -> float:
    return 2.0 / (LOG2 * (log_n + 2.0 * LOG2))


def logaddexp(first: float, second: float) -> float:
    high = max(first, second)
    return high + math.log(math.exp(first - high) + math.exp(second - high))


def check_exact_depth_plateau() -> None:
    lower_argument_log2 = math.log2(LOG_N1 / LOG2 + 2.0)
    upper_argument_log2 = math.log2(UPPER_HANDOFF / LOG2 + 2.0)
    assert 13.0 < lower_argument_log2 < 14.0
    assert 13.0 < upper_argument_log2 < 14.0

    for log_n in (LOG_N1, 8500.0, UPPER_HANDOFF):
        depth = 1 + math.ceil(math.log2(log_n / LOG2 + 2.0))
        delta = 3 + 2 * depth
        assert depth == 15
        assert delta == 33


def check_starting_margins() -> None:
    log_t = 0.6 * LOG_N1
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
        - 27.0 * LOG10
        - 4.0 * DELTA
        - (7.0 / 6.0) * LOG_N1
    )

    assert log_q1 + log_t - log_b > 4000.0
    assert log_q2 + log_t - log_b > 1.5

    log_d_seed = (
        math.log(32780.0)
        + LOG_N1
        + math.log(1.0 + math.log(2.0) + LOG_N1)
    )
    log_k = logaddexp(math.log(2.0), (math.log(6.0) + log_d_seed) / 3.0)
    log_four_return_ratio = (
        (15.0 / 16.0) * (LOG_N1 - math.log(96.0))
        - math.log(48.0)
        - log_k
        - log_t
    )
    log_two_variable_ratio = (
        LOG_N1 - math.log(64.0 * 48.0) - log_k - log_t
    )
    log_partner_ratio = LOG_N1 - math.log(2.0 * DELTA + 2.0)

    assert log_four_return_ratio > 19.0
    assert log_two_variable_ratio > 500.0
    assert log_partner_ratio > 8000.0


def check_plateau_monotonicity() -> None:
    for log_n in (LOG_N1, 8500.0, UPPER_HANDOFF):
        q1_ratio_derivative = (
            0.6 - 0.6 / (math.log(4.0) + 0.6 * log_n)
        )
        q2_ratio_derivative = 1.0 / 30.0
        return_ratio_derivative = 1.0 / 240.0 - 1.0 / (3.0 * log_n)
        assert q1_ratio_derivative > 0.0
        assert q2_ratio_derivative > 0.0
        assert return_ratio_derivative > 0.0


def check_smooth_handoff() -> None:
    derivative = delta_bar_derivative(UPPER_HANDOFF)
    assert derivative < 3.0 / UPPER_HANDOFF
    assert 0.6 - 4.0 * derivative - 0.6 / (
        math.log(4.0) + 0.6 * UPPER_HANDOFF
    ) > 0.0
    assert 1.0 / 30.0 - 6.0 * derivative > 0.0
    assert delta_bar(UPPER_HANDOFF) > DELTA


def main() -> None:
    check_exact_depth_plateau()
    check_starting_margins()
    check_plateau_monotonicity()
    check_smooth_handoff()
    print("PX479--PX482 compressed common-cutoff verifier: PASS")


if __name__ == "__main__":
    main()

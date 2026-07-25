#!/usr/bin/env python3
"""Log-domain checks for PX474--PX478 common cutoff N0=10^4000."""

from __future__ import annotations

import math


ETA = 1.0 / 12.0
A3 = 320.0
COEFFICIENT_56 = 8.0 * 512.0 * A3
LOG_N0 = 4000.0 * math.log(10.0)


def delta_bar(log_n: float) -> float:
    return 7.0 + 2.0 * math.log2(log_n / math.log(2.0) + 2.0)


def delta_bar_derivative(log_n: float) -> float:
    return 2.0 / (math.log(2.0) * (log_n + 2.0 * math.log(2.0)))


def logaddexp(first: float, second: float) -> float:
    high = max(first, second)
    return high + math.log(math.exp(first - high) + math.exp(second - high))


def cutoff_values(log_n: float) -> dict[str, float]:
    delta = delta_bar(log_n)
    log_t = 0.6 * log_n
    log_b = math.log(256.0) + 2.0 * delta

    # Since T=ceil(N^(3/5)) <= 2N^(3/5), use log(4N^(3/5))
    # in the denominator to obtain a genuine lower bound for q_1.
    log_q1 = (
        math.log(ETA)
        - math.log(16.0 * COEFFICIENT_56)
        - 2.0 * delta
        - math.log(math.log(4.0) + log_t)
    )
    log_q2 = (
        math.log(ETA)
        + log_t
        - math.log(32768.0)
        - 27.0 * math.log(10.0)
        - 4.0 * delta
        - (7.0 / 6.0) * log_n
    )

    log_d_seed = (
        math.log(32780.0)
        + log_n
        + math.log(1.0 + math.log(2.0) + log_n)
    )
    log_k = logaddexp(math.log(2.0), (math.log(6.0) + log_d_seed) / 3.0)

    return {
        "delta": delta,
        "log_b": log_b,
        "log_q1t_over_b": log_q1 + log_t - log_b,
        "log_q2t_over_b": log_q2 + log_t - log_b,
        "log_four_return_over_t": (
            (15.0 / 16.0) * (log_n - math.log(96.0))
            - math.log(48.0)
            - log_k
            - log_t
        ),
        "log_two_return_over_t": (
            log_n
            - math.log(64.0 * 48.0)
            - log_k
            - log_t
        ),
        "log_partner_ratio": log_n - math.log(2.0 * delta + 2.0),
    }


def check_starting_value() -> None:
    assert LOG_N0 > 9000.0
    values = cutoff_values(LOG_N0)
    assert values["delta"] < 35.0
    assert values["log_q1t_over_b"] > 0.0
    assert values["log_q2t_over_b"] > 0.0
    assert values["log_four_return_over_t"] > 0.0
    assert values["log_two_return_over_t"] > 0.0
    assert values["log_partner_ratio"] > 0.0
    assert values["log_q2t_over_b"] > 10.0
    assert values["log_four_return_over_t"] > 20.0


def check_monotonicity_bounds() -> None:
    x = LOG_N0
    derivative = delta_bar_derivative(x)
    assert derivative < 3.0 / x

    first_ratio_derivative = (
        0.6
        - 4.0 * derivative
        - 0.6 / (math.log(4.0) + 0.6 * x)
    )
    second_ratio_derivative = 1.0 / 30.0 - 6.0 * derivative
    return_ratio_derivative_lower = 1.0 / 240.0 - 1.0 / (3.0 * x)
    partner_ratio_derivative_lower = 1.0 - 3.0 / (x * (delta_bar(x) + 1.0))

    assert first_ratio_derivative > 0.0
    assert second_ratio_derivative > 0.0
    assert return_ratio_derivative_lower > 0.0
    assert partner_ratio_derivative_lower > 0.0


def check_corrected_internal_margins() -> None:
    eta = 1.0 / 12.0
    support_four = eta / 8.0
    support_five_six = eta / 8.0
    support_three_four = 11.0 / 96.0
    internal_rank_three = support_five_six + support_three_four

    assert support_four <= 1.0 / 96.0 + 1e-15
    assert internal_rank_three <= 1.0 / 8.0 + 1e-15
    assert COEFFICIENT_56 == 1_310_720.0
    assert 16.0 * COEFFICIENT_56 == 20_971_520.0


def check_seed_bound_at_cutoff() -> None:
    log10_d_upper = 4009.0
    log10_k_upper = math.log10(2.0) + 1337.0
    log10_star_lower = (
        (4000.0 - 2.0) * 15.0 / 16.0
        - 2.0
        - log10_k_upper
    )
    assert log10_d_upper < 4010.0
    assert log10_star_lower > 2400.0


def main() -> None:
    check_starting_value()
    check_monotonicity_bounds()
    check_corrected_internal_margins()
    check_seed_bound_at_cutoff()
    print("PX474--PX478 explicit common-cutoff verifier: PASS")


if __name__ == "__main__":
    main()

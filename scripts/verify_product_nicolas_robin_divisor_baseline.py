#!/usr/bin/env python3
"""Verify the Nicolas--Robin subexponential divisor baseline."""
from __future__ import annotations

from decimal import Decimal, getcontext

getcontext().prec = 80

D = Decimal
ETA = D(1) / D(12)
LOG2 = D(2).ln()
LOG10 = D(10).ln()
K = D(769) / D(500)  # 1.538 > the Nicolas--Robin maximum 1.5379...
HANDOFF = D(9000)


def logaddexp(first: Decimal, second: Decimal) -> Decimal:
    high = max(first, second)
    return high + ((first - high).exp() + (second - high).exp()).ln()


def delta_bar(log_n: Decimal) -> Decimal:
    return D(7) + D(2) * (log_n / LOG2 + D(2)).ln() / LOG2


def delta_bar_derivative(log_n: Decimal) -> Decimal:
    return D(2) / (LOG2 * (log_n + D(2) * LOG2))


def ambient_divisor_log(log_n: Decimal) -> Decimal:
    # Nicolas--Robin: log tau(m) / log 2 < 1.538 log m / log log m.
    # Every integer entering the ambient divisor maximum is below N^2.
    log_m = D(2) * log_n
    return K * LOG2 * log_m / log_m.ln()


def active_margins(decimal_power: int) -> tuple[Decimal, ...]:
    log_n = D(decimal_power) * LOG10
    delta = delta_bar(log_n)
    log_t = D(3) * log_n / D(5)
    log_b = D(256).ln() + D(2) * delta

    log_q1 = (
        ETA.ln()
        - D(16 * 1_310_720).ln()
        - D(2) * delta
        - (D(4).ln() + log_t).ln()
    )
    logarithmic_retained = log_q1 + log_t - log_b

    divisor_retained = (
        log_n / D(5)
        - ambient_divisor_log(log_n)
        - (D(32768 * 256) / ETA).ln()
        - D(6) * delta
    )

    log_d_seed = D(32780).ln() + log_n + (D(1) + LOG2 + log_n).ln()
    log_k = logaddexp(D(2).ln(), (D(6).ln() + log_d_seed) / D(3))
    four_return = (
        D(15) * (log_n - D(96).ln()) / D(16)
        - D(48).ln()
        - log_k
        - log_t
    )
    two_variable = log_n - D(64 * 48).ln() - log_k - log_t
    terminal_partner = log_n - (D(2) * delta + D(2)).ln()

    return (
        divisor_retained,
        logarithmic_retained,
        four_return,
        two_variable,
        terminal_partner,
    )


def check_persistence(decimal_power: int) -> None:
    log_n = D(decimal_power) * LOG10
    assert log_n > HANDOFF
    log_m_log = (D(2) * log_n).ln()
    delta_prime = delta_bar_derivative(log_n)

    divisor_derivative = (
        D(1) / D(5)
        - D(2) * K * LOG2 * (log_m_log - D(1)) / (log_m_log * log_m_log)
        - D(6) * delta_prime
    )
    assert divisor_derivative > D("0.024")

    logarithmic_derivative = (
        D(3) / D(5)
        - D(4) * delta_prime
        - (D(3) / D(5)) / (D(4).ln() + D(3) * log_n / D(5))
    )
    assert logarithmic_derivative > D("0.59")

    seed_log_derivative = D(1) + D(1) / (D(1) + LOG2 + log_n)
    log_k_derivative_upper = seed_log_derivative / D(3)
    four_derivative_lower = D(15) / D(16) - D(3) / D(5) - log_k_derivative_upper
    two_variable_derivative_lower = D(2) / D(5) - log_k_derivative_upper
    partner_derivative_lower = D(1) - delta_prime / (delta_bar(log_n) + D(1))
    assert four_derivative_lower > D("0.004")
    assert two_variable_derivative_lower > D("0.066")
    assert partner_derivative_lower > D("0.999")

    # For log(2 log N)>2, every negative derivative correction above decreases
    # with log N, so these positive derivative bounds persist.
    assert log_m_log > D(2)


def main() -> None:
    below = active_margins(14103)
    cutoff = active_margins(14104)
    assert below[0] < D("-0.037")
    assert cutoff[0] > D("0.019")
    assert min(cutoff[1:]) > D(119)
    check_persistence(14104)
    print("PX994--PX996 Nicolas--Robin divisor baseline: PASS")
    print("decimal_cutoff=14104 divisor_margin=", cutoff[0])


if __name__ == "__main__":
    main()

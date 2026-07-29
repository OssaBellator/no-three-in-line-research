#!/usr/bin/env python3
"""Finite audits for PP3bxp--PP3bxr."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product
from math import floor


getcontext().prec = 80


def decimal_fraction(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def main() -> None:
    shell_grid = [
        Fraction(3, 4),
        Fraction(1),
        Fraction(5, 4),
        Fraction(3, 2),
        Fraction(2),
    ]
    thresholds = [Fraction(1), Fraction(5, 4), Fraction(3, 2), Fraction(2)]
    profiles_checked = 0
    contracting_examples = 0

    for kappas in product(shell_grid, repeat=4):
        positive = [max(kappa, Fraction(1)) for kappa in kappas]
        contractive = [min(kappa, Fraction(1)) for kappa in kappas]
        # Power profile a=1, beta=1: choose drop Delta_j=p_j for expansive
        # boundaries and zero otherwise.
        drops = [p if p > 1 else Fraction(0) for p in positive]
        J0 = sum(drops, Fraction(0))
        B = max(positive)

        for threshold in thresholds[:-1]:
            q_i = sum(p > threshold for p in positive)
            eta_i = threshold
            assert q_i * eta_i <= J0
            assert q_i <= floor(J0 / eta_i)

        discrete_bound = Fraction(1)
        for i in range(len(thresholds) - 1):
            q_bound = floor(J0 / thresholds[i])
            discrete_bound *= (thresholds[i + 1] / thresholds[i]) ** q_bound
        actual_positive = Fraction(1)
        for p in positive:
            actual_positive *= p
        assert actual_positive <= discrete_bound

        if B > 1:
            exponent = decimal_fraction(J0 * (1 - 1 / B))
        else:
            exponent = Decimal(0)
        actual_log = sum(decimal_fraction(p).ln() for p in positive)
        assert actual_log <= exponent + Decimal("1e-60")

        Cprod = Fraction(1)
        for c in contractive:
            Cprod *= c
        tau = Fraction(1, 3)
        if decimal_fraction(tau * Cprod).ln() + actual_log < 0:
            contracting_examples += 1
        profiles_checked += 1

    print({
        "all_checks_passed": True,
        "profiles_checked": profiles_checked,
        "contracting_profiles_at_tau_one_third": contracting_examples,
        "decimal_precision": getcontext().prec,
    })


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact rational audits for PP3byi--PP3byk."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def minimal_drop(p: Fraction, base: Fraction) -> int:
    drop = 0
    power = Fraction(1)
    while power < p:
        drop += 1
        power *= base
    return drop


def main() -> None:
    shell_values = [
        Fraction(3, 4),
        Fraction(1),
        Fraction(6, 5),
        Fraction(3, 2),
        Fraction(9, 4),
    ]
    base = Fraction(3, 2)
    tau = Fraction(1, 5)
    profiles = 0
    contracting = 0
    strict_improvements = 0

    for kappas in product(shell_values, repeat=4):
        positives = [max(kappa, Fraction(1)) for kappa in kappas]
        contractive = [min(kappa, Fraction(1)) for kappa in kappas]
        drops = [minimal_drop(p, base) for p in positives]
        J = [sum(drops)]
        for drop in drops:
            J.append(J[-1] - drop)
        assert J[-1] == 0
        assert all(J[i] >= J[i + 1] for i in range(4))

        for index, p in enumerate(positives):
            assert p <= base ** (J[index] - J[index + 1])

        positive_product = Fraction(1)
        cprod = Fraction(1)
        actual_product = Fraction(1)
        for p, c, kappa in zip(positives, contractive, kappas):
            positive_product *= p
            cprod *= c
            actual_product *= kappa
        telescoped = base ** (J[0] - J[-1])
        assert positive_product <= telescoped
        assert actual_product == positive_product * cprod
        assert tau * actual_product <= tau * cprod * telescoped

        if tau * cprod * telescoped < 1:
            contracting += 1
        if cprod < 1 and tau * cprod * telescoped < tau * telescoped:
            strict_improvements += 1
        profiles += 1

    sample = [Fraction(6, 5), Fraction(9, 4), Fraction(1), Fraction(3, 2)]
    extra_drops = [2, 3, 1, 2]
    assert all(p <= base**drop for p, drop in zip(sample, extra_drops))
    J = [sum(extra_drops)]
    for drop in extra_drops:
        J.append(J[-1] - drop)
    product_sample = Fraction(1)
    for p in sample:
        product_sample *= p
    assert product_sample <= base ** (J[0] - J[-1])

    print({
        "all_checks_passed": True,
        "profiles_checked": profiles,
        "base": str(base),
        "terminal_factor": str(tau),
        "profiles_certified_contracting": contracting,
        "profiles_with_strict_contractive_credit": strict_improvements,
    })


if __name__ == "__main__":
    main()

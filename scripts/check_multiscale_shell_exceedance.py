#!/usr/bin/env python3
"""Exhaustively verify the discrete and hybrid shell bounds PP3bww--PP3bwx."""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product


def math_product(values: list[Fraction] | tuple[Fraction, ...]) -> Fraction:
    result = Fraction(1)
    for value in values:
        result *= value
    return result


def main() -> None:
    values = [
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(1),
        Fraction(6, 5),
        Fraction(3, 2),
        Fraction(2),
    ]
    thresholds = [Fraction(1), Fraction(5, 4), Fraction(3, 2), Fraction(2)]
    checked = 0
    maximum_slack = Fraction(0)

    for factors in product(values, repeat=4):
        positive = [max(value, Fraction(1)) for value in factors]
        contractive = [min(value, Fraction(1)) for value in factors]
        cprod = math_product(contractive)
        q = [
            sum(value > thresholds[i] for value in positive)
            for i in range(len(thresholds) - 1)
        ]
        envelope = Fraction(1)
        for i, count in enumerate(q):
            envelope *= (thresholds[i + 1] / thresholds[i]) ** count
        actual = math_product(factors)
        assert actual <= cprod * envelope

        strong = [value for value in factors if value > Fraction(3, 2)]
        mild = [value for value in factors if Fraction(1) < value <= Fraction(3, 2)]
        mild_excess = sum((value - 1 for value in mild), Fraction())
        hybrid = cprod * (Fraction(2) ** len(strong))
        if mild:
            hybrid *= (Fraction(1) + mild_excess / len(mild)) ** len(mild)
        assert actual <= hybrid
        maximum_slack = max(maximum_slack, cprod * envelope - actual)
        checked += 1

    print(
        json.dumps(
            {
                "profiles_checked": checked,
                "thresholds": [str(value) for value in thresholds],
                "maximum_discrete_envelope_slack": str(maximum_slack),
                "all_checks_passed": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

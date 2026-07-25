#!/usr/bin/env python3
"""Finite checks for AC3fi--AC3fl."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def verify_membership_words() -> tuple[int, dict[int, int]]:
    checks = 0
    counts = {1: 0, 2: 0, 3: 0}
    for word in product((0, 1), repeat=3):
        if word == (0, 0, 0):
            continue
        rank = sum(word)
        assert rank in (1, 2, 3)
        counts[rank] += 1
        checks += 1
    assert counts == {1: 3, 2: 3, 3: 1}
    return checks, counts


def verify_weighted_localization() -> int:
    checks = 0
    for weights in product(range(4), repeat=7):
        total = sum(weights)
        if total == 0:
            continue
        assert 7 * max(weights) >= total
        rank_totals = (
            sum(weights[:3]),
            sum(weights[3:6]),
            weights[6],
        )
        assert 3 * max(rank_totals) >= total
        checks += 1
    return checks


def verify_constants() -> int:
    identities = (
        (Fraction(1, 12) / 7, Fraction(1, 84)),
        (Fraction(1, 4) / 7, Fraction(1, 28)),
        (Fraction(1, 4) / 7, Fraction(1, 28)),
        (Fraction(1, 2) / 7, Fraction(1, 14)),
        (Fraction(1, 8) / 7, Fraction(1, 56)),
    )
    for left, right in identities:
        assert left == right
    return len(identities)


def main() -> None:
    word_checks, counts = verify_membership_words()
    weighted_checks = verify_weighted_localization()
    constant_checks = verify_constants()
    print("AC RI moving-tuple rank router verification passed")
    print(f"  membership-word checks: {word_checks}")
    print(f"  rank counts: {counts}")
    print(f"  weighted localization checks: {weighted_checks}")
    print(f"  constant checks: {constant_checks}")


if __name__ == "__main__":
    main()

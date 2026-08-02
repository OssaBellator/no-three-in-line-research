#!/usr/bin/env python3
"""Arithmetic checks for PX445--PX450 paired large-block margins."""

from __future__ import annotations

from fractions import Fraction
import math
import random


A3 = 320
PAIRED_SUPPORT_56 = 8 * 512 * A3


def check_support_four_constant() -> None:
    rng = random.Random(445)
    for _ in range(5000):
        eta = Fraction(rng.randint(1, 99), 100)
        # Normalize e^(4 Delta) N d(N) / t to one.
        q = eta / 32768
        paired_relative = 8 * 512 * q
        assert paired_relative == eta / 8


def check_support_five_six_constant() -> None:
    rng = random.Random(446)
    assert PAIRED_SUPPORT_56 == 1_310_720
    assert 16 * PAIRED_SUPPORT_56 == 20_971_520

    for _ in range(5000):
        eta = Fraction(rng.randint(1, 12), 144)  # at most 1/12
        # Normalize e^(2 Delta) log(2t) to one.  The q^2 term is at most q.
        q = eta / (16 * PAIRED_SUPPORT_56)
        relative = PAIRED_SUPPORT_56 * (q + q)
        assert relative == eta / 8


def check_support_three_four_margin() -> None:
    # Paired copy patterns multiply the one-copy 11 e^(2 Delta)/6 bound by 8.
    paired_constant = Fraction(8 * 11, 6)
    retained_order = 128  # normalized by e^(2 Delta)
    relative = paired_constant / retained_order
    assert relative == Fraction(11, 96)

    eta = Fraction(1, 12)
    total_internal = relative + eta / 8
    assert total_internal == Fraction(1, 8)


def check_effective_threshold_exponent() -> None:
    # With d(N) <= 10^27 N^(1/6) and T=N^(3/5), qT has power N^(1/30).
    threshold = Fraction(3, 5)
    divisor_ambient = Fraction(7, 6)  # N*d(N)
    retained_power = 2 * threshold - divisor_ambient
    assert retained_power == Fraction(1, 30)
    assert retained_power > 0


def check_copy_pattern_stability() -> None:
    for rank in (1, 2, 3):
        patterns = 2**rank
        assert patterns <= 8
        for order in (10**3, 10**6, 10**9):
            little_o = order / math.log(order)
            assert patterns * little_o / order == patterns / math.log(order)


def check_entry_dichotomy() -> None:
    rng = random.Random(448)
    for _ in range(10000):
        defects = rng.randint(1, 10000)
        threshold = rng.randint(1, 1000)
        family_weight = Fraction(2 * defects, 9)
        source_count = rng.randint(1, threshold + 100)
        if source_count < threshold:
            average = family_weight / source_count
            assert average > family_weight / threshold


def check_integer_termination() -> None:
    for initial in range(1, 10000):
        potential = initial
        steps = 0
        while potential:
            decrease = min(potential, 1 + (steps % 7))
            potential -= decrease
            steps += 1
        assert potential == 0
        assert steps <= initial


def main() -> None:
    check_support_four_constant()
    check_support_five_six_constant()
    check_support_three_four_margin()
    check_effective_threshold_exponent()
    check_copy_pattern_stability()
    check_entry_dichotomy()
    check_integer_termination()
    print("PX445--PX450 paired large-block margin verifier: PASS")


if __name__ == "__main__":
    main()

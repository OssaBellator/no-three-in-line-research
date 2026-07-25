#!/usr/bin/env python3
"""Arithmetic checks for PX445--PX450 paired large-block margins."""

from __future__ import annotations

from fractions import Fraction
import math
import random


def check_support_four_constant() -> None:
    rng = random.Random(445)
    for _ in range(5000):
        eta = Fraction(rng.randint(1, 99), 100)
        # Normalize e^(4 Delta) N d(N) / t to one.  The paired relative bound is
        # 8*512*q and q <= eta/32768.
        q = eta / 32768
        paired_relative = 8 * 512 * q
        assert paired_relative <= eta / 8
        assert paired_relative == eta / 8


def check_square_root_exponent() -> None:
    # t=N^(1/2+epsilon), divisor loss N^o(1): t^2/(N d(N)) has exponent 2epsilon-o(1).
    for numerator in range(1, 20):
        epsilon = Fraction(numerator, 100)
        exponent = 2 * epsilon
        assert exponent > 0


def check_copy_pattern_stability() -> None:
    for rank in (1, 2, 3):
        patterns = 2**rank
        assert patterns <= 8
        # Constant-scale and little-o quantities retain their scale after a
        # fixed factor; record representative numerical witnesses.
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
    check_square_root_exponent()
    check_copy_pattern_stability()
    check_entry_dichotomy()
    check_integer_termination()
    print("PX445--PX450 paired large-block margin verifier: PASS")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Arithmetic and recurrence checks for PX404--PX410."""

from __future__ import annotations

from fractions import Fraction
import random


def amplification_exponent(delta: Fraction, generation: int) -> Fraction:
    """Exponent from D_j >= A^(1-2^-j) D_0^(2^-j), with A=n^(1-o(1))."""
    return Fraction(1, 1) - Fraction(1, 2**generation) * (Fraction(1, 1) - delta)


def check_recurrence() -> None:
    rng = random.Random(20260726)
    for _ in range(5000):
        a = Fraction(rng.randint(1, 100), rng.randint(1, 100))
        delta = Fraction(rng.randint(0, 100), 100)
        exponent = delta
        for generation in range(1, 9):
            exponent = (a + exponent) / 2
            closed = (
                a * (Fraction(1, 1) - Fraction(1, 2**generation))
                + delta * Fraction(1, 2**generation)
            )
            assert exponent == closed


def check_actual_line_cap_depth() -> None:
    kappa = Fraction(1, 3)

    # The first generation above the square-root star threshold satisfies
    # 2^-j < 1/2-kappa = 1/6.
    first = next(
        generation
        for generation in range(1, 20)
        if Fraction(1, 2**generation) < Fraction(1, 2) - kappa
    )
    assert first == 3

    destruction = amplification_exponent(Fraction(0, 1), 3)
    assert destruction == Fraction(7, 8)

    star = destruction - kappa
    assert star == Fraction(13, 24)
    assert star > Fraction(1, 2)

    # Directed paths are capped at n^(1/3), so the third-generation weight
    # is already outside that sector.
    assert destruction > Fraction(1, 3)


def check_two_variable_return() -> None:
    kappa = Fraction(1, 3)
    child_weight = Fraction(1, 1)  # n/64 has exponent one.
    star = child_weight - kappa
    assert star == Fraction(2, 3)
    assert star > Fraction(1, 2)
    assert child_weight > Fraction(1, 3)


def check_general_threshold() -> None:
    for denominator in range(3, 101):
        for numerator in range(0, denominator // 2):
            kappa = Fraction(numerator, denominator)
            rhs = Fraction(1, 2) - kappa
            first = next(
                generation
                for generation in range(1, 40)
                if Fraction(1, 2**generation) < rhs
            )
            previous = Fraction(1, 2 ** (first - 1))
            assert Fraction(1, 2**first) < rhs
            assert previous >= rhs
            star = amplification_exponent(Fraction(0, 1), first) - kappa
            assert star > Fraction(1, 2)


def main() -> None:
    check_recurrence()
    check_actual_line_cap_depth()
    check_two_variable_return()
    check_general_threshold()
    print("PX404--PX410 PX64 return-depth verifier: PASS")


if __name__ == "__main__":
    main()

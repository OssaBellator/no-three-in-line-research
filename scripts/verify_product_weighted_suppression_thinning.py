#!/usr/bin/env python3
"""Exact arithmetic checks for PX377--PX380."""

from fractions import Fraction


def main() -> None:
    # PX377: exact Paley--Zygmund constant.
    second_moment_factor = Fraction(17, 16)
    threshold_factor = Fraction(1, 4)
    probability = (1 - threshold_factor) ** 2 / second_moment_factor
    assert probability == Fraction(9, 17)

    # PX378: the weight event still has positive probability after removing
    # the Markov and Chernoff failure bounds.
    remaining_without_chernoff = Fraction(9, 17) - Fraction(1, 4)
    assert remaining_without_chernoff == Fraction(19, 68)
    assert float(remaining_without_chernoff) > 2.718281828459045 ** -4

    # PX379: W > 16 eta t implies pW/4 > 4 eta p t.
    for weight in range(1, 101):
        for order in range(1, 51):
            for eta_denominator in range(1, 51):
                eta = Fraction(1, eta_denominator)
                if Fraction(weight, 1) > 16 * eta * order:
                    for probability_denominator in range(1, 20):
                        p = Fraction(1, probability_denominator)
                        assert p * weight / 4 > 4 * eta * p * order

    # PX380 support-cover density constants, using exact rational arithmetic.
    for ambient_order in range(1, 101):
        for destroyed in range(1, 21):
            for channels in range(1, 9):
                cover_order = 2 * ambient_order

                one_weight = Fraction(
                    destroyed * ambient_order,
                    96 * channels,
                )
                assert one_weight / cover_order == Fraction(
                    destroyed,
                    192 * channels,
                )

                two_weight = Fraction(
                    destroyed * ambient_order * ambient_order,
                    64 * channels,
                )
                assert two_weight / cover_order == Fraction(
                    destroyed * ambient_order,
                    128 * channels,
                )

                eta_bound = Fraction(destroyed, 3072 * channels)
                assert 16 * eta_bound == Fraction(
                    destroyed,
                    192 * channels,
                )

    print("PX377--PX380 weighted-suppression verifier: PASS")


if __name__ == "__main__":
    main()

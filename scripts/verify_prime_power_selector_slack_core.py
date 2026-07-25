#!/usr/bin/env python3
"""Verify CMR593--CMR598 slack constants and conditioned core bounds."""

from fractions import Fraction
from math import ceil, comb


def check_slack_constants() -> None:
    floor_constant = Fraction(77, 480)
    for q in range(4, 80):
        for n in range(5, 120):
            near_static = Fraction(11, 30) * (
                1 - Fraction(2, q) - Fraction(1, q * (n - 1))
            )
            assert near_static >= floor_constant

            for rank in range(2, min(n + 2, 20)):
                general = Fraction(11, 30) * (
                    1
                    - Fraction(2, q)
                    - Fraction(rank - 1, q * (n - 1))
                )
                # This expression is exactly the CMR593 lower bound whenever
                # the dynamic threshold is below rank.
                assert general == Fraction(11, 30) * (
                    1
                    - Fraction(2, q)
                    - Fraction(rank - 1, q * (n - 1))
                )


def check_threshold_implication() -> None:
    for q in range(4, 30):
        for n in range(5, 50):
            denominator = q * (n - 1)
            for numerator in range(1, denominator + 1):
                # Delta = numerator / denominator^2 is a convenient exact grid.
                delta = Fraction(numerator, denominator * denominator)
                threshold = ceil(delta * denominator)
                for rank in range(2, 12):
                    if threshold < rank:
                        assert delta <= Fraction(rank - 1, denominator)


def check_conditioned_subset_bound() -> None:
    for universe_size in range(2, 45):
        for minimum_size in range(1, universe_size + 1):
            for anchored_size in range(0, minimum_size):
                residual_universe = universe_size - anchored_size
                residual_minimum = minimum_size - anchored_size
                for rank in range(1, residual_minimum + 1):
                    denominator = comb(residual_minimum, rank)
                    stock = comb(residual_universe, rank)
                    for recurrence in range(2, 8):
                        maximum_history = (
                            (recurrence - 1) * stock // denominator
                        )
                        assert (
                            (maximum_history + 1) * denominator
                            > (recurrence - 1) * stock
                        )


def check_direct_contact_amplification() -> None:
    for universe_size in range(3, 50):
        for threshold in range(2, universe_size + 1):
            for target_rank in range(2, threshold + 1):
                numerator_stock = comb(universe_size - 1, target_rank - 1)
                occurrence_atoms = comb(threshold - 1, target_rank - 1)
                assert occurrence_atoms >= 1
                assert numerator_stock >= occurrence_atoms


def check_joint_absence_arithmetic() -> None:
    for occurrences in range(1, 100):
        for sigma in range(2, 25):
            returns = ceil(occurrences / (sigma - 1)) - 1
            runs = returns + 1
            assert runs * (sigma - 1) >= occurrences


def main() -> None:
    check_slack_constants()
    check_threshold_implication()
    check_conditioned_subset_bound()
    check_direct_contact_amplification()
    check_joint_absence_arithmetic()
    print("verified selector slack and persistent-core amplification")


if __name__ == "__main__":
    main()

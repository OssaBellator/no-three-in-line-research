#!/usr/bin/env python3
"""Verify the BDA3c finite-profile localization inequalities."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def positive_rank_pattern(ranks: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted((rank for rank in ranks if rank), reverse=True))


def verify() -> None:
    kernels = (
        Fraction(1, 2),
        Fraction(1, 3),
        Fraction(2, 5),
        Fraction(1, 4),
    )
    term_count = len(kernels)

    for profile_count in range(1, 4):
        for labels in product(range(profile_count), repeat=term_count):
            for weights in product(range(4), repeat=term_count):
                profile_sums = [Fraction(0) for _ in range(profile_count)]
                raw_sums = [0 for _ in range(profile_count)]
                profile_maxima = [Fraction(0) for _ in range(profile_count)]
                for label, weight, kernel in zip(labels, weights, kernels):
                    profile_sums[label] += weight * kernel
                    raw_sums[label] += weight
                    profile_maxima[label] = max(
                        profile_maxima[label], kernel
                    )

                collateral = sum(
                    (weight * kernel for weight, kernel in zip(weights, kernels)),
                    Fraction(0),
                )
                assert sum(profile_sums, Fraction(0)) == collateral
                assert all(
                    profile_sums[label]
                    <= profile_maxima[label] * raw_sums[label]
                    for label in range(profile_count)
                )

                for fixed in range(5):
                    for paid in range(9):
                        if Fraction(paid) > fixed + collateral:
                            continue
                        obstruction = max(0, paid - fixed)
                        heaviest = max(profile_sums)
                        assert heaviest * profile_count >= obstruction
                        label = profile_sums.index(heaviest)
                        if heaviest:
                            assert (
                                raw_sums[label] * profile_maxima[label]
                                >= heaviest
                            )

    observed_patterns = {
        positive_rank_pattern(ranks)
        for ranks in product(range(4), repeat=3)
        if 1 <= sum(ranks) <= 3
    }
    assert observed_patterns == {
        (1,),
        (2,),
        (1, 1),
        (3,),
        (2, 1),
        (1, 1, 1),
    }


def main() -> None:
    verify()
    print("BDA profile localization: exhaustive rational checks passed")


if __name__ == "__main__":
    main()

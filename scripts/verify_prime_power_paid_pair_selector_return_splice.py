#!/usr/bin/env python3
"""Finite checks for CMR1558--CMR1565."""

from __future__ import annotations

from fractions import Fraction
from random import Random


def selector_threshold(
    candidate_expectation: Fraction,
    unavailable_count: int,
    side: int,
) -> int:
    if not 0 <= candidate_expectation < 1:
        raise ValueError("candidate expectation must lie in [0,1)")
    if side < 2 or unavailable_count < 0:
        raise ValueError("invalid side or unavailable count")
    surcharge = Fraction(2, 1) + Fraction(unavailable_count, side - 1)
    return surcharge // (1 - candidate_expectation) + 1


def verify_exact_thresholds() -> int:
    checked = 0
    for side in range(3, 20):
        for unavailable_count in range(min(side * side, 60) + 1):
            surcharge = Fraction(2, 1) + Fraction(
                unavailable_count, side - 1
            )
            for denominator in range(2, 15):
                for numerator in range(denominator):
                    expectation = Fraction(numerator, denominator)
                    threshold = selector_threshold(
                        expectation, unavailable_count, side
                    )
                    assert expectation + surcharge / threshold < 1
                    if threshold > 1:
                        assert expectation + surcharge / (threshold - 1) >= 1
                    checked += 1
    return checked


def verify_restoration_histories() -> tuple[int, int]:
    rng = Random(1558)
    histories = 0
    incidences = 0
    for side in range(3, 16):
        universe = [
            (left, right)
            for left in range(side)
            for right in range(side)
        ]
        for _ in range(80):
            seen: set[tuple[int, int]] = set()
            first = 0
            repeated = 0
            total = 0
            for _episode in range(rng.randint(1, 50)):
                restored = rng.sample(
                    universe,
                    rng.randint(0, min(side, len(universe))),
                )
                for edge in restored:
                    total += 1
                    if edge in seen:
                        repeated += 1
                    else:
                        seen.add(edge)
                        first += 1
            assert total == first + repeated
            assert first == len(seen) <= side * side
            histories += 1
            incidences += total
    return histories, incidences


def verify_two_row_criterion() -> int:
    rng = Random(1562)
    checked = 0
    for _ in range(100_000):
        denominator = rng.randint(1, 50)
        return_to_return = Fraction(
            rng.randint(0, denominator + 10), denominator
        )
        return_to_selector = Fraction(
            rng.randint(0, denominator + 10), denominator
        )
        selector_to_return = rng.randint(0, 20)

        condition = (
            return_to_return
            + return_to_selector * selector_to_return
            < 1
        )

        if condition:
            if return_to_selector == 0:
                selector_weight = Fraction(selector_to_return + 1, 1)
            else:
                upper = (1 - return_to_return) / return_to_selector
                selector_weight = (
                    Fraction(selector_to_return, 1) + upper
                ) / 2
            assert selector_to_return < selector_weight
            assert (
                return_to_return
                + return_to_selector * selector_weight
                < 1
            )
        else:
            if return_to_selector == 0:
                assert return_to_return >= 1
            else:
                assert (
                    (1 - return_to_return) / return_to_selector
                    <= selector_to_return
                )
        checked += 1
    return checked


def verify_uniform_gap_caps() -> int:
    checked = 0
    for side in range(3, 30):
        for gap_denominator in range(2, 20):
            for gap_numerator in range(1, gap_denominator + 1):
                gap = Fraction(gap_numerator, gap_denominator)
                for unavailable_cap in range(
                    min(side * side, 40) + 1
                ):
                    cap = (
                        Fraction(2, 1)
                        + Fraction(unavailable_cap, side - 1)
                    ) // gap
                    for denominator in range(2, 12):
                        for numerator in range(denominator):
                            expectation = Fraction(numerator, denominator)
                            if expectation <= 1 - gap:
                                threshold = selector_threshold(
                                    expectation,
                                    unavailable_cap,
                                    side,
                                )
                                assert threshold - 1 <= cap
                                checked += 1
    return checked


def main() -> None:
    threshold_checks = verify_exact_thresholds()
    histories, incidences = verify_restoration_histories()
    matrix_checks = verify_two_row_criterion()
    gap_checks = verify_uniform_gap_caps()
    print(
        "verified paid-pair selector return splice: "
        f"{threshold_checks} exact thresholds, "
        f"{histories} restoration histories with {incidences} incidences, "
        f"{matrix_checks} two-row systems, and "
        f"{gap_checks} uniform-gap caps"
    )


if __name__ == "__main__":
    main()

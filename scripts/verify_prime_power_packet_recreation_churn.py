#!/usr/bin/env python3
"""Finite and arithmetic checks for CMR418--CMR421."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import log


def verify_universal_recreation_support() -> None:
    universe = set(range(7))
    triples = [set(choice) for choice in combinations(universe, 3)]
    subsets = [
        {value for value in universe if mask & (1 << value)}
        for mask in range(1 << len(universe))
    ]

    for before in subsets:
        conflicts = [triple for triple in triples if not triple <= before]
        maximum_degree = max(
            (sum(edge in triple for triple in conflicts) for edge in universe),
            default=0,
        )

        for returned in subsets:
            after = before | returned
            recreated = [triple for triple in conflicts if triple <= after]
            assert all(triple & returned for triple in recreated)
            assert len(recreated) <= len(returned) * maximum_degree


def verify_harmonic_degree_charges() -> None:
    for side in range(5, 500):
        for lower in (1, 2, 5, 10, max(1, side // 4)):
            upper = min(side, 2 * lower)
            heights = range(lower, upper)
            weight = sum(Fraction(1, height) for height in heights)
            degree_bound = 2 * (side - 1) ** 2 * weight

            for returned_count in (0, 1, side // 3, side):
                recreation_bound = degree_bound * returned_count
                assert recreation_bound >= 0
                if weight < Fraction(3, 2):
                    assert recreation_bound < 3 * side * side * returned_count + 1


def verify_total_weight_bound() -> None:
    maximum_side = 10_000
    harmonic = [0.0] * maximum_side
    for value in range(1, maximum_side):
        harmonic[value] = harmonic[value - 1] + 1.0 / value

    for side in range(5, maximum_side):
        for lower in (1, 2, 5, max(1, side // 10)):
            if lower >= side:
                continue
            interval_sum = harmonic[side - 1] - harmonic[lower - 1]
            bound = 1 + log(side / lower)
            assert interval_sum <= bound + 1e-12

    # Keep a few exact rational checks alongside the linear floating-point sweep.
    for side in (5, 10, 50, 100, 500):
        for lower in (1, 2, 5, max(1, side // 10)):
            if lower >= side:
                continue
            exact = sum(Fraction(1, height) for height in range(lower, side))
            assert float(exact) <= 1 + log(side / lower)


def verify_first_dirty_schedule_accounting() -> None:
    for packet_count in range(1, 8):
        histories: list[tuple[tuple[bool, ...], int, int]] = [
            ((False,) * packet_count, 0, 0)
        ]

        for _ in range(6):
            next_histories: list[tuple[tuple[bool, ...], int, int]] = []
            for clean, installations, losses in histories:
                if all(clean):
                    next_histories.append((clean, installations, losses))
                    continue

                target = next(index for index, value in enumerate(clean) if not value)
                previously_clean = [
                    index for index, value in enumerate(clean) if value
                ]

                for mask in range(1 << len(previously_clean)):
                    updated = list(clean)
                    updated[target] = True
                    new_losses = 0
                    for bit, packet in enumerate(previously_clean):
                        if mask & (1 << bit):
                            updated[packet] = False
                            new_losses += 1

                    total_installations = installations + 1
                    total_losses = losses + new_losses
                    assert total_installations <= packet_count + total_losses
                    next_histories.append(
                        (tuple(updated), total_installations, total_losses)
                    )

            histories = next_histories[:5000]


def verify_combined_churn_bound() -> None:
    for side in (25, 49, 81, 125):
        for packets in range(1, 10):
            total_weight = Fraction(3 * packets, 4)
            for churn in (0, 1, side, packets * side):
                recreated = 2 * (side - 1) ** 2 * total_weight * churn
                losses = int(recreated)
                installations = packets + losses
                assert installations <= packets + int(recreated)


def main() -> None:
    verify_universal_recreation_support()
    verify_harmonic_degree_charges()
    verify_total_weight_bound()
    verify_first_dirty_schedule_accounting()
    verify_combined_churn_bound()
    print(
        "verified packet recreation churn: returned-edge support, harmonic "
        "degree charges, packet losses, and first-dirty schedule bounds"
    )


if __name__ == "__main__":
    main()

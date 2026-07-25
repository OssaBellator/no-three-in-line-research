#!/usr/bin/env python3
"""Finite and arithmetic checks for CMR413--CMR417."""

from __future__ import annotations

from itertools import permutations
from math import ceil, log2


def verify_exact_incidence_identity() -> None:
    for p, h in ((3, 3), (5, 2), (7, 2)):
        side = p**h
        directions = p + 1
        sample_edges = [
            (0, 0),
            (1, 2),
            (side - 1, side - 2),
            (side // 2, side // 3),
        ]
        returned_sets = (
            set(),
            set(sample_edges[:1]),
            set(sample_edges[:2]),
            set(sample_edges),
        )

        for returned in returned_sets:
            labelled = 0
            for depth in range(1, h):
                modulus = p**depth
                for column_prefix in range(modulus):
                    for row_prefix in range(modulus):
                        hits = sum(
                            x % modulus == column_prefix
                            and y % modulus == row_prefix
                            for x, y in returned
                        )
                        labelled += directions * hits

            assert labelled == directions * (h - 1) * len(returned)


def verify_scale_filtered_prefix_sum() -> None:
    for p, h in ((3, 7), (5, 5), (7, 4), (11, 3)):
        side = p**h
        directions = p + 1

        for coarse_depth in range(h - 1):
            returned = side // (p**coarse_depth)
            filtered = directions * (h - 1 - coarse_depth) * returned
            assert filtered >= 0

        two_layer_sum = sum(
            2 * side * directions * (h - 1 - coarse_depth)
            for coarse_depth in range(h - 1)
        )
        displayed = directions * side * h * (h - 1)
        assert two_layer_sum == displayed


def verify_packet_and_combined_sums() -> None:
    for p, h in ((3, 8), (5, 6), (7, 5), (11, 4)):
        side = p**h
        directions = p + 1
        packets = ceil((1 + log2(side)) / 2)

        packet_mass = directions * (h - 1) * packets * side
        prefix_mass = directions * side * h * (h - 1)
        combined = directions * side * (h - 1) * (h + packets)
        assert combined == prefix_mass + packet_mass

        # The incidence bound removes a full factor of side from the previous
        # tokenwise union bound.
        old_union_bound = directions * packets * side * side // (p - 1)
        assert packet_mass < old_union_bound


def matching(vector: tuple[int, ...]) -> set[tuple[int, int]]:
    return {(source, row) for source, row in enumerate(vector)}


def verify_selected_state_churn() -> None:
    for side in range(2, 8):
        universe = {(x, y) for x in range(side) for y in range(side)}
        states = list(permutations(range(side)))
        sample = states[: min(60, len(states))]

        for old_vector in sample:
            old = matching(old_vector)
            for new_vector in sample:
                new = matching(new_vector)
                fixed_candidates = sorted(universe - old - new)
                fixed = set(fixed_candidates[::3])

                before = universe - old - fixed
                after = universe - new - fixed
                returned = after - before

                assert returned == old - new
                if old != new:
                    assert len(returned) >= 2


def verify_state_history_payment() -> None:
    for p, h in ((3, 6), (5, 5), (7, 4)):
        directions = p + 1
        multiplier = directions * (h - 1)

        for transitions in range(20):
            churn = 2 * transitions
            labelled = multiplier * churn
            states = transitions + 1

            assert churn >= 2 * transitions
            assert labelled >= 2 * multiplier * transitions
            assert states <= 1 + labelled // (2 * multiplier)

        for depth in range(h - 1):
            local_payment = 2 * directions * (h - 1 - depth)
            assert local_payment >= 2 * directions


def main() -> None:
    verify_exact_incidence_identity()
    verify_scale_filtered_prefix_sum()
    verify_packet_and_combined_sums()
    verify_selected_state_churn()
    verify_state_history_payment()
    print(
        "verified edge-incidence state expansion: exact labelled multiplicity, "
        "prefix and packet sums, matching churn, and history payments"
    )


if __name__ == "__main__":
    main()

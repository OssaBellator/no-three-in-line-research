#!/usr/bin/env python3
"""Finite checks for CMR517--CMR521."""

from __future__ import annotations

from itertools import combinations, product
from math import ceil


def verify_one_token_incidence() -> None:
    for universe_size in range(1, 9):
        universe = range(universe_size)
        subsets = [
            set(choice)
            for size in range(1, universe_size + 1)
            for choice in combinations(universe, size)
        ]
        for episode_count in range(1, 5):
            for family_indices in product(range(len(subsets)), repeat=episode_count):
                family = [subsets[index] for index in family_indices]
                minimum_size = min(len(edge_set) for edge_set in family)
                for threshold in range(2, 6):
                    multiplicity = {
                        edge: sum(edge in edge_set for edge_set in family)
                        for edge in universe
                    }
                    persistent = max(multiplicity.values(), default=0) >= threshold
                    if not persistent:
                        assert (
                            episode_count * minimum_size
                            <= (threshold - 1) * universe_size
                        )


def absence_run_counts(availability: tuple[int, ...], times: list[int]) -> list[int]:
    run_at: dict[int, int] = {}
    current_run = -1
    previously_absent = False
    for index, is_available in enumerate(availability):
        is_absent = not bool(is_available)
        if is_absent and not previously_absent:
            current_run += 1
        if is_absent:
            run_at[index] = current_run
        previously_absent = is_absent

    counts: dict[int, int] = {}
    for time in times:
        run = run_at[time]
        counts[run] = counts.get(run, 0) + 1
    return list(counts.values())


def verify_absence_runs() -> None:
    for final_time in range(1, 9):
        for availability in product((0, 1), repeat=final_time + 1):
            absent_times = [
                index
                for index, is_available in enumerate(availability)
                if not is_available
            ]
            if not absent_times:
                continue

            reintroductions = sum(
                availability[index] and not availability[index - 1]
                for index in range(1, final_time + 1)
            )

            for mask in range(1, 1 << len(absent_times)):
                times = [
                    absent_times[index]
                    for index in range(len(absent_times))
                    if mask & (1 << index)
                ]
                run_counts = absence_run_counts(availability, times)
                assert len(run_counts) <= 1 + reintroductions
                assert max(run_counts) >= ceil(len(times) / (1 + reintroductions))

                for threshold in range(2, 7):
                    if max(run_counts) < threshold:
                        assert reintroductions >= ceil(
                            len(times) / (threshold - 1)
                        ) - 1


def verify_global_label_stock() -> None:
    for prime in (3, 5, 7):
        for height in range(2, 6):
            side = prime**height
            labels_per_edge = (prime + 1) * (height - 1)
            labelled_stock = labels_per_edge * side * side

            direct_count = 0
            for depth in range(1, height):
                modulus = prime**depth
                token_size = (side // modulus) ** 2
                token_count = modulus * modulus * (prime + 1)
                direct_count += token_count * token_size
            assert direct_count == labelled_stock


def verify_absorption_incidence() -> None:
    for edge_stock in range(1, 30):
        for episode_count in range(1, 20):
            for absorbed_size in range(1, edge_stock + 1):
                for threshold in range(2, 8):
                    if episode_count * absorbed_size > (threshold - 1) * edge_stock:
                        # Double counting forces a recurrent physical edge.
                        assert ceil(
                            episode_count * absorbed_size / edge_stock
                        ) >= threshold


def main() -> None:
    verify_one_token_incidence()
    verify_absence_runs()
    verify_global_label_stock()
    verify_absorption_incidence()
    print(
        "verified CMR517--CMR521: token incidence persistence, exact global "
        "labelled stock, absence-run/reintroduction arithmetic, and free-"
        "absorption episode bounds"
    )


if __name__ == "__main__":
    main()

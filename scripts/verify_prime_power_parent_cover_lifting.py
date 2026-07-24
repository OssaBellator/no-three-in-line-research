#!/usr/bin/env python3
"""Exact finite checks for CMR186--CMR189."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import ceil, floor, sqrt


PARETO_PROFILES = (
    (3, 0, 0),
    (2, 1, 1),
    (2, 2, 0),
    (2, 0, 3),
    (1, 2, 2),
    (1, 3, 1),
    (1, 4, 0),
    (1, 1, 4),
    (1, 0, 6),
    (0, 3, 3),
    (0, 4, 2),
    (0, 5, 1),
    (0, 6, 0),
    (0, 2, 5),
    (0, 1, 7),
    (0, 0, 9),
)


def derangements(t: int) -> list[tuple[int, ...]]:
    return [
        state
        for state in permutations(range(t))
        if all(state[row] != row for row in range(t))
    ]


def compatible_prescriptions(t: int, rank: int):
    for rows in combinations(range(t), rank):
        for columns in permutations(range(t), rank):
            if any(row == column for row, column in zip(rows, columns)):
                continue
            yield tuple(zip(rows, columns))


def cylinder(states: list[tuple[int, ...]], prescription) -> frozenset[int]:
    return frozenset(
        index
        for index, state in enumerate(states)
        if all(state[row] == column for row, column in prescription)
    )


def verify_cylinder_maxima(max_t: int) -> None:
    # Exact enumeration is intentionally kept to t<=6. The proof for arbitrary
    # t uses the derangement-density inequalities from CMR176.
    for t in range(5, max_t + 1):
        states = derangements(t)
        rank_maxima = {}
        for rank in (1, 2, 3):
            rank_maxima[rank] = max(
                len(cylinder(states, prescription))
                for prescription in compatible_prescriptions(t, rank)
            )
        assert rank_maxima[1] * (t - 1) == len(states)
        assert rank_maxima[2] < rank_maxima[1]
        assert rank_maxima[3] < rank_maxima[1]


def verify_minimum_rank_one_covers_at_five() -> None:
    t = 5
    states = derangements(t)
    universe = frozenset(range(len(states)))
    cells = [(row, column) for row in range(t) for column in range(t) if row != column]
    cell_cylinders = {cell: cylinder(states, (cell,)) for cell in cells}

    covers = []
    for chosen in combinations(cells, t - 1):
        union = frozenset().union(*(cell_cylinders[cell] for cell in chosen))
        if union == universe:
            covers.append(frozenset(chosen))

    expected = []
    for row in range(t):
        expected.append(frozenset((row, column) for column in range(t) if column != row))
    for column in range(t):
        expected.append(frozenset((row, column) for row in range(t) if row != column))

    assert set(covers) == set(expected)
    assert len(covers) == 2 * t


def profile_bound(t: int, profile: tuple[int, int, int]) -> Fraction:
    u1, u2, u3 = profile
    return (
        Fraction(u1, t - 1)
        + Fraction(30 * u2, 11 * t * (t - 1))
        + Fraction(30 * u3, 11 * t * (t - 1) * (t - 2))
    )


def verify_profile_lifting(max_t: int) -> None:
    maximum_at_five = max(profile_bound(5, profile) for profile in PARETO_PROFILES)
    assert maximum_at_five == Fraction(9, 11)

    for t in range(6, max_t + 1):
        maximum = max(profile_bound(t, profile) for profile in PARETO_PROFILES)
        assert maximum <= Fraction(3, t - 1)
        assert maximum < Fraction(9, 11)

    for profile in PARETO_PROFILES:
        previous = profile_bound(5, profile)
        for t in range(6, max_t + 1):
            current = profile_bound(t, profile)
            assert current < previous
            previous = current


def verify_matching_star_arithmetic(max_edges: int) -> None:
    for edge_count in range(4, max_edges + 1):
        r = floor(sqrt(edge_count / 2))
        assert r >= 1
        # If a maximal matching has size q<r, the weakest forced-degree bound
        # occurs at q=r-1. Checking that endpoint is enough.
        if r > 1:
            forced_degree = ceil(edge_count / (2 * (r - 1)))
            assert forced_degree >= r
        movable = ceil(r / 2)
        assert movable >= 1


def main() -> None:
    verify_cylinder_maxima(max_t=6)
    verify_minimum_rank_one_covers_at_five()
    verify_profile_lifting(max_t=500)
    verify_matching_star_arithmetic(max_edges=100_000)
    print(
        "verified parent cover lifting: minimum t-1 cover at t=5, "
        "uniform 9/11 terminal mass cap, and matching-star extraction"
    )


if __name__ == "__main__":
    main()

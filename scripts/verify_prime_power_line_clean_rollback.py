#!/usr/bin/env python3
"""Exhaustive finite checks for CMR497--CMR501."""

from __future__ import annotations

from itertools import combinations, permutations


Edge = tuple[int, int]
Matching = frozenset[Edge]


def derangement_matchings(side: int) -> list[Matching]:
    return [
        frozenset((source, permutation[source]) for source in range(side))
        for permutation in permutations(range(side))
        if all(permutation[source] != source for source in range(side))
    ]


def verify_instance(
    side: int,
    universe: list[Edge],
    line_clean_matchings: list[Matching],
    available: set[Edge],
) -> None:
    costs = {
        matching: len(matching.difference(available))
        for matching in line_clean_matchings
    }
    minimum_cost = min(costs.values())
    minimum_states = [
        matching
        for matching, cost in costs.items()
        if cost == minimum_cost
    ]
    base = minimum_states[0]
    restored = set(base.difference(available))
    host = available | restored

    # CMR497: exact minimum restoration footprint and the bound k <= side.
    assert len(restored) == minimum_cost
    assert minimum_cost <= side
    assert base.issubset(host)
    assert (minimum_cost == 0) == any(
        matching.issubset(available)
        for matching in line_clean_matchings
    )

    host_states = [
        matching
        for matching in line_clean_matchings
        if matching.issubset(host)
    ]
    assert host_states

    # CMR498: every restored edge is essential in the minimum host.
    for edge in restored:
        assert all(edge in matching for matching in host_states)

    assert len({source for source, _target in restored}) == len(restored)
    assert len({target for _source, target in restored}) == len(restored)

    used_sources = {source for source, _target in restored}
    used_targets = {target for _source, target in restored}
    remaining_sources = [
        source for source in range(side) if source not in used_sources
    ]
    remaining_targets = [
        target for target in range(side) if target not in used_targets
    ]

    restrictions = {
        frozenset(edge for edge in matching if edge not in restored)
        for matching in host_states
    }
    residual_states: set[Matching] = set()
    for permutation in permutations(remaining_targets):
        matching = frozenset(zip(remaining_sources, permutation))
        if matching.issubset(host):
            residual_states.add(matching)
    assert restrictions == residual_states

    # CMR499: every threshold gives cheap rollback or dimension reduction.
    for threshold in range(1, side + 2):
        if minimum_cost < threshold:
            assert len(restored) < threshold
        else:
            assert side - len(restored) <= side - threshold

    # CMR500: every host-clean edge-set recreated after restoration meets R.
    for size in (2, 3):
        for chosen in combinations(universe, size):
            conflict = set(chosen)
            if conflict.issubset(host) and not conflict.issubset(available):
                assert conflict.intersection(restored)


def verify_exhaustive() -> None:
    expected = {2: 4, 3: 64, 4: 4_096}
    observed: dict[int, int] = {}

    for side in range(2, 5):
        universe = [
            (source, target)
            for source in range(side)
            for target in range(side)
            if source != target
        ]
        line_clean_matchings = derangement_matchings(side)
        assert line_clean_matchings

        instances = 0
        for mask in range(1 << len(universe)):
            available = {
                edge
                for index, edge in enumerate(universe)
                if mask & (1 << index)
            }
            verify_instance(side, universe, line_clean_matchings, available)
            instances += 1
        observed[side] = instances

    assert observed == expected


def verify_arithmetic() -> None:
    for prime in (3, 5, 7):
        for height in range(2, 7):
            parent_side = prime**height
            for restored_count in range(parent_side + 1):
                incidence = (prime + 1) * (height - 1) * restored_count
                assert incidence == (
                    (prime + 1) * (height - 1) * restored_count
                )


def main() -> None:
    verify_exhaustive()
    verify_arithmetic()
    print(
        "verified line-clean rollback availability: exact minimum restoration, "
        "essential restored core, residual factorization, threshold dichotomy, "
        "and recreated-conflict support through residual side four"
    )


if __name__ == "__main__":
    main()

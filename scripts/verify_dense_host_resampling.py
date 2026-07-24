#!/usr/bin/env python3
"""Verify SRR1d/SRR3f stationary kernels in dense missing-edge hosts."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations

Matching = tuple[int, ...]
State = tuple[Matching, Matching]
Host = tuple[frozenset[int], ...]


def perfect_matchings(host: Host) -> list[Matching]:
    n = len(host)
    return [
        permutation
        for permutation in permutations(range(n))
        if all(permutation[row] in host[row] for row in range(n))
    ]


def switch(matching: Matching, first: int, second: int) -> Matching:
    result = list(matching)
    result[first], result[second] = result[second], result[first]
    return tuple(result)


def column_degrees(host: Host) -> list[int]:
    n = len(host)
    return [
        sum(column in host[row] for row in range(n))
        for column in range(n)
    ]


def verify_symmetric_kernel(
    states: list[object],
    flawed: set[object],
    neighbours: dict[object, list[object]],
) -> None:
    transitions: dict[tuple[object, object], Fraction] = defaultdict(Fraction)
    reverse_sources: dict[object, set[object]] = defaultdict(set)
    row_sums: dict[object, Fraction] = defaultdict(Fraction)
    column_sums: dict[object, Fraction] = defaultdict(Fraction)

    for source in flawed:
        targets = neighbours[source]
        assert targets
        weight = Fraction(1, len(targets))
        for target in targets:
            assert target not in flawed
            transitions[source, target] += weight
            transitions[target, source] += weight
            row_sums[source] += weight
            column_sums[target] += weight
            row_sums[target] += weight
            column_sums[source] += weight
            reverse_sources[target].add(source)

    assert all(len(sources) <= 1 for sources in reverse_sources.values())
    for state in states:
        if state in flawed:
            continue
        used = row_sums[state]
        assert used <= 1
        self_loop = 1 - used
        transitions[state, state] += self_loop
        row_sums[state] += self_loop
        column_sums[state] += self_loop

    for state in states:
        assert row_sums[state] == 1
        assert column_sums[state] == 1

    assert all(
        weight == transitions[target, source]
        for (source, target), weight in transitions.items()
    )


def verify_one_layer(host: Host) -> None:
    n = len(host)
    matchings = perfect_matchings(host)
    columns = column_degrees(host)
    state_set = set(matchings)
    for row, neighbours_in_host in enumerate(host):
        for column in neighbours_in_host:
            flawed = {
                matching for matching in matchings if matching[row] == column
            }
            neighbours: dict[object, list[object]] = {}
            lower = len(host[row]) + columns[column] - n - 1
            assert lower >= 1
            for matching in flawed:
                valid: list[object] = []
                for partner in range(n):
                    if partner == row:
                        continue
                    if matching[partner] not in host[row]:
                        continue
                    if column not in host[partner]:
                        continue
                    target = switch(matching, row, partner)
                    assert target in state_set
                    assert target[row] != column
                    valid.append(target)
                assert len(valid) >= lower
                neighbours[matching] = valid
            verify_symmetric_kernel(
                list(matchings),
                set(flawed),
                neighbours,
            )


def verify_two_layer(host: Host) -> None:
    n = len(host)
    matchings = perfect_matchings(host)
    columns = column_degrees(host)
    states = [
        (first, second)
        for first in matchings
        for second in matchings
        if all(first[row] != second[row] for row in range(n))
    ]
    state_set = set(states)

    for row, neighbours_in_host in enumerate(host):
        for column in neighbours_in_host:
            flawed = {
                state for state in states if state[0][row] == column
            }
            neighbours: dict[object, list[object]] = {}
            lower = len(host[row]) + columns[column] - n - 3
            assert lower >= 1
            for state in flawed:
                first, second = state
                valid: list[object] = []
                for partner in range(n):
                    if partner == row:
                        continue
                    if first[partner] not in host[row]:
                        continue
                    if column not in host[partner]:
                        continue
                    switched = switch(first, row, partner)
                    if any(
                        switched[index] == second[index]
                        for index in (row, partner)
                    ):
                        continue
                    target = (switched, second)
                    assert target in state_set
                    assert target[0][row] != column
                    valid.append(target)
                assert len(valid) >= lower
                neighbours[state] = valid
            verify_symmetric_kernel(
                list(states),
                set(flawed),
                neighbours,
            )


def contains_labelled_edges(
    state: State,
    labelled_edges: tuple[tuple[int, int, int], ...],
) -> bool:
    return all(
        state[layer][row] == column
        for layer, row, column in labelled_edges
    )


def verify_two_layer_cylinder_spread(
    host: Host,
    maximum_rank: int = 3,
) -> None:
    n = len(host)
    matchings = perfect_matchings(host)
    states = [
        (first, second)
        for first in matchings
        for second in matchings
        if all(first[row] != second[row] for row in range(n))
    ]
    assert states
    columns = column_degrees(host)
    minimum_degree = min(
        min(map(len, host)),
        min(columns),
    )
    lower = 2 * minimum_degree - n - 3
    if lower < 1:
        return
    atoms = tuple(
        (layer, row, column)
        for layer in range(2)
        for row, row_neighbours in enumerate(host)
        for column in row_neighbours
    )
    total = len(states)
    for rank in range(1, min(maximum_rank, lower) + 1):
        denominator = 1
        for offset in range(rank):
            denominator *= lower + 1 - offset
        for cylinder in combinations(atoms, rank):
            previous_states = states
            for offset, atom in enumerate(cylinder):
                next_states = [
                    state
                    for state in previous_states
                    if contains_labelled_edges(state, (atom,))
                ]
                if previous_states:
                    assert Fraction(
                        len(next_states),
                        len(previous_states),
                    ) <= Fraction(1, lower - offset + 1)
                previous_states = next_states
            assert Fraction(len(previous_states), total) <= Fraction(
                1,
                denominator,
            )


def complete_host(n: int) -> Host:
    return tuple(frozenset(range(n)) for _ in range(n))


def one_edge_deleted_host(n: int) -> Host:
    return tuple(
        frozenset(
            column
            for column in range(n)
            if not (row == 0 and column == 0)
        )
        for row in range(n)
    )


def main() -> None:
    verify_one_layer(one_edge_deleted_host(4))
    verify_two_layer(complete_host(4))
    verify_two_layer(one_edge_deleted_host(5))
    verify_two_layer_cylinder_spread(complete_host(5))
    print("dense-host stationary resampling: all enumerated kernels passed")


if __name__ == "__main__":
    main()

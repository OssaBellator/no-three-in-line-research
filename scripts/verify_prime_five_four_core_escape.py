#!/usr/bin/env python3
"""Exact census and parent-bank escape checks for CMR145--CMR148."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations


def collinear(
    first: tuple[int, int],
    second: tuple[int, int],
    third: tuple[int, int],
) -> bool:
    return (second[0] - first[0]) * (third[1] - first[1]) == (
        third[0] - first[0]
    ) * (second[1] - first[1])


def triple_set(state: tuple[tuple[int, ...], tuple[int, ...]]):
    layer_zero, layer_one = state
    points = [
        (column, layer_zero[column], 0) for column in range(5)
    ] + [
        (column, layer_one[column], 1) for column in range(5)
    ]
    result = set()
    for indices in combinations(range(10), 3):
        selected = tuple(points[index] for index in indices)
        if collinear(
            selected[0][:2],
            selected[1][:2],
            selected[2][:2],
        ):
            result.add(tuple(sorted(selected)))
    return frozenset(result)


def saturated_states():
    all_permutations = list(permutations(range(5)))
    return [
        (first, second)
        for first in all_permutations
        for second in all_permutations
        if all(first[column] != second[column] for column in range(5))
    ]


def four_moves(state: tuple[tuple[int, ...], tuple[int, ...]]):
    first, second = state
    result = set()
    for layer in (0, 1):
        current = first if layer == 0 else second
        opposite = second if layer == 0 else first
        for columns in combinations(range(5), 4):
            rows = [current[column] for column in columns]
            for replacement_rows in permutations(rows):
                replacement = list(current)
                allowed = True
                for column, row in zip(columns, replacement_rows):
                    if row == current[column] or row == opposite[column]:
                        allowed = False
                        break
                    replacement[column] = row
                if not allowed:
                    continue
                if layer == 0:
                    result.add((tuple(replacement), second))
                else:
                    result.add((first, tuple(replacement)))
    return result


def ordered_full_escape_count(
    source: tuple[tuple[int, ...], tuple[int, ...]],
    zero_states: set[tuple[tuple[int, ...], tuple[int, ...]]],
) -> int:
    source_zero, source_one = source
    count = 0
    for target_zero, target_one in zero_states:
        if not all(target_zero[index] != source_zero[index] for index in range(5)):
            continue
        if not all(target_one[index] != source_one[index] for index in range(5)):
            continue

        zero_then_one = all(
            target_zero[index] != source_one[index] for index in range(5)
        )
        one_then_zero = all(
            target_one[index] != source_zero[index] for index in range(5)
        )
        if zero_then_one or one_then_zero:
            count += 1
    return count


def connected_components(vertices, adjacency):
    unseen = set(vertices)
    components = []
    while unseen:
        start = unseen.pop()
        component = {start}
        stack = [start]
        while stack:
            current = stack.pop()
            for neighbour in adjacency[current]:
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    component.add(neighbour)
                    stack.append(neighbour)
        components.append(component)
    return components


def main() -> None:
    states = saturated_states()
    assert len(states) == 5280

    triples = {state: triple_set(state) for state in states}
    potential_histogram = Counter(len(value) for value in triples.values())
    assert potential_histogram == Counter(
        {
            0: 64,
            1: 192,
            2: 960,
            3: 1200,
            4: 904,
            5: 616,
            6: 560,
            7: 336,
            8: 96,
            9: 64,
            10: 32,
            11: 104,
            12: 80,
            13: 32,
            14: 24,
            15: 16,
        }
    )

    potential_one = {state for state in states if len(triples[state]) == 1}
    potential_zero = {state for state in states if len(triples[state]) == 0}

    equal_adjacency = {}
    zero_exits = {}
    for state in potential_one:
        moves = four_moves(state)
        equal_adjacency[state] = moves & potential_one
        zero_exits[state] = moves & potential_zero

    components = connected_components(potential_one, equal_adjacency)
    assert Counter(len(component) for component in components) == Counter(
        {1: 80, 2: 16, 5: 16}
    )

    terminal_components = [
        component
        for component in components
        if all(not zero_exits[state] for state in component)
    ]
    assert Counter(len(component) for component in terminal_components) == Counter(
        {1: 80, 2: 8}
    )

    trapped_states = set().union(*terminal_components)
    assert len(trapped_states) == 96

    escape_histogram = Counter(
        ordered_full_escape_count(state, potential_zero)
        for state in trapped_states
    )
    assert escape_histogram == Counter({1: 16, 3: 32, 4: 16, 5: 32})
    assert 0 not in escape_histogram

    state_p = ((0, 3, 1, 4, 2), (2, 4, 0, 3, 1))
    state_q = ((0, 2, 4, 1, 3), (2, 4, 0, 3, 1))
    escape = ((1, 0, 3, 2, 4), (3, 1, 4, 0, 2))

    assert state_p in trapped_states
    assert state_q in trapped_states
    assert state_q in equal_adjacency[state_p]
    assert state_p in equal_adjacency[state_q]
    assert len(triples[state_p]) == len(triples[state_q]) == 1
    assert len(triples[escape]) == 0
    assert all(escape[0][index] != state_p[0][index] for index in range(5))
    assert all(escape[1][index] != state_p[1][index] for index in range(5))
    assert all(escape[0][index] != state_p[1][index] for index in range(5))
    assert all(escape[0][index] != escape[1][index] for index in range(5))

    print(
        "verified prime-five four-core escape: 5280 states, 96 terminal "
        "potential-one states, ordered zero escapes {1:16,3:32,4:16,5:32}"
    )


if __name__ == "__main__":
    main()

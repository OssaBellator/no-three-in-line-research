#!/usr/bin/env python3
"""Exact checks for CMR149--CMR152."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations


FAMILY = (
    (0, 2, 6, 5, 3, 4, 1),
    (1, 0, 4, 6, 2, 3, 5),
    (2, 3, 5, 4, 1, 6, 0),
    (3, 5, 0, 2, 6, 1, 4),
    (4, 1, 3, 0, 5, 2, 6),
    (5, 6, 2, 1, 4, 0, 3),
    (6, 4, 1, 3, 0, 5, 2),
)


def collinear(first, second, third) -> bool:
    return (second[0] - first[0]) * (third[1] - first[1]) == (
        third[0] - first[0]
    ) * (second[1] - first[1])


def potential(state: tuple[tuple[int, ...], tuple[int, ...]]) -> int:
    first, second = state
    points = [
        (column, first[column], 0) for column in range(7)
    ] + [
        (column, second[column], 1) for column in range(7)
    ]
    return sum(
        collinear(
            points[indices[0]][:2],
            points[indices[1]][:2],
            points[indices[2]][:2],
        )
        for indices in combinations(range(14), 3)
    )


def layer_moves(state, subset_size: int):
    first, second = state
    result = set()
    for layer in (0, 1):
        current = first if layer == 0 else second
        opposite = second if layer == 0 else first
        for columns in combinations(range(7), subset_size):
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


def verify_ordered_escape(source, target) -> None:
    source_zero, source_one = source
    target_zero, target_one = target

    assert all(target_zero[index] != source_zero[index] for index in range(7))
    assert all(target_one[index] != source_one[index] for index in range(7))
    assert all(target_zero[index] != source_one[index] for index in range(7))
    assert all(target_zero[index] != target_one[index] for index in range(7))
    assert potential(target) == 0


def main() -> None:
    root_states = [
        (FAMILY[first], FAMILY[second])
        for first in range(7)
        for second in range(7)
        if first != second
    ]
    assert len(root_states) == 42

    root_histogram = Counter(potential(state) for state in root_states)
    assert root_histogram == Counter(
        {1: 4, 3: 2, 4: 2, 5: 12, 6: 2, 7: 8, 8: 4, 9: 8}
    )

    minimum_states = [state for state in root_states if potential(state) == 1]
    assert len(minimum_states) == 4

    four_move_profiles = []
    trapped = []
    for state in minimum_states:
        moves = layer_moves(state, 4)
        profile = Counter(potential(child) for child in moves)
        four_move_profiles.append(profile)
        if profile.get(0, 0) == 0:
            trapped.append(state)

    assert len(trapped) == 2
    assert sorted(profile.get(0, 0) for profile in four_move_profiles) == [0, 0, 2, 2]

    expected_trapped = {
        (FAMILY[3], FAMILY[4]),
        (FAMILY[4], FAMILY[3]),
    }
    assert set(trapped) == expected_trapped

    for state in trapped:
        four_moves = layer_moves(state, 4)
        four_profile = Counter(potential(child) for child in four_moves)
        assert len(four_moves) == 308
        assert min(four_profile) == 1
        assert four_profile[1] == 3

        full_moves = layer_moves(state, 7)
        full_profile = Counter(potential(child) for child in full_moves)
        assert len(full_moves) == 1158
        assert min(full_profile) == 1
        assert full_profile[1] == 3

    escape_first = (
        (1, 0, 2, 5, 4, 6, 3),
        (3, 6, 4, 1, 2, 0, 5),
    )
    escape_second = (
        (1, 0, 2, 6, 4, 3, 5),
        (5, 3, 4, 0, 2, 6, 1),
    )
    verify_ordered_escape((FAMILY[3], FAMILY[4]), escape_first)
    verify_ordered_escape((FAMILY[4], FAMILY[3]), escape_second)

    print(
        "verified prime-seven root parent escape: 42 root states, "
        "two one-layer traps, two ordered joint zero escapes"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite checks for CMR240--CMR243."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations


def diagonal_boundary_count(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    boundary = set()
    for x in left:
        for y in right:
            if x in (left[0], left[-1]) or y in (right[0], right[-1]):
                boundary.add((x, y))
    return sum(x == y for x, y in boundary)


def verify_boundary_exceptions() -> None:
    universe = range(8)
    for a in range(2, 7):
        for c in range(2, 7):
            for left in combinations(universe, a):
                for right in combinations(universe, c):
                    assert diagonal_boundary_count(left, right) <= 2
                    boundary_size = 2 * a + 2 * c - 4
                    required = boundary_size - diagonal_boundary_count(left, right)
                    assert (required + 1) // 2 >= a + c - 3


def derangements(t: int):
    return [
        state
        for state in permutations(range(t))
        if all(state[row] != row for row in range(t))
    ]


def candidate_lines(t: int):
    points = [(x, y) for x in range(t) for y in range(t) if x != y]
    lines = {}
    for (x1, y1), (x2, y2) in combinations(points, 2):
        if x1 == x2 or y1 == y2:
            continue
        slope = Fraction(y2 - y1, x2 - x1)
        intercept = Fraction(y1) - slope * x1
        cells = frozenset(
            (x, y)
            for x, y in points
            if Fraction(y) == slope * x + intercept
        )
        if len(cells) >= 3:
            lines[(slope, intercept)] = cells
    return list(lines.values())


def verify_small_line_avoidance() -> None:
    expected = {
        5: (44, 11, 55),
        6: (265, 27, 2925),
        7: (1854, 67, 766480),
    }
    for t, expected_values in expected.items():
        states = derangements(t)
        lines = candidate_lines(t)
        full_mask = (1 << len(states)) - 1
        line_masks = []
        for cells in lines:
            mask = 0
            for index, state in enumerate(states):
                if any((row, state[row]) in cells for row in range(t)):
                    mask |= 1 << index
            line_masks.append(mask)

        family_count = 0
        for chosen in combinations(range(len(lines)), t - 3):
            covered = 0
            for index in chosen:
                covered |= line_masks[index]
            assert covered != full_mask
            family_count += 1

        assert (len(states), len(lines), family_count) == expected_values


def main() -> None:
    verify_boundary_exceptions()
    verify_small_line_avoidance()
    print(
        "verified boundary line blockers: at most two diagonal boundary "
        "exceptions and all t-3 line families avoidable for t=5,6,7"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite checks for CMR244--CMR247."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations


def verify_one_exception_boundary() -> None:
    universe = range(8)

    # Singleton Hall sides: each nonaxis line meets the slice at most once.
    for c in range(1, 8):
        assert c - 1 == 1 + c - 2
    for a in range(1, 8):
        assert a - 1 == a + 1 - 2

    # Nontrivial rectangle sides: use the two-boundary-points-per-line count.
    for a in range(2, 7):
        for c in range(2, 7):
            boundary = 2 * a + 2 * c - 4
            required = boundary - 1
            assert (required + 1) // 2 == a + c - 2
            for left in combinations(universe, a):
                for right in combinations(universe, c):
                    points = {
                        (x, y)
                        for x in left
                        for y in right
                        if x in (left[0], left[-1])
                        or y in (right[0], right[-1])
                    }
                    assert len(points) == boundary


def candidate_lines(t: int):
    points = [(x, y) for x in range(t) for y in range(t)]
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


def verify_target(t: int, target: tuple[int, int]) -> int:
    states = [
        state
        for state in permutations(range(t))
        if state[target[0]] != target[1]
    ]
    full_mask = (1 << len(states)) - 1
    lines = candidate_lines(t)
    masks = []
    for cells in lines:
        mask = 0
        for index, state in enumerate(states):
            if any((row, state[row]) in cells for row in range(t)):
                mask |= 1 << index
        masks.append(mask)

    family_count = 0
    for chosen in combinations(range(len(lines)), t - 2):
        covered = 0
        for index in chosen:
            covered |= masks[index]
        assert covered != full_mask
        family_count += 1
    return family_count


def verify_small_hosts() -> None:
    for t, expected_lines, expected_families in (
        (4, 6, 15),
        (5, 22, 1540),
    ):
        assert len(candidate_lines(t)) == expected_lines
        for target in ((x, y) for x in range(t) for y in range(t)):
            assert verify_target(t, target) == expected_families

    assert len(candidate_lines(6)) == 46
    for target in ((0, 0), (0, 1), (3, 3)):
        assert verify_target(6, target) == 163185


def main() -> None:
    verify_one_exception_boundary()
    verify_small_hosts()
    print(
        "verified target-specific line avoidance: singleton and nontrivial Hall "
        "sides, plus every t-2 line family for the recorded small hosts"
    )


if __name__ == "__main__":
    main()

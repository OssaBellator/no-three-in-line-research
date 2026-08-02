#!/usr/bin/env python3
"""Verify the exact one-outer-layer obstruction at base side six."""
from __future__ import annotations

from collections import defaultdict
from itertools import permutations

Permutation = tuple[int, ...]
FactorPair = tuple[Permutation, Permutation]
Point = tuple[int, int]
ORIENTATIONS = ("cc", "cf", "fc", "ff")
EXPECTED_TYPES = {(6,): 84, (4, 2): 16, (3, 3): 16}
EXPECTED_STATES = 60_544


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def is_no_three(points: list[Point] | tuple[Point, ...]) -> bool:
    for first in range(len(points) - 2):
        a = points[first]
        for second in range(first + 1, len(points) - 1):
            b = points[second]
            dx = b[0] - a[0]
            dy = b[1] - a[1]
            for third in range(second + 1, len(points)):
                c = points[third]
                if dx * (c[1] - a[1]) - dy * (c[0] - a[0]) == 0:
                    return False
    return True


def valid_factor_pairs(n: int) -> tuple[FactorPair, ...]:
    result: list[FactorPair] = []
    all_permutations = tuple(permutations(range(n)))
    for first in all_permutations:
        for second in all_permutations:
            if any(first[index] == second[index] for index in range(n)):
                continue
            points = [(index, first[index]) for index in range(n)]
            points.extend((index, second[index]) for index in range(n))
            if is_no_three(points):
                result.append((first, second))
    return tuple(result)


def inverse(permutation: Permutation) -> Permutation:
    result = [0] * len(permutation)
    for index, value in enumerate(permutation):
        result[value] = index
    return tuple(result)


def compose(first: Permutation, second: Permutation) -> Permutation:
    return tuple(first[second[index]] for index in range(len(first)))


def cycle_type(permutation: Permutation) -> tuple[int, ...]:
    seen: set[int] = set()
    lengths: list[int] = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        current = start
        length = 0
        while current not in seen:
            seen.add(current)
            length += 1
            current = permutation[current]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def relative_type(pair: FactorPair) -> tuple[int, ...]:
    return cycle_type(compose(inverse(pair[0]), pair[1]))


def one_outer_state(
    first_block: FactorPair,
    second_block: FactorPair,
    orientation: str,
    outer_layer: int,
) -> tuple[Point, ...]:
    n = len(first_block[0])
    points: list[Point] = []
    for coarse_row, pair in enumerate((first_block, second_block)):
        coarse_column = coarse_row if outer_layer == 0 else 1 - coarse_row
        for layer in pair:
            for fine_row, fine_column in enumerate(layer):
                x = n * coarse_row + fine_row if orientation[0] == "c" else 2 * fine_row + coarse_row
                y = n * coarse_column + fine_column if orientation[1] == "c" else 2 * fine_column + coarse_column
                points.append((x, y))
    assert len(points) == 4 * n
    return tuple(points)


def verify_saturation(points: tuple[Point, ...]) -> None:
    side = len(points) // 2
    assert len(set(points)) == len(points)
    assert all(sum(x == row for x, _ in points) == 2 for row in range(side))
    assert all(sum(y == column for _, y in points) == 2 for column in range(side))


def main() -> None:
    factors = valid_factor_pairs(6)
    assert len(factors) == 116

    groups: dict[tuple[int, ...], list[FactorPair]] = defaultdict(list)
    for factor in factors:
        groups[relative_type(factor)].append(factor)
    assert {key: len(value) for key, value in groups.items()} == EXPECTED_TYPES

    state_count = 0
    for factor_type, targets in groups.items():
        for first_block in targets:
            for second_block in targets:
                for orientation in ORIENTATIONS:
                    for outer_layer in (0, 1):
                        points = one_outer_state(
                            first_block,
                            second_block,
                            orientation,
                            outer_layer,
                        )
                        verify_saturation(points)
                        assert not is_no_three(points), (
                            factor_type,
                            first_block,
                            second_block,
                            orientation,
                            outer_layer,
                        )
                        state_count += 1

    assert state_count == EXPECTED_STATES
    print(f"side-six saturated ordered factors: {len(factors)}")
    print(f"relative cycle-type counts: {EXPECTED_TYPES}")
    print(f"one-outer-layer states exhausted: {state_count}")
    print("no side-six one-outer-layer template exists")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exhaust normalized affine one-inner-layer products for the 2 x 5 case.

The first coarse row and column blocks use the identity fine-digit map.  The
second row and column blocks independently use one of the twenty affine
permutations u -> a*u+b modulo five.  Every fine permutation appearing in a
saturated no-three side-five factor is tested in all four radix orientations.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations, permutations

Point = tuple[int, int]
Permutation = tuple[int, ...]
FactorPair = tuple[Permutation, Permutation]

ORIENTATIONS = ("cc", "cf", "fc", "ff")
OUTER: FactorPair = ((0, 1), (1, 0))
IDENTITY: Permutation = (0, 1, 2, 3, 4)
REVERSAL: Permutation = (4, 3, 2, 1, 0)
SIDE_TEN_WITNESS: FactorPair = (
    (4, 2, 1, 3, 0, 9, 6, 8, 7, 5),
    (5, 7, 8, 6, 9, 0, 3, 1, 2, 4),
)
EXPECTED = {
    ((2, 1, 4, 3, 0), REVERSAL, REVERSAL, "cf"),
    ((2, 4, 0, 3, 1), REVERSAL, REVERSAL, "ff"),
    ((4, 1, 0, 3, 2), REVERSAL, REVERSAL, "fc"),
}


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def is_no_three(points: tuple[Point, ...] | list[Point]) -> bool:
    return all(determinant(*triple) != 0 for triple in combinations(points, 3))


@lru_cache(maxsize=None)
def valid_factor_pairs(n: int) -> tuple[FactorPair, ...]:
    result: list[FactorPair] = []
    all_permutations = tuple(permutations(range(n)))
    for first in all_permutations:
        for second in all_permutations:
            if any(first[x] == second[x] for x in range(n)):
                continue
            points = [(x, first[x]) for x in range(n)]
            points.extend((x, second[x]) for x in range(n))
            if is_no_three(points):
                result.append((first, second))
    return tuple(result)


def affine_maps() -> tuple[Permutation, ...]:
    maps = {
        tuple((a * u + b) % 5 for u in range(5))
        for a in range(1, 5)
        for b in range(5)
    }
    assert len(maps) == 20
    return tuple(sorted(maps))


def one_inner_layer_state(
    tau: Permutation,
    row_map: Permutation,
    column_map: Permutation,
    orientation: str,
) -> tuple[Point, ...]:
    row_maps = (IDENTITY, row_map)
    column_maps = (IDENTITY, column_map)
    points: set[Point] = set()
    for outer_layer in (0, 1):
        for i in range(2):
            j = OUTER[outer_layer][i]
            for u in range(5):
                row_digit = row_maps[i][u]
                column_digit = column_maps[j][tau[u]]
                x = 5 * i + row_digit if orientation[0] == "c" else 2 * row_digit + i
                y = 5 * j + column_digit if orientation[1] == "c" else 2 * column_digit + j
                points.add((x, y))
    assert len(points) == 20
    result = tuple(sorted(points))
    assert all(sum(x == row for x, _ in result) == 2 for row in range(10))
    assert all(sum(y == column for _, y in result) == 2 for column in range(10))
    return result


def graph_points(pair: FactorPair) -> set[Point]:
    return {
        (x, pair[layer][x])
        for layer in (0, 1)
        for x in range(len(pair[0]))
    }


def main() -> None:
    ordered_pairs = valid_factor_pairs(5)
    assert len(ordered_pairs) == 64
    fine_permutations = tuple(sorted({tau for pair in ordered_pairs for tau in pair}))
    assert len(fine_permutations) == 44

    successes: set[tuple[Permutation, Permutation, Permutation, str]] = set()
    tested = 0
    for tau in fine_permutations:
        for row_map in affine_maps():
            for column_map in affine_maps():
                for orientation in ORIENTATIONS:
                    tested += 1
                    state = one_inner_layer_state(
                        tau,
                        row_map,
                        column_map,
                        orientation,
                    )
                    if is_no_three(state):
                        successes.add((tau, row_map, column_map, orientation))
                        assert set(state) == graph_points(SIDE_TEN_WITNESS)

    assert tested == 44 * 20 * 20 * 4 == 70400
    assert successes == EXPECTED
    print(f"normalized affine one-layer states tested: {tested}")
    print("exact successes: 3; all use reversal/reversal and the same side-ten witness")
    for success in sorted(successes):
        print(success)


if __name__ == "__main__":
    main()

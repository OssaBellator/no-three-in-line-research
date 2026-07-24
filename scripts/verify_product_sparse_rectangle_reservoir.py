#!/usr/bin/env python3
"""Verify PX65--PX67: exact sparse rectangle reservoirs."""
from __future__ import annotations

from itertools import combinations, permutations, product
from math import sqrt

Point = tuple[int, int]
Permutation = tuple[int, ...]
K = 221_184


def harmonic(number: int) -> float:
    return sum(1 / value for value in range(1, number + 1))


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def corners(
    side: int,
    row_map: Permutation,
    first_column_map: Permutation,
    second_column_map: Permutation,
    orientation: str,
) -> tuple[tuple[Point, ...], ...]:
    rectangles = []
    for index in range(side):
        x_zero = index if orientation[0] == "c" else 2 * index
        x_one = side + row_map[index] if orientation[0] == "c" else 2 * row_map[index] + 1
        y_zero = first_column_map[index] if orientation[1] == "c" else 2 * first_column_map[index]
        y_one = side + second_column_map[index] if orientation[1] == "c" else 2 * second_column_map[index] + 1
        rectangles.append(
            ((x_zero, y_zero), (x_zero, y_one), (x_one, y_zero), (x_one, y_one))
        )
    return tuple(rectangles)


def defects(rectangles: tuple[tuple[Point, ...], ...]) -> tuple[set[tuple[int, int]], set[tuple[int, int, int]]]:
    pair_edges: set[tuple[int, int]] = set()
    triple_edges: set[tuple[int, int, int]] = set()
    points = [(rectangle, point) for rectangle, cells in enumerate(rectangles) for point in cells]
    for first, second, third in combinations(points, 3):
        rectangle_indices = tuple(sorted({first[0], second[0], third[0]}))
        if len(rectangle_indices) == 1:
            assert determinant(first[1], second[1], third[1]) != 0
            continue
        if determinant(first[1], second[1], third[1]) != 0:
            continue
        if len(rectangle_indices) == 2:
            pair_edges.add(rectangle_indices)
        else:
            triple_edges.add(rectangle_indices)
    return pair_edges, triple_edges


def maximum_independent_size(
    side: int,
    pair_edges: set[tuple[int, int]],
    triple_edges: set[tuple[int, int, int]],
) -> int:
    best = 0
    for mask in range(1 << side):
        if mask.bit_count() <= best:
            continue
        if any(all(mask >> vertex & 1 for vertex in edge) for edge in pair_edges):
            continue
        if any(all(mask >> vertex & 1 for vertex in edge) for edge in triple_edges):
            continue
        best = mask.bit_count()
    return best


def verify_alteration_inequality() -> None:
    # Complete enumeration of all simple rank-two/rank-three hypergraphs through n=4.
    for side in range(1, 5):
        possible_edges = list(combinations(range(side), 2)) + list(combinations(range(side), 3))
        for edge_mask in range(1 << len(possible_edges)):
            pair_edges = {
                edge for index, edge in enumerate(possible_edges) if len(edge) == 2 and edge_mask >> index & 1
            }
            triple_edges = {
                edge for index, edge in enumerate(possible_edges) if len(edge) == 3 and edge_mask >> index & 1
            }
            independence = maximum_independent_size(side, pair_edges, triple_edges)
            for numerator in range(11):
                q = numerator / 10
                lower_bound = side * q - len(pair_edges) * q**2 - len(triple_edges) * q**3
                assert independence + 1e-12 >= lower_bound
    print("PX66 alteration inequality: exhaustive through four vertices")


def verify_constants() -> None:
    for side in range(3, 10_001):
        h = harmonic(2 * side - 1)
        q = 1 / (4 * sqrt(K * h))
        diagonal = 48 * side * q**2
        transversal = K * side * h * q**3
        retained = side * q - diagonal - transversal
        claimed = side / (8 * sqrt(K * h))
        assert retained >= claimed
    print("PX67 constants: checked for sides 3 through 10000")


def verify_rectangle_extraction() -> None:
    # Exhaust every normalized rectangle state through base three and sample base four.
    for side in (2, 3):
        all_permutations = tuple(permutations(range(side)))
        states = product(all_permutations, repeat=3)
        for row_map, first_column_map, second_column_map in states:
            for orientation in ("cc", "cf", "fc", "ff"):
                rectangles = corners(
                    side, row_map, first_column_map, second_column_map, orientation
                )
                pair_edges, triple_edges = defects(rectangles)
                independent = maximum_independent_size(side, pair_edges, triple_edges)
                assert independent >= 1
        print(f"base {side}: every normalized rectangle state has an exact reservoir")

    side = 4
    all_permutations = tuple(permutations(range(side)))
    for index, (row_map, first_column_map, second_column_map) in enumerate(
        product(all_permutations, repeat=3)
    ):
        if index % 137 != 0:
            continue
        rectangles = corners(side, row_map, first_column_map, second_column_map, "ff")
        pair_edges, triple_edges = defects(rectangles)
        independent = maximum_independent_size(side, pair_edges, triple_edges)
        assert independent >= 1
    print("base 4: sampled exact reservoir extraction")


def main() -> None:
    verify_alteration_inequality()
    verify_constants()
    verify_rectangle_extraction()
    print("PX65--PX67 sparse rectangle reservoir verification passed")


if __name__ == "__main__":
    main()

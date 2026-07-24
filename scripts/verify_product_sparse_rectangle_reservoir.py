#!/usr/bin/env python3
"""Verify PX84--PX86: exact sparse rectangle reservoirs."""
from __future__ import annotations

from itertools import combinations, permutations, product
from math import sqrt

Point = tuple[int, int]
K = 221_184


def harmonic(number: int) -> float:
    return sum(1 / value for value in range(1, number + 1))


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


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


def verify_alteration() -> None:
    for side in range(1, 5):
        edges = list(combinations(range(side), 2)) + list(combinations(range(side), 3))
        for chosen in range(1 << len(edges)):
            pairs = {edge for index, edge in enumerate(edges) if len(edge) == 2 and chosen >> index & 1}
            triples = {edge for index, edge in enumerate(edges) if len(edge) == 3 and chosen >> index & 1}
            alpha = maximum_independent_size(side, pairs, triples)
            for numerator in range(21):
                q = numerator / 20
                lower = side * q - len(pairs) * q**2 - len(triples) * q**3
                assert alpha + 1e-12 >= lower
    print("PX85 alteration bound: exhaustive through four vertices")


def verify_constants() -> None:
    for side in range(3, 10_001):
        h = harmonic(2 * side - 1)
        q = 1 / (4 * sqrt(K * h))
        retained = side * q - 48 * side * q**2 - K * side * h * q**3
        claimed = side / (8 * sqrt(K * h))
        assert retained >= claimed
    print("PX86 constants: checked through side 10000")


def rectangle_state(side: int, row_map: tuple[int, ...], low: tuple[int, ...], high: tuple[int, ...]):
    return tuple(
        (
            (index, low[index]),
            (index, side + high[index]),
            (side + row_map[index], low[index]),
            (side + row_map[index], side + high[index]),
        )
        for index in range(side)
    )


def defect_edges(rectangles):
    pairs: set[tuple[int, int]] = set()
    triples: set[tuple[int, int, int]] = set()
    labelled = [(index, point) for index, rectangle in enumerate(rectangles) for point in rectangle]
    for first, second, third in combinations(labelled, 3):
        if determinant(first[1], second[1], third[1]) != 0:
            continue
        support = tuple(sorted({first[0], second[0], third[0]}))
        assert len(support) in (2, 3)
        (pairs if len(support) == 2 else triples).add(support)
    return pairs, triples


def verify_small_states() -> None:
    for side in (2, 3):
        all_permutations = tuple(permutations(range(side)))
        for row_map, low, high in product(all_permutations, repeat=3):
            rectangles = rectangle_state(side, row_map, low, high)
            pairs, triples = defect_edges(rectangles)
            independent = maximum_independent_size(side, pairs, triples)
            assert independent >= 1
            for subset in combinations(range(side), independent):
                if any(set(edge).issubset(subset) for edge in pairs | triples):
                    continue
                points = [point for index in subset for point in rectangles[index]]
                assert all(determinant(*three) != 0 for three in combinations(points, 3))
                break
            else:
                raise AssertionError("maximum independent set not realized")
        print(f"base {side}: exact reservoir extraction verified in every state")


def main() -> None:
    verify_alteration()
    verify_constants()
    verify_small_states()
    print("PX84--PX86 verification passed")


if __name__ == "__main__":
    main()

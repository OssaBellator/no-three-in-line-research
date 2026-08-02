#!/usr/bin/env python3
"""Verify rectangle conflict-degree bounds on the complete small instances."""
from __future__ import annotations

from itertools import combinations, product

from verify_product_rectangle_reduction import ORIENTATIONS, determinant

Edge = tuple[int, int, int, int]
Point = tuple[int, int]


def compatible(first: Edge, second: Edge) -> bool:
    return all(first[index] != second[index] for index in range(4))


def corners(n: int, edge: Edge, orientation: str) -> tuple[Point, ...]:
    u, p, t, r = edge
    x_0 = u if orientation[0] == "c" else 2 * u
    x_1 = n + p if orientation[0] == "c" else 2 * p + 1
    y_0 = t if orientation[1] == "c" else 2 * t
    y_1 = n + r if orientation[1] == "c" else 2 * r + 1
    return (x_0, y_0), (x_0, y_1), (x_1, y_0), (x_1, y_1)


def pair_conflict(n: int, first: Edge, second: Edge, orientation: str) -> bool:
    points = corners(n, first, orientation) + corners(n, second, orientation)
    return any(determinant(*triple) == 0 for triple in combinations(points, 3))


def transversal_conflict(
    n: int,
    first: Edge,
    second: Edge,
    third: Edge,
    orientation: str,
) -> bool:
    return any(
        determinant(a, b, c) == 0
        for a in corners(n, first, orientation)
        for b in corners(n, second, orientation)
        for c in corners(n, third, orientation)
    )


def main() -> None:
    for n in range(2, 5):
        edges = tuple(product(range(n), repeat=4))
        pair_cap = 16 * n * (n - 1) ** 2
        triple_codegree_cap = 64 * n * max(n - 2, 0) ** 2
        for orientation in ORIENTATIONS:
            maximum_pair_degree = 0
            maximum_triple_codegree = 0
            for first in edges:
                degree = sum(
                    compatible(first, second)
                    and pair_conflict(n, first, second, orientation)
                    for second in edges
                )
                maximum_pair_degree = max(maximum_pair_degree, degree)
                assert degree <= pair_cap

            for first_index, first in enumerate(edges):
                for second in edges[first_index + 1 :]:
                    if not compatible(first, second):
                        continue
                    codegree = sum(
                        compatible(first, third)
                        and compatible(second, third)
                        and transversal_conflict(
                            n, first, second, third, orientation
                        )
                        for third in edges
                    )
                    maximum_triple_codegree = max(
                        maximum_triple_codegree, codegree
                    )
                    assert codegree <= triple_codegree_cap

            print(
                f"n={n}, orientation={orientation}: "
                f"pair_degree={maximum_pair_degree}/{pair_cap}, "
                f"triple_codegree={maximum_triple_codegree}/{triple_codegree_cap}"
            )

    print("rectangle conflict-degree bounds verified")


if __name__ == "__main__":
    main()

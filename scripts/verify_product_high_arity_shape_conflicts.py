#!/usr/bin/env python3
"""Verify PX162--PX163 affine-shape occurrence counts and covering bound."""
from __future__ import annotations

from collections import Counter
from itertools import combinations

Edge = tuple[int, int, int, int]
Shape = tuple[int, int, int]


def edge(prime: int, row: int, column: int) -> Edge:
    return row, column, (row - column) % prime, (row + column) % prime


def compatible(prime: int, shape: Shape) -> bool:
    slope, row_ratio, image_ratio = shape
    if slope in (0, 1, prime - 1):
        return False
    if row_ratio in (0, 1) or image_ratio in (0, 1):
        return False
    return all(
        value % prime != 0
        for value in (
            row_ratio - slope * image_ratio,
            row_ratio - 1 - slope * (image_ratio - 1),
            row_ratio + slope * image_ratio,
            row_ratio - 1 + slope * (image_ratio - 1),
        )
    )


def occurrence(
    prime: int,
    shape: Shape,
    base_row: int,
    step: int,
    base_image: int,
) -> tuple[Edge, Edge, Edge]:
    slope, row_ratio, image_ratio = shape
    return (
        edge(prime, base_row, base_image),
        edge(
            prime,
            (base_row + step) % prime,
            (base_image + slope * step) % prime,
        ),
        edge(
            prime,
            (base_row + row_ratio * step) % prime,
            (base_image + image_ratio * slope * step) % prime,
        ),
    )


def is_matching(items: tuple[Edge, ...]) -> bool:
    return all(
        len({item[part] for item in items}) == len(items)
        for part in range(4)
    )


def verify_occurrences(prime: int) -> None:
    shapes = [
        (slope, row_ratio, image_ratio)
        for slope in range(prime)
        for row_ratio in range(prime)
        for image_ratio in range(prime)
        if compatible(prime, (slope, row_ratio, image_ratio))
    ]
    assert len(shapes) >= (prime - 3) * (prime - 2) * max(0, prime - 6)

    for shape in shapes:
        row_incidence = Counter()
        edge_incidence = Counter()
        count = 0
        for base_row in range(prime):
            for step in range(1, prime):
                for base_image in range(prime):
                    item = occurrence(
                        prime, shape, base_row, step, base_image
                    )
                    assert is_matching(item)
                    count += 1
                    for selected_edge in item:
                        row_incidence[selected_edge[0]] += 1
                        edge_incidence[selected_edge] += 1

        assert count == prime * prime * (prime - 1)
        assert set(row_incidence.values()) == {3 * prime * (prime - 1)}
        assert set(edge_incidence.values()) == {3 * (prime - 1)}

    print(
        f"p={prime}: compatible shapes={len(shapes)}, "
        f"occurrences/shape={prime * prime * (prime - 1)}"
    )


def maximum_matching_size(edges: list[frozenset[int]]) -> int:
    best = 0

    def search(position: int, used: frozenset[int], size: int) -> None:
        nonlocal best
        if position == len(edges):
            best = max(best, size)
            return
        search(position + 1, used, size)
        if edges[position].isdisjoint(used):
            search(position + 1, used | edges[position], size + 1)

    search(0, frozenset(), 0)
    return best


def verify_covering_inequality() -> None:
    # Exhaust all small 3-graphs on six vertices.  If the matching number is
    # below q, then a maximal matching covers every edge, giving
    # |E| <= 3(q-1) Delta.
    vertices = range(6)
    triples = [frozenset(item) for item in combinations(vertices, 3)]
    for mask in range(1 << len(triples)):
        if mask.bit_count() > 8:
            continue
        selected = [
            triples[index]
            for index in range(len(triples))
            if mask & (1 << index)
        ]
        if not selected:
            continue
        degrees = Counter(vertex for item in selected for vertex in item)
        maximum_degree = max(degrees.values())
        matching_number = maximum_matching_size(selected)
        q = matching_number + 1
        assert len(selected) <= 3 * (q - 1) * maximum_degree

    print("3-uniform matching-cover inequality verified on small hypergraphs")


def main() -> None:
    for prime in (7, 11):
        verify_occurrences(prime)
    verify_covering_inequality()
    print("PX162--PX163 high-arity shape framework verified")


if __name__ == "__main__":
    main()

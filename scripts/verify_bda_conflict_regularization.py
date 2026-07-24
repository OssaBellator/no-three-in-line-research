#!/usr/bin/env python3
"""Verify the deterministic BDA3a conflict regularization bounds."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


def regularize(
    size: int, edges: tuple[tuple[int, int], ...]
) -> tuple[list[int], list[list[int]]]:
    mass = len(edges)
    loads = [0] * size
    adjacency = [set() for _ in range(size)]
    for left, right in edges:
        loads[left] += 1
        loads[right] += 1
        adjacency[left].add(right)
        adjacency[right].add(left)

    low = [
        vertex
        for vertex in range(size)
        if Fraction(loads[vertex], 1) <= Fraction(4 * mass, size)
    ]
    colours: list[list[int]] = []
    for vertex in low:
        for colour in colours:
            if all(other not in adjacency[vertex] for other in colour):
                colour.append(vertex)
                break
        else:
            colours.append([vertex])
    return low, colours


def verify(max_size: int = 6) -> None:
    for size in range(1, max_size + 1):
        pairs = tuple(combinations(range(size), 2))
        for mask in range(1 << len(pairs)):
            edges = tuple(
                pair for index, pair in enumerate(pairs) if mask & (1 << index)
            )
            low, colours = regularize(size, edges)
            assert len(low) * 2 >= size

            adjacency = {vertex: set() for vertex in low}
            for left, right in edges:
                if left in adjacency and right in adjacency:
                    adjacency[left].add(right)
                    adjacency[right].add(left)
            maximum_degree = max((len(adjacency[v]) for v in low), default=0)
            mass = len(edges)
            assert all(
                Fraction(len(adjacency[v]), 1) <= Fraction(4 * mass, size)
                for v in low
            )
            assert len(colours) <= maximum_degree + 1
            assert all(
                all(
                    right not in adjacency[left]
                    for left, right in combinations(colour, 2)
                )
                for colour in colours
            )
            largest = max((len(colour) for colour in colours), default=0)
            assert largest * (maximum_degree + 1) >= len(low)

            weights = [1 + (3 * vertex + mask) % 7 for vertex in range(size)]
            low_weight = sum(weights[vertex] for vertex in low)
            heaviest = max(
                (sum(weights[vertex] for vertex in colour) for colour in colours),
                default=0,
            )
            assert heaviest * (maximum_degree + 1) >= low_weight


def main() -> None:
    verify()
    print("BDA conflict regularization: verified through six blocks")


if __name__ == "__main__":
    main()

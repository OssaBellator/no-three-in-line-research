#!/usr/bin/env python3
"""Finite audit for GC2dm--GC2dq cross-tuple line/cell regularization."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import comb
from random import Random


def degeneracy_coloring(adjacency: list[set[int]]) -> tuple[list[int], int]:
    """Colour through a minimum-degree elimination order."""
    remaining = set(range(len(adjacency)))
    degree = [len(neighbours) for neighbours in adjacency]
    order: list[int] = []
    degeneracy = 0

    while remaining:
        vertex = min(remaining, key=lambda item: (degree[item], item))
        degeneracy = max(degeneracy, degree[vertex])
        remaining.remove(vertex)
        order.append(vertex)
        for neighbour in adjacency[vertex]:
            if neighbour in remaining:
                degree[neighbour] -= 1

    colours = [-1] * len(adjacency)
    for vertex in reversed(order):
        used = {colours[n] for n in adjacency[vertex] if colours[n] >= 0}
        colour = 0
        while colour in used:
            colour += 1
        colours[vertex] = colour
    return colours, degeneracy


def main() -> None:
    rng = Random(271828)
    stats: defaultdict[str, int] = defaultdict(int)

    for _ in range(40_000):
        order = rng.randint(3, 12)
        line_stock = comb(order * order, 2)
        tuple_count = rng.randint(1, 28)

        tuple_weight = [
            Fraction(rng.randint(1, 40), rng.randint(1, 12))
            for _ in range(tuple_count)
        ]
        axis_weight = [
            weight * Fraction(rng.randint(0, 12), 12)
            for weight in tuple_weight
        ]
        nonaxis_weight = [
            weight - axis
            for weight, axis in zip(tuple_weight, axis_weight)
        ]

        total = sum(tuple_weight, Fraction())
        axis_total = sum(axis_weight, Fraction())
        nonaxis_total = sum(nonaxis_weight, Fraction())

        if axis_total >= total / 2:
            stats["axis_dominant_systems"] += 1
        else:
            witness_total = sum(
                weight / (order * order * line_stock)
                for weight in nonaxis_weight
            )
            assert witness_total >= total / (2 * order * order * line_stock)
            stats["nonaxis_witness_systems"] += 1
            stats["witness_vertices"] += tuple_count

        block_cap = rng.randint(1, 6)
        line_cap = rng.randint(1, 10)
        cell_cap = rng.randint(1, 8)
        outdegree_cap = (
            3 * (block_cap - 1)
            + (line_cap - 1)
            + (cell_cap - 1)
        )

        adjacency = [set() for _ in range(tuple_count)]
        outdegree = [0] * tuple_count
        pairs = [
            (left, right)
            for left in range(tuple_count)
            for right in range(left + 1, tuple_count)
        ]
        rng.shuffle(pairs)

        for left, right in pairs:
            if rng.random() >= 0.16:
                continue
            orientations: list[tuple[int, int]] = []
            if outdegree[left] < outdegree_cap:
                orientations.append((left, right))
            if outdegree[right] < outdegree_cap:
                orientations.append((right, left))
            if not orientations:
                continue
            tail, _head = rng.choice(orientations)
            outdegree[tail] += 1
            adjacency[left].add(right)
            adjacency[right].add(left)

        assert max(outdegree, default=0) <= outdegree_cap

        colours, degeneracy = degeneracy_coloring(adjacency)
        assert degeneracy <= 2 * outdegree_cap
        colour_count = max(colours, default=-1) + 1
        assert colour_count <= 2 * outdegree_cap + 1

        weights = [
            Fraction(rng.randint(1, 30), rng.randint(1, 8))
            for _ in range(tuple_count)
        ]
        colour_weight: defaultdict[int, Fraction] = defaultdict(Fraction)
        for vertex, colour in enumerate(colours):
            colour_weight[colour] += weights[vertex]

        retained = max(colour_weight.values(), default=Fraction())
        assert retained >= sum(weights, Fraction()) / (2 * outdegree_cap + 1)

        stats["cause_graphs"] += 1
        stats["cause_edges"] += sum(len(row) for row in adjacency) // 2
        stats["compatible_vertices"] += sum(
            1
            for colour in colours
            if colour == max(colour_weight, key=colour_weight.get)
        ) if colour_weight else 0

    print("GC cross-tuple line/cell regularization audit passed")
    for key in sorted(stats):
        print(f"{key}: {stats[key]}")


if __name__ == "__main__":
    main()

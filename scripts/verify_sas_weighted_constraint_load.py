#!/usr/bin/env python3
"""Finite audit for SAS5hn--SAS5hr."""

from fractions import Fraction
from itertools import product


def maximum_weight_independent_set(weights, adjacency) -> Fraction:
    vertex_count = len(weights)
    best = Fraction(0)
    for mask in range(1 << vertex_count):
        independent = True
        for vertex in range(vertex_count):
            if not ((mask >> vertex) & 1):
                continue
            if any(
                neighbour > vertex and ((mask >> neighbour) & 1)
                for neighbour in adjacency[vertex]
            ):
                independent = False
                break
        if independent:
            total = sum(
                (weights[vertex] for vertex in range(vertex_count) if (mask >> vertex) & 1),
                Fraction(0),
            )
            best = max(best, total)
    return best


def main() -> None:
    systems = heavy = light = 0
    atom_universe = range(4)
    patterns = [
        {atom for atom in atom_universe if (mask >> atom) & 1}
        for mask in range(1, 8)
    ]
    menu_size = 2
    threshold = Fraction(6)

    for square_count in range(2, 5):
        for square_weights in product(range(1, 4), repeat=square_count):
            choices = product(range(len(patterns)), repeat=square_count * menu_size)
            for index, pattern_indices in enumerate(choices):
                if index >= 300:
                    break

                atom_sets = [patterns[value] for value in pattern_indices]
                weights = [
                    Fraction(square_weights[square])
                    for square in range(square_count)
                    for _ in range(menu_size)
                ]
                vertex_count = square_count * menu_size
                adjacency = [set() for _ in range(vertex_count)]

                for left in range(vertex_count):
                    left_square = left // menu_size
                    for right in range(left + 1, vertex_count):
                        right_square = right // menu_size
                        if left_square == right_square or atom_sets[left] & atom_sets[right]:
                            adjacency[left].add(right)
                            adjacency[right].add(left)

                atom_load = {
                    atom: sum(
                        (
                            weights[vertex]
                            for vertex, atom_set in enumerate(atom_sets)
                            if atom in atom_set
                        ),
                        Fraction(0),
                    )
                    for atom in atom_universe
                }
                systems += 1

                if max(atom_load.values(), default=Fraction(0)) > threshold:
                    heavy += 1
                    continue

                light += 1
                support_bound = max(len(atom_set) for atom_set in atom_sets)
                guaranteed = sum(
                    (
                        Fraction(
                            menu_size * square_weights[square] ** 2,
                            menu_size * square_weights[square] + support_bound * threshold,
                        )
                        for square in range(square_count)
                    ),
                    Fraction(0),
                )
                optimum = maximum_weight_independent_set(weights, adjacency)
                assert optimum >= guaranteed

    assert systems == 35100
    assert heavy == 31844
    assert light == 3256
    print(
        "weighted constraint-load audit passed:",
        f"{systems} systems, {heavy} heavy-atom, {light} light-load",
    )


if __name__ == "__main__":
    main()

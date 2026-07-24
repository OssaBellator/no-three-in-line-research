#!/usr/bin/env python3
"""Verify RI2k/RI3a product-coloured quotient dynamics."""

from __future__ import annotations

from itertools import product
from math import gcd


def walk(
    start: int,
    root_colour: int,
    colours: tuple[int, ...],
    order: int,
) -> tuple[int, ...]:
    vertices = [start]
    for colour in colours:
        vertices.append(
            (root_colour + colour - vertices[-1]) % order
        )
    return tuple(vertices)


def generated_ratio_subgroup(
    colours: set[int],
    order: int,
) -> set[int]:
    if not colours:
        return {0}
    base = min(colours)
    step = order
    for colour in colours:
        step = gcd(step, (colour - base) % order)
    return {
        multiple * step % order
        for multiple in range(order // step)
    }


def verify_walk_formula(maximum_order: int = 8, maximum_length: int = 4) -> None:
    """Exhaustively check every colour word in the advertised small range."""
    for order in range(1, maximum_order + 1):
        for root_colour in range(order):
            for start in range(order):
                for length in range(1, maximum_length + 1):
                    for colours in product(range(order), repeat=length):
                        vertices = walk(
                            start,
                            root_colour,
                            colours,
                            order,
                        )
                        for index, vertex in enumerate(vertices):
                            if index % 2 == 0:
                                half = index // 2
                                closed = start
                                for offset in range(half):
                                    closed += (
                                        colours[2 * offset + 1]
                                        - colours[2 * offset]
                                    )
                            else:
                                half = (index - 1) // 2
                                closed = root_colour - start
                                closed += sum(
                                    colours[2 * offset]
                                    for offset in range(half + 1)
                                )
                                closed -= sum(
                                    colours[2 * offset + 1]
                                    for offset in range(half)
                                )
                            assert vertex == closed % order

                        if vertices[-1] == start:
                            if length % 2 == 0:
                                assert sum(colours[1::2]) % order == (
                                    sum(colours[0::2]) % order
                                )
                            else:
                                assert 2 * start % order == (
                                    root_colour
                                    + sum(colours[0::2])
                                    - sum(colours[1::2])
                                ) % order

                        colour_set = set(colours)
                        subgroup = generated_ratio_subgroup(
                            colour_set,
                            order,
                        )
                        base = min(colour_set)
                        even_coset = {
                            (start + element) % order
                            for element in subgroup
                        }
                        odd_coset = {
                            (
                                root_colour
                                - start
                                + base
                                + element
                            ) % order
                            for element in subgroup
                        }
                        assert set(vertices[0::2]) <= even_coset
                        assert set(vertices[1::2]) <= odd_coset
                        assert colour_set <= {
                            (base + element) % order
                            for element in subgroup
                        }
                        assert len(set(vertices)) <= 2 * len(subgroup)


def verify_cycle_multiplicity(maximum_order: int = 30) -> None:
    for order in range(1, maximum_order + 1):
        for target in range(order):
            roots = [
                value
                for value in range(order)
                if 2 * value % order == target
            ]
            assert len(roots) in (0, gcd(2, order))
            if len(roots) == 2:
                assert (roots[1] - roots[0]) % order == order // 2

        for root_colour in range(order):
            for colour in range(order):
                neighbour = lambda value: (
                    root_colour + colour - value
                ) % order
                assert all(
                    neighbour(neighbour(value)) == value
                    for value in range(order)
                )


def main() -> None:
    verify_walk_formula()
    verify_cycle_multiplicity()
    print("rational quotient cycle dynamics: verified")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite checks for PX256--PX259."""

from __future__ import annotations

import random
from collections import Counter


def colour(n: int, anchor: int, block: int, row: int, column: int) -> int:
    multiplier = (anchor + 1) % n or 1
    return (row + multiplier * column + block * anchor) % n


def matching_edges(permutation: tuple[int, ...]) -> set[tuple[int, int]]:
    return {(row, permutation[row]) for row in range(len(permutation))}


def executable_swaps(
    permutation: tuple[int, ...], forbidden: set[tuple[int, int]]
) -> list[tuple[int, int, tuple[int, int], tuple[int, int]]]:
    output = []
    for first in range(len(permutation)):
        for second in range(first + 1, len(permutation)):
            cross_one = (first, permutation[second])
            cross_two = (second, permutation[first])
            if cross_one not in forbidden and cross_two not in forbidden:
                output.append((first, second, cross_one, cross_two))
    return output


def swapped(permutation: tuple[int, ...], first: int, second: int) -> tuple[int, ...]:
    output = list(permutation)
    output[first], output[second] = output[second], output[first]
    return tuple(output)


def potential(
    first_matching: tuple[int, ...],
    second_matching: tuple[int, ...],
    anchors: range,
) -> int:
    order = len(first_matching)
    value = 0
    for anchor in anchors:
        first_counts = Counter(
            colour(order, anchor, 1, row, first_matching[row])
            for row in range(order)
        )
        second_counts = Counter(
            colour(order, anchor, 2, row, second_matching[row])
            for row in range(order)
        )
        value += sum(
            first_counts[key] * second_counts[key]
            for key in set(first_counts) | set(second_counts)
        )
    return value


def shadow(
    other_matching: tuple[int, ...],
    anchors: range,
    block: int,
    other_block: int,
    edge: tuple[int, int],
) -> int:
    order = len(other_matching)
    value = 0
    for anchor in anchors:
        edge_colour = colour(order, anchor, block, *edge)
        value += sum(
            colour(order, anchor, other_block, row, other_matching[row])
            == edge_colour
            for row in range(order)
        )
    return value


def maximum_degree(edges: set[tuple[int, int]], order: int) -> int:
    return max(
        [sum(row == edge_row for edge_row, _ in edges) for row in range(order)]
        + [sum(column == edge_column for _, edge_column in edges) for column in range(order)]
        + [0]
    )


def check(seed: int = 256) -> None:
    rng = random.Random(seed)
    for order in (5, 7):
        anchors = range(min(3, order - 1))
        for _ in range(800):
            first = list(range(order))
            second = list(range(order))
            rng.shuffle(first)
            rng.shuffle(second)
            first = tuple(first)
            second = tuple(second)

            forbidden_one: set[tuple[int, int]] = set()
            forbidden_two: set[tuple[int, int]] = set()
            for forbidden, selected in ((forbidden_one, first), (forbidden_two, second)):
                partial = list(range(order))
                rng.shuffle(partial)
                for row in range(order):
                    if rng.random() < 0.35:
                        forbidden.add((row, partial[row]))
                forbidden.difference_update(matching_edges(selected))

            delta_one = maximum_degree(forbidden_one, order)
            delta_two = maximum_degree(forbidden_two, order)
            swaps_one = executable_swaps(first, forbidden_one)
            swaps_two = executable_swaps(second, forbidden_two)
            base = potential(first, second, anchors)

            left = sum(
                potential(swapped(first, i, j), second, anchors) - base
                for i, j, _f, _g in swaps_one
            )
            left += sum(
                potential(first, swapped(second, i, j), anchors) - base
                for i, j, _f, _g in swaps_two
            )

            shadow_one = sum(
                shadow(second, anchors, 1, 2, (row, column))
                for row in range(order)
                for column in range(order)
                if column != first[row] and (row, column) not in forbidden_one
            )
            shadow_two = sum(
                shadow(first, anchors, 2, 1, (row, column))
                for row in range(order)
                for column in range(order)
                if column != second[row] and (row, column) not in forbidden_two
            )
            destruction = 2 * order - 2 - 2 * (delta_one + delta_two)
            assert left <= shadow_one + shadow_two - destruction * base


def main() -> None:
    check()
    print("PX256--PX259 two-block rainbow checks passed")


if __name__ == "__main__":
    main()

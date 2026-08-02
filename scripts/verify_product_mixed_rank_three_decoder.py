#!/usr/bin/env python3
"""Finite checks for PX260--PX262."""

from __future__ import annotations

import random
from collections import Counter


def anchor_colour(anchor_matching: tuple[int, ...], anchor_row: int, row: int, column: int) -> int:
    order = len(anchor_matching)
    anchor_code = (anchor_row + 2 * anchor_matching[anchor_row] + 1) % order
    multiplier = (anchor_code + 1) % order or 1
    return (row + multiplier * column + anchor_code) % order


def potential(first: tuple[int, ...], anchors: tuple[int, ...]) -> int:
    value = 0
    for anchor_row in range(len(anchors)):
        counts = Counter(
            anchor_colour(anchors, anchor_row, row, first[row])
            for row in range(len(first))
        )
        value += sum(count * (count - 1) // 2 for count in counts.values())
    return value


def swaps(permutation: tuple[int, ...], forbidden: set[tuple[int, int]]):
    for first in range(len(permutation)):
        for second in range(first + 1, len(permutation)):
            cross_one = (first, permutation[second])
            cross_two = (second, permutation[first])
            if cross_one not in forbidden and cross_two not in forbidden:
                yield first, second, cross_one, cross_two


def swapped(permutation: tuple[int, ...], first: int, second: int) -> tuple[int, ...]:
    output = list(permutation)
    output[first], output[second] = output[second], output[first]
    return tuple(output)


def maximum_degree(edges: set[tuple[int, int]], order: int) -> int:
    return max(
        [sum(edge_row == row for edge_row, _ in edges) for row in range(order)]
        + [sum(edge_column == column for _, edge_column in edges) for column in range(order)]
        + [0]
    )


def one_shadow(
    first: tuple[int, ...], anchors: tuple[int, ...], edge: tuple[int, int]
) -> int:
    value = 0
    row, column = edge
    for anchor_row in range(len(anchors)):
        edge_colour = anchor_colour(anchors, anchor_row, row, column)
        for selected_row in range(len(first)):
            if selected_row == row or first[selected_row] == column:
                continue
            value += (
                anchor_colour(
                    anchors, anchor_row, selected_row, first[selected_row]
                )
                == edge_colour
            )
    return value


def pair_anchor_weight(
    anchors: tuple[int, ...], first_edge: tuple[int, int], second_edge: tuple[int, int]
) -> int:
    return sum(
        anchor_colour(anchors, anchor_row, *first_edge)
        == anchor_colour(anchors, anchor_row, *second_edge)
        for anchor_row in range(len(anchors))
    )


def check(seed: int = 260) -> None:
    rng = random.Random(seed)
    for order in (5, 7):
        for _ in range(1000):
            first = list(range(order))
            anchors = list(range(order))
            rng.shuffle(first)
            rng.shuffle(anchors)
            first = tuple(first)
            anchors = tuple(anchors)

            forbidden: set[tuple[int, int]] = set()
            partial = list(range(order))
            rng.shuffle(partial)
            for row in range(order):
                if rng.random() < 0.4:
                    forbidden.add((row, partial[row]))
            forbidden.difference_update((row, first[row]) for row in range(order))
            delta = maximum_degree(forbidden, order)
            executable = list(swaps(first, forbidden))
            base = potential(first, anchors)

            left = sum(
                potential(swapped(first, i, j), anchors) - base
                for i, j, _f, _g in executable
            )
            shadow_one = sum(
                one_shadow(first, anchors, (row, column))
                for row in range(order)
                for column in range(order)
                if column != first[row] and (row, column) not in forbidden
            )
            shadow_two = sum(
                pair_anchor_weight(anchors, cross_one, cross_two)
                for _i, _j, cross_one, cross_two in executable
            )
            destruction = 2 * (order - 2 - 2 * delta)
            assert left <= shadow_one + shadow_two - destruction * base


def main() -> None:
    check()
    print("PX260--PX262 mixed rank-three checks passed")


if __name__ == "__main__":
    main()

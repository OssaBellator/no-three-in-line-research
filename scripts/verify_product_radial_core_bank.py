#!/usr/bin/env python3
"""Verify the radial-core line count and common-layer endpoint extraction."""
from __future__ import annotations

from itertools import product
from math import comb, gcd
from random import Random

TaggedPoint = tuple[int, int, int]
Permutation = tuple[int, ...]
ORIENTATIONS = ("cc", "cf", "fc", "ff")


def flatten(n: int, coarse: int, fine: int, mode: str) -> int:
    return n * coarse + fine if mode == "c" else 2 * fine + coarse


def tagged_rectangle_state(
    p: Permutation,
    t: Permutation,
    r: Permutation,
    orientation: str,
) -> tuple[TaggedPoint, ...]:
    n = len(p)
    points: list[TaggedPoint] = []
    for rectangle in range(n):
        for coarse_row, coarse_column in product((0, 1), repeat=2):
            row_digit = rectangle if coarse_row == 0 else p[rectangle]
            column_digit = (
                t[rectangle] if coarse_column == 0 else r[rectangle]
            )
            layer = coarse_row ^ coarse_column
            points.append(
                (
                    flatten(n, coarse_row, row_digit, orientation[0]),
                    flatten(n, coarse_column, column_digit, orientation[1]),
                    layer,
                )
            )
    return tuple(points)


def direction(center: tuple[int, int], point: TaggedPoint) -> tuple[int, int]:
    delta_x = point[0] - center[0]
    delta_y = point[1] - center[1]
    divisor = gcd(abs(delta_x), abs(delta_y))
    delta_x //= divisor
    delta_y //= divisor
    if delta_x < 0 or (delta_x == 0 and delta_y < 0):
        delta_x = -delta_x
        delta_y = -delta_y
    return delta_x, delta_y


def verify_center(points: tuple[TaggedPoint, ...], center: tuple[int, int]) -> None:
    groups: dict[tuple[int, int], list[TaggedPoint]] = {}
    for point in points:
        groups.setdefault(direction(center, point), []).append(point)

    loaded = [group for group in groups.values() if 3 <= len(group) <= 12]
    if any(len(group) >= 13 for group in groups.values()):
        return

    radial_mass = sum(comb(len(group), 3) for group in loaded)
    assert 220 * len(loaded) >= radial_mass

    represented = {
        layer: [group for group in loaded if any(point[2] == layer for point in group)]
        for layer in (0, 1)
    }
    chosen_layer = max(represented, key=lambda layer: len(represented[layer]))
    chosen_groups = represented[chosen_layer]
    assert 2 * len(chosen_groups) >= len(loaded)

    chosen = [
        next(point for point in group if point[2] == chosen_layer)
        for group in chosen_groups
    ]
    assert len({point[0] for point in chosen}) == len(chosen)
    assert len({point[1] for point in chosen}) == len(chosen)

    if radial_mass:
        assert len(chosen) * 440 >= radial_mass


def main() -> None:
    random = Random(590080)
    for n in range(4, 11):
        checked = 0
        for orientation in ORIENTATIONS:
            for _ in range(8):
                permutations_list: list[Permutation] = []
                for _ in range(3):
                    values = list(range(n))
                    random.shuffle(values)
                    permutations_list.append(tuple(values))
                points = tagged_rectangle_state(*permutations_list, orientation)
                selected = {(x, y) for x, y, _ in points}
                side = 2 * n
                for center in set(product(range(side), repeat=2)) - selected:
                    verify_center(points, center)
                    checked += 1
        print(f"n={n}: radial-core centers checked={checked}")

    print("radial-core extraction checks passed")


if __name__ == "__main__":
    main()

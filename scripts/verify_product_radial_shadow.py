#!/usr/bin/env python3
"""Verify the radial shadow decomposition in rectangle states."""
from __future__ import annotations

from itertools import product
from math import comb, gcd
from random import Random

Point = tuple[int, int]
Permutation = tuple[int, ...]
ORIENTATIONS = ("cc", "cf", "fc", "ff")


def flatten(n: int, coarse: int, fine: int, mode: str) -> int:
    return n * coarse + fine if mode == "c" else 2 * fine + coarse


def rectangle_state(
    p: Permutation,
    t: Permutation,
    r: Permutation,
    orientation: str,
) -> set[Point]:
    n = len(p)
    return {
        (
            flatten(n, coarse_row, rectangle if coarse_row == 0 else p[rectangle], orientation[0]),
            flatten(n, coarse_column, t[rectangle] if coarse_column == 0 else r[rectangle], orientation[1]),
        )
        for rectangle in range(n)
        for coarse_row, coarse_column in product((0, 1), repeat=2)
    }


def direction(center: Point, point: Point) -> Point:
    delta_x = point[0] - center[0]
    delta_y = point[1] - center[1]
    divisor = gcd(abs(delta_x), abs(delta_y))
    delta_x //= divisor
    delta_y //= divisor
    if delta_x < 0 or (delta_x == 0 and delta_y < 0):
        delta_x = -delta_x
        delta_y = -delta_y
    return delta_x, delta_y


def verify_center(selected: set[Point], center: Point) -> None:
    populations: dict[Point, int] = {}
    for point in selected:
        key = direction(center, point)
        populations[key] = populations.get(key, 0) + 1

    pair_shadow = sum(comb(population, 2) for population in populations.values())
    radial_triples = sum(
        comb(population, 3) for population in populations.values()
    )
    clean_secants = sum(population == 2 for population in populations.values())

    assert clean_secants >= pair_shadow - 3 * radial_triples
    assert 2 * clean_secants >= pair_shadow or 6 * radial_triples >= pair_shadow


def main() -> None:
    random = Random(560069)
    for n in range(3, 9):
        checked_centers = 0
        for orientation in ORIENTATIONS:
            for _ in range(5):
                permutations_list: list[Permutation] = []
                for _ in range(3):
                    values = list(range(n))
                    random.shuffle(values)
                    permutations_list.append(tuple(values))
                selected = rectangle_state(*permutations_list, orientation)
                side = 2 * n
                for center in set(product(range(side), repeat=2)) - selected:
                    verify_center(selected, center)
                    checked_centers += 1
        print(f"n={n}: radial centers checked={checked_centers}")

    print("radial shadow decomposition checks passed")


if __name__ == "__main__":
    main()

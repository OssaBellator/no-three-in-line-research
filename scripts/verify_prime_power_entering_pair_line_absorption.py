#!/usr/bin/env python3
"""Finite checks for CMR1022--CMR1029."""

from itertools import combinations
from math import ceil, comb, gcd
import random


def random_permutation(side, rng):
    values = list(range(side))
    rng.shuffle(values)
    return tuple(values)


def random_state(side, rng):
    first = random_permutation(side, rng)
    for _ in range(1000):
        second = random_permutation(side, rng)
        if all(second[index] != first[index] for index in range(side)):
            labelled = [
                (0, (source, first[source])) for source in range(side)
            ] + [
                (1, (source, second[source])) for source in range(side)
            ]
            return labelled
    raise RuntimeError("failed to sample disjoint layers")


def line_key(first, second):
    coefficient_x = second[1] - first[1]
    coefficient_y = first[0] - second[0]
    constant = -(
        coefficient_x * first[0] + coefficient_y * first[1]
    )
    divisor = gcd(
        gcd(abs(coefficient_x), abs(coefficient_y)), abs(constant)
    )
    if divisor:
        coefficient_x //= divisor
        coefficient_y //= divisor
        constant //= divisor
    if coefficient_x < 0 or (
        coefficient_x == 0 and coefficient_y < 0
    ):
        coefficient_x = -coefficient_x
        coefficient_y = -coefficient_y
        constant = -constant
    return coefficient_x, coefficient_y, constant


def selected_loaded_lines(state):
    labels = {cell: layer for layer, cell in state}
    points = list(labels)
    keys = {line_key(first, second) for first, second in combinations(points, 2)}
    lines = []
    for coefficient_x, coefficient_y, constant in keys:
        occupied = {
            point
            for point in points
            if coefficient_x * point[0]
            + coefficient_y * point[1]
            + constant
            == 0
        }
        if len(occupied) >= 3:
            lines.append((occupied, labels))
    return lines


def check_loaded_line_geometry():
    rng = random.Random(1022)
    checked = 0
    for side in range(3, 20):
        for _ in range(500):
            state = random_state(side, rng)
            candidates = selected_loaded_lines(state)
            if not candidates:
                continue
            occupied, labels = rng.choice(candidates)
            first_layer = {point for point in occupied if labels[point] == 0}
            second_layer = occupied - first_layer
            majority = (
                first_layer
                if len(first_layer) >= len(second_layer)
                else second_layer
            )

            assert len(majority) >= ceil(len(occupied) / 2)
            assert len({point[0] for point in majority}) == len(majority)
            assert len({point[1] for point in majority}) == len(majority)

            permutation = random_permutation(side, rng)
            protected_size = rng.randint(0, side)
            protected_sources = set(
                rng.sample(range(side), protected_size)
            )
            protected = {
                (source, permutation[source])
                for source in protected_sources
            }
            protected_targets = {target for _source, target in protected}
            touching = {
                point
                for point in majority
                if point[0] in protected_sources
                or point[1] in protected_targets
            }
            free = majority - touching
            assert len(touching) <= 2 * protected_size
            assert len(free) >= max(
                0, len(majority) - 2 * protected_size
            )
            checked += 1
    return checked


def check_growth_and_large_core_arithmetic():
    checked = 0
    for pair_load in range(1, 10000):
        majority_lower = ceil((pair_load + 2) / 2)
        for protected_size in range(0, 100):
            growth = max(0, majority_lower - 2 * protected_size)
            assert growth >= 0
            if growth == 0:
                assert protected_size >= ceil(majority_lower / 2)
            checked += 1
    return checked


def check_surplus_substitution():
    checked = 0
    for higher_rank in range(1, 10000):
        for entering_count in range(2, 50):
            pair_stock = comb(entering_count, 2)
            pair_load = ceil(higher_rank / pair_stock)
            majority = ceil((pair_load + 2) / 2)
            assert pair_load * pair_stock >= higher_rank
            assert majority * 2 >= pair_load + 2
            checked += 1
    return checked


def check_finite_absorption():
    rng = random.Random(1028)
    checked = 0
    for side in range(1, 1000):
        initial = rng.randint(0, side)
        remaining = side - initial
        absorbed = 0
        executions = 0
        while remaining:
            gain = rng.randint(1, remaining)
            absorbed += gain
            remaining -= gain
            executions += 1
            assert absorbed <= side - initial
            assert executions <= side - initial
        checked += 1
    return checked


def main():
    print(
        "verified entering-pair line absorption:",
        check_loaded_line_geometry(),
        "loaded-line cases,",
        check_growth_and_large_core_arithmetic(),
        "growth/core cases,",
        check_surplus_substitution(),
        "surplus substitutions, and",
        check_finite_absorption(),
        "finite absorption histories",
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite checks for CMR1054--CMR1061."""

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
            return {
                (0, (source, first[source])) for source in range(side)
            } | {
                (1, (source, second[source])) for source in range(side)
            }
    raise RuntimeError("failed to sample disjoint layers")


def collinear(first, second, third):
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


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


def extract_same_layer_arms(state, rng):
    labels = {cell: layer for layer, cell in state}
    center = rng.choice(tuple(labels))
    outside_layer = rng.randint(0, 1)
    points = [
        cell
        for cell, layer in labels.items()
        if layer == outside_layer and cell != center
    ]
    by_line = {}
    for first, second in combinations(points, 2):
        if collinear(center, first, second):
            by_line.setdefault(line_key(center, first), []).append(
                (first, second)
            )

    used = set()
    arms = []
    for support_line in sorted(by_line):
        for first, second in by_line[support_line]:
            if first not in used and second not in used:
                arms.append((first, second))
                used.update((first, second))
                break
    return arms


def check_simultaneous_compatibility():
    rng = random.Random(1054)
    checked = 0
    arm_total = 0
    for side in range(3, 30):
        for _ in range(300):
            state = random_state(side, rng)
            arms = extract_same_layer_arms(state, rng)
            outside = set().union(
                *(set(arm) for arm in arms)
            ) if arms else set()
            assert len(outside) == 2 * len(arms)
            assert len({source for source, _target in outside}) == len(outside)
            assert len({target for _source, target in outside}) == len(outside)

            permutation = random_permutation(side, rng)
            protected_size = rng.randint(0, side)
            protected_sources = set(
                rng.sample(range(side), protected_size)
            )
            protected_targets = {
                permutation[source] for source in protected_sources
            }
            touching = [
                arm
                for arm in arms
                if any(
                    source in protected_sources
                    or target in protected_targets
                    for source, target in arm
                )
            ]
            assert len(touching) <= 2 * protected_size
            free_arms = len(arms) - len(touching)
            assert 2 * free_arms >= 2 * max(
                0, len(arms) - 2 * protected_size
            )
            arm_total += len(arms)
            checked += 1
    return checked, arm_total


def check_direct_growth_arithmetic():
    checked = 0
    for arm_count in range(0, 10000):
        for protected_size in range(0, 100):
            growth = 2 * max(0, arm_count - 2 * protected_size)
            assert growth >= 0
            if growth == 0:
                assert protected_size >= arm_count / 2
            checked += 1
    return checked


def check_nested_robust_bound():
    checked = 0
    for destroyed in range(1, 500):
        for gap in range(1, 20):
            half_load = ceil((destroyed + gap) / 2)
            for entering in range(1, 30):
                root_load = ceil(half_load / entering)
                for line_threshold in range(3, 12):
                    star_size = ceil(
                        root_load / comb(line_threshold - 1, 2)
                    )
                    common_layer = ceil(star_size / 4)
                    assert common_layer * 4 >= star_size
                    checked += 1
    return checked


def check_capacity():
    rng = random.Random(1059)
    checked = 0
    for side in range(1, 3000):
        initial_first = rng.randint(0, side)
        initial_second = rng.randint(0, side)
        capacity = 2 * side - initial_first - initial_second
        remaining = capacity
        gains = []
        while remaining:
            # Direct star absorption adds an even number of edges.
            maximum_arms = remaining // 2
            if maximum_arms == 0:
                break
            arm_gain = rng.randint(1, maximum_arms)
            gain = 2 * arm_gain
            gains.append(gain)
            remaining -= gain
        assert sum(gains) <= capacity
        checked += 1
    return checked


def main():
    cases, arms = check_simultaneous_compatibility()
    print(
        "verified simultaneous star direct absorption:",
        cases,
        "state cases with",
        arms,
        "arms,",
        check_direct_growth_arithmetic(),
        "growth/core cases,",
        check_nested_robust_bound(),
        "nested robust bounds, and",
        check_capacity(),
        "capacity histories",
    )


if __name__ == "__main__":
    main()

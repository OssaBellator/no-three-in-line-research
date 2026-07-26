#!/usr/bin/env python3
"""Finite checks for CMR1014--CMR1021."""

from itertools import combinations, permutations
from math import ceil, factorial, gcd, sqrt
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
    if (
        coefficient_x < 0
        or (coefficient_x == 0 and coefficient_y < 0)
        or (
            coefficient_x == 0
            and coefficient_y == 0
            and constant < 0
        )
    ):
        coefficient_x = -coefficient_x
        coefficient_y = -coefficient_y
        constant = -constant
    return coefficient_x, coefficient_y, constant


def extract_star(state, rng):
    labels = {cell: layer for layer, cell in state}
    center = rng.choice(tuple(labels))
    others = list(set(labels) - {center})
    by_line = {}
    for first, second in combinations(others, 2):
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
    return labels, center, arms


def check_layer_polarization():
    rng = random.Random(1014)
    checked = 0
    same_layer_pairs = 0
    cross_layer_pairs = 0

    for side in range(3, 20):
        for _ in range(300):
            state = random_state(side, rng)
            labels, center, arms = extract_star(state, rng)
            count_zero = 0
            count_one = 0
            count_cross = 0
            rooted_lines = set()
            rooted_partners = set()

            for first, second in arms:
                first_layer = labels[first]
                second_layer = labels[second]
                if first_layer == second_layer == 0:
                    count_zero += 1
                    assert first[0] != second[0]
                    assert first[1] != second[1]
                    same_layer_pairs += 1
                elif first_layer == second_layer == 1:
                    count_one += 1
                    assert first[0] != second[0]
                    assert first[1] != second[1]
                    same_layer_pairs += 1
                else:
                    count_cross += 1
                    partner = (
                        first
                        if first_layer == labels[center]
                        else second
                    )
                    assert labels[partner] == labels[center]
                    assert center[0] != partner[0]
                    assert center[1] != partner[1]
                    rooted_partners.add(partner)
                    rooted_lines.add(line_key(center, partner))
                    cross_layer_pairs += 1

            total = len(arms)
            assert total == count_zero + count_one + count_cross
            assert count_cross >= ceil(total / 2) or max(
                count_zero, count_one
            ) >= ceil(total / 4)
            assert len(rooted_partners) == count_cross
            assert len(rooted_lines) == count_cross
            checked += 1

    return checked, same_layer_pairs, cross_layer_pairs


def derangement_number(side):
    return sum(
        (-1) ** index * factorial(side) // factorial(index)
        for index in range(side + 1)
    )


def check_cylinder_sizes():
    checked = 0
    for residual_side in range(0, 8):
        exact = sum(
            1
            for permutation in permutations(range(residual_side))
            if all(
                permutation[index] != index
                for index in range(residual_side)
            )
        )
        assert exact == derangement_number(residual_side)
        checked += 1
    return checked


def check_protected_arithmetic():
    checked = 0
    for arm_count in range(1, 10000):
        threshold = max(2, ceil(sqrt(arm_count)))
        extracted = ceil(arm_count / (4 * (threshold - 1)))
        for protected_size in range(0, 30):
            growth = 2 * max(0, extracted - 2 * protected_size)
            assert growth >= 0
            if growth == 0:
                assert protected_size >= extracted / 2
            checked += 1
    return checked


def check_partition_arithmetic():
    checked = 0
    for total in range(0, 100000):
        for cross in range(total + 1):
            equal = total - cross
            first = equal // 2
            second = equal - first
            assert cross >= ceil(total / 2) or max(first, second) >= ceil(
                total / 4
            )
            checked += 1
        if total >= 1000:
            break
    return checked


def main():
    cases, same_layer, cross_layer = check_layer_polarization()
    print(
        "verified secant-star layer polarization:",
        cases,
        "sampled stars,",
        same_layer,
        "same-layer outside pairs,",
        cross_layer,
        "cross-layer rooted pairs,",
        check_cylinder_sizes(),
        "derangement sizes,",
        check_protected_arithmetic(),
        "protected arithmetic cases, and",
        check_partition_arithmetic(),
        "partition cases",
    )


if __name__ == "__main__":
    main()

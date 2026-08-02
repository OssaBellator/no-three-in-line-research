#!/usr/bin/env python3
"""Exact dependent-bank checks for PX253--PX255."""

from __future__ import annotations

import itertools
import math
import random
from collections import Counter


def falling(order: int, rank: int) -> int:
    value = 1
    for offset in range(rank):
        value *= order - offset
    return value


def spread_factor(order: int, degree: int) -> float:
    return (1 - 1 / (order - 4 * degree)) ** (-degree * order)


def contains(permutation: tuple[int, ...], event: tuple[tuple[int, int], ...]) -> bool:
    return all(permutation[row] == column for row, column in event)


def inverse(permutation: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * len(permutation)
    for row, column in enumerate(permutation):
        result[column] = row
    return tuple(result)


def transform_columns(
    event: tuple[tuple[int, int], ...],
    forbidden_matching: tuple[int, ...],
) -> tuple[tuple[int, int], ...]:
    inverse_forbidden = inverse(forbidden_matching)
    return tuple(sorted((row, inverse_forbidden[column]) for row, column in event))


def build_derangement_cylinders(order: int) -> tuple[list[tuple[int, ...]], Counter]:
    permutations = list(itertools.permutations(range(order)))
    derangements = [
        permutation
        for permutation in permutations
        if all(permutation[row] != row for row in range(order))
    ]
    cylinder_count: Counter[tuple[tuple[int, int], ...]] = Counter()
    for permutation in derangements:
        edges = [(row, permutation[row]) for row in range(order)]
        for rank in range(1, 4):
            for event in itertools.combinations(edges, rank):
                cylinder_count[tuple(sorted(event))] += 1
    return derangements, cylinder_count


def joint_probability(
    first_family: list[tuple[int, ...]],
    second_cylinders: Counter,
    first_event: tuple[tuple[int, int], ...],
    second_event: tuple[tuple[int, int], ...],
) -> float:
    family_size = len(first_family)
    numerator = 0
    for first_matching in first_family:
        if not contains(first_matching, first_event):
            continue
        transformed = transform_columns(second_event, first_matching)
        numerator += second_cylinders.get(transformed, 0)
    return numerator / (family_size * family_size)


def random_partial_event(
    rng: random.Random,
    permutation: tuple[int, ...],
    rank: int,
) -> tuple[tuple[int, int], ...]:
    rows = rng.sample(range(len(permutation)), rank)
    return tuple(sorted((row, permutation[row]) for row in rows))


def check_dependent_product_cylinders(seed: int = 253) -> None:
    # First matching avoids the identity.  Conditional on the first matching M_1,
    # the second matching avoids M_1 itself.  The second bank therefore depends
    # genuinely on the first, but column relabelling reduces every conditional
    # count to a derangement cylinder.
    order = 8
    degree = 1
    all_permutations = list(itertools.permutations(range(order)))
    first_family, cylinders = build_derangement_cylinders(order)
    factor = spread_factor(order, degree)
    rng = random.Random(seed)

    for _ in range(600):
        first_rank = rng.randint(0, 2)
        second_rank = rng.randint(0, 2)
        if first_rank + second_rank == 0:
            first_rank = 1

        first_event = random_partial_event(rng, rng.choice(all_permutations), first_rank)
        second_event = random_partial_event(rng, rng.choice(all_permutations), second_rank)
        probability = joint_probability(
            first_family,
            cylinders,
            first_event,
            second_event,
        )
        bound = (
            (factor if first_rank else 1) / falling(order, first_rank)
            * (factor if second_rank else 1) / falling(order, second_rank)
        )
        assert probability <= bound + 1e-15


def check_weighted_transfer(seed: int = 254) -> None:
    order = 8
    degree = 1
    all_permutations = list(itertools.permutations(range(order)))
    first_family, cylinders = build_derangement_cylinders(order)
    factor = spread_factor(order, degree)
    rng = random.Random(seed)

    exact_expectation = 0.0
    transfer_bound = 0.0
    for _ in range(150):
        first_rank = rng.randint(0, 2)
        second_rank = rng.randint(0, 2)
        if first_rank + second_rank == 0 or first_rank + second_rank > 3:
            continue
        first_event = random_partial_event(rng, rng.choice(all_permutations), first_rank)
        second_event = random_partial_event(rng, rng.choice(all_permutations), second_rank)
        weight = rng.randint(1, 7)

        exact_expectation += weight * joint_probability(
            first_family,
            cylinders,
            first_event,
            second_event,
        )
        transfer_bound += weight * (
            (factor if first_rank else 1) / falling(order, first_rank)
            * (factor if second_rank else 1) / falling(order, second_rank)
        )

    assert exact_expectation <= transfer_bound + 1e-12


def potential(points: set[str], triples: set[tuple[str, str, str]]) -> int:
    return sum(set(triple) <= points for triple in triples)


def check_union_shadow_no_double_count(seed: int = 255) -> None:
    rng = random.Random(seed)
    x = [f"x{i}" for i in range(4)]
    first = [f"a{i}" for i in range(3)]
    second = [f"b{i}" for i in range(3)]
    universe = x + first + second
    all_triples = list(itertools.combinations(universe, 3))

    for _ in range(1000):
        triples = {triple for triple in all_triples if rng.random() < 0.25}
        current = set(universe)
        background = set(x)
        union_shadow = potential(current, triples) - potential(background, triples)
        old_meeting_union = {
            triple
            for triple in triples
            if set(triple) <= current and set(triple) & set(first + second)
        }
        assert union_shadow == len(old_meeting_union)

        first_shadow = potential(current, triples) - potential(set(x + second), triples)
        second_shadow = potential(current, triples) - potential(set(x + first), triples)
        overlap = sum(
            set(triple) & set(first) and set(triple) & set(second)
            for triple in triples
        )
        assert first_shadow + second_shadow - overlap == union_shadow


def main() -> None:
    check_dependent_product_cylinders()
    check_weighted_transfer()
    check_union_shadow_no_double_count()
    print("PX253--PX255 coupled two-block spread checks passed")


if __name__ == "__main__":
    main()

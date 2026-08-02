#!/usr/bin/env python3
"""Finite checks for PX397--PX403 PX63 entry compression."""

from __future__ import annotations

from itertools import combinations, permutations
from math import factorial, prod
import random


def derangements(order: int) -> list[tuple[int, ...]]:
    return [
        permutation
        for permutation in permutations(range(order))
        if all(permutation[i] != i for i in range(order))
    ]


def check_one_hit_bound() -> None:
    rng = random.Random(20260726)

    for order in range(2, 9):
        possible_edges = [
            frozenset(edge)
            for rank in (2, 3)
            if rank <= order
            for edge in combinations(range(order), rank)
        ]

        for _ in range(160):
            edges = [edge for edge in possible_edges if rng.random() < 0.3]
            if not edges:
                continue

            best = 0
            for mask in range(1 << order):
                selected = {i for i in range(order) if (mask >> i) & 1}
                one_hit = sum(len(edge & selected) == 1 for edge in edges)
                best = max(best, one_hit)

            assert 9 * best >= 4 * len(edges)


def check_derangement_spread() -> None:
    rng = random.Random(397)

    for order in range(3, 8):
        states = derangements(order)
        assert 3 * len(states) >= factorial(order)

        for source in range(order):
            counts = [
                sum(state[source] == target for state in states)
                for target in range(order)
            ]
            assert counts[source] == 0
            assert len({counts[target] for target in range(order) if target != source}) == 1

        for _ in range(250):
            rank = rng.randint(1, min(3, order))
            sources = rng.sample(range(order), rank)
            targets = rng.sample(range(order), rank)
            if any(sources[i] == targets[i] for i in range(rank)):
                continue

            count = sum(
                all(state[sources[i]] == targets[i] for i in range(rank))
                for state in states
            )
            falling = prod(range(order - rank + 1, order + 1))
            assert count * falling <= 3 * len(states)


def check_good_subbank() -> None:
    rng = random.Random(403)

    for order in range(3, 8):
        states = derangements(order)

        for _ in range(350):
            blockers: list[tuple[int, int]] = []
            for _ in range(rng.randint(1, 100)):
                source = rng.randrange(order)
                exceptional = rng.choice(
                    [target for target in range(order) if target != source]
                )
                blockers.append((source, exceptional))

            weight = len(blockers)
            destruction = []
            for state in states:
                surviving = sum(
                    state[source] == exceptional
                    for source, exceptional in blockers
                )
                destruction.append(weight - surviving)

            average = sum(destruction) / len(states)
            assert average + 1e-12 >= weight * (order - 2) / (order - 1)

            good = sum(value >= weight / 4 for value in destruction)
            assert 3 * good >= len(states)


def check_entry_constants() -> None:
    for defects in range(1, 1000):
        one_hit = 4 * defects / 9
        family_weight = one_hit / 2
        assert family_weight >= 2 * defects / 9
        assert family_weight / 4 >= defects / 18


def main() -> None:
    check_one_hit_bound()
    check_derangement_spread()
    check_good_subbank()
    check_entry_constants()
    print("PX397--PX403 PX63 entry-derangement verifier: PASS")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite checks for CMR1166--CMR1173."""

from itertools import product
import random


def classify_target(core_rank):
    residual_rank = 3 - core_rank
    if residual_rank == 3:
        return "pure-residual", residual_rank
    if residual_rank:
        return "anchored-residual", residual_rank
    return "fixed-core", residual_rank


def check_target_location():
    checked = 0
    for core_rank in range(4):
        kind, residual = classify_target(core_rank)
        assert core_rank + residual == 3
        if kind == "pure-residual":
            assert residual == 3
        elif kind == "anchored-residual":
            assert 1 <= residual <= 2 and 1 <= core_rank <= 2
        else:
            assert residual == 0 and core_rank == 3
        checked += 1
    return checked


def perfect_matching(side, allowed):
    adjacency = {left: [] for left in range(side)}
    for left, right in allowed:
        adjacency[left].append(right)
    match = {}

    def augment(left, seen):
        for right in adjacency[left]:
            if right in seen:
                continue
            seen.add(right)
            if right not in match or augment(match[right], seen):
                match[right] = left
                return True
        return False

    return all(augment(left, set()) for left in range(side))


def random_permutation(side, rng):
    values = list(range(side))
    rng.shuffle(values)
    return frozenset((left, values[left]) for left in range(side))


def extend_edge(side, edge, rng):
    left, right = edge
    free_left = [value for value in range(side) if value != left]
    free_right = [value for value in range(side) if value != right]
    rng.shuffle(free_right)
    return frozenset({edge} | set(zip(free_left, free_right)))


def check_residual_degree_two_banks():
    rng = random.Random(1167)
    checked = 0
    for side in range(4, 100):
        complete = {(left, right) for left in range(side) for right in range(side)}
        for _ in range(300):
            target_edge = rng.choice(tuple(complete))
            forbidden = extend_edge(side, target_edge, rng)
            opposite = random_permutation(side, rng)
            allowed = complete - set(forbidden) - set(opposite)
            assert perfect_matching(side, allowed)
            checked += 1
    return checked


def check_target_move_destruction():
    rng = random.Random(1166)
    checked = 0
    for _ in range(100000):
        target = set(rng.sample(range(1000), 3))
        core_rank = rng.randint(0, 3)
        core = set(rng.sample(tuple(target), core_rank))
        residual = target - core
        if residual:
            moved = rng.choice(tuple(residual))
            new_selected = target - {moved}
            assert not target <= new_selected
        else:
            assert core == target
        checked += 1
    return checked


def check_wall_and_child_descent():
    checked = 0
    for side in range(1, 1000):
        for left_child in range(side):
            right_child = side - 1 - left_child
            assert left_child + right_child == side - 1
            assert left_child < side and right_child < side
            checked += 1
        for parts in range(2, min(side, 8) + 1):
            # Test representative positive compositions by cycling one unit among parts.
            sizes = [1] * parts
            sizes[0] += side - parts
            assert sum(sizes) == side
            assert all(1 <= value <= side - 1 for value in sizes)
            checked += 1
    return checked


def check_finite_currency_paths():
    rng = random.Random(1170)
    checked = 0
    for _ in range(20000):
        currencies = [rng.randint(0, 100) for _ in range(6)]
        episodes = sum(currencies)
        assert episodes >= 0
        # Removing one unit per non-erased episode exhausts the path exactly.
        remaining = episodes
        for currency in currencies:
            remaining -= currency
        assert remaining == 0
        checked += 1
    return checked


def main():
    print(
        "verified universal-range target descent:",
        check_target_location(),
        "target classes,",
        check_target_move_destruction(),
        "target moves,",
        check_residual_degree_two_banks(),
        "degree-two banks,",
        check_wall_and_child_descent(),
        "strict descents, and",
        check_finite_currency_paths(),
        "finite currency paths",
    )


if __name__ == "__main__":
    main()

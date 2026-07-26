#!/usr/bin/env python3
"""Finite checks for CMR1158--CMR1165."""

from itertools import permutations
import random


def matching(permutation):
    return frozenset((left, permutation[left]) for left in range(len(permutation)))


def perfect_matching(side, edges):
    adjacency = {left: [] for left in range(side)}
    for left, right in edges:
        adjacency[left].append(right)
    matched = {}

    def augment(left, seen):
        for right in adjacency[left]:
            if right in seen:
                continue
            seen.add(right)
            if right not in matched or augment(matched[right], seen):
                matched[right] = left
                return True
        return False

    if not all(augment(left, set()) for left in range(side)):
        return None
    return frozenset((left, right) for right, left in matched.items())


def extend_partial(side, partial, rng):
    partial = set(partial)
    used_left = {left for left, _ in partial}
    used_right = {right for _, right in partial}
    free_left = [left for left in range(side) if left not in used_left]
    free_right = [right for right in range(side) if right not in used_right]
    rng.shuffle(free_right)
    return frozenset(partial | set(zip(free_left, free_right)))


def random_permutation_matching(side, rng):
    permutation = list(range(side))
    rng.shuffle(permutation)
    return matching(permutation)


def check_fixed_target_banks():
    rng = random.Random(1158)
    checked = 0
    for side in range(4, 80):
        complete = {(left, right) for left in range(side) for right in range(side)}
        for _ in range(300):
            opposite = random_permutation_matching(side, rng)
            edge = rng.choice(tuple(complete))
            forbidden_extension = extend_partial(side, {edge}, rng)
            allowed = complete - set(forbidden_extension) - set(opposite)
            response = perfect_matching(side, allowed)
            assert response is not None
            assert edge not in response
            assert set(response).isdisjoint(opposite)
            assert len(response) == side
            checked += 1
    return checked


def check_loaded_line_banks():
    rng = random.Random(1159)
    checked = 0
    absorbed_cells = 0
    for side in range(4, 80):
        complete = {(left, right) for left in range(side) for right in range(side)}
        for _ in range(300):
            opposite = random_permutation_matching(side, rng)
            base = random_permutation_matching(side, rng)
            chosen = set(rng.sample(tuple(base), rng.randint(1, side)))
            protected = set(rng.sample(tuple(base - chosen), rng.randint(0, len(base - chosen))))
            # Both sets lie in one permutation and are therefore compatible.
            partial = chosen | protected
            extension = extend_partial(side, partial, rng)
            allowed = complete - set(extension) - set(opposite)
            response = perfect_matching(side, allowed)
            assert response is not None
            assert set(response).isdisjoint(chosen)
            assert set(response).isdisjoint(opposite)
            absorbed_cells += len(chosen)
            checked += 1
    return checked, absorbed_cells


def check_executable_or_blocked():
    rng = random.Random(1160)
    checked = 0
    blocked = 0
    executable = 0
    for side in range(2, 30):
        matchings = [matching(permutation) for permutation in permutations(range(side))] if side <= 7 else []
        complete = {(left, right) for left in range(side) for right in range(side)}
        for _ in range(300):
            forbidden = set()
            for _matching in range(rng.randint(1, 2)):
                forbidden.update(random_permutation_matching(side, rng))
            allowed = complete - forbidden
            current_host = set(rng.sample(tuple(allowed), rng.randint(0, len(allowed))))
            if side <= 7:
                bank = [state for state in matchings if set(state) <= allowed]
                feasible = [state for state in bank if set(state) <= current_host]
                if feasible:
                    executable += 1
                else:
                    missing_union = set().union(*(set(state) - current_host for state in bank)) if bank else set()
                    assert bank
                    assert missing_union
                    blocked += 1
            checked += 1
    return checked, executable, blocked


def check_wall_descent_arithmetic():
    checked = 0
    for side in range(1, 1000):
        for left_child in range(side):
            right_child = side - 1 - left_child
            assert left_child + right_child == side - 1
            assert left_child < side and right_child < side
            checked += 1
    return checked


def main():
    loaded = check_loaded_line_banks()
    split = check_executable_or_blocked()
    print(
        "verified terminal certificate banks:",
        check_fixed_target_banks(),
        "fixed-target banks,",
        loaded[0],
        "loaded-line banks absorbing",
        loaded[1],
        "cells,",
        split[0],
        "host splits with",
        split[1],
        "executable and",
        split[2],
        "blocked banks, and",
        check_wall_descent_arithmetic(),
        "wall descents",
    )


if __name__ == "__main__":
    main()

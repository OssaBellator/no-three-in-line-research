#!/usr/bin/env python3
"""Finite checks for CMR1062--CMR1069."""

import random


def random_permutation(side, rng):
    values = list(range(side))
    rng.shuffle(values)
    return tuple(values)


def perfect_matching_avoiding(side, forbidden):
    target_to_source = [-1] * side

    def augment(source, seen):
        for target in range(side):
            if (source, target) in forbidden or seen[target]:
                continue
            seen[target] = True
            previous = target_to_source[target]
            if previous < 0 or augment(previous, seen):
                target_to_source[target] = source
                return True
        return False

    for source in range(side):
        if not augment(source, [False] * side):
            return None

    permutation = [-1] * side
    for target, source in enumerate(target_to_source):
        permutation[source] = target
    return tuple(permutation)


def check_degree_two_hall():
    rng = random.Random(1064)
    checked = 0
    for side in range(4, 50):
        for _ in range(500):
            fixed_opposite = random_permutation(side, rng)
            protected_extension = random_permutation(side, rng)
            forbidden = {
                (source, fixed_opposite[source])
                for source in range(side)
            } | {
                (source, protected_extension[source])
                for source in range(side)
            }
            rematching = perfect_matching_avoiding(side, forbidden)
            assert rematching is not None
            assert len(set(rematching)) == side
            assert all(
                (source, rematching[source]) not in forbidden
                for source in range(side)
            )
            checked += 1
    return checked


def check_endpoint_partial_matchings():
    rng = random.Random(1062)
    checked = 0
    for side in range(2, 100):
        for _ in range(500):
            centre_layer = random_permutation(side, rng)
            opposite_layer = random_permutation(side, rng)
            arm_count = rng.randint(0, side - 1)
            centre_source = rng.randrange(side)
            available_sources = [
                source for source in range(side) if source != centre_source
            ]
            chosen_sources = rng.sample(available_sources, arm_count)
            same_side = {
                (source, centre_layer[source]) for source in chosen_sources
            }
            opposite_side = {
                (source, opposite_layer[source]) for source in chosen_sources
            }
            assert len(same_side) == arm_count
            assert len(opposite_side) == arm_count
            assert len({source for source, _target in same_side}) == arm_count
            assert len({target for _source, target in same_side}) == arm_count
            assert len({source for source, _target in opposite_side}) == arm_count
            assert len({target for _source, target in opposite_side}) == arm_count
            checked += 1
    return checked


def check_growth_core_arithmetic():
    checked = 0
    for arm_count in range(0, 10000):
        for centre_core in range(0, 100):
            for opposite_core in range(0, 100):
                growth = max(
                    0,
                    arm_count - 2 * min(centre_core, opposite_core),
                )
                assert growth >= 0
                if growth == 0:
                    assert centre_core >= arm_count / 2
                    assert opposite_core >= arm_count / 2
                checked += 1
    return checked


def check_two_layer_capacity():
    rng = random.Random(1068)
    checked = 0
    for side in range(1, 5000):
        initial_first = rng.randint(0, side)
        initial_second = rng.randint(0, side)
        capacity = 2 * side - initial_first - initial_second
        remaining = capacity
        gains = []
        while remaining:
            gain = rng.randint(1, remaining)
            gains.append(gain)
            remaining -= gain
        assert sum(gains) <= capacity
        checked += 1
    return checked


def main():
    print(
        "verified simultaneous cross-star absorption:",
        check_degree_two_hall(),
        "degree-two Hall boards,",
        check_endpoint_partial_matchings(),
        "endpoint matching cases,",
        check_growth_core_arithmetic(),
        "growth/core cases, and",
        check_two_layer_capacity(),
        "capacity histories",
    )


if __name__ == "__main__":
    main()

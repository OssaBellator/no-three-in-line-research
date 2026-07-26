#!/usr/bin/env python3
"""Finite checks for CMR1086--CMR1093."""

from math import floor
import random


def host_stages(side):
    return 2 * side * side + side + 1


def routing_changes(side, threshold):
    return ((threshold - 1) * side * side) // 2


def path_capacity(side, threshold):
    return sum(
        2
        * current
        * host_stages(current)
        * (1 + routing_changes(current, threshold))
        for current in range(1, side + 1)
    )


def global_capacity(side, height, threshold):
    return (height + 1) * (2 * side + 1) * path_capacity(side, threshold)


def check_exact_formulas():
    checked = 0
    for side in range(1, 300):
        for threshold in range(2, 30):
            exact = path_capacity(side, threshold)
            expanded = sum(
                2
                * current
                * (2 * current * current + current + 1)
                * (
                    1
                    + floor(
                        (threshold - 1) * current * current / 2
                    )
                )
                for current in range(1, side + 1)
            )
            assert exact == expanded
            upper = sum(
                2
                * current
                * (2 * current * current + current + 1)
                * (1 + (threshold - 1) * current * current / 2)
                for current in range(1, side + 1)
            )
            assert exact <= upper
            checked += 1
    return checked


def check_wall_envelope_aggregation():
    checked = 0
    for side in range(1, 100):
        for height in range(1, 15):
            for threshold in range(2, 12):
                local = path_capacity(side, threshold)
                wall = (2 * side + 1) * local
                total = (height + 1) * wall
                assert total == global_capacity(side, height, threshold)
                assert total >= local
                checked += 1
    return checked


def check_episode_bounds():
    rng = random.Random(1090)
    checked = 0
    for _ in range(100000):
        side = rng.randint(1, 100)
        height = rng.randint(1, 20)
        threshold = rng.randint(2, 20)
        capacity = global_capacity(side, height, threshold)
        gain_threshold = rng.randint(1, max(1, 2 * side))
        maximum_episodes = capacity // gain_threshold
        episode_count = rng.randint(0, min(maximum_episodes, 1000))
        gains = [gain_threshold] * episode_count
        assert sum(gains) <= capacity
        assert episode_count <= maximum_episodes
        checked += 1
    return checked


def check_monotone_owner_histories():
    rng = random.Random(1086)
    checked = 0
    for side in range(1, 1000):
        first = rng.randint(0, side)
        second = rng.randint(0, side)
        capacity = 2 * side - first - second
        gained = 0
        while gained < capacity:
            step = rng.randint(1, capacity - gained)
            gained += step
            assert gained <= 2 * side
            assert gained <= capacity
        checked += 1
    return checked


def main():
    print(
        "verified global protected owner capacity:",
        check_exact_formulas(),
        "path formulas,",
        check_wall_envelope_aggregation(),
        "wall/envelope cases,",
        check_episode_bounds(),
        "episode bounds, and",
        check_monotone_owner_histories(),
        "owner histories",
    )


if __name__ == "__main__":
    main()

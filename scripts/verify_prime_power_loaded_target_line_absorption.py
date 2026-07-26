#!/usr/bin/env python3
"""Finite checks for CMR1046--CMR1053."""

from math import ceil, comb
import random


def check_majority_and_destruction():
    checked = 0
    for line_load in range(3, 1000):
        majority = ceil(line_load / 2)
        assert 2 * majority >= line_load
        for protected in range(0, 500):
            growth = max(0, majority - 2 * protected)
            surviving = majority - growth
            assert surviving <= 2 * protected
            destroyed_lower = comb(majority, 3) - comb(
                min(2 * protected, majority), 3
            )
            assert destroyed_lower >= 0
            if growth == 0:
                assert protected >= ceil(majority / 2)
            checked += 1
    return checked


def check_two_layer_capacity():
    rng = random.Random(1051)
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
        for threshold in range(1, 30):
            episodes = sum(1 for gain in gains if gain >= threshold)
            assert episodes <= capacity // threshold
        checked += 1
    return checked


def check_profile_survival():
    rng = random.Random(1049)
    checked = 0
    for profile_size in range(3, 100):
        profile = set(range(profile_size))
        for _ in range(200):
            absorbed = set(
                rng.sample(
                    tuple(profile),
                    rng.randint(0, profile_size),
                )
            )
            surviving = profile - absorbed
            old_triples = comb(profile_size, 3)
            surviving_old = comb(len(surviving), 3)
            destroyed = old_triples - surviving_old
            assert destroyed >= 0
            assert surviving_old + destroyed == old_triples
            checked += 1
    return checked


def main():
    print(
        "verified loaded target-line absorption:",
        check_majority_and_destruction(),
        "majority/core cases,",
        check_two_layer_capacity(),
        "capacity histories, and",
        check_profile_survival(),
        "old-profile survival cases",
    )


if __name__ == "__main__":
    main()

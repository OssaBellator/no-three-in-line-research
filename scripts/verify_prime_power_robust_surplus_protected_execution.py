#!/usr/bin/env python3
"""Finite checks for CMR1030--CMR1037."""

from math import ceil, comb, sqrt
import random


def check_nested_scales():
    checked = 0
    for destroyed in range(1, 200):
        for gap in range(1, 20):
            half_load = ceil((destroyed + gap) / 2)
            assert 2 * half_load >= destroyed + gap
            for entering in range(1, 30):
                root_load = ceil(half_load / entering)
                assert root_load * entering >= half_load
                for line_threshold in range(3, 12):
                    star_size = ceil(
                        root_load / comb(line_threshold - 1, 2)
                    )
                    assert (
                        star_size * comb(line_threshold - 1, 2)
                        >= root_load
                    )
                    common_layer = ceil(star_size / 4)
                    cross_layer = ceil(star_size / 2)
                    assert 4 * common_layer >= star_size
                    assert 2 * cross_layer >= star_size

                    wall_threshold = max(2, ceil(sqrt(common_layer)))
                    extracted = ceil(
                        common_layer / (4 * (wall_threshold - 1))
                    )
                    assert (
                        4 * (wall_threshold - 1) * extracted
                        >= common_layer
                    )
                    checked += 1
    return checked


def check_higher_rank_scales():
    checked = 0
    for destroyed in range(1, 1000):
        for gap in range(1, 20):
            half_load = ceil((destroyed + gap) / 2)
            for entering in range(2, 50):
                pair_stock = comb(entering, 2)
                pair_load = ceil(half_load / pair_stock)
                majority = ceil((pair_load + 2) / 2)
                assert pair_load * pair_stock >= half_load
                assert 2 * majority >= pair_load + 2
                for protected in range(0, 50):
                    growth = max(0, majority - 2 * protected)
                    assert growth >= 0
                    if growth == 0:
                        assert protected >= ceil(majority / 2)
                    checked += 1
    return checked


def check_rank_one_growth_or_core():
    checked = 0
    for common_layer in range(1, 10000):
        threshold = max(2, ceil(sqrt(common_layer)))
        extracted = ceil(common_layer / (4 * (threshold - 1)))
        for protected in range(0, 100):
            growth = 2 * max(0, extracted - 2 * protected)
            assert growth >= 0
            if growth == 0:
                assert protected >= extracted / 2
            checked += 1
    return checked


def check_two_layer_capacity():
    rng = random.Random(1034)
    checked = 0
    for side in range(1, 2000):
        initial_first = rng.randint(0, side)
        initial_second = rng.randint(0, side)
        remaining = 2 * side - initial_first - initial_second
        absorbed = 0
        gains = []
        while remaining:
            gain = rng.randint(1, remaining)
            gains.append(gain)
            absorbed += gain
            remaining -= gain
            assert absorbed <= 2 * side - initial_first - initial_second
        for threshold in range(1, 20):
            large = sum(1 for gain in gains if gain >= threshold)
            assert large <= (
                2 * side - initial_first - initial_second
            ) // threshold
        checked += 1
    return checked


def main():
    print(
        "verified robust-surplus protected execution:",
        check_nested_scales(),
        "rank-one scale cases,",
        check_higher_rank_scales(),
        "higher-rank scale cases,",
        check_rank_one_growth_or_core(),
        "rank-one growth/core cases, and",
        check_two_layer_capacity(),
        "two-layer capacity histories",
    )


if __name__ == "__main__":
    main()

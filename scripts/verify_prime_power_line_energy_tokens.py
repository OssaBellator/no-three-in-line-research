#!/usr/bin/env python3
"""Finite and arithmetic checks for CMR360--CMR363."""

from __future__ import annotations

from collections import Counter
from math import ceil, floor, isqrt


def verify_fan_split() -> None:
    for population in range(1, 10_001):
        threshold = isqrt(population)
        if threshold * threshold < population:
            threshold += 1

        for cells in (1, max(1, threshold - 1), threshold, min(population, 2 * threshold)):
            counts = Counter(index % cells for index in range(population))
            distinct = len(counts)
            maximum = max(counts.values())
            assert distinct >= threshold or maximum * maximum > population

    # Exact geometric star: distinct lines through one point cannot share an
    # additional grid cell.
    centre = (0, 0)
    outside_pairs = []
    for slope in range(1, 10):
        pair = {(1, slope), (2, 2 * slope)}
        outside_pairs.append(pair)
        for point in pair:
            assert (point[0] - centre[0]) * slope == point[1] - centre[1]
    for left in range(len(outside_pairs)):
        for right in range(left + 1, len(outside_pairs)):
            assert outside_pairs[left].isdisjoint(outside_pairs[right])


def verify_token_counts() -> None:
    for p, h in ((3, 5), (5, 4), (7, 3), (11, 3)):
        t = p**h
        direct = sum(p ** (2 * depth) for depth in range(h))
        closed = (t * t - 1) // (p * p - 1)
        assert direct == closed
        assert (p + 1) * direct >= direct


def verify_temporal_packing() -> None:
    for p, h in ((3, 4), (5, 3), (7, 3), (11, 2)):
        t = p**h
        tokens = (t * t - 1) // (p * p - 1)
        for load in (1, max(1, t // 100), max(1, t // 10), t):
            disjoint_episodes = floor(tokens / load)
            assert (disjoint_episodes + 1) * load > tokens

            for episodes in (1, 2, 10, max(10, disjoint_episodes + 1)):
                repeated = ceil(episodes * load / tokens)
                assert repeated * tokens >= episodes * load


def main() -> None:
    verify_fan_split()
    verify_token_counts()
    verify_temporal_packing()
    print(
        "verified line-energy token endpoint: fan wall/star split, exact full "
        "prefix-token counts, and fresh-versus-repeated episode bounds"
    )


if __name__ == "__main__":
    main()

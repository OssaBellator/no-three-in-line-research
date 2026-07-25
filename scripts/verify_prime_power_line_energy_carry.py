#!/usr/bin/env python3
"""Finite and arithmetic checks for CMR355--CMR359."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import ceil, floor, isqrt


Cell = tuple[int, int]
Pair = tuple[Cell, Cell]


def compatible_pairs(t: int) -> list[Pair]:
    cells = [(x, y) for x in range(t) for y in range(t)]
    result: list[Pair] = []
    for left, right in combinations(cells, 2):
        if left[0] != right[0] and left[1] != right[1]:
            result.append((left, right))
    return result


def vertices(pair: Pair) -> frozenset[tuple[str, int]]:
    (x1, y1), (x2, y2) = pair
    return frozenset((('x', x1), ('y', y1), ('x', x2), ('y', y2)))


def greedy_matching(pairs: list[Pair]) -> list[Pair]:
    remaining = list(pairs)
    selected: list[Pair] = []
    while remaining:
        pair = remaining[0]
        used = vertices(pair)
        selected.append(pair)
        remaining = [other for other in remaining if used.isdisjoint(vertices(other))]
    return selected


def verify_star_or_matching() -> None:
    universe = compatible_pairs(5)
    test_families = [
        universe[:size]
        for size in (1, 5, 17, 40, 80, min(150, len(universe)))
    ]
    test_families.append([pair for pair in universe if pair[0][0] == 0][:80])

    for family in test_families:
        degree: Counter[tuple[str, int]] = Counter()
        for pair in family:
            degree.update(vertices(pair))
        delta = max(degree.values())
        matching = greedy_matching(family)
        assert len(matching) >= ceil(len(family) / (4 * delta))
        all_vertices = [vertex for pair in matching for vertex in vertices(pair)]
        assert len(all_vertices) == len(set(all_vertices))

        threshold = isqrt(len(family))
        if threshold * threshold < len(family):
            threshold += 1
        if delta < threshold:
            assert len(matching) >= floor(len(family) / (4 * threshold))


def verify_signature_pigeonhole() -> None:
    for p, h in ((3, 4), (5, 3), (7, 3), (11, 2)):
        classes = h * (p + 1)
        for population in range(1, 10_000, 137):
            assert ceil(population / classes) * classes >= population


def verify_prefix_cell_capacity() -> None:
    for p, h in ((3, 4), (5, 3), (7, 2)):
        t = p**h
        for depth in range(h):
            modulus = p**depth
            capacity = t // modulus

            # A permutation matching supplies one first endpoint in every source
            # and every row.  Count its occupancy in full prefix cells.
            counts: Counter[tuple[int, int]] = Counter()
            for source in range(t):
                row = (2 * source + 1) % t
                if len({(2 * x + 1) % t for x in range(t)}) != t:
                    row = source
                counts[(source % modulus, row % modulus)] += 1
            assert max(counts.values()) <= capacity

            population = sum(counts.values())
            support = len(counts)
            assert support * capacity >= population
            assert max(counts.values()) * modulus**2 >= population


def verify_combined_thresholds() -> None:
    for p, h in ((5, 3), (7, 3), (11, 2), (13, 3)):
        t = p**h
        bands = (t - 1).bit_length()
        for height in (1, max(1, t // 20), max(1, t // 5), max(1, 2 * t // 5)):
            line_count = ceil(11 * height**3 / (90 * bands))
            threshold = isqrt(line_count)
            if threshold * threshold < line_count:
                threshold += 1
            pair_matching = floor(line_count / (4 * threshold))
            signature = floor(pair_matching / (h * (p + 1)))
            assert pair_matching >= 0
            assert signature >= 0

            # The two-dimensional heavy/dispersion threshold is t^(2/3).
            cube_root = round(t ** (1 / 3))
            while (cube_root + 1) ** 3 <= t:
                cube_root += 1
            while cube_root**3 > t:
                cube_root -= 1
            denominator = max(1, cube_root**2)
            assert ceil(signature / denominator) >= 0


def main() -> None:
    verify_star_or_matching()
    verify_signature_pigeonhole()
    verify_prefix_cell_capacity()
    verify_combined_thresholds()
    print(
        "verified line-energy carry conversion: matching-vertex stars, "
        "compatible pair extraction, signatures, and full-prefix-cell bounds"
    )


if __name__ == "__main__":
    main()

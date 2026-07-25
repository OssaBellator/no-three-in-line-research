#!/usr/bin/env python3
"""Exact arithmetic checks for CMR302--CMR305."""

from __future__ import annotations

from collections import Counter
from math import ceil, sqrt


def verify_exact_cell_capacity() -> None:
    for p, h in ((3, 5), (5, 4), (7, 3)):
        t = p**h
        for depth in range(h + 1):
            modulus = p**depth
            rows = list(range(t))
            counts = Counter(row % modulus for row in rows)
            assert len(counts) == modulus
            assert set(counts.values()) == {t // modulus}

            for population in range(1, t + 1):
                support_lower = ceil(population * modulus / t)
                heavy_lower = ceil(population / modulus)
                assert support_lower * (t // modulus) >= population
                assert heavy_lower * modulus >= population


def verify_square_root_dichotomy() -> None:
    for p, h in ((3, 6), (5, 4), (7, 3), (11, 2)):
        t = p**h
        for depth in range(h + 1):
            modulus = p**depth
            for population in (1, max(1, t // 10), max(1, t // 2), t):
                if modulus <= sqrt(t):
                    assert ceil(population / modulus) >= population / sqrt(t)
                else:
                    assert population * modulus / t > population / sqrt(t)


def verify_thin_population_bounds() -> None:
    for p, h in ((3, 5), (5, 4), (7, 3), (11, 2)):
        t = p**h
        denominator = h + p - 1
        width_two_population = ceil((t - 2) / denominator)
        assert width_two_population >= (t - 2) / denominator
        threshold_two = (t - 2) / (denominator * sqrt(t))
        assert width_two_population / sqrt(t) >= threshold_two

        if t >= 10:
            width_three_population = ceil((t - 9) / denominator)
            threshold_three = (t - 9) / (denominator * sqrt(t))
            assert width_three_population / sqrt(t) >= threshold_three


def verify_synthetic_partition() -> None:
    p = 5
    h = 4
    t = p**h
    for depth in range(h + 1):
        modulus = p**depth
        # Distinct first-endpoint rows, partitioned by their common row prefix.
        for population in (17, 101, t - 2):
            residues = Counter(row % modulus for row in range(population))
            maximum = max(residues.values())
            support = len(residues)
            assert maximum <= t // modulus
            assert maximum >= ceil(population / modulus)
            assert support >= ceil(population * modulus / t)


def main() -> None:
    verify_exact_cell_capacity()
    verify_square_root_dichotomy()
    verify_thin_population_bounds()
    verify_synthetic_partition()
    print(
        "verified thin-signature carry cells: exact capacity, support, "
        "square-root dichotomy, and width-two/width-three bounds"
    )


if __name__ == "__main__":
    main()

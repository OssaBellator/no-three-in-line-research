#!/usr/bin/env python3
"""Finite checks for CMR227--CMR230.

The general proofs are order/Hall arguments.  This script exhausts small finite
coordinate sets for the affine-transversal lemma and verifies every arithmetic
case in the essential-edge contradiction.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


def affine_maps(source: tuple[int, ...], target: tuple[int, ...]):
    """Return affine maps carrying source bijectively onto target."""
    maps: set[tuple[Fraction, Fraction]] = set()
    x0, x1 = source[0], source[1]
    for y0 in target:
        for y1 in target:
            if y0 == y1:
                continue
            slope = Fraction(y1 - y0, x1 - x0)
            intercept = Fraction(y0) - slope * x0
            image = tuple(slope * x + intercept for x in source)
            if set(image) == set(target):
                maps.add((slope, intercept))
    return maps


def verify_affine_transversals() -> None:
    universe = range(8)
    for size in range(2, 6):
        subsets = list(combinations(universe, size))
        for source in subsets:
            for target in subsets:
                maps = affine_maps(source, target)
                assert len(maps) <= 2
                positive = [item for item in maps if item[0] > 0]
                negative = [item for item in maps if item[0] < 0]
                assert len(positive) <= 1
                assert len(negative) <= 1


def verify_hall_factor_arithmetic(max_h: int = 100_000) -> None:
    for h in range(4, max_h + 1):
        t = 2 * h + 1
        required_values = []
        for a in (h, h + 1, h + 2):
            c = t - a + 1
            required = a * c - 1 - min(a, c)
            required_values.append(required)
            assert required == h * (h + 1) - 1

            if a != h + 1:
                assert h * min(a, c) < required

        assert len(set(required_values)) == 1
        assert h - 1 >= 3

        # In the balanced middle case, h line matchings have total capacity
        # h(h+1).  Covering the required population leaves deficiency at most 1,
        # so at least h-1 lines must be full transversals.
        total_capacity = h * (h + 1)
        required = h * (h + 1) - 1
        assert total_capacity - required == 1
        assert h - 1 > 2


def verify_deletion_threshold(max_h: int = 100_000) -> None:
    for h in range(4, max_h + 1):
        t = 2 * h + 1
        for deleted_lines in range(h):
            minimum_degree = (t - 1) - deleted_lines
            assert minimum_degree >= h + 1
            assert 2 * minimum_degree >= t

        final_minimum_degree = (t - 1) - h
        assert final_minimum_degree == h


def main() -> None:
    verify_affine_transversals()
    verify_hall_factor_arithmetic()
    verify_deletion_threshold()
    print(
        "verified odd parent line resilience: at most two affine transversals, "
        "uniform Hall deficit h(h+1)-1, and half-line deletion thresholds"
    )


if __name__ == "__main__":
    main()

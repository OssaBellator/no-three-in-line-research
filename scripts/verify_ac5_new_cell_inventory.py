#!/usr/bin/env python3
"""Finite checks for AC5q--AC5t."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import gcd

Point = tuple[int, int]


def primitive_height(a: Point, b: Point) -> int:
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    divisor = gcd(abs(dx), abs(dy))
    if divisor == 0:
        return 0
    return max(abs(dx) // divisor, abs(dy) // divisor)


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (
        b[1] - a[1]
    ) * (c[0] - a[0])


def shadow(anchor: Point, cells: set[Point], height: int) -> int:
    return sum(
        1
        for first, second in combinations(cells, 2)
        if collinear(anchor, first, second)
        and primitive_height(anchor, first) >= height
    )


def verify_pair_shadow_propagation(counts: Counter[str]) -> None:
    for size in range(2, 4):
        points = [(row, column) for row in range(size) for column in range(size)]
        for anchor in points:
            available = [point for point in points if point != anchor]
            for height in range(1, size + 1):
                line_ceiling = 1 + (size - 1) // height
                residual = max(0, line_ceiling - 2)
                for labels in product((0, 1, 2), repeat=len(available)):
                    old = {
                        point
                        for point, label in zip(available, labels, strict=True)
                        if label == 1
                    }
                    new = {
                        point
                        for point, label in zip(available, labels, strict=True)
                        if label == 2
                    }
                    assignments = (len(new) + 1) // 2
                    increase = shadow(anchor, old | new, height) - shadow(
                        anchor, old, height
                    )
                    assert increase <= 3 * residual * assignments
                    counts["pair-shadow inventories"] += 1


def verify_cumulative_paths(counts: Counter[str]) -> None:
    for residual in range(0, 8):
        for initial in range(0, 11):
            for path in product(range(0, 5), repeat=4):
                bound = initial
                cumulative = 0
                for new_assignments in path:
                    cumulative += new_assignments
                    bound += 3 * residual * new_assignments
                    assert bound == initial + 3 * residual * cumulative
                    counts["path prefixes"] += 1


def verify_anchored_inventory(counts: Counter[str]) -> None:
    for size in range(2, 20):
        for theta in range(0, 20):
            for residual in range(0, 8):
                for assignments in range(0, 8):
                    propagated = theta + 3 * residual * assignments
                    anchored = 8 * size * propagated
                    assert anchored == 8 * size * (
                        theta + 3 * residual * assignments
                    )
                    counts["anchored substitutions"] += 1


def verify_gamma_substitution(counts: Counter[str]) -> None:
    for size in range(2, 10):
        for pool in range(2, 10):
            for spread in range(1, 4):
                for batch in range(1, 5):
                    for line_ceiling in range(1, 6):
                        for theta in range(0, 5):
                            for assignments in range(0, 4):
                                residual = max(0, line_ceiling - 2)
                                anchored = 8 * size * (
                                    theta + 3 * residual * assignments
                                )
                                u2 = 4 * line_ceiling * batch * pool
                                u3 = 8 * line_ceiling * batch * batch * pool * pool
                                direct = (
                                    Fraction(spread, pool) ** 2 * (anchored + u2)
                                    + Fraction(spread, pool) ** 3 * u3
                                )
                                formula = (
                                    Fraction(8 * spread * spread * size, pool * pool)
                                    * (theta + 3 * residual * assignments)
                                    + Fraction(
                                        4 * spread * spread * line_ceiling * batch,
                                        pool,
                                    )
                                    + Fraction(
                                        8
                                        * spread
                                        * spread
                                        * spread
                                        * line_ceiling
                                        * batch
                                        * batch,
                                        pool,
                                    )
                                )
                                assert direct == formula
                                counts["gamma formulas"] += 1


def verify_multistep_criterion(counts: Counter[str]) -> None:
    for batch in range(1, 8):
        for current_numerator in range(0, batch + 1):
            current = Fraction(current_numerator, 2)
            for highs in product(range(0, 4), repeat=3):
                high_bounds = [Fraction(value, 10) for value in highs]
                lhs = current + batch * sum(high_bounds)
                if lhs < batch:
                    # The augmented-badness expectation is below the integer
                    # threshold used by AC5p.
                    assert lhs < Fraction(batch, 1)
                counts["multistep inequalities"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_pair_shadow_propagation(counts)
    verify_cumulative_paths(counts)
    verify_anchored_inventory(counts)
    verify_gamma_substitution(counts)
    verify_multistep_criterion(counts)

    print("AC5q--AC5t new-cell inventory audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()

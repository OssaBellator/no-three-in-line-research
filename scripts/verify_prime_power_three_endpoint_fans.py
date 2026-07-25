#!/usr/bin/env python3
"""Exact checks for CMR257--CMR260."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


def verify_moment_obstruction(max_t: int = 20) -> None:
    for t in range(4, max_t + 1):
        values = range(t)
        for x1, x2, x3 in combinations(values, 3):
            lam = Fraction(x3 - x2, x3 - x1)
            for y1 in values:
                for y3 in values:
                    if y1 == y3:
                        continue
                    y2 = lam * y1 + (1 - lam) * y3
                    if y2.denominator != 1 or not 0 <= y2 < t:
                        continue
                    y2_int = int(y2)

                    for r1 in values:
                        if r1 == y1:
                            continue
                        for r3 in values:
                            if r3 == y3:
                                continue
                            r2 = lam * r1 + (1 - lam) * r3
                            if r2.denominator != 1 or not 0 <= r2 < t:
                                continue
                            r2_int = int(r2)
                            if r2_int == y2_int:
                                continue

                            convexity_gap = (
                                lam * (y1 * y1 + r1 * r1)
                                + (1 - lam) * (y3 * y3 + r3 * r3)
                                - (y2_int * y2_int + r2_int * r2_int)
                            )
                            assert convexity_gap > 0


def verify_sharp_parallel_examples(max_t: int = 100) -> None:
    for t in range(4, max_t + 1):
        target = {(0, 0), (1, 1), (2, 2)}
        lines = []
        for shift in range(1, t - 2):
            intersections = {
                (0, shift),
                (1, shift + 1),
                (2, shift + 2),
            }
            assert intersections.isdisjoint(target)
            lines.append(intersections)

        assert len(lines) == t - 3
        for slice_x, target_y in ((0, 0), (1, 1), (2, 2)):
            ordinates = {
                next(y for x, y in line if x == slice_x)
                for line in lines
            }
            assert len(ordinates) == t - 3
            assert target_y not in ordinates


def verify_union_arithmetic(max_t: int = 1000) -> None:
    for t in range(4, max_t + 1):
        universe = set(range(t))
        blockers = [universe - {omitted} for omitted in (0, 1, 2)]
        assert all(len(blocker) == t - 1 for blocker in blockers)
        assert len(set.intersection(*blockers)) == t - 3
        assert len(set.union(*blockers)) == t


def main() -> None:
    verify_moment_obstruction()
    verify_sharp_parallel_examples()
    verify_union_arithmetic()
    print(
        "verified three-endpoint fan obstruction: strict moment gap, "
        "sharp t-3 parallel families, and the t-line union threshold"
    )


if __name__ == "__main__":
    main()

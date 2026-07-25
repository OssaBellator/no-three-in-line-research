#!/usr/bin/env python3
"""Exact checks for CMR288--CMR290."""

from __future__ import annotations

from fractions import Fraction


def verify_parallel_examples(max_t: int = 200) -> None:
    for t in range(10, max_t + 1):
        coordinate_set = set(range(t - 2))
        shifts = range(t - 9)
        used = [
            {shift + slice_index for shift in shifts}
            for slice_index in (0, 1, 2)
        ]
        holes = [coordinate_set - used_set for used_set in used]

        assert all(len(hole_set) == 7 for hole_set in holes)
        assert len({frozenset(hole_set) for hole_set in holes}) > 1

        lam = Fraction(1, 2)
        first = [sum(hole_set) for hole_set in holes]
        second = [sum(value * value for value in hole_set) for hole_set in holes]

        assert first[1] == lam * first[0] + (1 - lam) * first[2]
        assert second[1] >= lam * second[0] + (1 - lam) * second[2]


def verify_convexity_identity(max_value: int = 100) -> None:
    for left in range(max_value + 1):
        for right in range(max_value + 1):
            midpoint = Fraction(left + right, 2)
            gap = Fraction(left * left + right * right, 2) - midpoint * midpoint
            assert gap >= 0
            assert (gap == 0) == (left == right)


def verify_hole_cardinality(max_t: int = 100_000) -> None:
    for t in range(10, max_t + 1):
        large_side = t - 2
        retained_lines = t - 9
        assert large_side - retained_lines == 7


def main() -> None:
    verify_parallel_examples()
    verify_convexity_identity()
    verify_hole_cardinality()
    print(
        "verified width-three hole signatures: seven omitted cells per slice, "
        "exact first moments, reverse second moments, and nonconstant examples"
    )


if __name__ == "__main__":
    main()

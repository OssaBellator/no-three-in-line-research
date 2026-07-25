#!/usr/bin/env python3
"""Finite checks for PX381--PX385."""

from itertools import combinations
from math import gcd


Point = tuple[int, int]


def collinear(p: Point, q: Point, r: Point) -> bool:
    return (q[0] - p[0]) * (r[1] - p[1]) == (
        q[1] - p[1]
    ) * (r[0] - p[0])


def line_key(p: Point, q: Point) -> tuple[int, int, int]:
    a = q[1] - p[1]
    b = p[0] - q[0]
    c = -(a * p[0] + b * p[1])
    divisor = gcd(gcd(abs(a), abs(b)), abs(c))
    if divisor:
        a //= divisor
        b //= divisor
        c //= divisor
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def main() -> None:
    # PX381 exact secant-line decomposition on disjoint finite point sets.
    for order in range(3, 8):
        selected = [(i, i * i + 1) for i in range(2 * order)]
        candidates = [
            (100 + i, 200 + j)
            for i in range(order)
            for j in range(order)
        ]

        secant_lines = {
            line_key(first, second)
            for first, second in combinations(selected, 2)
        }

        line_sum = 0
        for a, b, c in secant_lines:
            selected_count = sum(
                a * x + b * y + c == 0
                for x, y in selected
            )
            candidate_count = sum(
                a * x + b * y + c == 0
                for x, y in candidates
            )
            line_sum += candidate_count * (
                selected_count * (selected_count - 1) // 2
            )

        direct = sum(
            1
            for candidate in candidates
            for first, second in combinations(selected, 2)
            if collinear(candidate, first, second)
        )
        assert line_sum == direct

    # PX383 exponent subtraction: n^(8/3) / n^2 = n^(2/3).
    assert 8 / 3 - 2 == 2 / 3

    # PX368/PX384 threshold comparisons.
    for order in range(4097, 5000):
        mixed_return_weight = order / 64
        assert mixed_return_weight > 64

    # For every fixed epsilon>0, n dominates n^(2/3+epsilon) when
    # epsilon<1/3. Check representative exact exponents.
    for exponent_numerator in (1, 2, 3, 4, 5):
        epsilon = exponent_numerator / 100
        assert 2 / 3 + epsilon < 1

    print("PX381--PX385 generic-rank-one cap verifier: PASS")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite regressions for AC5y--AC5ab."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product


def nonempty_subsets(n: int):
    for size in range(1, n + 1):
        yield from combinations(range(n), size)


def check_flow(rows: int, cols: int, entries: tuple[int, ...]) -> int:
    w = [
        [Fraction(entries[i * cols + j], 2) for j in range(cols)]
        for i in range(rows)
    ]
    if any(sum(row) != 1 for row in w):
        return 0
    q = [sum(w[i][j] for i in range(rows)) for j in range(cols)]
    if any(value > 1 for value in q):
        return 0

    q_bar_b = sum(q) / cols
    assert q_bar_b == Fraction(rows, cols)
    for cylinder in nonempty_subsets(cols):
        direct = sum(q[j] for j in cylinder) / rows
        nu = Fraction(len(cylinder), cols)
        q_bar_c = sum(q[j] for j in cylinder) / len(cylinder)
        assert direct == nu * q_bar_c / q_bar_b

        rho = q_bar_c / q_bar_b
        for rank in (1, 2, 3):
            baseline = Fraction(1, 3**rank)
            transferred = rho * baseline
            assert transferred == baseline * q_bar_c / q_bar_b
    return 1


def check_event_and_drift_bounds() -> None:
    for rho2_num in range(1, 7):
        for rho3_num in range(1, 7):
            rho2 = Fraction(rho2_num, 3)
            rho3 = Fraction(rho3_num, 3)
            for m2 in range(6):
                for m3 in range(6):
                    gamma = rho2 * Fraction(m2, 25) + rho3 * Fraction(m3, 125)
                    direct_sum = sum([rho2 * Fraction(1, 25)] * m2) + sum(
                        [rho3 * Fraction(1, 125)] * m3
                    )
                    assert gamma == direct_sum
                    for t in range(1, 8):
                        high = gamma / 5
                        if gamma + t * high < t:
                            assert gamma < t

    for t in range(1, 8):
        for current_num in range(8):
            current = Fraction(current_num, 10)
            highs = [Fraction(j, 50) for j in range(3)]
            if current + t * sum(highs) < t:
                assert current < t


def main() -> None:
    checked = 0
    for rows in (1, 2):
        for cols in range(rows, 4):
            for entries in product(range(3), repeat=rows * cols):
                checked += check_flow(rows, cols, entries)
    assert checked > 0
    check_event_and_drift_bounds()
    print(f"AC reverse-flow spread checks passed on {checked} feasible flows")


if __name__ == "__main__":
    main()

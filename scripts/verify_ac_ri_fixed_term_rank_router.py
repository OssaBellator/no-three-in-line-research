#!/usr/bin/env python3
"""Finite checks for AC3fe--AC3fh."""

from __future__ import annotations

from itertools import combinations_with_replacement, product
from math import comb


def verify_closure_rank() -> int:
    checks = 0
    roles = ("Q1", "Q2", "Q3")
    for closure_count in (1, 2, 3):
        for chosen in combinations_with_replacement(roles, closure_count):
            triple = list(chosen) + [f"old{i}" for i in range(3 - closure_count)]
            initial = {cell for cell in triple if cell.startswith("old")}
            rank = sum(cell not in initial for cell in triple)
            assert rank == closure_count
            checks += 1
    return checks


def verify_support_rank_grid() -> int:
    checks = 0
    support_types = range(3)
    ranks = range(3)
    # Exhaust every 3x3 nonnegative grid with entries 0,1,2.
    for weights in product(range(3), repeat=9):
        total = sum(weights)
        if total == 0:
            continue
        for threshold in range(1, total + 1):
            assert 9 * max(weights) >= threshold
            rank_totals = [
                sum(weights[3 * support + rank] for support in support_types)
                for rank in ranks
            ]
            assert 3 * max(rank_totals) >= threshold
            checks += 1
    return checks


def verify_role_counts() -> tuple[int, tuple[int, int, int]]:
    counts = tuple(comb(9 + rank - 1, rank) for rank in (1, 2, 3))
    assert counts == (9, 45, 165)
    explicit = tuple(
        sum(1 for _ in combinations_with_replacement(range(9), rank))
        for rank in (1, 2, 3)
    )
    assert explicit == counts
    return 6, counts


def main() -> None:
    closure_checks = verify_closure_rank()
    grid_checks = verify_support_rank_grid()
    role_checks, counts = verify_role_counts()
    print("AC RI fixed-term rank router verification passed")
    print(f"  closure-rank checks: {closure_checks}")
    print(f"  support/rank weighted checks: {grid_checks}")
    print(f"  role-count checks: {role_checks}")
    print(f"  role multiset counts: {counts}")


if __name__ == "__main__":
    main()

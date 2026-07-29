#!/usr/bin/env python3
"""Finite checks for SRR2s--SRR2u.

The exhaustive range is intentionally small. The proof in the Markdown note
is the arbitrary-size argument.
"""

from __future__ import annotations

from itertools import combinations, permutations, product


def row_masks(n: int, delta: int):
    full = (1 << n) - 1
    for holes_count in range(delta + 1):
        for holes in combinations(range(n), holes_count):
            mask = full
            for b in holes:
                mask &= ~(1 << b)
            yield mask


def saturating_matchings(rows: tuple[int, ...], n: int):
    m = len(rows)
    for chosen in permutations(range(n), m):
        if all(rows[a] & (1 << chosen[a]) for a in range(m)):
            yield chosen


def hall_feasible(rows: tuple[int, ...], n: int) -> bool:
    return next(saturating_matchings(rows, n), None) is not None


def max_rank_into(rows: tuple[int, ...], subset_mask: int) -> int:
    m = len(rows)
    endpoints = [b for b in range(subset_mask.bit_length()) if subset_mask & (1 << b)]
    best = 0
    for r in range(1, m + 1):
        for left in combinations(range(m), r):
            for right in permutations(range(len(endpoints)), r):
                if all(rows[a] & (1 << endpoints[right[j]]) for j, a in enumerate(left)):
                    best = max(best, r)
                    break
            if best == r:
                break
    return best


def matching_cost(matching: tuple[int, ...], costs: tuple[int, ...]) -> int:
    return sum(costs[b] for b in matching)


def check_instance(rows: tuple[int, ...], n: int, delta: int) -> None:
    m = len(rows)
    assert all(n - row.bit_count() <= delta for row in rows)
    matchings = list(saturating_matchings(rows, n))
    if not matchings:
        return

    for subset in range(1 << n):
        rank = max_rank_into(rows, subset)
        lower = min(m, max(0, subset.bit_count() - delta))
        assert rank >= lower, (rows, subset, rank, lower)

    if n < m + delta:
        return
    for costs in product(range(3), repeat=n):
        optimum = min(matching_cost(M, costs) for M in matchings)
        ordered = sorted(costs)
        bound = sum(ordered[i + delta] for i in range(m))
        assert optimum <= bound, (rows, costs, optimum, bound)


def main() -> None:
    checked_graphs = 0
    for m in range(1, 4):
        for n in range(m, 5):
            for delta in range(0, min(2, n) + 1):
                masks = tuple(row_masks(n, delta))
                for rows in product(masks, repeat=m):
                    if not hall_feasible(rows, n):
                        continue
                    check_instance(rows, n, delta)
                    checked_graphs += 1
    print(f"verified SRR bounded-hole flow on {checked_graphs} Hall-feasible graphs")


if __name__ == "__main__":
    main()

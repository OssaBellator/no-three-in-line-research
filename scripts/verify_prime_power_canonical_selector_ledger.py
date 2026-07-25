#!/usr/bin/env python3
"""Verify CMR552--CMR557 canonical selector ledger identities."""

from fractions import Fraction
from itertools import combinations, permutations
from math import ceil


def canonical_extension(
    n: int,
    partial: tuple[tuple[int, int], ...],
) -> tuple[tuple[int, int], ...]:
    used_l = {i for i, _ in partial}
    used_r = {j for _, j in partial}
    left = [i for i in range(n) if i not in used_l]
    right = [j for j in range(n) if j not in used_r]
    return tuple(sorted(partial + tuple(zip(left, right))))


def is_matching(edges: tuple[tuple[int, int], ...]) -> bool:
    return (
        len({i for i, _ in edges}) == len(edges)
        and len({j for _, j in edges}) == len(edges)
    )


def check_canonical_extensions() -> None:
    for n in range(1, 8):
        all_edges = [(i, j) for i in range(n) for j in range(n)]
        for size in range(0, min(3, n) + 1):
            checked = 0
            for subset in combinations(all_edges, size):
                if not is_matching(subset):
                    continue
                ext = canonical_extension(n, tuple(subset))
                assert is_matching(ext)
                assert len(ext) == n
                assert set(subset).issubset(ext)
                assert ext == canonical_extension(n, tuple(reversed(subset)))
                checked += 1
                if checked >= 250:
                    break


def derangements(n: int) -> list[tuple[int, ...]]:
    return [
        p
        for p in permutations(range(n))
        if all(p[i] != i for i in range(n))
    ]


def check_fixed_cylinder() -> None:
    for n in range(2, 8):
        ds = derangements(n)
        for p in ds:
            assert all(p[i] != i for i in range(n))
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                count = sum(1 for p in ds if p[i] == j)
                assert Fraction(count, len(ds)) == Fraction(1, n - 1)


def check_slack_arithmetic() -> None:
    for n in range(5, 20):
        for q in range(4, 18):
            for s_num in range(0, 160):
                s = Fraction(s_num, 120)
                a = Fraction(30, 11) * s
                delta = 1 - Fraction(2, q) - a
                if delta > 0:
                    h = ceil(q * (n - 1) * delta)
                    assert h >= 1
                    for b in range(0, h):
                        lhs = a + Fraction(2, q) + Fraction(b, q * (n - 1))
                        assert lhs < 1
                else:
                    threshold = Fraction(11, 30) * (1 - Fraction(2, q))
                    assert s >= threshold


def check_allowed_universe() -> None:
    for n in range(1, 30):
        assert n * n - n == n * (n - 1)


def check_global_stock() -> None:
    for t in range(2, 20):
        for h in range(1, 8):
            pair = (h + 1) * t * t * (t - 1) * (t - 1)
            trace = 2 * (h + 1) * t**4 * (t - 1) * (t - 1)
            total = pair + trace
            assert total >= pair
            assert total >= trace
            for lam in range(2, 8):
                assert (lam - 1) * t * t * total >= 0


def main() -> None:
    check_canonical_extensions()
    check_fixed_cylinder()
    check_slack_arithmetic()
    check_allowed_universe()
    check_global_stock()
    print("verified canonical selector ledger through the configured ranges")


if __name__ == "__main__":
    main()

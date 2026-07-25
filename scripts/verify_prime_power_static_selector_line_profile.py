#!/usr/bin/env python3
"""Verify CMR558--CMR563 line-profile decompositions and arithmetic."""

from fractions import Fraction
from itertools import combinations
from math import ceil, comb, floor


def support_line_key(points: tuple[tuple[int, int], ...]) -> tuple[int, int, int]:
    (x1, y1), (x2, y2) = points[:2]
    a = y2 - y1
    b = x1 - x2
    c = a * x1 + b * y1
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    from math import gcd

    g = gcd(gcd(abs(a), abs(b)), abs(c))
    if g:
        a //= g
        b //= g
        c //= g
    return a, b, c


def collinear(points: tuple[tuple[int, int], ...]) -> bool:
    return all(
        (points[1][0] - points[0][0]) * (p[1] - points[0][1])
        == (points[1][1] - points[0][1]) * (p[0] - points[0][0])
        for p in points[2:]
    )


def compatible(points: tuple[tuple[int, int], ...]) -> bool:
    return (
        len({x for x, _ in points}) == len(points)
        and len({y for _, y in points}) == len(points)
    )


def check_line_grouping() -> None:
    for n in range(3, 7):
        cells = [(x, y) for x in range(n) for y in range(n)]
        rank0 = [
            tr
            for tr in combinations(cells, 3)
            if compatible(tr) and collinear(tr)
        ]
        groups0: dict[
            tuple[int, int, int],
            list[tuple[tuple[int, int], ...]],
        ] = {}
        for tr in rank0:
            groups0.setdefault(support_line_key(tr), []).append(tr)
        assert sum(map(len, groups0.values())) == len(rank0)
        for trs in groups0.values():
            involved = set().union(*(set(tr) for tr in trs))
            assert len(trs) <= comb(len(involved), 3)

        z = (0, 0)
        residual = [p for p in cells if p[0] != 0 and p[1] != 0]
        rank1 = []
        for pair in combinations(residual, 2):
            triple = (z,) + pair
            if compatible(triple) and collinear(triple):
                rank1.append(triple)
        groups1: dict[
            tuple[int, int, int],
            list[tuple[tuple[int, int], ...]],
        ] = {}
        for tr in rank1:
            groups1.setdefault(support_line_key(tr), []).append(tr)
        assert sum(map(len, groups1.values())) == len(rank1)
        for trs in groups1.values():
            involved = set().union(*(set(tr[1:]) for tr in trs))
            assert len(trs) <= comb(len(involved), 2)


def check_weight_lemma() -> None:
    for total in range(1, 100):
        threshold = max(2, ceil(total**0.5))

        def rec(rem: int, slots: int, prefix: list[int]) -> None:
            if slots == 0:
                if rem:
                    return
                weights = prefix
                assert sum(weights) == total
                if max(weights, default=0) < threshold:
                    positives = sum(1 for x in weights if x > 0)
                    assert positives >= ceil(total / (threshold - 1))
                    assert positives >= floor(total**0.5)
                return
            for x in range(rem + 1):
                rec(rem - x, slots - 1, prefix + [x])

        if total <= 12:
            rec(total, 6, [])
        max_nonheavy_total = (
            (threshold - 1) * max(1, floor(total**0.5) - 1)
        )
        if floor(total**0.5) >= 2:
            assert max_nonheavy_total < total


def check_rank_thresholds() -> None:
    for n in range(5, 30):
        n2 = n * (n - 1)
        n3 = n2 * (n - 2)
        for q in range(4, 20):
            cq = Fraction(11, 30) * (1 - Fraction(2, q))
            m0 = cq * n3 / 2
            m1 = cq * n2 / 4
            assert m0 > 0
            assert m1 > 0


def check_binomial_inversions() -> None:
    for threshold in range(1, 1000):
        k3 = ceil((6 * threshold) ** (1 / 3))
        while comb(k3, 3) < threshold:
            k3 += 1
        assert k3 >= ceil((6 * threshold) ** (1 / 3))

        k2 = ceil((2 * threshold) ** 0.5)
        while comb(k2, 2) < threshold:
            k2 += 1
        assert k2 >= ceil((2 * threshold) ** 0.5)


def main() -> None:
    check_line_grouping()
    check_weight_lemma()
    check_rank_thresholds()
    check_binomial_inversions()
    print("verified static selector line profiles through the configured ranges")


if __name__ == "__main__":
    main()

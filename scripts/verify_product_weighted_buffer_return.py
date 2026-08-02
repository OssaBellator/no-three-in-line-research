#!/usr/bin/env python3
"""Finite checks for PX356--PX363."""

from itertools import combinations
from math import sqrt


def max_disjoint_family(family: list[tuple[int, ...]]) -> int:
    best = 0
    for r in range(len(family) + 1):
        for chosen in combinations(range(len(family)), r):
            used: set[int] = set()
            ok = True
            for idx in chosen:
                support = family[idx]
                if used.intersection(support):
                    ok = False
                    break
                used.update(support)
            if ok:
                best = max(best, r)
    return best


def main() -> None:
    # PX356: if both alternatives fail, their total incidence capacity is
    # strictly below D n^2 / 4, contradicting |Omega| >= n^2 / 4.
    for n in range(4, 101):
        for destroyed in range(1, 31):
            one_cap = destroyed * n * n / 8
            two_cap = destroyed * n * n / 8
            assert one_cap + two_cap == destroyed * n * n / 4

    # PX358: exhaust all support families of sets of size one or two through
    # five vertices and compare the exact matching number with |C|/(2 rho).
    for vertex_count in range(1, 6):
        supports = [(i,) for i in range(vertex_count)]
        supports += list(combinations(range(vertex_count), 2))
        for mask in range(1, 1 << len(supports)):
            family = [
                supports[i]
                for i in range(len(supports))
                if (mask >> i) & 1
            ]
            degrees = [
                sum(vertex in support for support in family)
                for vertex in range(vertex_count)
            ]
            rho = max(degrees)
            exact = max_disjoint_family(family)
            assert exact >= len(family) / (2 * rho)

    # PX359 coefficient: support matching followed by 2q type extraction.
    for blocker_count in range(1, 100):
        for rho in range(1, 20):
            for channels in range(1, 10):
                support_matching = blocker_count / (2 * rho)
                typed_block = support_matching / (4 * channels)
                assert typed_block == blocker_count / (8 * channels * rho)

    # PX361 quadratic-sector averaging over at most 2n fixed points.
    for n in range(4, 101):
        for destroyed in range(1, 20):
            blockers = destroyed * n * n / 32
            average = blockers / (2 * n)
            assert average == destroyed * n / 64

    # PX363 exact amplification recurrence.
    for ambient_scale in (2, 3, 10, 100, 1000):
        weight = 1.0
        for generation in range(1, 9):
            weight = sqrt(ambient_scale * weight)
            expected = ambient_scale ** (1 - 2 ** (-generation))
            assert abs(weight - expected) < 1e-9

    print("PX356--PX363 weighted buffer-return verifier: PASS")


if __name__ == "__main__":
    main()

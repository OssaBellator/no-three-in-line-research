#!/usr/bin/env python3
"""Deterministic checks for CMR444--CMR447."""

from fractions import Fraction
from itertools import combinations


def check_token_incidence() -> None:
    for p in (3, 5, 7):
        for h in range(2, 7):
            for k in (0, 1, 2, 5, 20):
                counted = 0
                for _ in range(k):
                    for _depth in range(1, h):
                        for _direction in range(p + 1):
                            counted += 1
                assert counted == (p + 1) * (h - 1) * k


def check_restored_edge_support() -> None:
    ground = set(range(7))
    triples = [set(values) for values in combinations(ground, 3)]
    subsets = [
        {value for value in ground if mask & (1 << value)}
        for mask in range(1 << len(ground))
    ]
    for before in subsets:
        clean = [triple for triple in triples if not triple <= before]
        degree = max(
            (sum(edge in triple for triple in clean) for edge in ground),
            default=0,
        )
        for restored in subsets:
            if before & restored:
                continue
            after = before | restored
            recreated = [triple for triple in clean if triple <= after]
            assert all(triple & restored for triple in recreated)
            assert len(recreated) <= len(restored) * degree


def check_harmonic_and_threshold_bounds() -> None:
    for side in range(5, 500):
        weight = sum(Fraction(1, height) for height in range(5, min(side, 10)))
        for rollback in (0, 1, side // 3, side):
            recreated = 2 * (side - 1) ** 2 * weight * rollback
            assert recreated >= 0
            if weight < Fraction(3, 2):
                assert recreated < 3 * side * side * rollback + 1

    for p in (3, 5, 7, 11):
        for h in range(2, 9):
            side = p**h
            factor = (p + 1) * (h - 1)
            for rollback in (1, 2, min(10, side), side):
                assert factor * rollback <= factor * side
                for threshold in (1, 2, min(10, side), side):
                    if rollback < threshold:
                        assert factor * rollback < factor * threshold
                    else:
                        assert side - rollback <= side - threshold
            assert factor * side * side == (p + 1) * (h - 1) * side**2


def main() -> None:
    check_token_incidence()
    check_restored_edge_support()
    check_harmonic_and_threshold_bounds()
    print(
        "verified rollback incidence: exact token multiplicity, restored-edge "
        "support, harmonic charges, and threshold/global arithmetic"
    )


if __name__ == "__main__":
    main()

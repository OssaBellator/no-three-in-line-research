#!/usr/bin/env python3
"""Finite checks for AC5au--AC5ax imports."""

from itertools import permutations, product
from fractions import Fraction


def swap(p, i, j):
    q = list(p)
    q[i], q[j] = q[j], q[i]
    return tuple(q)


def verify_ri():
    checked = 0
    for m in range(2, 6):
        for h in range(1, 5):
            states = [
                (sigma, shifts)
                for sigma in permutations(range(m))
                for shifts in product(range(h), repeat=m)
            ]
            count = sum(
                sigma[0] == 0
                and sigma[1] == 1
                and shifts[0] == 0
                and shifts[1] == 0
                for sigma, shifts in states
            )
            assert Fraction(count, len(states)) == Fraction(1, m * (m - 1) * h * h)
            checked += 1
    return checked


def verify_overlap():
    checked = 0
    for n in range(3, 7):
        for p in permutations(range(n)):
            for i, j, k in permutations(range(n), 3):
                q = swap(swap(p, i, j), j, k)
                assert (q[i], q[j], q[k]) == (p[j], p[k], p[i])
                checked += 1
    return checked


def verify_quantile_order():
    checked = 0
    for length in range(3, 9):
        for k in range(0, min(3, length - 1)):
            for costs in product(range(4), repeat=length):
                ordered = sorted(costs)
                for deleted_mask in range(1 << length):
                    if deleted_mask.bit_count() != k:
                        continue
                    survivors = sorted(costs[i] for i in range(length) if not (deleted_mask >> i) & 1)
                    for j, value in enumerate(survivors):
                        assert value <= ordered[j + k]
                        checked += 1
    return checked


def main():
    print(
        "verified",
        verify_ri(),
        "RI cylinders,",
        verify_overlap(),
        "overlap words, and",
        verify_quantile_order(),
        "conditioned quantile positions",
    )


if __name__ == "__main__":
    main()

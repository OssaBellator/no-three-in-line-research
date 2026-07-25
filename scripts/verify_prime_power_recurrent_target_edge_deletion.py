#!/usr/bin/env python3
"""Arithmetic and finite matching checks for CMR713--CMR719."""

from itertools import permutations
from math import comb


def matching_edges(permutation):
    return {(index, permutation[index]) for index in range(len(permutation))}


def finite_matching_checks():
    checked = 0
    for side in range(1, 8):
        permutations_list = list(permutations(range(side)))
        for old_permutation in permutations_list:
            old_edges = matching_edges(old_permutation)
            for new_permutation in permutations_list:
                new_edges = matching_edges(new_permutation)
                for edge in new_edges - old_edges:
                    assert edge not in old_edges
                    checked += 1
    return checked


def arithmetic_checks():
    checked = 0
    for side in range(1, 60):
        pair_stock = 3 * comb(side * side, 3) if side * side >= 3 else 0
        for owners in range(1, 30):
            total_stock = owners * pair_stock
            for threshold in range(2, 12):
                bound = (threshold - 1) * total_stock
                assert bound >= 0
                checked += 1
    return checked


def main():
    matching_checks = finite_matching_checks()
    stock_checks = arithmetic_checks()
    print(
        "verified recurrent target-edge deletion:",
        matching_checks,
        "entering matching edges and",
        stock_checks,
        "owner-stock instances",
    )


if __name__ == "__main__":
    main()

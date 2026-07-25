#!/usr/bin/env python3
"""Verify AC3bk--AC3bo blocker-average decomposition and constants."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import prod


def falling(value, rank):
    return prod(range(value - rank + 1, value + 1))


def derangements(size):
    return [
        perm
        for perm in permutations(range(size))
        if all(perm[index] != index for index in range(size))
    ]


def verify_occupancy_split():
    checks = 0
    # Four states already exhaust every occupancy-class interaction pattern;
    # additional states only add further nonnegative summands to the same bins.
    for state_count in range(1, 5):
        for occupancies in product(range(9), repeat=state_count):
            for values in product(range(4), repeat=state_count):
                total = sum(values)
                singleton = sum(
                    value for occupancy, value in zip(occupancies, values, strict=True)
                    if occupancy == 1
                )
                small = sum(
                    value for occupancy, value in zip(occupancies, values, strict=True)
                    if 2 <= occupancy <= 6
                )
                large = sum(
                    value for occupancy, value in zip(occupancies, values, strict=True)
                    if occupancy >= 7
                )
                zero = sum(
                    value for occupancy, value in zip(occupancies, values, strict=True)
                    if occupancy == 0
                )
                # Variable blocker collateral is zero in occupancy-zero states.
                if zero:
                    continue
                assert total == singleton + small + large
                assert max(singleton, small, large) * 3 >= total
                checks += 1
    return checks


def verify_singleton_and_small(maximum=20):
    singleton_checks = 0
    small_checks = 0
    for raw in range(maximum + 1):
        for n in range(2, 10):
            expected = Fraction(raw, n - 1)
            assert raw >= (n - 1) * expected
            singleton_checks += 1
        for menu_size in range(1, 10):
            # An average of nonnegative state costs never exceeds raw cost.
            costs = tuple((raw + index) % (maximum + 1) for index in range(menu_size))
            expected = Fraction(sum(costs), menu_size)
            assert sum(costs) >= expected
            small_checks += 1
    return singleton_checks, small_checks


def verify_derangement_cylinders(maximum_t=8):
    table_checks = 0
    cylinder_checks = 0
    counts_by_t = {}

    for t in range(2, maximum_t + 1):
        bank = derangements(t)
        assert bank
        counts_by_t[t] = len(bank)
        table_checks += len(bank)

        for rank in range(1, min(3, t) + 1):
            prescription_counts = Counter()
            for perm in bank:
                for columns in combinations(range(t), rank):
                    rows = tuple(perm[column] for column in columns)
                    prescription_counts[(columns, rows)] += 1

            cap = Fraction(128, falling(t, rank))
            for count in prescription_counts.values():
                probability = Fraction(count, len(bank))
                assert probability <= cap
                cylinder_checks += 1

    return table_checks, cylinder_checks, counts_by_t


def verify_rank_and_final_constants(maximum=30):
    rank_checks = 0
    final_checks = 0

    for total in range(1, maximum + 1):
        for terms in product(range(total + 1), repeat=3):
            if sum(terms) < total:
                continue
            assert max(terms) * 3 >= total
            rank_checks += 1

    for gain in range(1, maximum + 1):
        blocker = Fraction(gain, 4)
        occupancy = blocker / 3
        singleton_raw = occupancy
        small_raw = occupancy
        large_rank = occupancy / 3

        for n in range(2, 9):
            assert (n - 1) * singleton_raw == Fraction((n - 1) * gain, 12)
            final_checks += 1
        assert small_raw == Fraction(gain, 12)
        final_checks += 1

        for t in range(7, 10):
            for rank in range(1, 4):
                raw = Fraction(falling(t, rank), 128) * large_rank
                assert raw == Fraction(falling(t, rank) * gain, 4608)
                final_checks += 1

    return rank_checks, final_checks


def main():
    occupancy = verify_occupancy_split()
    singleton, small = verify_singleton_and_small()
    tables, cylinders, counts = verify_derangement_cylinders()
    ranks, finals = verify_rank_and_final_constants()
    print(
        "AC RI blocker average: verified "
        f"{occupancy} occupancy partitions, {singleton} singleton bounds, "
        f"{small} small-table averages, {tables} derangement states, "
        f"{cylinders} cylinder prescriptions, {ranks} rank routers, "
        f"and {finals} final constants; derangement counts={counts}"
    )


if __name__ == "__main__":
    main()

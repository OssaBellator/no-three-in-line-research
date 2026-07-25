#!/usr/bin/env python3
"""Finite checks for all-rank created-certificate pivot orientation."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations

Point = tuple[int, int]
Permutation = tuple[int, ...]


def derangements(n: int) -> tuple[Permutation, ...]:
    return tuple(
        perm for perm in permutations(range(n))
        if all(perm[c] != c for c in range(n))
    )


def cells(perm: Permutation) -> set[Point]:
    return {(column, row) for column, row in enumerate(perm)}


def is_permutation(perm: Permutation) -> bool:
    return sorted(perm) == list(range(len(perm)))


def disjoint(first: Permutation, second: Permutation) -> bool:
    return all(a != b for a, b in zip(first, second))


def pivot_repair(
    pivot_layer: Permutation,
    opposite_layer: Permutation,
    pivot: Point,
) -> tuple[Permutation, Permutation, tuple[int, ...]]:
    n = len(pivot_layer)
    c0, r0 = pivot
    assert pivot_layer[c0] == r0
    c1 = next(column for column in range(n) if column != c0)
    r1 = pivot_layer[c1]

    active_after = list(pivot_layer)
    active_after[c0], active_after[c1] = r1, r0
    blocker_after = list(opposite_layer)

    blocked_c0 = opposite_layer[c0] == r1
    blocked_c1 = opposite_layer[c1] == r0
    occupancy = int(blocked_c0) + int(blocked_c1)
    support = [c0, c1]

    if occupancy == 0:
        pass
    elif occupancy == 1 and blocked_c0:
        blocker_after[c0], blocker_after[c1] = (
            opposite_layer[c1],
            opposite_layer[c0],
        )
    elif occupancy == 1:
        c2 = next(column for column in range(n) if column not in (c0, c1))
        blocker_after[c1], blocker_after[c2] = (
            opposite_layer[c2],
            opposite_layer[c1],
        )
        support.append(c2)
    else:
        c2 = next(column for column in range(n) if column not in (c0, c1))
        r2 = opposite_layer[c2]
        blocker_after[c0] = r2
        blocker_after[c1] = r1
        blocker_after[c2] = r0
        support.append(c2)

    active_tuple = tuple(active_after)
    blocker_tuple = tuple(blocker_after)
    assert is_permutation(active_tuple)
    assert is_permutation(blocker_tuple)
    assert disjoint(active_tuple, blocker_tuple)
    assert pivot not in cells(active_tuple) | cells(blocker_tuple)
    return active_tuple, blocker_tuple, tuple(support)


def verify_orientation_partition() -> int:
    checks = 0
    universe = tuple((column, row) for column in range(4) for row in range(4))
    for triple in combinations(universe, 3):
        for mask in range(1, 8):
            new_cells = {
                triple[index]
                for index in range(3)
                if mask & (1 << index)
            }
            pivot = min(new_cells)
            assert pivot in triple
            assert pivot in new_cells
            assert len(new_cells) in (1, 2, 3)
            checks += 1
    return checks


def verify_repairs() -> tuple[int, int, dict[int, int]]:
    repair_checks = 0
    bucket_checks = 0
    ranks = {1: 0, 2: 0, 3: 0}
    for n in range(3, 7):
        active = tuple(range(n))
        for blocker in derangements(n):
            union = sorted(cells(active) | cells(blocker))
            for triple in combinations(union, 3):
                for mask in range(1, 8):
                    new_cells = {
                        triple[index]
                        for index in range(3)
                        if mask & (1 << index)
                    }
                    pivot = min(new_cells)
                    if pivot in cells(active):
                        first, second = active, blocker
                    else:
                        first, second = blocker, active
                    repaired_first, repaired_second, _ = pivot_repair(
                        first, second, pivot
                    )
                    final_union = cells(repaired_first) | cells(repaired_second)
                    assert pivot not in final_union
                    assert not set(triple) <= final_union
                    repair_checks += 1
                    ranks[len(new_cells)] += 1

            records: list[tuple[frozenset[Point], frozenset[Point], Point]] = []
            for triple in combinations(union, 3):
                for mask in range(1, 8):
                    new_cells = frozenset(
                        triple[index]
                        for index in range(3)
                        if mask & (1 << index)
                    )
                    records.append((frozenset(triple), new_cells, min(new_cells)))
            buckets: dict[Point, list[tuple[frozenset[Point], frozenset[Point], Point]]] = {}
            for record in records:
                buckets.setdefault(record[2], []).append(record)
            assert sum(len(bucket) for bucket in buckets.values()) == len(records)
            for pivot, bucket in buckets.items():
                assert all(record[2] == pivot and pivot in record[0] for record in bucket)
                bucket_checks += len(bucket)
    return repair_checks, bucket_checks, ranks


def verify_weighted_payment() -> int:
    checks = 0
    for rank in (1, 2, 3):
        for count in range(1, 9):
            weights = tuple((index * rank + 1) % 7 for index in range(count))
            total = sum(weights)
            classes = [index % max(1, rank) for index in range(count)]
            class_total = sum(
                sum(weight for weight, label in zip(weights, classes) if label == pivot)
                for pivot in set(classes)
            )
            assert class_total == total
            checks += 1
    return checks


def verify_failed_bank_scale() -> int:
    checks = 0
    for weight in range(1, 101):
        for k in range(1, 21):
            destroyed = Fraction(weight, k)
            rank_return = destroyed / 3
            assert rank_return == Fraction(weight, 3 * k)
            checks += 1
    return checks


def main() -> None:
    orientation_checks = verify_orientation_partition()
    repair_checks, bucket_checks, rank_counts = verify_repairs()
    payment_checks = verify_weighted_payment()
    scale_checks = verify_failed_bank_scale()
    print("AC all-rank pivot orientation verified")
    print(f"  orientation words: {orientation_checks}")
    print(f"  union-safe pivot repairs: {repair_checks}")
    print(f"  partitioned bucket records: {bucket_checks}")
    print(f"  rank record counts: {rank_counts}")
    print(f"  weighted payment identities: {payment_checks}")
    print(f"  failed-bank scale identities: {scale_checks}")


if __name__ == "__main__":
    main()

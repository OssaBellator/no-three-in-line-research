#!/usr/bin/env python3
"""Finite checks for GC3j--GC3n."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import gcd

Point = tuple[int, int]
Assignment = tuple[Point, Point, Point, Point]


def line_key(a: Point, b: Point) -> tuple[int, int, int]:
    r1, c1 = a
    r2, c2 = b
    A = c2 - c1
    B = r1 - r2
    C = A * r1 + B * c1
    common = gcd(gcd(abs(A), abs(B)), abs(C))
    if common:
        A //= common
        B //= common
        C //= common
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def on_line(point: Point, line: tuple[int, int, int]) -> bool:
    r, c = point
    A, B, C = line
    return A * r + B * c == C


def assignments(targets: tuple[Point, ...], partners: tuple[Point, ...]) -> tuple[Assignment, ...]:
    out: list[Assignment] = []
    for target in targets:
        for partner in partners:
            cross_one = (target[0], partner[1])
            cross_two = (partner[0], target[1])
            out.append((target, partner, cross_one, cross_two))
    return tuple(out)


def verify_role_degrees(
    grid: tuple[Point, ...],
    targets: tuple[Point, ...],
    partners: tuple[Point, ...],
    records: tuple[Assignment, ...],
    counts: Counter[str],
) -> None:
    p = len(partners)
    t = len(targets)
    target_set = set(targets)
    partner_set = set(partners)

    target_degree: Counter[Point] = Counter()
    partner_degree: Counter[Point] = Counter()
    cross_one_degree: Counter[Point] = Counter()
    cross_two_degree: Counter[Point] = Counter()
    support_degree: Counter[Point] = Counter()

    for target, partner, cross_one, cross_two in records:
        target_degree[target] += 1
        partner_degree[partner] += 1
        cross_one_degree[cross_one] += 1
        cross_two_degree[cross_two] += 1
        for point in {target, partner, cross_one, cross_two}:
            support_degree[point] += 1

    for point in grid:
        assert target_degree[point] <= (p if point in target_set else 0)
        assert partner_degree[point] <= (t if point in partner_set else 0)
        assert cross_one_degree[point] <= 1
        assert cross_two_degree[point] <= 1
        bound = p * int(point in target_set) + t * int(point in partner_set) + 2
        assert support_degree[point] <= bound
        counts["cell role checks"] += 1


def verify_support_bound(
    grid: tuple[Point, ...],
    targets: tuple[Point, ...],
    partners: tuple[Point, ...],
    records: tuple[Assignment, ...],
    counts: Counter[str],
) -> None:
    p = len(partners)
    t = len(targets)
    target_set = set(targets)
    partner_set = set(partners)

    for rank in range(3):
        for support_tuple in combinations(grid, rank):
            support = set(support_tuple)
            touched = sum(
                1
                for target, partner, cross_one, cross_two in records
                if support.intersection({target, partner, cross_one, cross_two})
            )
            bound = (
                p * len(support.intersection(target_set))
                + t * len(support.intersection(partner_set))
                + 2 * len(support)
            )
            assert touched <= bound
            if support.isdisjoint(target_set) and support.isdisjoint(partner_set):
                assert touched <= 2 * len(support)
            counts["support checks"] += 1


def verify_line_bound(
    grid: tuple[Point, ...],
    targets: tuple[Point, ...],
    records: tuple[Assignment, ...],
    counts: Counter[str],
) -> None:
    lines = {
        line_key(a, b)
        for a, b in combinations(grid, 2)
        if line_key(a, b)[0] != 0 and line_key(a, b)[1] != 0
    }
    t = len(targets)
    for line in lines:
        total = sum(
            1
            for _, _, cross_one, cross_two in records
            if on_line(cross_one, line) or on_line(cross_two, line)
        )
        assert total <= 2 * t
        for target in targets:
            local = sum(
                1
                for record in records
                if record[0] == target
                and (on_line(record[2], line) or on_line(record[3], line))
            )
            assert local <= 2
        counts["non-axis line checks"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    for order in range(2, 6):
        grid = tuple((row, column) for row in range(order) for column in range(order))
        for permutation in permutations(range(order)):
            layer = tuple((row, permutation[row]) for row in range(order))
            for target_mask in range(1, 1 << order):
                targets = tuple(layer[index] for index in range(order) if target_mask >> index & 1)
                partners = tuple(layer[index] for index in range(order) if not (target_mask >> index & 1))
                if not partners:
                    continue
                records = assignments(targets, partners)
                verify_role_degrees(grid, targets, partners, records, counts)
                verify_support_bound(grid, targets, partners, records, counts)
                verify_line_bound(grid, targets, records, counts)
                counts["permutation partitions"] += 1

    print("GC3j--GC3n rectangle cause-degree audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()

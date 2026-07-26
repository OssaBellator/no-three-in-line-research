#!/usr/bin/env python3
"""Finite checks for GC1c--GC1f."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import gcd

Point = tuple[int, int]


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


def rectangle(target: Point, partner: Point) -> set[Point]:
    return {
        target,
        partner,
        (target[0], partner[1]),
        (partner[0], target[1]),
    }


def verify_physical_and_line_bounds(counts: Counter[str]) -> None:
    for order in range(2, 6):
        grid = tuple((row, column) for row in range(order) for column in range(order))
        nonaxis_lines = {
            line_key(a, b)
            for a, b in combinations(grid, 2)
            if line_key(a, b)[0] != 0 and line_key(a, b)[1] != 0
        }
        for permutation in permutations(range(order)):
            layer = tuple((row, permutation[row]) for row in range(order))
            for target_index, target in enumerate(layer):
                remaining = tuple(point for index, point in enumerate(layer) if index != target_index)
                for mask in range(1, 1 << len(remaining)):
                    partners = tuple(
                        point for index, point in enumerate(remaining) if mask >> index & 1
                    )
                    p = len(partners)
                    partner_set = set(partners)
                    rectangles = {partner: rectangle(target, partner) for partner in partners}

                    for rank in range(3):
                        for support_tuple in combinations(grid, rank):
                            support = set(support_tuple)
                            blocked = {
                                partner
                                for partner, scope in rectangles.items()
                                if scope.intersection(support)
                            }
                            bound = (
                                p * int(target in support)
                                + len(partner_set.intersection(support))
                                + 2 * len(support)
                            )
                            assert len(blocked) <= bound
                            if target not in support:
                                assert len(blocked) <= len(partner_set.intersection(support)) + 2 * len(support)
                            if target not in support and partner_set.isdisjoint(support):
                                assert len(blocked) <= 2 * len(support)
                            counts["physical support checks"] += 1

                    for line in nonaxis_lines:
                        blocked = {
                            partner
                            for partner in partners
                            if on_line((target[0], partner[1]), line)
                            or on_line((partner[0], target[1]), line)
                        }
                        assert len(blocked) <= 2
                        counts["one-target line checks"] += 1

                    counts["target-pool systems"] += 1


def verify_combined_union_bound(counts: Counter[str]) -> None:
    # A smaller fully crossed audit checks simultaneous physical, line and residual
    # blockers without making the order-five run unnecessarily large.
    for order in range(2, 5):
        grid = tuple((row, column) for row in range(order) for column in range(order))
        lines = sorted(
            {
                line_key(a, b)
                for a, b in combinations(grid, 2)
                if line_key(a, b)[0] != 0 and line_key(a, b)[1] != 0
            }
        )
        line_families = [tuple()]
        line_families.extend((line,) for line in lines)
        line_families.extend(combinations(lines, 2))

        for permutation in permutations(range(order)):
            layer = tuple((row, permutation[row]) for row in range(order))
            for target_index, target in enumerate(layer):
                partners = tuple(point for index, point in enumerate(layer) if index != target_index)
                p = len(partners)
                rectangles = {partner: rectangle(target, partner) for partner in partners}
                for support_rank in range(2):
                    for support_tuple in combinations(grid, support_rank):
                        support = set(support_tuple)
                        cell_blocked = {
                            partner
                            for partner, scope in rectangles.items()
                            if scope.intersection(support)
                        }
                        cell_bound = (
                            p * int(target in support)
                            + len(set(partners).intersection(support))
                            + 2 * len(support)
                        )
                        for family in line_families:
                            line_blocked = {
                                partner
                                for partner in partners
                                if any(
                                    on_line((target[0], partner[1]), line)
                                    or on_line((partner[0], target[1]), line)
                                    for line in family
                                )
                            }
                            # Use every subset of the partner pool as the exact
                            # global residual set.
                            for residual_mask in range(1 << p):
                                residual = {
                                    partner
                                    for index, partner in enumerate(partners)
                                    if residual_mask >> index & 1
                                }
                                total = cell_blocked | line_blocked | residual
                                assert len(total) <= cell_bound + 2 * len(family) + len(residual)
                                counts["combined blocker systems"] += 1


def verify_spread_entry_arithmetic(counts: Counter[str]) -> None:
    for p in range(1, 30):
        for t in range(1, p + 1):
            for blocker_budget in range(p + 1):
                if blocker_budget + t >= p:
                    continue
                minimum_choices = p - blocker_budget - (t - 1)
                denominator = p - blocker_budget - t
                assert denominator > 0
                assert minimum_choices >= denominator
                # K = p / denominator, so p/K = denominator.
                counts["spread parameter checks"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_physical_and_line_bounds(counts)
    verify_combined_union_bound(counts)
    verify_spread_entry_arithmetic(counts)
    print("GC1c--GC1f partner-blocker audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()

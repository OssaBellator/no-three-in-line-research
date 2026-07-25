#!/usr/bin/env python3
"""Verify CMR527--CMR534 finite identities.

Checks:
* persistent-cross partner pairs are compatible and have injective joining lines;
* distinct pair types cannot lie in one perfect matching;
* partner-support multiplicity and König matching/cover alternatives;
* fixed paid-pair restoration surcharge under the derangement law;
* joint continuous-absence runs versus the two reintroduction counts;
* trace witnesses split onto one arm.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product
from math import ceil, factorial, gcd


def norm_line(p: tuple[int, int], q: tuple[int, int]) -> tuple[int, int, int]:
    x1, y1 = p
    x2, y2 = q
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    g = 0
    for value in (a, b, c):
        g = gcd(g, abs(value))
    if g:
        a //= g
        b //= g
        c //= g
    for value in (a, b, c):
        if value:
            if value < 0:
                a, b, c = -a, -b, -c
            break
    return a, b, c


def check_cross_geometry() -> None:
    for m in range(3, 7):
        all_perms = list(permutations(range(m)))
        for u in range(m):
            for v in range(m):
                line_owner: dict[tuple[int, int, int], tuple[int, int]] = {}
                containing: dict[tuple[int, int], set[tuple[int, ...]]] = {}
                pair_types: list[tuple[int, int]] = []
                for x in range(m):
                    if x == u:
                        continue
                    for y in range(m):
                        if y == v:
                            continue
                        pair_type = (x, y)
                        line = norm_line((u, y), (x, v))
                        assert line not in line_owner
                        line_owner[line] = pair_type
                        states = {
                            perm
                            for perm in all_perms
                            if perm[u] == y and perm[x] == v
                        }
                        assert len(states) == factorial(m - 2)
                        containing[pair_type] = states
                        pair_types.append(pair_type)

                for first, second in combinations(pair_types, 2):
                    assert containing[first].isdisjoint(containing[second])


def max_matching_size(
    left_size: int,
    right_size: int,
    edges: set[tuple[int, int]],
) -> int:
    edge_list = list(edges)
    best = 0
    for size in range(len(edge_list) + 1):
        for chosen in combinations(edge_list, size):
            if (
                len({left for left, _ in chosen}) == size
                and len({right for _, right in chosen}) == size
            ):
                best = max(best, size)
    return best


def min_vertex_cover_size(
    left_size: int,
    right_size: int,
    edges: set[tuple[int, int]],
) -> int:
    vertices = [("L", i) for i in range(left_size)]
    vertices += [("R", j) for j in range(right_size)]
    for size in range(len(vertices) + 1):
        for chosen in combinations(vertices, size):
            cover = set(chosen)
            if all(
                ("L", left) in cover or ("R", right) in cover
                for left, right in edges
            ):
                return size
    raise AssertionError("no vertex cover found")


def check_partner_graphs() -> None:
    for left_size in range(1, 5):
        for right_size in range(1, 5):
            all_edges = [
                (left, right)
                for left in range(left_size)
                for right in range(right_size)
            ]
            for mask in range(1 << len(all_edges)):
                edges = {
                    edge
                    for index, edge in enumerate(all_edges)
                    if (mask >> index) & 1
                }
                matching = max_matching_size(left_size, right_size, edges)
                cover = min_vertex_cover_size(left_size, right_size, edges)
                assert matching == cover

                support_size = len(edges)
                for threshold in range(2, min(left_size, right_size) + 2):
                    if matching >= threshold or support_size == 0:
                        continue
                    assert cover <= threshold - 1
                    degrees = [
                        sum(left == vertex for left, _ in edges)
                        for vertex in range(left_size)
                    ]
                    degrees += [
                        sum(right == vertex for _, right in edges)
                        for vertex in range(right_size)
                    ]
                    assert max(degrees) >= ceil(
                        support_size / (threshold - 1)
                    )


def check_multiplicity_support() -> None:
    for left_size in range(1, 4):
        for right_size in range(1, 4):
            edges = [
                (left, right)
                for left in range(left_size)
                for right in range(right_size)
            ]
            for multiplicities in product(range(4), repeat=len(edges)):
                total = sum(multiplicities)
                if total == 0:
                    continue
                support = sum(value > 0 for value in multiplicities)
                for threshold in range(2, 5):
                    if max(multiplicities) >= threshold:
                        continue
                    assert support >= ceil(total / (threshold - 1))


def derangements(n: int) -> list[tuple[int, ...]]:
    return [
        perm
        for perm in permutations(range(n))
        if all(perm[index] != index for index in range(n))
    ]


def check_fixed_pair_surcharge() -> None:
    for n in range(2, 8):
        states = derangements(n)
        for row in range(n):
            for column in range(n):
                if row == column:
                    continue
                marginal = Fraction(
                    sum(perm[row] == column for perm in states),
                    len(states),
                )
                assert marginal == Fraction(1, n - 1)

        allowed = [
            (row, column)
            for row in range(n)
            for column in range(n)
            if row != column
        ]
        samples = [
            set(),
            set(allowed[::2]),
            set(allowed[1::3]),
            set(allowed),
        ]
        for unavailable in samples:
            average_residual = Fraction(
                sum(
                    sum(
                        (row, perm[row]) in unavailable
                        for row in range(n)
                    )
                    for perm in states
                ),
                len(states),
            )
            assert average_residual == Fraction(len(unavailable), n - 1)
            for fixed_cost in range(3):
                average_total = Fraction(
                    sum(
                        fixed_cost
                        + sum(
                            (row, perm[row]) in unavailable
                            for row in range(n)
                        )
                        for perm in states
                    ),
                    len(states),
                )
                assert average_total == (
                    fixed_cost + Fraction(len(unavailable), n - 1)
                )


def reintroductions(available: tuple[bool, ...]) -> int:
    return sum(
        available[index] and not available[index - 1]
        for index in range(1, len(available))
    )


def joint_absence_runs(
    first: tuple[bool, ...],
    second: tuple[bool, ...],
    selected: set[int],
) -> int:
    runs = 0
    in_selected_joint_run = False
    for index, (a, b) in enumerate(zip(first, second)):
        jointly_absent = not a and not b
        if not jointly_absent:
            in_selected_joint_run = False
            continue
        if index in selected and not in_selected_joint_run:
            runs += 1
            in_selected_joint_run = True
    return runs


def check_joint_persistence() -> None:
    for length in range(1, 9):
        sequences = list(product((False, True), repeat=length))
        for first in sequences:
            for second in sequences:
                joint_times = [
                    index
                    for index in range(length)
                    if not first[index] and not second[index]
                ]
                for mask in range(1 << len(joint_times)):
                    selected = {
                        time
                        for index, time in enumerate(joint_times)
                        if (mask >> index) & 1
                    }
                    if not selected:
                        continue
                    runs = joint_absence_runs(first, second, selected)
                    assert runs <= (
                        1 + reintroductions(first) + reintroductions(second)
                    )


def check_trace_split() -> None:
    for total in range(1, 200):
        for row_count in range(total + 1):
            column_count = total - row_count
            assert max(row_count, column_count) >= ceil(total / 2)


def main() -> None:
    check_cross_geometry()
    check_partner_graphs()
    check_multiplicity_support()
    check_fixed_pair_surcharge()
    check_joint_persistence()
    check_trace_split()
    print("verified persistent-cross pair-bank identities through side six")


if __name__ == "__main__":
    main()

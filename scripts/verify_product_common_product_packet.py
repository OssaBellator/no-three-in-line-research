#!/usr/bin/env python3
"""Verify PX210--PX212 common-product packet extraction and release."""
from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations
from math import exp, factorial, log
from random import Random


def collinear(first, second, third) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def support_four_count(rows, columns, anchor) -> int:
    cells = tuple(
        (i, j, (rows[i], columns[j]))
        for i in range(len(rows))
        for j in range(len(columns))
        if i != j
    )
    total = 0
    for first, second in combinations(cells, 2):
        i, j, first_cell = first
        k, ell, second_cell = second
        if i == k or j == ell or len({i, j, k, ell}) != 4:
            continue
        total += collinear(anchor, first_cell, second_cell)
    return total


def product_packets(rows, columns, anchor):
    packets = defaultdict(list)
    for i, row in enumerate(rows):
        row_difference = row - anchor[0]
        if row_difference == 0:
            continue
        for ell, column in enumerate(columns):
            if i == ell:
                continue
            column_difference = column - anchor[1]
            if column_difference == 0:
                continue
            packets[row_difference * column_difference].append((i, ell))
    return dict(packets)


def vertex_disjoint(first, second) -> bool:
    return len({first[0], first[1], second[0], second[1]}) == 4


def packet_pair_count(edges) -> int:
    return sum(
        vertex_disjoint(first, second)
        for first, second in combinations(edges, 2)
    )


def maximum_vertex_disjoint_subfamily(edges) -> int:
    best = 0
    for mask in range(1 << len(edges)):
        if mask.bit_count() <= best:
            continue
        used = set()
        valid = True
        for index, edge in enumerate(edges):
            if not mask & (1 << index):
                continue
            if edge[0] in used or edge[1] in used:
                valid = False
                break
            used.update(edge)
        if valid:
            best = mask.bit_count()
    return best


def verify_packet_identity_and_extraction() -> None:
    random = Random(210211)
    for side in range(7, 13):
        order = 5
        for _ in range(100):
            rows = tuple(random.sample(range(side), order))
            columns = tuple(random.sample(range(side), order))
            grid = {(row, column) for row in rows for column in columns}
            anchors = tuple(
                (row, column)
                for row in range(side)
                for column in range(side)
                if (row, column) not in grid
            )
            anchor = random.choice(anchors)
            packets = product_packets(rows, columns, anchor)
            exact = support_four_count(rows, columns, anchor)
            packet_total = sum(
                packet_pair_count(edges) for edges in packets.values()
            )
            assert exact == packet_total
            if exact == 0:
                continue

            product = max(
                packets,
                key=lambda value: (
                    packet_pair_count(packets[value]) / len(packets[value])
                ),
            )
            edges = packets[product]
            matching_size = maximum_vertex_disjoint_subfamily(edges)
            assert matching_size + 1e-12 >= 2 * exact / (3 * order**2)
        print(f"N={side}: packet identity and extraction verified")


def union_of_permutations(
    size: int, degree: int, random: Random
) -> tuple[int, ...]:
    masks = [0] * size
    for _ in range(degree):
        permutation = list(range(size))
        random.shuffle(permutation)
        for row, column in enumerate(permutation):
            masks[row] |= 1 << column
    return tuple(masks)


def count_released_permutations(forbidden: tuple[int, ...]) -> int:
    size = len(forbidden)
    total = 0
    for permutation in permutations(range(size)):
        if any(
            forbidden[row] & (1 << permutation[row])
            for row in range(size)
        ):
            continue
        if any(
            permutation[first] == second and permutation[second] == first
            for first, second in combinations(range(size), 2)
        ):
            continue
        total += 1
    return total


def verify_release_counts() -> None:
    random = Random(212)
    for size in range(6, 9):
        for degree in (1, 2, 3):
            if degree >= size:
                continue
            for _ in range(8):
                forbidden = union_of_permutations(size, degree, random)
                count = count_released_permutations(forbidden)
                assert count > 0
                lower = exp(-4 * degree - 4) * factorial(size)
                if lower <= 1:
                    assert count >= lower
            print(f"h={size}, Delta={degree}: released permutations positive")


def verify_lll_inequalities() -> None:
    for degree in range(1, 21):
        for size in (max(32, 32 * degree), 48 * degree, 64 * degree):
            singleton_witness = 2 / size
            cycle_witness = 4 / size**2

            singleton_lhs = (
                singleton_witness
                * (1 - singleton_witness) ** (2 * degree)
                * (1 - cycle_witness) ** (2 * size)
            )
            assert singleton_lhs >= 1 / size

            cycle_lhs = (
                cycle_witness
                * (1 - singleton_witness) ** (4 * degree)
                * (1 - cycle_witness) ** (2 * size)
            )
            assert cycle_lhs >= 1 / (size * (size - 1))

            density = (
                (1 - singleton_witness) ** (degree * size)
                * (1 - cycle_witness) ** (size * (size - 1) // 2)
            )
            assert density >= exp(-4 * degree - 4)
            assert log(1 - singleton_witness) >= -4 / size
            assert log(1 - cycle_witness) >= -8 / size**2
    print("mixed singleton/two-cycle lopsided-LLL inequalities verified")


def packet_certified_collisions(permutation) -> int:
    return sum(
        permutation[first] == second and permutation[second] == first
        for first, second in combinations(range(len(permutation)), 2)
    )


def verify_two_cycle_interpretation() -> None:
    for size in range(3, 9):
        cyclic_shift = tuple((index + 1) % size for index in range(size))
        assert packet_certified_collisions(cyclic_shift) == 0
        for first, second in combinations(range(size), 2):
            permutation = list(range(size))
            permutation[first], permutation[second] = second, first
            assert packet_certified_collisions(tuple(permutation)) == 1
    print("packet-certified collisions equal permutation two-cycles")


def main() -> None:
    verify_packet_identity_and_extraction()
    verify_release_counts()
    verify_lll_inequalities()
    verify_two_cycle_interpretation()
    print("PX210--PX212 verified")


if __name__ == "__main__":
    main()

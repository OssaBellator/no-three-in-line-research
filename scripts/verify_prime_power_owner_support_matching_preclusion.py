#!/usr/bin/env python3
"""Finite checks for CMR1406--CMR1413."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def extension_free_edges(side, target=(0, 1)):
    return frozenset(
        (row, column)
        for row in range(side)
        for column in range(side)
        if row != column and (row, column) != target
    )


def maximum_matching_size(edges, side):
    adjacency = {
        row: tuple(column for r, column in edges if r == row)
        for row in range(side)
    }
    matched_row = {}

    def augment(row, seen):
        for column in adjacency[row]:
            if column in seen:
                continue
            seen.add(column)
            if column not in matched_row or augment(matched_row[column], seen):
                matched_row[column] = row
                return True
        return False

    value = 0
    for row in range(side):
        if augment(row, set()):
            value += 1
    return value


def cut_edges(edges, rows, columns):
    return frozenset(
        edge for edge in edges if edge[0] in rows and edge[1] in columns
    )


def check_wall_sizes():
    cuts = 0
    equality = 0
    for side in range(4, 11):
        edges = extension_free_edges(side)
        target = (0, 1)
        exceptional_row = frozenset(edge for edge in edges if edge[0] == target[0])
        exceptional_column = frozenset(edge for edge in edges if edge[1] == target[1])
        for row_count in range(1, side + 1):
            column_count = side - row_count + 1
            for rows in combinations(range(side), row_count):
                row_set = frozenset(rows)
                for columns in combinations(range(side), column_count):
                    column_set = frozenset(columns)
                    wall = cut_edges(edges, row_set, column_set)
                    overlap = len(row_set & column_set)
                    target_missing = int(
                        target[0] in row_set and target[1] in column_set
                    )
                    assert len(wall) == (
                        row_count * column_count - overlap - target_missing
                    )
                    assert len(wall) >= side - 2
                    if len(wall) == side - 2:
                        assert wall in (exceptional_row, exceptional_column)
                        equality += 1
                    cuts += 1
        assert len(exceptional_row) == side - 2
        assert len(exceptional_column) == side - 2
    return cuts, equality


def check_small_deletion_resilience():
    checked = 0
    blocked = 0
    for side in range(4, 7):
        edges = extension_free_edges(side)
        target = (0, 1)
        exceptional_row = frozenset(edge for edge in edges if edge[0] == target[0])
        exceptional_column = frozenset(edge for edge in edges if edge[1] == target[1])
        edge_list = tuple(sorted(edges))
        for size in range(side - 1):
            for deleted_tuple in combinations(edge_list, size):
                deleted = frozenset(deleted_tuple)
                matchable = maximum_matching_size(edges - deleted, side) == side
                expected = not (
                    size == side - 2
                    and deleted in (exceptional_row, exceptional_column)
                )
                assert matchable == expected
                checked += 1
                blocked += int(not matchable)
    return checked, blocked


def compatible(prescription):
    return (
        len({row for row, _column in prescription}) == len(prescription)
        and len({column for _row, column in prescription}) == len(prescription)
    )


def true_cost(response, candidates, weights):
    return sum(
        weights[index]
        for index, prescription in enumerate(candidates)
        if prescription <= response
    )


def admissible_support(edges, target, support, side):
    if len(support) <= side - 3:
        return True
    if len(support) != side - 2:
        return False
    exceptional_row = frozenset(edge for edge in edges if edge[0] == target[0])
    exceptional_column = frozenset(edge for edge in edges if edge[1] == target[1])
    return support not in (exceptional_row, exceptional_column)


def check_owner_tail_policy():
    rng = random.Random(1409)
    systems = 0
    supports = 0
    for side in range(4, 7):
        target = (0, 1)
        edges = extension_free_edges(side, target)
        responses = tuple(
            matching(value)
            for value in permutations(range(side))
            if matching(value) <= edges
        )
        assert responses
        for _ in range(180):
            candidates = []
            owners = []
            weights = []
            for _candidate in range(rng.randint(1, 22)):
                witness = rng.choice(responses)
                rank = rng.randint(1, min(3, side))
                prescription = frozenset(rng.sample(tuple(witness), rank))
                assert compatible(prescription)
                candidates.append(prescription)
                owners.append(rng.choice(tuple(prescription)))
                weights.append(rng.randint(1, 9))

            owner_weight = defaultdict(int)
            for owner, weight in zip(owners, weights):
                owner_weight[owner] += weight
            total_weight = sum(weights)

            edge_list = tuple(sorted(edges))
            for _support in range(35):
                size = rng.randint(0, side - 2)
                support = frozenset(rng.sample(edge_list, size))
                if not admissible_support(edges, target, support, side):
                    continue
                survivor = next(
                    response for response in responses if response.isdisjoint(support)
                )
                tail = total_weight - sum(owner_weight[edge] for edge in support)
                assert true_cost(survivor, candidates, weights) <= tail
                supports += 1
            systems += 1
    return systems, supports


def check_fractional_rounding():
    rng = random.Random(1412)
    systems = 0
    low_support = 0
    for side in range(4, 11):
        target = (0, 1)
        edges = extension_free_edges(side, target)
        edge_list = tuple(sorted(edges))

        # General feasible fractional covers.
        for _ in range(300):
            denominator = 12
            numerators = {edge: rng.randint(0, denominator) for edge in edge_list}
            threshold = frozenset(
                edge for edge, value in numerators.items() if 3 * value >= denominator
            )
            if not threshold:
                chosen = rng.choice(edge_list)
                numerators[chosen] = denominator
                threshold = frozenset({chosen})
            candidates = []
            for _candidate in range(rng.randint(1, 30)):
                rank = rng.randint(1, 3)
                anchor = rng.choice(tuple(threshold))
                available = [
                    edge for edge in edge_list
                    if edge != anchor
                    and edge[0] != anchor[0]
                    and edge[1] != anchor[1]
                ]
                extra = rng.sample(available, min(rank - 1, len(available)))
                prescription = frozenset([anchor] + extra)
                if sum(numerators[edge] for edge in prescription) < denominator:
                    numerators[anchor] = denominator
                candidates.append(prescription)
            cover_value = sum(
                Fraction(value, denominator) for value in numerators.values()
            )
            rounded = frozenset(
                edge for edge, value in numerators.items() if 3 * value >= denominator
            )
            assert all(prescription & rounded for prescription in candidates)
            assert len(rounded) <= 3 * cover_value
            systems += 1

        # Concentrated covers exercise the strict threshold criterion.
        if side >= 6:
            max_support = (side - 3) // 3
            assert max_support >= 1
            for _ in range(120):
                support_size = rng.randint(1, max_support)
                support = frozenset(rng.sample(edge_list, support_size))
                numerators = {edge: int(edge in support) for edge in edge_list}
                candidates = []
                for _candidate in range(rng.randint(1, 35)):
                    anchor = rng.choice(tuple(support))
                    rank = rng.randint(1, 3)
                    available = [
                        edge for edge in edge_list
                        if edge != anchor
                        and edge[0] != anchor[0]
                        and edge[1] != anchor[1]
                    ]
                    candidates.append(
                        frozenset([anchor] + rng.sample(available, rank - 1))
                    )
                cover_value = sum(
                    Fraction(value, 1) for value in numerators.values()
                )
                rounded = support
                assert all(prescription & rounded for prescription in candidates)
                assert len(rounded) <= 3 * cover_value
                assert 3 * cover_value < side - 2
                assert len(rounded) <= side - 3
                assert maximum_matching_size(edges - rounded, side) == side
                low_support += 1
                systems += 1
    return systems, low_support


def main():
    walls = check_wall_sizes()
    deletions = check_small_deletion_resilience()
    owners = check_owner_tail_policy()
    fractional = check_fractional_rounding()
    print(
        "verified extension-free owner-support matching preclusion:",
        walls[0],
        "unit-wall cuts with",
        walls[1],
        "sharp equality cuts,",
        deletions[0],
        "small deletion sets with",
        deletions[1],
        "blockers,",
        owners[0],
        "owner systems over",
        owners[1],
        "admissible supports, and",
        fractional[0],
        "fractional-cover roundings with",
        fractional[1],
        "strict small-support certificates",
    )


if __name__ == "__main__":
    main()

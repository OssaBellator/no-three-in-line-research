#!/usr/bin/env python3
from __future__ import annotations
from collections import Counter
from itertools import combinations, permutations


def collinear(first, second, third):
    return (second[0] - first[0]) * (third[1] - first[1]) == (second[1] - first[1]) * (third[0] - first[0])


def triple_count(response):
    return sum(collinear(*triple) for triple in combinations(response, 3))


def perfect_matchings(side, allowed):
    return [
        tuple((row, permutation[row]) for row in range(side))
        for permutation in permutations(range(side))
        if all((row, permutation[row]) in allowed for row in range(side))
    ]


side = 4
base_host = {
    (row, column)
    for row in range(side)
    for column in range(side)
    if row != column and (row, column) != (0, 1)
}
deletions = [frozenset()]
for rank in range(1, side + 1):
    for deletion in combinations(base_host, rank):
        if len({row for row, _ in deletion}) == rank and len({column for _, column in deletion}) == rank:
            deletions.append(frozenset(deletion))

hosts = []
for deletion in deletions:
    responses = perfect_matchings(side, base_host - deletion)
    if responses:
        values = [triple_count(response) for response in responses]
        hosts.append((deletion, values))

assert len(hosts) == 86
zero_free = [(deletion, values) for deletion, values in hosts if all(value > 0 for value in values)]
assert len(zero_free) == 11
assert sum(any(value == 0 for value in values) for _, values in hosts) == 75
minimal = []
for deletion, values in zero_free:
    if not any(smaller < deletion and all(value > 0 for value in smaller_values) for smaller, smaller_values in hosts):
        minimal.append(deletion)
expected = {
    frozenset({(0, 2), (2, 0)}),
    frozenset({(0, 2), (3, 1)}),
    frozenset({(1, 3), (3, 1)}),
}
assert set(minimal) == expected
assert all(any(blocker <= deletion for blocker in expected) for deletion, _ in zero_free)
minimum_counts = Counter(min(values) for _, values in zero_free)
assert minimum_counts == Counter({1: 9, 4: 2})
print(
    f"verified rank-three zero-response atlas hosts={len(hosts)} "
    f"blockers={len(minimal)} survivor_minima={dict(minimum_counts)}"
)

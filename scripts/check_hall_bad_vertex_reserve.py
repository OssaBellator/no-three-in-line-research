#!/usr/bin/env python3
"""Verify the bad-vertex reserve condition for extracting a robust K4,4 core."""
from __future__ import annotations

from itertools import combinations, permutations, product


def partial_matchings(n: int):
    edges = tuple(product(range(n), repeat=2))
    result = []
    for size in range(n + 1):
        for subset in combinations(edges, size):
            if len({r for r, _ in subset}) == size == len({c for _, c in subset}):
                result.append(frozenset(subset))
    return tuple(result)


def perfect_matchings(n: int, forbidden: frozenset[tuple[int, int]]):
    return tuple(
        image for image in permutations(range(n))
        if all((row, image[row]) not in forbidden for row in range(n))
    )

matchings = partial_matchings(4)
assert len(matchings) == 209
unions = {partner | source for partner in matchings for source in matchings}
assert len(unions) == 7343
minimum_before = 24
for forbidden in unions:
    completions = perfect_matchings(4, forbidden)
    assert len(completions) >= 2
    minimum_before = min(minimum_before, len(completions))
    for edge in product(range(4), repeat=2):
        if edge not in forbidden:
            assert perfect_matchings(4, forbidden | {edge})
assert minimum_before == 2

reserve_table = []
for total_resources in range(6, 13):
    unused = total_resources - 2
    for bad_left in range(unused + 1):
        for bad_right in range(unused + 1):
            slack = min(unused - bad_left - 4, unused - bad_right - 4)
            sufficient = slack >= 0
            formula = total_resources >= 6 + max(bad_left, bad_right)
            assert sufficient == formula
            reserve_table.append((total_resources, bad_left, bad_right, slack, sufficient))

assert next(r for r in reserve_table if r[:3] == (6, 0, 0))[4]
assert not next(r for r in reserve_table if r[:3] == (6, 1, 0))[4]
assert next(r for r in reserve_table if r[:3] == (8, 2, 2))[4]

print({
    "partial_matchings_in_K4_4": len(matchings),
    "distinct_two_family_unions": len(unions),
    "minimum_perfect_matchings_before_extra_exclusion": minimum_before,
    "one_additional_exclusion_always_survives": True,
    "reserve_formula": "total_resources >= 6 + max(bad_left,bad_right)",
    "six_resource_case": "requires zero bad vertices on both sides",
    "eight_resource_case": "tolerates two bad vertices on each side",
    "reserve_parameter_cases_checked": len(reserve_table),
    "remaining_gap": "the asymptotic host has not been shown to bound the real bad-vertex sets",
    "evidence_level": "quantitative_bad_vertex_hall_reserve_lemma",
    "status": "passed",
})

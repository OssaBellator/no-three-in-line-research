#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, permutations

N = 4
EDGES = tuple((row, column) for row in range(N) for column in range(N))
PERFECT_MATCHINGS = tuple(
    frozenset((row, image[row]) for row in range(N))
    for image in permutations(range(N))
)


def partial_matchings():
    result = []
    for size in range(N + 1):
        for subset in combinations(EDGES, size):
            if len({row for row, _ in subset}) == size == len({column for _, column in subset}):
                result.append(frozenset(subset))
    return tuple(result)


PARTIAL = partial_matchings()
assert len(PARTIAL) == 209
ordered_pairs = 0
distinct_unions = set()
for partner_fibre in PARTIAL:
    for source_exclusions in PARTIAL:
        ordered_pairs += 1
        distinct_unions.add(partner_fibre | source_exclusions)
assert ordered_pairs == 43681
assert len(distinct_unions) == 7343

matching_histogram = Counter()
minimum_before = len(PERFECT_MATCHINGS)
minimum_after = len(PERFECT_MATCHINGS)
for forbidden in distinct_unions:
    matchings = tuple(matching for matching in PERFECT_MATCHINGS if matching.isdisjoint(forbidden))
    assert matchings
    matching_histogram[len(matchings)] += 1
    minimum_before = min(minimum_before, len(matchings))
    for extra_cell in (cell for cell in EDGES if cell not in forbidden):
        survivors = sum(extra_cell not in matching for matching in matchings)
        assert survivors > 0
        minimum_after = min(minimum_after, survivors)

assert minimum_before == 2
assert minimum_after == 1
assert matching_histogram == Counter({
    2: 72, 3: 672, 4: 2094, 5: 1440, 6: 1296, 7: 576,
    8: 648, 9: 24, 10: 288, 11: 96, 12: 48, 14: 72,
    18: 16, 24: 1,
})

print({
    "residual_host": "K_4,4 after selecting two resources in a six-resource host",
    "partial_matchings": len(PARTIAL),
    "ordered_partner_source_matching_pairs": ordered_pairs,
    "distinct_forbidden_unions": len(distinct_unions),
    "minimum_perfect_matchings_before_extra_exclusion": minimum_before,
    "minimum_perfect_matchings_after_any_one_extra_exclusion": minimum_after,
    "matching_count_histogram": dict(sorted(matching_histogram.items())),
    "sufficient_source_condition": "after selecting the local pair, retain four unused resources per side; both the restricted partner fibre and the restricted source-exclusion set are partial matchings",
    "remaining_gap": "the asymptotic PP3 host has not yet been proved to supply six total resources with both restricted forbidden families matching-shaped",
    "evidence_level": "exact_two_matching_spare_resource_lemma",
    "status": "passed",
})

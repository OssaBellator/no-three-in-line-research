#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, permutations


def perfect_matchings(rows, columns, forbidden):
    return tuple(
        tuple(zip(rows, image))
        for image in permutations(columns)
        if not set(zip(rows, image)).intersection(forbidden)
    )


def blocker_number(matchings):
    used = sorted(set().union(*(set(matching) for matching in matchings)))
    for size in range(1, len(used) + 1):
        for subset in combinations(used, size):
            if all(set(subset).intersection(matching) for matching in matchings):
                return size
    raise AssertionError("nonempty matching family must have a blocker")


def partial_matchings(rows, columns):
    edges = tuple((row, column) for row in rows for column in columns)
    result = []
    for size in range(4):
        for subset in combinations(edges, size):
            if len({row for row, _ in subset}) == size == len({column for _, column in subset}):
                result.append(subset)
    return tuple(result)


rows = columns = tuple(range(3))
records = []
for forbidden in partial_matchings(rows, columns):
    matchings = perfect_matchings(rows, columns, set(forbidden))
    blocker = blocker_number(matchings)
    assert matchings and blocker >= 2
    for extra_cell in ((row, column) for row in rows for column in columns if (row, column) not in forbidden):
        assert perfect_matchings(rows, columns, set(forbidden) | {extra_cell})
    records.append((len(forbidden), len(matchings), blocker))

assert len(records) == 34
assert Counter(records) == {(0, 6, 3): 1, (1, 4, 2): 9, (2, 3, 2): 18, (3, 2, 2): 6}

N = 5
CONFLICTS = (
    ((0, 0), (1, 1)), ((0, 0), (1, 2)), ((0, 0), (1, 3)),
    ((0, 1), (1, 0)), ((0, 3), (2, 0)), ((0, 3), (3, 1)),
)
FIBRES = {(0, column): set() for column in range(N)}
for first, second in CONFLICTS:
    centre, partner = (first, second) if first[0] == 0 else (second, first)
    FIBRES[centre].add(partner)

choice_columns = (1, 2, 3, 4)
second_row = 1
fixture_records = []
for syndrome in range(3):
    for choice in range(4):
        pair = ((0, choice_columns[choice]), (second_row, choice_columns[(choice + syndrome + 1) % 4]))
        residual_rows = tuple(row for row in range(N) if row not in {0, second_row})
        residual_columns = tuple(column for column in range(N) if column not in {pair[0][1], pair[1][1]})
        restricted_fibre = tuple(sorted(cell for cell in FIBRES[pair[0]] if cell[0] in residual_rows and cell[1] in residual_columns))
        assert len({row for row, _ in restricted_fibre}) == len(restricted_fibre) == len({column for _, column in restricted_fibre})
        matchings = perfect_matchings(residual_rows, residual_columns, set(restricted_fibre))
        blocker = blocker_number(matchings)
        assert blocker >= 2
        fixture_records.append((syndrome, choice, pair, restricted_fibre, len(matchings), blocker))

assert sorted(record[4] for record in fixture_records) == [3, 3, 4] + [6] * 9
assert sorted(record[5] for record in fixture_records) == [2, 2, 2] + [3] * 9

print({
    "residual_host": "K_3,3 after selecting two resources in a five-resource host",
    "partial_partner_fibres_checked": len(records),
    "matching_count_and_blocker_histogram": dict(Counter(records)),
    "single_additional_exclusion_always_survives": True,
    "source_fixture_choices": len(fixture_records),
    "source_fixture_total_conditional_matchings": sum(record[4] for record in fixture_records),
    "source_fixture_minimum_blocker": min(record[5] for record in fixture_records),
    "missing_resource_condition": "the asymptotic conditional host must supply one spare left and right resource and leave a matching-shaped restricted partner fibre",
    "evidence_level": "source_typed_spare_resource_completion_lemma",
    "status": "passed",
})

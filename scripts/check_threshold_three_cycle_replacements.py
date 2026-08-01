#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations

SOURCE = (
    (2, 1, 1, 0),
    (0, 2, 1, 1),
    (1, 0, 2, 1),
    (1, 1, 0, 2),
)
PERMUTATIONS = tuple(permutations(range(4)))


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def legal(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points, 3))


def matrix(layers):
    result = [[0] * 4 for _ in range(4)]
    for layer in layers:
        for row, column in enumerate(layer):
            result[row][column] += 1
    return tuple(tuple(row) for row in result)


def distance(left, right):
    return sum(abs(left[row][column] - right[row][column]) for row in range(4) for column in range(4))


legal_layers = tuple(permutation for permutation in PERMUTATIONS if legal(permutation))
assert len(legal_layers) == 18
nearest_distance = None
nearest = []
for indices in combinations_with_replacement(range(len(legal_layers)), 4):
    layers = tuple(legal_layers[index] for index in indices)
    candidate = matrix(layers)
    current_distance = distance(candidate, SOURCE)
    if nearest_distance is None or current_distance < nearest_distance:
        nearest_distance = current_distance
        nearest = [(candidate, layers)]
    elif current_distance == nearest_distance:
        nearest.append((candidate, layers))

assert nearest_distance == 6
assert len(nearest) == 8
trade_records = []
for candidate, layers in nearest:
    removed = []
    added = []
    changed_rows = []
    for row in range(4):
        row_removed = []
        row_added = []
        for column in range(4):
            delta = candidate[row][column] - SOURCE[row][column]
            if delta < 0:
                row_removed.extend([column] * (-delta))
            elif delta > 0:
                row_added.extend([column] * delta)
        assert len(row_removed) == len(row_added)
        if row_removed:
            assert len(row_removed) == 1
            changed_rows.append(row)
            removed.append((row, row_removed[0]))
            added.append((row, row_added[0]))
    assert len(changed_rows) == 3
    assert len({column for _, column in removed}) == 3
    assert len({column for _, column in added}) == 3
    assert {column for _, column in removed} == {column for _, column in added}
    action_map = {old_column: new_column for (_, old_column), (_, new_column) in zip(removed, added)}
    start = min(action_map)
    orbit = [start]
    while action_map[orbit[-1]] != start:
        orbit.append(action_map[orbit[-1]])
    assert len(orbit) == 3
    assert set(orbit) == set(action_map)
    trade_records.append((tuple(changed_rows), tuple(removed), tuple(added), tuple(orbit)))

assert len(set(record[1:] for record in trade_records)) == 8
row_histogram = Counter(tuple(sorted(record[0])) for record in trade_records)
assert row_histogram == Counter({
    (0, 1, 2): 2,
    (0, 1, 3): 2,
    (0, 2, 3): 2,
    (1, 2, 3): 2,
})

print({
    "legal_degree_four_layers": len(legal_layers),
    "nearest_source_preserving_legal_matrices": len(nearest),
    "minimum_entrywise_l1_distance": nearest_distance,
    "mass_units_moved": nearest_distance // 2,
    "replacement_structure": "each nearest legal matrix is obtained by one unit alternating three-cycle trade on three source rows and three action columns",
    "changed_row_triple_histogram": {str(key): value for key, value in sorted(row_histogram.items())},
    "canonical_trade": {
        "removed": trade_records[0][1],
        "added": trade_records[0][2],
        "action_cycle": trade_records[0][3],
    },
    "remaining_gap": "the repository has no source-derived geometric operation implementing any of the eight unit three-cycle trades",
    "evidence_level": "exact_source_preserving_threshold_trade_catalogue",
    "status": "passed",
})

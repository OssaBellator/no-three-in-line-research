#!/usr/bin/env python3
from itertools import combinations, permutations

ROWS = range(4)
COLUMNS = range(4)


def decoded_pair(syndrome, choice):
    return choice, (choice + syndrome + 1) % 4


def first_collinear(points):
    for a, b, c in combinations(points, 3):
        if (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0]):
            return a, b, c
    return None


pairs = {}
legal_extensions = {}
for syndrome in range(3):
    for choice in range(4):
        first_column, second_column = decoded_pair(syndrome, choice)
        assert first_column != second_column
        pair = ((0, first_column), (1, second_column))
        pairs[(syndrome, choice)] = pair

        remaining_columns = tuple(column for column in COLUMNS if column not in (first_column, second_column))
        extensions = []
        for assignment in permutations(remaining_columns):
            matching = pair + ((2, assignment[0]), (3, assignment[1]))
            if first_collinear(matching) is None:
                extensions.append(matching)
        legal_extensions[(syndrome, choice)] = tuple(extensions)

assert len(set(pairs.values())) == 12
assert set(pairs.values()) == {
    ((0, first_column), (1, second_column))
    for first_column in COLUMNS
    for second_column in COLUMNS
    if first_column != second_column
}
assert all(legal_extensions[key] for key in legal_extensions)
assert sum(len(value) for value in legal_extensions.values()) == 18
assert sorted(len(value) for value in legal_extensions.values()) == [1] * 6 + [2] * 6

# Every extension is a perfect matching and avoids all collinear triples.
for extensions in legal_extensions.values():
    for matching in extensions:
        assert sorted(row for row, _ in matching) == list(ROWS)
        assert sorted(column for _, column in matching) == list(COLUMNS)
        assert first_collinear(matching) is None

# Both microscopic orientations witness the same decoded pair.
microscopic_witnesses = {
    (syndrome, orientation, choice): pairs[(syndrome, choice)]
    for syndrome in range(3)
    for orientation in range(2)
    for choice in range(4)
}
assert len(microscopic_witnesses) == 24
assert all(
    microscopic_witnesses[(syndrome, 0, choice)] == microscopic_witnesses[(syndrome, 1, choice)]
    for syndrome in range(3)
    for choice in range(4)
)

print({
    "coordinate_host": "four rows by four columns",
    "decoded_pairs": len(pairs),
    "no_three_in_line_matching_extensions": sum(len(value) for value in legal_extensions.values()),
    "pairs_with_one_extension": sum(len(value) == 1 for value in legal_extensions.values()),
    "pairs_with_two_extensions": sum(len(value) == 2 for value in legal_extensions.values()),
    "minimum_extensions_per_pair": min(len(value) for value in legal_extensions.values()),
    "microscopic_orientation_witnesses": len(microscopic_witnesses),
    "remaining_gap": "the four columns are not yet identified with endpoint cells of an actual prime-patching host",
    "evidence_level": "coordinate_level_complete_grid_candidate",
    "status": "passed",
})

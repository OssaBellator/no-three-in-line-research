#!/usr/bin/env python3
from itertools import combinations, permutations

SOURCE = (
    (2, 1, 1, 0),
    (0, 2, 1, 1),
    (1, 0, 2, 1),
    (1, 1, 0, 2),
)
PERMUTATIONS = tuple(permutations(range(4)))


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def legal_layer(permutation):
    points = tuple((source, action) for source, action in enumerate(permutation))
    return all(not collinear(*triple) for triple in combinations(points, 3))


def add_layer(matrix, permutation):
    return tuple(
        tuple(matrix[source][action] + int(action == permutation[source]) for action in range(4))
        for source in range(4)
    )


def subtract_layer(matrix, permutation):
    rows = [list(row) for row in matrix]
    for source, action in enumerate(permutation):
        if rows[source][action] == 0:
            return None
        rows[source][action] -= 1
    return tuple(tuple(row) for row in rows)


def ordered_decomposition_count(matrix, steps):
    memo = {}

    def rec(current, remaining):
        key = (current, remaining)
        if key in memo:
            return memo[key]
        if remaining == 0:
            value = int(all(entry == 0 for row in current for entry in row))
        else:
            value = 0
            for permutation in PERMUTATIONS:
                if not legal_layer(permutation):
                    continue
                next_matrix = subtract_layer(current, permutation)
                if next_matrix is not None:
                    value += rec(next_matrix, remaining - 1)
        memo[key] = value
        return value

    return rec(matrix, steps)


successful = []
for augmentation in PERMUTATIONS:
    augmented = add_layer(SOURCE, augmentation)
    count = ordered_decomposition_count(augmented, 5)
    if count:
        successful.append((augmentation, augmented, count))

assert len(successful) == 1
augmentation, augmented, count = successful[0]
assert augmentation == (3, 0, 1, 2)
assert augmented == (
    (2, 1, 1, 1),
    (1, 2, 1, 1),
    (1, 1, 2, 1),
    (1, 1, 1, 2),
)
assert count == 120
assert all(sum(row) == 4 for row in SOURCE)
assert all(sum(SOURCE[row][column] for row in range(4)) == 4 for column in range(4))
assert all(sum(row) == 5 for row in augmented)
assert all(sum(augmented[row][column] for row in range(4)) == 5 for column in range(4))

print(
    {
        "source_row_and_column_degree": 4,
        "successful_single_layer_augmentations": len(successful),
        "unique_augmentation": augmentation,
        "augmented_row_and_column_degree": 5,
        "legal_ordered_five_layer_decompositions": count,
        "new_source_cell_mass": 4,
        "extra_slot_fraction_of_augmented_schedule": "1/5",
        "relative_slot_count_increase": "1/4",
        "source_mechanism_obstruction": "all stored threshold operations reorder or decompose a fixed degree-four matrix and therefore cannot supply the required degree-five margins",
        "evidence_level": "exact_threshold_source_margin_obstruction",
        "status": "passed",
    }
)

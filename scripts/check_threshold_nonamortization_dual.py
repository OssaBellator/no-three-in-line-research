#!/usr/bin/env python3
from itertools import combinations, permutations

SOURCE = (
    (2, 1, 1, 0),
    (0, 2, 1, 1),
    (1, 0, 2, 1),
    (1, 1, 0, 2),
)
DUAL = (
    (3, 1, 2, 0),
    (0, 0, 0, -1),
    (-1, -3, -1, -3),
    (1, 0, 0, 0),
)
AUGMENTATION = (3, 0, 1, 2)
PERMUTATIONS = tuple(permutations(range(4)))


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def legal(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points, 3))


def permutation_score(permutation):
    return sum(DUAL[row][permutation[row]] for row in range(4))


def matrix_score(matrix):
    return sum(DUAL[row][column] * matrix[row][column] for row in range(4) for column in range(4))


legal_scores = {permutation: permutation_score(permutation) for permutation in PERMUTATIONS if legal(permutation)}
all_scores = {permutation: permutation_score(permutation) for permutation in PERMUTATIONS}
assert len(legal_scores) == 18
assert max(legal_scores.values()) == 0
assert min(all_scores.values()) == -3
assert matrix_score(SOURCE) == 3
assert permutation_score(AUGMENTATION) == -3

LEGAL_DECOMPOSITION = (
    (0, 1, 3, 2),
    (0, 2, 1, 3),
    (1, 0, 2, 3),
    (2, 3, 0, 1),
    (3, 1, 2, 0),
)
assert all(legal(permutation) and permutation_score(permutation) == 0 for permutation in LEGAL_DECOMPOSITION)
for row in range(4):
    for column in range(4):
        left = SOURCE[row][column] + int(AUGMENTATION[row] == column)
        right = sum(int(permutation[row] == column) for permutation in LEGAL_DECOMPOSITION)
        assert left == right

print({
    "integer_dual_matrix": DUAL,
    "source_score": matrix_score(SOURCE),
    "maximum_legal_layer_score": max(legal_scores.values()),
    "minimum_arbitrary_augmentation_score": min(all_scores.values()),
    "sharp_augmentation": AUGMENTATION,
    "minimum_augmentations_for_k_source_periods": "k",
    "amortized_augmentation_density": "1 per source period",
    "extra_slot_fraction": "1/5",
    "relative_slot_increase": "1/4",
    "conclusion": "the legal fifth layer cannot be diluted or residue-amortized across several source periods",
    "evidence_level": "exact_threshold_nonamortization_dual",
    "status": "passed",
})

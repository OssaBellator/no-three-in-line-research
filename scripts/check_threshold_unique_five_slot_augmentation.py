#!/usr/bin/env python3
from functools import lru_cache
from itertools import combinations, permutations

SOURCE = (
    (2, 1, 1, 0),
    (0, 2, 1, 1),
    (1, 0, 2, 1),
    (1, 1, 0, 2),
)
PERMS = tuple(permutations(range(4)))

def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])

def legal_layer(permutation):
    points = tuple((source, action) for source, action in enumerate(permutation))
    return all(not collinear(*triple) for triple in combinations(points, 3))

LEGAL = tuple(permutation for permutation in PERMS if legal_layer(permutation))
assert len(LEGAL) == 18

def add_layer(matrix, permutation):
    work = [list(row) for row in matrix]
    for source, action in enumerate(permutation):
        work[source][action] += 1
    return tuple(tuple(row) for row in work)

def subtract_layer(matrix, permutation):
    work = [list(row) for row in matrix]
    for source, action in enumerate(permutation):
        if work[source][action] == 0:
            return None
        work[source][action] -= 1
    return tuple(tuple(row) for row in work)

@lru_cache(None)
def count_decompositions(matrix, steps):
    if steps == 0:
        return int(all(value == 0 for row in matrix for value in row))
    total = 0
    for permutation in LEGAL:
        next_matrix = subtract_layer(matrix, permutation)
        if next_matrix is not None:
            total += count_decompositions(next_matrix, steps - 1)
    return total

successful = []
for augmentation in PERMS:
    augmented = add_layer(SOURCE, augmentation)
    count = count_decompositions(augmented, 5)
    if count:
        successful.append((augmentation, augmented, count))

assert len(successful) == 1
augmentation, augmented, ordered_count = successful[0]
assert augmentation == (3, 0, 1, 2)
assert ordered_count == 120
assert not legal_layer(augmentation)
assert augmented == (
    (2, 1, 1, 1),
    (1, 2, 1, 1),
    (1, 1, 2, 1),
    (1, 1, 1, 2),
)

print({
    "source_matrix": SOURCE,
    "one_slot_augmentations_checked": len(PERMS),
    "unique_successful_augmentation": augmentation,
    "augmented_matrix": augmented,
    "ordered_legal_five_layer_decompositions": ordered_count,
    "augmentation_itself_is_legal_layer": False,
    "conclusion": "one additional source unit per row and column is sufficient and uniquely placed for a legal five-slot decomposition",
    "remaining_gap": "the extra slot and its source mass are not charged by an actual prime-patching threshold inequality",
    "evidence_level": "exact_five_slot_threshold_enlargement",
    "status": "passed",
})

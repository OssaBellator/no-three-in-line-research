#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations

SOURCE = ((2,1,1,0),(0,2,1,1),(1,0,2,1),(1,1,0,2))

def collinear(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1]) == (b[1]-a[1])*(c[0]-a[0])

def legal(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points, 3))

def layer_matrix(layers):
    matrix = [[0]*4 for _ in range(4)]
    for layer in layers:
        for row, column in enumerate(layer):
            matrix[row][column] += 1
    return tuple(tuple(row) for row in matrix)

def distance(first, second):
    return sum(abs(first[r][c]-second[r][c]) for r in range(4) for c in range(4))

def swaps(matrix):
    for r1,r2 in combinations(range(4),2):
        for c1,c2 in combinations(range(4),2):
            for orientation in (0,1):
                removed = ((r1,c1),(r2,c2)) if orientation == 0 else ((r1,c2),(r2,c1))
                added = ((r1,c2),(r2,c1)) if orientation == 0 else ((r1,c1),(r2,c2))
                if not all(matrix[r][c] > 0 for r,c in removed):
                    continue
                updated = [list(row) for row in matrix]
                for r,c in removed: updated[r][c] -= 1
                for r,c in added: updated[r][c] += 1
                yield tuple(tuple(row) for row in updated), removed, added

legal_layers = tuple(item for item in permutations(range(4)) if legal(item))
legal_matrices = {
    layer_matrix(tuple(legal_layers[index] for index in indices))
    for indices in combinations_with_replacement(range(len(legal_layers)),4)
}
minimum = min(distance(SOURCE, matrix) for matrix in legal_matrices)
targets = tuple(matrix for matrix in legal_matrices if distance(SOURCE, matrix) == minimum)
assert minimum == 6 and len(targets) == 8

records = []
for intermediate, removed_first, added_first in swaps(SOURCE):
    for target, removed_second, added_second in swaps(intermediate):
        if target not in targets:
            continue
        first_support = set(removed_first) | set(added_first)
        second_support = set(removed_second) | set(added_second)
        target_support = {
            (r,c) for r in range(4) for c in range(4)
            if SOURCE[r][c] != target[r][c]
        }
        union = first_support | second_support
        transient = union - target_support
        records.append((target, union, transient))

assert len(records) == 48
assert all(len(union) == 7 and len(transient) == 1 for _, union, transient in records)
transient_counts = Counter(next(iter(transient)) for _, _, transient in records)
SOURCE_UNIT_CELLS = {
    (r,c) for r in range(4) for c in range(4) if SOURCE[r][c] == 1
}
assert set(transient_counts) == SOURCE_UNIT_CELLS
assert set(transient_counts.values()) == {6}
assert len(SOURCE_UNIT_CELLS) == 8

print({
    "ordered_two_swap_factorizations": len(records),
    "target_support_cells": 6,
    "atomic_batch_union_support_cells": 7,
    "transient_cells_per_factorization": 1,
    "possible_transient_cells": tuple(sorted(SOURCE_UNIT_CELLS)),
    "factorizations_per_transient_cell": 6,
    "transient_cells_are_exactly_source_unit_cells": True,
    "conclusion": "every repository-native two-swap batch needs the six target cells plus one cancelling buffer cell",
    "remaining_gap": "no geometric source edit protects the seven-cell batch footprint while preserving all exposed no-three constraints",
    "evidence_level": "exact_threshold_transient_buffer_cell_catalogue",
    "status": "passed",
})

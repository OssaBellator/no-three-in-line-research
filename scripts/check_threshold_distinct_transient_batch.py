#!/usr/bin/env python3
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations

SOURCE = ((2,1,1,0),(0,2,1,1),(1,0,2,1),(1,1,0,2))

def collinear(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1]) == (b[1]-a[1])*(c[0]-a[0])

def legal(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points,3))

def layer_matrix(layers):
    return tuple(tuple(sum(layer[row] == column for layer in layers) for column in range(4)) for row in range(4))

def distance(first,second):
    return sum(abs(first[row][column]-second[row][column]) for row in range(4) for column in range(4))

def swaps(matrix):
    for r1,r2 in combinations(range(4),2):
        for c1,c2 in combinations(range(4),2):
            for orientation in (0,1):
                removed = ((r1,c1),(r2,c2)) if orientation == 0 else ((r1,c2),(r2,c1))
                added = ((r1,c2),(r2,c1)) if orientation == 0 else ((r1,c1),(r2,c2))
                if not all(matrix[row][column] > 0 for row,column in removed):
                    continue
                updated = [list(row) for row in matrix]
                for row,column in removed:
                    updated[row][column] -= 1
                for row,column in added:
                    updated[row][column] += 1
                yield tuple(tuple(row) for row in updated)

layers = tuple(item for item in permutations(range(4)) if legal(item))
legal_matrices = {
    layer_matrix(tuple(layers[index] for index in indices))
    for indices in combinations_with_replacement(range(len(layers)),4)
}
minimum = min(distance(SOURCE,matrix) for matrix in legal_matrices)
targets = tuple(sorted(matrix for matrix in legal_matrices if distance(SOURCE,matrix) == minimum))
assert len(targets) == 8 and minimum == 6

adjacency = defaultdict(set)
path_counts = Counter()
for target_index,target in enumerate(targets):
    support = {(row,column) for row in range(4) for column in range(4) if target[row][column] != SOURCE[row][column]}
    for intermediate in swaps(SOURCE):
        for endpoint in swaps(intermediate):
            if endpoint != target:
                continue
            transient = {(row,column) for row in range(4) for column in range(4) if intermediate[row][column] != SOURCE[row][column]} - support
            assert len(transient) == 1
            cell = next(iter(transient))
            adjacency[target_index].add(cell)
            path_counts[(target_index,cell)] += 1

transient_cells = tuple(sorted({cell for cells in adjacency.values() for cell in cells}))
assert transient_cells == tuple(sorted((row,column) for row in range(4) for column in range(4) if SOURCE[row][column] == 1))
assert all(len(adjacency[index]) == 3 for index in range(8))
assert Counter(cell for cells in adjacency.values() for cell in cells) == Counter({cell:3 for cell in transient_cells})
assert set(path_counts.values()) == {2}
assert sum(path_counts.values()) == 48

seen_targets = {0}
seen_cells = set()
changed = True
while changed:
    changed = False
    for target in tuple(seen_targets):
        for cell in adjacency[target]:
            if cell not in seen_cells:
                seen_cells.add(cell)
                changed = True
    for target in range(8):
        if target not in seen_targets and adjacency[target] & seen_cells:
            seen_targets.add(target)
            changed = True
assert len(seen_targets) == 8 and len(seen_cells) == 8

perfect_matchings = []
for image in permutations(transient_cells):
    if all(image[target] in adjacency[target] for target in range(8)):
        perfect_matchings.append(image)
assert len(perfect_matchings) == 49
assert all(len(set(image)) == 8 for image in perfect_matchings)
ORDERED_BATCHES = len(perfect_matchings) * (2 ** 8)
assert ORDERED_BATCHES == 12544

print({
    "targets": len(targets),
    "transient_cells": len(transient_cells),
    "target_degree_in_incidence_graph": 3,
    "transient_degree_in_incidence_graph": 3,
    "target_transient_incidences": 24,
    "incidence_graph_connected": True,
    "orders_per_incidence": 2,
    "distinct_transient_assignments_for_all_eight_targets": len(perfect_matchings),
    "ordered_distinct_buffer_batches": ORDERED_BATCHES,
    "buffer_reuse_within_each_batch": 0,
    "remaining_gap": "the balanced matrix-level batch still lacks a geometric realization in which every transient buffer cell and exposed state is no-three legal",
    "evidence_level": "exact_distinct_transient_threshold_batch",
    "status": "passed",
})

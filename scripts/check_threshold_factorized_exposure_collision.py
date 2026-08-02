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
supports = []
for target_index,target in enumerate(targets):
    support = {(row,column) for row in range(4) for column in range(4) if target[row][column] != SOURCE[row][column]}
    supports.append(support)
    for intermediate in swaps(SOURCE):
        for endpoint in swaps(intermediate):
            if endpoint != target:
                continue
            transient = {(row,column) for row in range(4) for column in range(4) if intermediate[row][column] != SOURCE[row][column]} - support
            assert len(transient) == 1
            adjacency[target_index].add(next(iter(transient)))

transient_cells = tuple(sorted({cell for cells in adjacency.values() for cell in cells}))
matchings = [
    image for image in permutations(transient_cells)
    if all(image[target] in adjacency[target] for target in range(8))
]
assert len(matchings) == 49
matching_edges = [{(target,image[target]) for target in range(8)} for image in matchings]
all_edges = {(target,cell) for target in range(8) for cell in adjacency[target]}

factorizations = []
for first in range(len(matchings)):
    for second in range(first+1,len(matchings)):
        if matching_edges[first] & matching_edges[second]:
            continue
        remainder = all_edges - matching_edges[first] - matching_edges[second]
        for third in range(second+1,len(matchings)):
            if matching_edges[third] == remainder:
                factorizations.append((first,second,third))
                break
assert len(factorizations) == 44
assert all(set().union(*(matching_edges[index] for index in factorization)) == all_edges for factorization in factorizations)
ORDERED_FACTORIZATIONS = 6 * len(factorizations)
ORDERED_NATIVE_SCHEDULES = ORDERED_FACTORIZATIONS * (2 ** 24)
assert ORDERED_FACTORIZATIONS == 264
assert ORDERED_NATIVE_SCHEDULES == 4429185024

heavy_cells = {(row,column) for row in range(4) for column in range(4) if SOURCE[row][column] != 1}
unit_cells = {(row,column) for row in range(4) for column in range(4) if SOURCE[row][column] == 1}
assert len(heavy_cells) == len(unit_cells) == 8

support_loads = Counter(cell for support in supports for cell in support)
assert {cell for cell,load in support_loads.items() if load == 5} == heavy_cells
assert {cell for cell,load in support_loads.items() if load == 1} == unit_cells

for image in matchings:
    loads = Counter()
    for target in range(8):
        for cell in supports[target] | {image[target]}:
            loads[cell] += 1
    assert set(loads) == {(row,column) for row in range(4) for column in range(4)}
    assert Counter(loads.values()) == Counter({2:8,5:8})
    assert max(loads.values()) == 5

print({
    "perfect_matchings": len(matchings),
    "unordered_three_round_factorizations": len(factorizations),
    "ordered_three_round_factorizations": ORDERED_FACTORIZATIONS,
    "ordered_native_three_round_schedules": ORDERED_NATIVE_SCHEDULES,
    "footprint_union_cells_per_round": 16,
    "footprint_load_histogram_per_round": {2:8,5:8},
    "maximum_shared_cell_load": 5,
    "heavy_cells": tuple(sorted(heavy_cells)),
    "unit_buffer_cells": tuple(sorted(unit_cells)),
    "remaining_gap": "balanced distinct-buffer scheduling still requires a geometric operation protecting the full 4x4 footprint and fivefold-shared heavy cells in every round",
    "evidence_level": "exact_threshold_factorization_and_exposure_collision_obstruction",
    "status": "passed",
})

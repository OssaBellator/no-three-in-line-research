#!/usr/bin/env python3
from collections import Counter, defaultdict
from itertools import combinations, combinations_with_replacement, permutations, product

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
assert minimum == 6 and len(targets) == 8

adjacency = defaultdict(set)
intermediate_options = defaultdict(list)
for target_index,target in enumerate(targets):
    target_support = {
        (row,column)
        for row in range(4)
        for column in range(4)
        if target[row][column] != SOURCE[row][column]
    }
    for intermediate in swaps(SOURCE):
        for endpoint in swaps(intermediate):
            if endpoint != target:
                continue
            transient = {
                (row,column)
                for row in range(4)
                for column in range(4)
                if intermediate[row][column] != SOURCE[row][column]
            } - target_support
            assert len(transient) == 1
            cell = next(iter(transient))
            adjacency[target_index].add(cell)
            intermediate_options[(target_index,cell)].append(intermediate)

transient_cells = tuple(sorted({cell for cells in adjacency.values() for cell in cells}))
assert len(transient_cells) == 8
assert all(len(adjacency[index]) == 3 for index in range(8))
assert all(len(options) == 2 and len(set(options)) == 2 for options in intermediate_options.values())

perfect_matchings = []
for image in permutations(transient_cells):
    if all(image[target] in adjacency[target] for target in range(8)):
        perfect_matchings.append(image)
assert len(perfect_matchings) == 49

distinct_intermediate_histogram = Counter()
support_union_histogram = Counter()
maximum_exposure_histogram = Counter()
balanced_orders_per_matching = []
balanced_legal_intermediates = Counter()

for image in perfect_matchings:
    balanced = 0
    for choices in product((0,1), repeat=8):
        intermediates = [
            intermediate_options[(target,image[target])][choices[target]]
            for target in range(8)
        ]
        distinct_intermediate_histogram[len(set(intermediates))] += 1
        supports = [
            {
                (row,column)
                for row in range(4)
                for column in range(4)
                if intermediate[row][column] != SOURCE[row][column]
            }
            for intermediate in intermediates
        ]
        exposures = Counter(cell for support in supports for cell in support)
        support_union_histogram[len(exposures)] += 1
        maximum_exposure_histogram[max(exposures.values())] += 1
        if len(exposures) == 16 and set(exposures.values()) == {2}:
            balanced += 1
            balanced_legal_intermediates[sum(intermediate in legal_matrices for intermediate in intermediates)] += 1
    balanced_orders_per_matching.append(balanced)

assert sum(distinct_intermediate_histogram.values()) == 49 * (2 ** 8) == 12544
assert distinct_intermediate_histogram == Counter({4:7,5:84,6:634,7:2804,8:9015})
assert support_union_histogram == Counter({14:164,15:2808,16:9572})
assert maximum_exposure_histogram == Counter({2:49,3:1553,4:7970,5:2972})
assert Counter(balanced_orders_per_matching) == Counter({1:49})
assert balanced_legal_intermediates == Counter({0:49})

print({
    "perfect_matchings": len(perfect_matchings),
    "ordered_distinct_buffer_batches": 12544,
    "distinct_intermediate_histogram": dict(sorted(distinct_intermediate_histogram.items())),
    "exposed_support_union_histogram": dict(sorted(support_union_histogram.items())),
    "maximum_cell_exposure_histogram": dict(sorted(maximum_exposure_histogram.items())),
    "perfectly_balanced_exposure_batches": 49,
    "balanced_orders_per_matching": 1,
    "balanced_batch_cell_exposure": 2,
    "balanced_batch_legal_intermediates": 0,
    "remaining_gap": "even the uniquely balanced order for each matching exposes eight matrix-illegal intermediate states, so geometric legality is not obtained by exposure balancing alone",
    "evidence_level": "exact_balanced_exposure_threshold_batch",
    "status": "passed",
})

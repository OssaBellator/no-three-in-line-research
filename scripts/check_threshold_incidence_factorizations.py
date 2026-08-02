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
                for row,column in removed: updated[row][column] -= 1
                for row,column in added: updated[row][column] += 1
                yield tuple(tuple(row) for row in updated)

layers = tuple(item for item in permutations(range(4)) if legal(item))
legal_matrices = {layer_matrix(tuple(layers[index] for index in indices)) for indices in combinations_with_replacement(range(len(layers)),4)}
minimum = min(distance(SOURCE,matrix) for matrix in legal_matrices)
targets = tuple(sorted(matrix for matrix in legal_matrices if distance(SOURCE,matrix) == minimum))
assert len(targets) == 8 and minimum == 6

adjacency = defaultdict(set)
for target_index,target in enumerate(targets):
    support = {(row,column) for row in range(4) for column in range(4) if target[row][column] != SOURCE[row][column]}
    for intermediate in swaps(SOURCE):
        for endpoint in swaps(intermediate):
            if endpoint != target: continue
            transient = {(row,column) for row in range(4) for column in range(4) if intermediate[row][column] != SOURCE[row][column]} - support
            if len(transient) == 1: adjacency[target_index].add(next(iter(transient)))

cells = tuple(sorted({cell for neighbours in adjacency.values() for cell in neighbours}))
matchings = []
for image in permutations(cells):
    if all(image[target] in adjacency[target] for target in range(8)):
        matchings.append(image)
assert len(matchings) == 49
edge_sets = [frozenset((target,image[target]) for target in range(8)) for image in matchings]

factorizations = []
for first in range(len(matchings)):
    for second in range(first+1,len(matchings)):
        if edge_sets[first] & edge_sets[second]: continue
        complement = frozenset((target,cell) for target in range(8) for cell in adjacency[target]) - edge_sets[first] - edge_sets[second]
        if len(complement) != 8: continue
        try: third = edge_sets.index(complement)
        except ValueError: continue
        if second < third: factorizations.append((first,second,third))

assert len(factorizations) == 44
assert len({pair for triple in factorizations for pair in combinations(triple,2)}) == 132
all_edges = frozenset((target,cell) for target in range(8) for cell in adjacency[target])
for triple in factorizations:
    union = frozenset().union(*(edge_sets[index] for index in triple))
    assert union == all_edges and len(union) == 24
    for target in range(8):
        assert {matchings[index][target] for index in triple} == adjacency[target]

participation = Counter(index for triple in factorizations for index in triple)
assert Counter(participation.values()) == Counter({1:10,2:21,4:16,8:2})
ordered_factorizations = len(factorizations) * 6
ordered_swap_schedules = ordered_factorizations * (2 ** 24)
assert ordered_factorizations == 264
assert ordered_swap_schedules == 4429185024

print({
    "perfect_matchings": len(matchings),
    "edge_disjoint_matching_pairs": 132,
    "unordered_three_batch_factorizations": len(factorizations),
    "ordered_three_batch_factorizations": ordered_factorizations,
    "incidences_covered_once_per_factorization": 24,
    "each_target_uses_all_three_buffers_once": True,
    "matching_factorization_participation_histogram": dict(sorted(Counter(participation.values()).items())),
    "fully_ordered_swap_schedules": ordered_swap_schedules,
    "remaining_gap": "balanced incidence exposure does not make any intermediate geometric state legal",
    "evidence_level": "exact_threshold_incidence_factorization",
    "status": "passed",
})

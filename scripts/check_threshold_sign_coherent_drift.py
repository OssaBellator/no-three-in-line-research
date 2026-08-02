#!/usr/bin/env python3
from itertools import combinations, combinations_with_replacement, permutations

SOURCE = ((2,1,1,0),(0,2,1,1),(1,0,2,1),(1,1,0,2))

def collinear(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1]) == (b[1]-a[1])*(c[0]-a[0])

def legal(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points,3))

def layer_matrix(layers):
    return tuple(tuple(sum(layer[row] == column for layer in layers) for column in range(4)) for row in range(4))

def distance(first, second):
    return sum(abs(first[r][c]-second[r][c]) for r in range(4) for c in range(4))

layers = tuple(item for item in permutations(range(4)) if legal(item))
legal_matrices = {
    layer_matrix(tuple(layers[index] for index in indices))
    for indices in combinations_with_replacement(range(len(layers)), 4)
}
minimum = min(distance(SOURCE, matrix) for matrix in legal_matrices)
targets = tuple(sorted(matrix for matrix in legal_matrices if distance(SOURCE, matrix) == minimum))
assert len(targets) == 8 and minimum == 6

deltas = tuple(
    tuple(target[r][c]-SOURCE[r][c] for r in range(4) for c in range(4))
    for target in targets
)
for cell in range(16):
    values = {delta[cell] for delta in deltas}
    assert not ({-1, 1} <= values)

subset_records = {}
for size in range(1, len(targets)+1):
    l1_values = set()
    zero_count = 0
    for subset in combinations(range(len(targets)), size):
        aggregate = tuple(sum(deltas[index][cell] for index in subset) for cell in range(16))
        l1 = sum(abs(value) for value in aggregate)
        l1_values.add(l1)
        zero_count += int(all(value == 0 for value in aggregate))
    assert l1_values == {6*size}
    assert zero_count == 0
    subset_records[size] = {"aggregate_l1": 6*size, "zero_aggregate_subsets": 0}

aggregate_all = tuple(sum(delta[cell] for delta in deltas) for cell in range(16))
assert aggregate_all == (-5,-1,1,5,5,-5,-1,1,1,5,-5,-1,-1,1,5,-5)

print({
    "nearest_targets": 8,
    "single_target_l1": 6,
    "cellwise_sign_coherent": True,
    "nonempty_subset_l1_rule": "6*subset_size",
    "nonempty_zero_drift_subsets": 0,
    "all_target_aggregate": aggregate_all,
    "distinct_transient_assignment_changes_endpoint_drift": False,
    "subset_audit": subset_records,
    "remaining_gap": "buffer distinctness removes transient reuse but cannot neutralize the sign-coherent target displacement; a geometric batch needs an additional inverse or compensating source operation",
    "evidence_level": "exact_sign_coherent_threshold_drift",
    "status": "passed",
})

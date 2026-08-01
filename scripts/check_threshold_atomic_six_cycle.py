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
    result = [[0]*4 for _ in range(4)]
    for layer in layers:
        for row,column in enumerate(layer):
            result[row][column] += 1
    return tuple(tuple(row) for row in result)

def distance(left,right):
    return sum(abs(left[r][c]-right[r][c]) for r in range(4) for c in range(4))

def elementary_swaps(matrix):
    for r1,r2 in combinations(range(4),2):
        for c1,c2 in combinations(range(4),2):
            for orientation in (0,1):
                removed = ((r1,c1),(r2,c2)) if orientation == 0 else ((r1,c2),(r2,c1))
                added = ((r1,c2),(r2,c1)) if orientation == 0 else ((r1,c1),(r2,c2))
                if not all(matrix[r][c] > 0 for r,c in removed):
                    continue
                candidate = [list(row) for row in matrix]
                for r,c in removed:
                    candidate[r][c] -= 1
                for r,c in added:
                    candidate[r][c] += 1
                yield tuple(tuple(row) for row in candidate), removed, added

permutations_all = tuple(permutations(range(4)))
legal_layers = tuple(item for item in permutations_all if legal(item))
legal_matrices = {}
for indices in combinations_with_replacement(range(len(legal_layers)),4):
    matrix = layer_matrix(tuple(legal_layers[index] for index in indices))
    legal_matrices[matrix] = legal_matrices.get(matrix,0)+1
assert len(legal_layers)==18 and len(legal_matrices)==4475
minimum = min(distance(SOURCE,matrix) for matrix in legal_matrices)
targets = tuple(sorted(matrix for matrix in legal_matrices if distance(SOURCE,matrix)==minimum))
assert minimum==6 and len(targets)==8

cycle_supports=[]
for target in targets:
    negative=[]; positive=[]
    for row in range(4):
        for column in range(4):
            delta = target[row][column]-SOURCE[row][column]
            assert delta in (-1,0,1)
            if delta==-1: negative.append((row,column))
            elif delta==1: positive.append((row,column))
    assert len(negative)==len(positive)==3
    rows={row for row,_ in negative+positive}; columns={column for _,column in negative+positive}
    assert len(rows)==len(columns)==3
    assert set(Counter(row for row,_ in negative+positive).values())=={2}
    assert set(Counter(column for _,column in negative+positive).values())=={2}
    cycle_supports.append((tuple(negative),tuple(positive)))
assert len(set(cycle_supports))==8

paths=[]
for intermediate,removed_a,added_a in elementary_swaps(SOURCE):
    for target,removed_b,added_b in elementary_swaps(intermediate):
        if target in targets:
            paths.append((target,intermediate,removed_a,added_a,removed_b,added_b))
assert len(paths)==48
assert Counter(record[0] for record in paths)==Counter({target:6 for target in targets})
assert len({record[1] for record in paths})==20
assert all(record[1] not in legal_matrices for record in paths)

print({
    "nearest_legal_targets": len(targets),
    "atomic_support_cells_per_target": 6,
    "atomic_support_rows_per_target": 3,
    "atomic_support_columns_per_target": 3,
    "support_graph": "simple alternating C6",
    "distinct_atomic_support_cycles": len(set(cycle_supports)),
    "ordered_two_swap_factorizations": len(paths),
    "factorizations_per_target": 6,
    "legal_visible_intermediates": 0,
    "conclusion": "the missing geometric source operation is exactly a simultaneous six-cell alternating cycle on three rows and three columns",
    "remaining_gap": "no actual prime-patching edit realizes this C6 atom while preserving exposed no-three legality",
    "evidence_level": "exact_atomic_threshold_c6_support",
    "status": "passed",
})

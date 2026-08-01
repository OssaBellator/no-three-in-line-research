#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations

M = (
    (2, 1, 1, 0),
    (0, 2, 1, 1),
    (1, 0, 2, 1),
    (1, 1, 0, 2),
)
PERMS = tuple(permutations(range(4)))
SELECTED = (
    (0, 2, 3, 1),
    (0, 1, 2, 3),
    (1, 3, 2, 0),
    (2, 1, 0, 3),
)


def subtract(matrix, permutation):
    rows = [list(row) for row in matrix]
    for source, action in enumerate(permutation):
        if rows[source][action] == 0:
            return None
        rows[source][action] -= 1
    return tuple(tuple(row) for row in rows)


@lru_cache(None)
def decompositions(matrix, steps):
    if steps == 0:
        return ((),) if all(value == 0 for row in matrix for value in row) else ()
    out = []
    for permutation in PERMS:
        next_matrix = subtract(matrix, permutation)
        if next_matrix is None:
            continue
        for tail in decompositions(next_matrix, steps - 1):
            out.append((permutation,) + tail)
    return tuple(out)


def collinear_triples(points):
    out = []
    for a, b, c in combinations(points, 3):
        if (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0]):
            out.append((a, b, c))
    return tuple(out)


def legal_permutation(permutation):
    return not collinear_triples(tuple((source, action) for source, action in enumerate(permutation)))


def rank(rows):
    work = [list(map(Fraction, row)) for row in rows]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(pivot_row, len(work)) if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        value = work[pivot_row][column]
        work[pivot_row] = [entry / value for entry in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][index] - factor * work[pivot_row][index]
                for index in range(len(work[0]))
            ]
        pivot_row += 1
    return pivot_row


all_decompositions = decompositions(M, 4)
assert len(all_decompositions) == 84
legal_permutations = tuple(permutation for permutation in PERMS if legal_permutation(permutation))
assert len(legal_permutations) == 18
illegal_layer_distribution = Counter(
    sum(not legal_permutation(permutation) for permutation in decomposition)
    for decomposition in all_decompositions
)
assert illegal_layer_distribution == Counter({2: 48, 3: 12, 4: 24})
assert not any(all(legal_permutation(permutation) for permutation in decomposition) for decomposition in all_decompositions)
assert min(illegal_layer_distribution) == 2

selected_triples = tuple(collinear_triples(tuple((source, action) for source, action in enumerate(permutation))) for permutation in SELECTED)
assert tuple(len(value) for value in selected_triples) == (0, 4, 0, 1)

# The aligned quotient consists of the constant row, fixed-point counts, and cyclic-forward counts.
def observables(permutation):
    return (
        sum(action == source for source, action in enumerate(permutation)),
        sum(action == (source + 1) % 4 for source, action in enumerate(permutation)),
    )

vectors = tuple(observables(permutation) for permutation in SELECTED)
Q = (
    (1, 1, 1, 1),
    tuple(vector[0] for vector in vectors),
    tuple(vector[1] for vector in vectors),
)
base_rank = rank(Q)
assert base_rank == 3

positive_cells = tuple((source, action) for source in range(4) for action in range(4) if M[source][action])
cell_normal = {
    cell: tuple(int(permutation[cell[0]] == cell[1]) for permutation in SELECTED)
    for cell in positive_cells
}
geometric_triples = []
for triple in combinations(positive_cells, 3):
    if not collinear_triples(triple):
        continue
    normal = tuple(sum(cell_normal[cell][layer] for cell in triple) for layer in range(4))
    controlled = rank(Q + (normal,)) == base_rank
    geometric_triples.append((triple, normal, controlled))

assert len(geometric_triples) == 15
assert sum(controlled for _, _, controlled in geometric_triples) == 11
hidden = tuple((triple, normal) for triple, normal, controlled in geometric_triples if not controlled)
assert len(hidden) == 4
assert (((0, 0), (1, 1), (3, 3)), (1, 3, 0, 2)) in hidden

print({
    "permutation_layers": len(PERMS),
    "geometrically_legal_permutation_layers": len(legal_permutations),
    "ordered_decompositions": len(all_decompositions),
    "all_legal_decompositions": 0,
    "illegal_layers_per_decomposition": dict(sorted(illegal_layer_distribution.items())),
    "selected_layer_collinear_triples": [len(value) for value in selected_triples],
    "positive_cell_collinear_triples": len(geometric_triples),
    "controlled_geometric_normals": 11,
    "hidden_geometric_normals": 4,
    "hidden_witness": hidden[0],
    "conclusion": "the aligned conservative matrix has no four-slot decomposition into no-three-in-line permutation layers",
    "evidence_level": "source_matrix_geometric_obstruction",
    "status": "passed",
})

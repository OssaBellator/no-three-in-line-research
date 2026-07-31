#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product
from math import gcd

M = (
    (2, 1, 1, 0),
    (0, 2, 1, 1),
    (1, 0, 2, 1),
    (1, 1, 0, 2),
)
PERMS = tuple(permutations(range(4)))


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


def observables(permutation):
    fixed = sum(action == source for source, action in enumerate(permutation))
    cyclic_forward = sum(action == (source + 1) % 4 for source, action in enumerate(permutation))
    return fixed, cyclic_forward


def discrepancy(decomposition):
    vectors = tuple(observables(permutation) for permutation in decomposition)
    mean = tuple(Fraction(sum(vector[j] for vector in vectors), 4) for j in range(2))
    prefix = [Fraction(0), Fraction(0)]
    maximum = Fraction(0)
    for vector in vectors:
        for j in range(2):
            prefix[j] += vector[j] - mean[j]
        maximum = max(maximum, abs(prefix[0]), abs(prefix[1]))
    return maximum, vectors, mean


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
            work[row] = [work[row][j] - factor * work[pivot_row][j] for j in range(len(work[0]))]
        pivot_row += 1
    return pivot_row


def canonical_primitive(vector):
    divisor = 0
    for value in vector:
        divisor = gcd(divisor, abs(value))
    return divisor == 1 and next(value for value in vector if value) > 0


all_decompositions = decompositions(M, 4)
assert len(all_decompositions) == 84
best_discrepancy = min(discrepancy(decomposition)[0] for decomposition in all_decompositions)
optimal = tuple(decomposition for decomposition in all_decompositions if discrepancy(decomposition)[0] == best_discrepancy)
assert best_discrepancy == 1
assert len(optimal) == 16
selected = min(optimal)
selected_vectors = discrepancy(selected)[1]
assert selected == (
    (0, 2, 3, 1),
    (0, 1, 2, 3),
    (1, 3, 2, 0),
    (2, 1, 0, 3),
)
assert selected_vectors == ((1, 2), (4, 0), (1, 2), (2, 0))

# Constant total plus the two exact layer observables define the aligned quotient row space.
Q = (
    (1, 1, 1, 1),
    tuple(vector[0] for vector in selected_vectors),
    tuple(vector[1] for vector in selected_vectors),
)
base_rank = rank(Q)
assert base_rank == 3
controlled = []
hidden = []
for vector in product(range(-3, 4), repeat=4):
    if vector == (0, 0, 0, 0) or not canonical_primitive(vector):
        continue
    if rank(Q + (vector,)) == base_rank:
        controlled.append(vector)
    else:
        hidden.append(vector)
assert len(controlled) == 145
assert len(hidden) == 975

print({
    "source_matrix": M,
    "ordered_decompositions": len(all_decompositions),
    "derived_observables": ["fixed points", "cyclic-forward edges"],
    "minimum_prefix_discrepancy": str(best_discrepancy),
    "optimal_decompositions": len(optimal),
    "selected_decomposition": selected,
    "selected_observable_vectors": selected_vectors,
    "aligned_quotient_rank_including_constant": base_rank,
    "primitive_normals_checked": len(controlled) + len(hidden),
    "controlled_normals": len(controlled),
    "hidden_normals": len(hidden),
    "remaining_gap": "repository does not list the actual residual threshold normals",
    "evidence_level": "source_aligned_benchmark",
    "status": "passed",
})

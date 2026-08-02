#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations


SOURCE = (
    (2,1,1,0),
    (0,2,1,1),
    (1,0,2,1),
    (1,1,0,2),
)
IDENTITY = (0,1,2,3)
WITNESS_LAYERS = (
    (2,3,0,1),
    (2,1,3,0),
    (1,3,2,0),
    (1,2,0,3),
    (0,2,3,1),
)


def collinear(first, second, third):
    return (
        (second[0]-first[0])*(third[1]-first[1])
        == (second[1]-first[1])*(third[0]-first[0])
    )


def legal_layer(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points, 3))


def matrix_of(permutation_layers):
    matrix = [[0] * 4 for _ in range(4)]
    for permutation in permutation_layers:
        for row, column in enumerate(permutation):
            matrix[row][column] += 1
    return tuple(tuple(row) for row in matrix)


ALL_LAYERS = tuple(permutations(range(4)))
LEGAL_LAYERS = tuple(layer for layer in ALL_LAYERS if legal_layer(layer))
assert len(ALL_LAYERS) == 24
assert len(LEGAL_LAYERS) == 18
assert IDENTITY not in LEGAL_LAYERS
assert all(layer in LEGAL_LAYERS for layer in WITNESS_LAYERS)

LEGAL_MATRICES = {
    matrix_of(LEGAL_LAYERS[index] for index in indices)
    for indices in combinations_with_replacement(range(len(LEGAL_LAYERS)), 4)
}
assert len(LEGAL_MATRICES) == 4475

HIDDEN = matrix_of((IDENTITY,) * 4)
WITNESSES = tuple(matrix_of((layer,) * 4) for layer in WITNESS_LAYERS)

all_decompositions = {}
for indices in combinations_with_replacement(range(len(ALL_LAYERS)), 4):
    matrix = matrix_of(ALL_LAYERS[index] for index in indices)
    all_decompositions.setdefault(matrix, []).append(indices)

assert all_decompositions[HIDDEN] == [(
    ALL_LAYERS.index(IDENTITY),
) * 4]
for matrix, layer in zip(WITNESSES, WITNESS_LAYERS):
    assert all_decompositions[matrix] == [(
        ALL_LAYERS.index(layer),
    ) * 4]

primitive_total = matrix_of((IDENTITY,) * 3 + WITNESS_LAYERS)
assert primitive_total == tuple(
    tuple(2 * entry for entry in row) for row in SOURCE
)

types = (IDENTITY,) + WITNESS_LAYERS
admissible_submultisets = []
for indices in combinations_with_replacement(range(len(types)), 4):
    counts = Counter(indices)
    if counts[0] > 3:
        continue
    if any(counts[index] > 1 for index in range(1, len(types))):
        continue
    identity_count = counts[0]
    legal = matrix_of(types[index] for index in indices) in LEGAL_MATRICES
    admissible_submultisets.append((identity_count, legal))

assert len(admissible_submultisets) == 30
assert Counter(admissible_submultisets) == Counter({
    (0, True): 5,
    (1, False): 10,
    (2, False): 10,
    (3, False): 5,
})

orders = set(permutations((IDENTITY,) * 3 + WITNESS_LAYERS))
assert len(orders) == 6720
window_histogram = Counter()
for order in orders:
    legal_windows = 0
    for start in range(8):
        window = tuple(order[(start + offset) % 8] for offset in range(4))
        legal = matrix_of(window) in LEGAL_MATRICES
        assert legal == all(layer != IDENTITY for layer in window)
        legal_windows += legal
    window_histogram[legal_windows] += 1

assert window_histogram == Counter({0: 3840, 1: 1920, 2: 960})
assert max(window_histogram) == 2

print({
    "all_permutation_layers": len(ALL_LAYERS),
    "legal_permutation_layers": len(LEGAL_LAYERS),
    "legal_four_layer_matrices": len(LEGAL_MATRICES),
    "exposed_witness_decompositions_unique": True,
    "hidden_decomposition": "four identity layers, uniquely",
    "primitive_identity": "3*I+P1+P2+P3+P4+P5=2*S",
    "admissible_four_layer_submultisets": 30,
    "legal_submultisets": 5,
    "legal_iff_no_identity_layer": True,
    "cyclic_primitive_orders": len(orders),
    "legal_window_histogram": dict(sorted(window_histogram.items())),
    "maximum_legal_cyclic_four_windows": 2,
    "remaining_gap": "a geometric hidden phase must avoid exposing every four-layer window containing an identity layer",
    "evidence_level": "exact_minimal_mixture_layer_obstruction",
    "status": "passed",
})

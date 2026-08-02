#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, permutations

SOURCE = (
    (2, 1, 1, 0),
    (0, 2, 1, 1),
    (1, 0, 2, 1),
    (1, 1, 0, 2),
)
PHI = (
    (-1, 0, 0, 0),
    (1, 0, 1, 0),
    (0, 1, 0, 0),
    (0, 0, 1, -1),
)
IDENTITY = (0, 1, 2, 3)
EXPOSED = (
    (2, 3, 0, 1),
    (2, 1, 3, 0),
    (1, 3, 2, 0),
    (1, 2, 0, 3),
    (0, 2, 3, 1),
)


def collinear(first, second, third):
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def legal(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points, 3))


def score(permutation):
    return sum(PHI[row][permutation[row]] for row in range(4))


def layer_vector(permutation):
    return tuple(
        int(permutation[row] == column)
        for row in range(4)
        for column in range(4)
    )


all_layers = tuple(permutations(range(4)))
legal_layers = tuple(layer for layer in all_layers if legal(layer))
illegal_layers = tuple(layer for layer in all_layers if not legal(layer))
assert len(legal_layers) == 18
assert len(illegal_layers) == 6
assert Counter(score(layer) for layer in legal_layers) == Counter({0: 9, 1: 8, 2: 1})
assert Counter(score(layer) for layer in illegal_layers) == Counter({-2: 1, -1: 2, 1: 1, 2: 1, 3: 1})
assert score(IDENTITY) == -2
assert [layer for layer in illegal_layers if score(layer) == -2] == [IDENTITY]
assert all(legal(layer) and score(layer) == 0 for layer in EXPOSED)

target = tuple(8 * SOURCE[row][column] for row in range(4) for column in range(4))
target_score = sum(
    PHI[row][column] * target[4 * row + column]
    for row in range(4)
    for column in range(4)
)
assert target_score == -24

minimum_illegal_layers = (-target_score + 1) // 2
assert minimum_illegal_layers == 12

identity_vector = layer_vector(IDENTITY)
residual = tuple(target[index] - 12 * identity_vector[index] for index in range(16))
assert min(residual) >= 0
zero_legal = tuple(layer for layer in legal_layers if score(layer) == 0)
zero_vectors = tuple(layer_vector(layer) for layer in zero_legal)

solutions = []


def enumerate_counts(index, remaining, layers_left, counts):
    if index == len(zero_vectors) - 1:
        count = layers_left
        vector = zero_vectors[index]
        if all(count * vector[cell] == remaining[cell] for cell in range(16)):
            solutions.append(tuple(counts + [count]))
        return

    vector = zero_vectors[index]
    maximum = layers_left
    for cell, value in enumerate(vector):
        if value:
            maximum = min(maximum, remaining[cell])
    for count in range(maximum + 1):
        next_remaining = tuple(
            remaining[cell] - count * vector[cell]
            for cell in range(16)
        )
        if min(next_remaining) < 0:
            break
        enumerate_counts(index + 1, next_remaining, layers_left - count, counts + [count])


enumerate_counts(0, residual, 20, [])
assert len(solutions) == 1
unique_counts = solutions[0]
observed = {
    layer: count
    for layer, count in zip(zero_legal, unique_counts)
    if count
}
assert observed == {layer: 4 for layer in EXPOSED}

aggregate = [0] * 16
for layer, count in [(IDENTITY, 12), *[(layer, 4) for layer in EXPOSED]]:
    vector = layer_vector(layer)
    for cell in range(16):
        aggregate[cell] += count * vector[cell]
assert tuple(aggregate) == target

print({
    "permutation_layers": len(all_layers),
    "legal_layers": len(legal_layers),
    "illegal_layers": len(illegal_layers),
    "target_layers": 32,
    "target_score": target_score,
    "minimum_illegal_layers": minimum_illegal_layers,
    "unique_minimum_illegal_type": IDENTITY,
    "minimum_decomposition_unique": True,
    "minimum_decomposition": {
        "identity_layers": 12,
        "legal_exposed_layers": {str(layer): 4 for layer in EXPOSED},
    },
    "remaining_gap": "the unique optimal algebraic decomposition still contains twelve collinear identity layers and has no geometric hidden-state execution",
    "evidence_level": "exact_unique_minimum_illegal_layer_decomposition",
    "status": "passed",
})

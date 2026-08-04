#!/usr/bin/env python3
from itertools import combinations, combinations_with_replacement, permutations
from math import comb

IDENTITY = (0, 1, 2, 3)
LEGAL_TYPES = (
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


def legal_permutation(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points, 3))


def matrix(layers):
    result = [[0] * 4 for _ in range(4)]
    for layer in layers:
        for row, column in enumerate(layer):
            result[row][column] += 1
    return tuple(tuple(row) for row in result)


all_legal_layers = tuple(
    permutation for permutation in permutations(range(4))
    if legal_permutation(permutation)
)
assert len(all_legal_layers) == 18
legal_catalogue = {
    matrix(all_legal_layers[index] for index in indices)
    for indices in combinations_with_replacement(range(len(all_legal_layers)), 4)
}
assert len(legal_catalogue) == 4475

symbols = (IDENTITY,) + LEGAL_TYPES
with_identity = 0
without_identity = 0
legal_with_identity = 0
legal_without_identity = 0
for indices in combinations_with_replacement(range(len(symbols)), 4):
    is_legal = matrix(symbols[index] for index in indices) in legal_catalogue
    if 0 in indices:
        with_identity += 1
        legal_with_identity += is_legal
    else:
        without_identity += 1
        legal_without_identity += is_legal
assert (with_identity, legal_with_identity) == (56, 0)
assert (without_identity, legal_without_identity) == (70, 70)


def identity_free_windows(length, identity_positions):
    identity_positions = set(identity_positions)
    return sum(
        all((start + offset) % length not in identity_positions for offset in range(4))
        for start in range(length)
    )


small_census = {}
for multiple in range(1, 4):
    length = 8 * multiple
    identities = 3 * multiple
    histogram = {}
    maximum = -1
    maximizers = 0
    for positions in combinations(range(length), identities):
        value = identity_free_windows(length, positions)
        histogram[value] = histogram.get(value, 0) + 1
        if value > maximum:
            maximum = value
            maximizers = 1
        elif value == maximum:
            maximizers += 1
    assert sum(histogram.values()) == comb(length, identities)
    assert maximum == 5 * multiple - 3
    assert maximizers == length
    small_census[multiple] = {
        "identity_position_sets": comb(length, identities),
        "maximum_legal_windows": maximum,
        "maximizers": maximizers,
        "histogram": histogram,
    }

# A contiguous block of 3K identities contaminates exactly 3K+3 cyclic starts,
# leaving 8K-(3K+3)=5K-3 identity-free windows. The edge-isoperimetric inequality
# on a cycle says every nonempty set S with |S|<=N-4 has |S+{0,1,2,3}|>=|S|+3,
# so no arrangement can do better.
for multiple in range(1, 33):
    length = 8 * multiple
    positions = tuple(range(3 * multiple))
    assert identity_free_windows(length, positions) == 5 * multiple - 3

print({
    "four_layer_type_multisets": 126,
    "with_identity": 56,
    "legal_with_identity": 0,
    "without_identity": 70,
    "legal_without_identity": 70,
    "small_multiple_census": small_census,
    "exact_maximum_for_K_batches": "5K-3",
    "exact_illegal_minimum_for_K_batches": "3K+3",
    "asymptotic_legal_window_density": "5/8",
    "status": "passed",
})

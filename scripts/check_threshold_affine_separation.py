#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations

SOURCE = ((2,1,1,0),(0,2,1,1),(1,0,2,1),(1,1,0,2))
WEIGHT = ((0,0,0,1),(1,-1,0,0),(0,0,-1,0),(1,0,1,0))

def collinear(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) == (b[1]-a[1])*(c[0]-a[0])

def legal(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points, 3))

def layer_matrix(layers):
    return tuple(
        tuple(sum(layer[row] == column for layer in layers) for column in range(4))
        for row in range(4)
    )

def score(matrix):
    return sum(WEIGHT[row][column] * matrix[row][column]
               for row in range(4) for column in range(4))

def distance(first, second):
    return sum(abs(first[row][column] - second[row][column])
               for row in range(4) for column in range(4))

layers = tuple(item for item in permutations(range(4)) if legal(item))
assert len(layers) == 18
layer_scores = Counter(sum(WEIGHT[row][layer[row]] for row in range(4)) for layer in layers)
assert layer_scores == Counter({0: 9, 1: 8, 2: 1})

legal_matrices = {
    layer_matrix(tuple(layers[index] for index in indices))
    for indices in combinations_with_replacement(range(len(layers)), 4)
}
assert len(legal_matrices) == 4475
score_distribution = Counter(map(score, legal_matrices))
assert score_distribution == Counter({0:495,1:956,2:1193,3:1012,4:590,5:176,6:44,7:8,8:1})
assert score(SOURCE) == -3
assert min(map(score, legal_matrices)) == 0

minimum_distance = min(distance(SOURCE, matrix) for matrix in legal_matrices)
nearest = tuple(matrix for matrix in legal_matrices if distance(SOURCE, matrix) == minimum_distance)
assert minimum_distance == 6 and len(nearest) == 8
assert {score(matrix) for matrix in nearest} == {0}

for length in range(1, 20):
    source_total = length * score(SOURCE)
    least_legal_total = length * min(map(score, legal_matrices))
    assert source_total < least_legal_total

print({
    "legal_permutation_layers": len(layers),
    "legal_four_layer_matrices": len(legal_matrices),
    "separator": "Phi(M)=M03+M10-M11-M22+M30+M32",
    "source_score": score(SOURCE),
    "legal_score_distribution": dict(sorted(score_distribution.items())),
    "nearest_target_count": len(nearest),
    "nearest_target_score": 0,
    "finite_legal_endpoint_compensation": False,
    "status": "passed",
})

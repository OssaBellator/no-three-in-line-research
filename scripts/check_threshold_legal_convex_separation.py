#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations

SOURCE = ((2,1,1,0),(0,2,1,1),(1,0,2,1),(1,1,0,2))
WEIGHT = ((-1,0,0,0),(1,0,1,0),(0,1,0,0),(0,0,1,-1))


def collinear(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1]) == (b[1]-a[1])*(c[0]-a[0])


def legal(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points,3))


def layer_matrix(layers):
    return tuple(tuple(sum(layer[row] == column for layer in layers) for column in range(4)) for row in range(4))


def score(matrix):
    return sum(WEIGHT[row][column] * matrix[row][column] for row in range(4) for column in range(4))


def distance(first, second):
    return sum(abs(first[row][column]-second[row][column]) for row in range(4) for column in range(4))


layers = tuple(permutation for permutation in permutations(range(4)) if legal(permutation))
assert len(layers) == 18
legal_matrices = tuple(sorted({
    layer_matrix(tuple(layers[index] for index in indices))
    for indices in combinations_with_replacement(range(len(layers)), 4)
}))
assert len(legal_matrices) == 4475

source_score = score(SOURCE)
score_histogram = Counter(score(matrix) for matrix in legal_matrices)
assert source_score == -3
assert min(score_histogram) == 0
assert max(score_histogram) == 8
assert score_histogram == Counter({0:495,1:956,2:1193,3:1012,4:590,5:176,6:44,7:8,8:1})

minimum_distance = min(distance(SOURCE, matrix) for matrix in legal_matrices)
nearest = tuple(matrix for matrix in legal_matrices if distance(SOURCE, matrix) == minimum_distance)
assert minimum_distance == 6
assert len(nearest) == 8
assert {score(matrix) for matrix in nearest} == {0}

# Any convex combination or finite average of legal matrices has score at least
# zero, while SOURCE has score -3. Thus SOURCE is outside the legal convex hull
# and no endpoint-only legal compensating batch can average back to SOURCE.
for matrix in legal_matrices:
    assert score(matrix) >= 0

print({
    "legal_permutation_layers": len(layers),
    "legal_four_layer_matrices": len(legal_matrices),
    "separator_weight": WEIGHT,
    "source_score": source_score,
    "legal_score_histogram": dict(sorted(score_histogram.items())),
    "minimum_legal_score": min(score_histogram),
    "nearest_legal_targets": len(nearest),
    "nearest_target_l1_distance": minimum_distance,
    "nearest_target_scores": [0] * len(nearest),
    "source_in_convex_hull_of_legal_matrices": False,
    "finite_legal_endpoint_compensating_batch_exists": False,
    "remaining_gap": "endpoint compensation requires a source state outside the present legal four-layer catalogue, a hidden-state primitive, or a different matrix model",
    "evidence_level": "exact_legal_convex_separation_obstruction",
    "status": "passed",
})

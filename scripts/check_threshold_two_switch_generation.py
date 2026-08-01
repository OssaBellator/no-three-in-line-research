#!/usr/bin/env python3
from collections import deque
from itertools import combinations, permutations, product

SOURCE = (
    (2, 1, 1, 0),
    (0, 2, 1, 1),
    (1, 0, 2, 1),
    (1, 1, 0, 2),
)


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def legal_layer(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points, 3))


def matrix(layers):
    return tuple(
        tuple(sum(permutation[row] == column for permutation in layers) for column in range(4))
        for row in range(4)
    )


def distance(first, second):
    return sum(abs(first[row][column] - second[row][column]) for row in range(4) for column in range(4))


def switches(current):
    for first_row, second_row in combinations(range(4), 2):
        for first_column, second_column in combinations(range(4), 2):
            for sign in (1, -1):
                candidate = [list(row) for row in current]
                delta = {
                    (first_row, first_column): sign,
                    (second_row, second_column): sign,
                    (first_row, second_column): -sign,
                    (second_row, first_column): -sign,
                }
                for (row, column), value in delta.items():
                    candidate[row][column] += value
                if min(entry for row in candidate for entry in row) >= 0:
                    yield tuple(tuple(row) for row in candidate), (
                        first_row,
                        second_row,
                        first_column,
                        second_column,
                        sign,
                    )


legal_permutations = tuple(permutation for permutation in permutations(range(4)) if legal_layer(permutation))
legal_matrices = {matrix(layers) for layers in product(legal_permutations, repeat=4)}
minimum_distance = min(distance(SOURCE, candidate) for candidate in legal_matrices)
targets = tuple(sorted(candidate for candidate in legal_matrices if distance(SOURCE, candidate) == minimum_distance))

assert len(legal_permutations) == 18
assert len(legal_matrices) == 4475
assert minimum_distance == 6
assert len(targets) == 8

paths = []
for target in targets:
    queue = deque([SOURCE])
    previous = {SOURCE: None}
    move = {}
    while queue:
        current = queue.popleft()
        if current == target:
            break
        for candidate, switch in switches(current):
            if distance(SOURCE, candidate) <= 6 and candidate not in previous:
                previous[candidate] = current
                move[candidate] = switch
                queue.append(candidate)
    path = []
    current = target
    while current != SOURCE:
        path.append(move[current])
        current = previous[current]
    path.reverse()
    assert len(path) == 2
    paths.append(tuple(path))

canonical_target = targets[0]
canonical_path = paths[0]
assert canonical_path == ((0, 2, 0, 2, -1), (0, 3, 2, 3, -1))
assert all(sum(row) == 4 for row in canonical_target)
assert all(sum(canonical_target[row][column] for row in range(4)) == 4 for column in range(4))

print(
    {
        "legal_permutation_layers": len(legal_permutations),
        "legal_degree_four_matrices": len(legal_matrices),
        "nearest_legal_targets": len(targets),
        "entrywise_l1_distance": minimum_distance,
        "minimum_nonnegative_two_by_two_switches": 2,
        "all_nearest_targets_generated_in_two_switches": True,
        "canonical_target": canonical_target,
        "canonical_switch_path": canonical_path,
        "source_margins_preserved_at_every_step": True,
        "remaining_gap": "the conservative two-by-two switch is an exact matrix-kernel operation but is not yet identified with a geometric prime-patching source move",
        "status": "passed",
    }
)

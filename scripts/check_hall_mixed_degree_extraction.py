#!/usr/bin/env python3
from itertools import combinations

RESERVE = 6
DEGREES = (1, 2, 2)
COLLISION_MAXIMUM_DEGREE = sum(degree * (degree - 1) for degree in DEGREES)
assert COLLISION_MAXIMUM_DEGREE == 4
SUFFICIENT_RESIDUAL = RESERVE * (COLLISION_MAXIMUM_DEGREE + 1) - COLLISION_MAXIMUM_DEGREE
assert SUFFICIENT_RESIDUAL == 26
assert (SUFFICIENT_RESIDUAL + COLLISION_MAXIMUM_DEGREE) // (COLLISION_MAXIMUM_DEGREE + 1) == 6
assert (25 + COLLISION_MAXIMUM_DEGREE) // (COLLISION_MAXIMUM_DEGREE + 1) == 5


def cycle_edges(step):
    return frozenset(tuple(sorted((vertex, (vertex + step) % 5))) for vertex in range(5))

cycles = (cycle_edges(1), cycle_edges(2))
assert all(len(cycle) == 5 for cycle in cycles)
assert len(frozenset().union(*cycles)) == len(tuple(combinations(range(5), 2))) == 10
for cycle in cycles:
    degree = {vertex: 0 for vertex in range(5)}
    for first, second in cycle:
        degree[first] += 1
        degree[second] += 1
    assert set(degree.values()) == {2}

# Realize each collision-cycle edge by a unique opposite-side resource incident
# with its two endpoints.  Every resource then has forbidden-family degree two.
def forbidden_family_from_cycle(cycle):
    incidence = []
    for neighbour, (first, second) in enumerate(sorted(cycle)):
        incidence.append((first, neighbour))
        incidence.append((second, neighbour))
    return tuple(incidence)

for cycle in cycles:
    family = forbidden_family_from_cycle(cycle)
    left_degree = {vertex: 0 for vertex in range(5)}
    right_degree = {vertex: 0 for vertex in range(5)}
    for left, right in family:
        left_degree[left] += 1
        right_degree[right] += 1
    assert set(left_degree.values()) == {2}
    assert set(right_degree.values()) == {2}

print({
    "forbidden_family_maximum_degrees": DEGREES,
    "matching_shaped_families": 1,
    "degree_two_families": 2,
    "collision_graph_maximum_degree": COLLISION_MAXIMUM_DEGREE,
    "sharp_residual_resources_for_six_good_vertices": SUFFICIENT_RESIDUAL,
    "sharp_total_resources_before_selected_pair": SUFFICIENT_RESIDUAL + 2,
    "sharpness_obstruction_at_25": "five disjoint K5 collision components",
    "k5_decomposition": "two Hamilton cycles supplied by the two degree-two families",
    "remaining_gap": "the actual conditional host must verify that the partner restriction is matching-shaped and the source and host-defect restrictions have degree at most two",
    "evidence_level": "sharp_mixed_degree_hall_extraction_threshold",
    "status": "passed",
})

#!/usr/bin/env python3
from itertools import combinations

RESERVE = 6
FAMILIES = 3
MAX_COLLISION_DEGREE = 2 * FAMILIES
SUFFICIENT_RESIDUAL = RESERVE * (MAX_COLLISION_DEGREE + 1) - MAX_COLLISION_DEGREE
assert SUFFICIENT_RESIDUAL == 36
assert (SUFFICIENT_RESIDUAL + 6) // 7 == 6
assert (35 + 6) // 7 == 5

def cycle_edges(step):
    return frozenset(tuple(sorted((vertex, (vertex + step) % 7))) for vertex in range(7))

cycles = (cycle_edges(1), cycle_edges(2), cycle_edges(3))
assert all(len(cycle) == 7 for cycle in cycles)
assert len(frozenset().union(*cycles)) == len(tuple(combinations(range(7), 2))) == 21
for cycle in cycles:
    degree = {vertex: 0 for vertex in range(7)}
    for first, second in cycle:
        degree[first] += 1
        degree[second] += 1
    assert set(degree.values()) == {2}

def greedy_bound(vertices, maximum_degree):
    return (vertices + maximum_degree) // (maximum_degree + 1)

assert greedy_bound(36, 6) == 6
assert greedy_bound(35, 6) == 5

print({
    "forbidden_families": FAMILIES,
    "maximum_degree_per_family": 2,
    "collision_graph_maximum_degree": MAX_COLLISION_DEGREE,
    "sharp_residual_resources_for_six_good_vertices": SUFFICIENT_RESIDUAL,
    "sharp_total_resources_before_selected_pair": SUFFICIENT_RESIDUAL + 2,
    "sharpness_obstruction_at_35": "five disjoint K7 collision components",
    "k7_decomposition": "three Hamilton cycles",
    "remaining_gap": "the asymptotic conditional host must verify degree at most two for all three restricted forbidden families",
    "evidence_level": "sharp_degree_two_hall_extraction_threshold",
    "status": "passed",
})

#!/usr/bin/env python3
from math import comb


def reserve_threshold(families: int, maximum_degree: int, reserve: int) -> int:
    return reserve * (1 + 2 * families * comb(maximum_degree, 2))


# Collision-graph independence bound used in PP3cwi.
assert reserve_threshold(3, 2, 6) == 42
assert reserve_threshold(2, 2, 4) == 20
assert reserve_threshold(3, 1, 6) == 6

# Two endpoint resources are consumed before the residual reserve is extracted.
residual_resources = reserve_threshold(3, 2, 6)
total_resources = residual_resources + 2
assert residual_resources == 42
assert total_resources == 44

# Exact bad-vertex formula from PP3cwh.
for resources in range(8, 65):
    for bad_left in range(resources - 1):
        for bad_right in range(resources - 1):
            enough_good = (
                resources - 2 - bad_left >= 6
                and resources - 2 - bad_right >= 6
            )
            formula = resources >= 8 + max(bad_left, bad_right)
            assert enough_good == formula

print({
    "forbidden_families": 3,
    "maximum_family_degree": 2,
    "target_matching_shaped_reserve": 6,
    "collision_graph_residual_threshold": residual_resources,
    "total_resources_before_local_pair": total_resources,
    "bad_vertex_formula": "m >= 8 + max(b_L,b_R)",
    "conclusion": "degree-two restrictions admit a six-resource matching-shaped core from forty-two residual resources",
    "remaining_gap": "the asymptotic conditional host has not been shown to satisfy the required degree or bad-vertex bounds",
    "evidence_level": "quantitative_hall_reserve_extraction",
    "status": "passed",
})

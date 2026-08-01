#!/usr/bin/env python3
from math import comb


def threshold(delta: int) -> int:
    return 4 * (1 + 4 * comb(delta, 2))

records = []
for delta in range(1, 17):
    b = comb(delta, 2)
    n = threshold(delta)
    left_collision_edges = 2 * n * b
    left_independence_lower_numerator = n * n
    left_independence_lower_denominator = n + 2 * left_collision_edges
    assert left_independence_lower_numerator >= 4 * left_independence_lower_denominator

    right_collision_edges = 8 * b
    right_independence_lower_numerator = n * n
    right_independence_lower_denominator = n + 2 * right_collision_edges
    assert right_independence_lower_numerator >= 4 * right_independence_lower_denominator

    records.append(
        {
            "maximum_forbidden_degree": delta,
            "residual_pool_threshold": n,
            "left_collision_edge_bound": left_collision_edges,
            "right_collision_edge_bound_after_four_left_choices": right_collision_edges,
        }
    )

assert threshold(1) == 4
assert threshold(2) == 20
assert threshold(3) == 52

print(
    {
        "reserve_extraction_rule": "N >= 4*(1+4*C(Delta,2))",
        "forbidden_families": 2,
        "extracted_left_resources": 4,
        "extracted_right_resources": 4,
        "restricted_family_shape": "each forbidden family is a partial matching",
        "degree_two_residual_threshold": threshold(2),
        "host_resources_before_two decoder choices": threshold(2) + 2,
        "checked_degree_range": [1, 16],
        "consequence": "combine the extracted K4,4 reserve with the exact two-matching exclusion lemma to survive one additional blocked cell",
        "remaining_gap": "the asymptotic PP3 host has not yet supplied a uniform maximum forbidden degree and residual-pool lower bound meeting this criterion",
        "status": "passed",
    }
)

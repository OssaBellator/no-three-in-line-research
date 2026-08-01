#!/usr/bin/env python3
from math import comb


def threshold(families: int, reserve: int, delta: int) -> int:
    return reserve * (1 + 2 * families * comb(delta, 2))

records = []
for families in range(1, 6):
    for reserve in range(2, 9):
        for delta in range(1, 9):
            b = comb(delta, 2)
            n = threshold(families, reserve, delta)
            left_collision_edges = families * n * b
            assert n * n >= reserve * (n + 2 * left_collision_edges)
            right_collision_edges = families * reserve * b
            assert n * n >= reserve * (n + 2 * right_collision_edges)
            records.append((families, reserve, delta, n))

assert threshold(2, 4, 2) == 20
assert threshold(3, 6, 2) == 42

# A Hall obstruction on six residual resources would require one of these
# complete forbidden rectangles. Three partial matchings plus one edge cannot
# contain any of them.
dimensions = tuple((size, 7 - size) for size in range(1, 7))
assert dimensions == ((1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1))
for rows, columns in dimensions:
    if max(rows, columns) > 4:
        continue
    rows_requiring_four = rows if columns == 4 else 0
    columns_requiring_four = columns if rows == 4 else 0
    assert rows_requiring_four > 1 or columns_requiring_four > 1

# Sharpness on five residual resources: K3,3 is three cyclic matchings.
matchings = (
    frozenset((row, row) for row in range(3)),
    frozenset((row, (row + 1) % 3) for row in range(3)),
    frozenset((row, (row + 2) % 3) for row in range(3)),
)
assert len(frozenset().union(*matchings)) == 9

print({
    "reserve_extraction_rule": "N >= r*(1+2*k*C(Delta,2))",
    "checked_parameter_triples": len(records),
    "three_family_degree_two_residual_threshold": threshold(3, 6, 2),
    "host_resources_before_two_selected_choices": threshold(3, 6, 2) + 2,
    "sharp_residual_completion_threshold": 6,
    "sharp_five_resource_obstruction": "K_3,3 decomposed into three cyclic matchings",
    "consequence": "extract six resources where partner, source, and host-defect restrictions are partial matchings, then survive one additional blocked cell",
    "remaining_gap": "the asymptotic host has not supplied the required degree-two bounds and forty-two-resource residual pool",
    "status": "passed",
})

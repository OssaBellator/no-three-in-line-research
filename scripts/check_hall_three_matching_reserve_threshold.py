#!/usr/bin/env python3


def obstruction_dimensions(n):
    return tuple((size, n - size + 1) for size in range(1, n + 1))


def coverable_by_three_matchings_plus_edge(rows, columns):
    # Three matchings give degree at most three at every vertex. One extra edge
    # can raise the degree of at most one row and one column from three to four.
    if max(rows, columns) > 4:
        return False
    rows_needing_extra = rows if columns == 4 else 0
    columns_needing_extra = columns if rows == 4 else 0
    return rows_needing_extra <= 1 and columns_needing_extra <= 1

# A Hall failure in the complement of the forbidden graph requires a complete
# forbidden rectangle K_{s,n-s+1}.
dimensions_six = obstruction_dimensions(6)
assert dimensions_six == ((1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1))
assert all(not coverable_by_three_matchings_plus_edge(*dims) for dims in dimensions_six)

# Sharpness at five residual resources: K_{3,3} is the union of three matchings
# and leaves three selected rows with only the other two columns as neighbours.
matchings = (
    frozenset((row, row) for row in range(3)),
    frozenset((row, (row + 1) % 3) for row in range(3)),
    frozenset((row, (row + 2) % 3) for row in range(3)),
)
forbidden_k33 = frozenset().union(*matchings)
assert len(forbidden_k33) == 9
assert all(sum((row, column) in forbidden_k33 for column in range(3)) == 3 for row in range(3))
assert coverable_by_three_matchings_plus_edge(3, 3)

print({
    "forbidden_families": 3,
    "additional_arbitrary_exclusions": 1,
    "minimum_residual_resources_per_side": 6,
    "minimum_total_resources_after_two_selected": 8,
    "hall_rectangle_dimensions_checked_at_six": dimensions_six,
    "sharp_five_resource_obstruction": "K_3,3 decomposed into three perfect matchings",
    "sufficient_condition": "partner, source, and host-defect restrictions are partial matchings on six unused resources per side",
    "remaining_gap": "the asymptotic conditional host must supply six unused resources and matching-shaped restrictions after real conditioning",
    "evidence_level": "sharp_three_matching_hall_reserve_threshold",
    "status": "passed",
})

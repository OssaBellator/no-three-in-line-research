#!/usr/bin/env python3
"""Verify the exact bad-vertex reserve formula for a six-resource Hall core."""

GOOD_RESOURCES_REQUIRED = 6
SELECTED_RESOURCES_PER_SIDE = 2

records = []
for total_resources in range(8, 65):
    unused = total_resources - SELECTED_RESOURCES_PER_SIDE
    for bad_left in range(unused + 1):
        for bad_right in range(unused + 1):
            good_left = unused - bad_left
            good_right = unused - bad_right
            sufficient = (
                good_left >= GOOD_RESOURCES_REQUIRED
                and good_right >= GOOD_RESOURCES_REQUIRED
            )
            formula = total_resources >= 8 + max(bad_left, bad_right)
            assert sufficient == formula
            records.append(
                (total_resources, bad_left, bad_right, good_left, good_right, sufficient)
            )

assert next(record for record in records if record[:3] == (8, 0, 0))[-1]
assert not next(record for record in records if record[:3] == (8, 1, 0))[-1]
assert next(record for record in records if record[:3] == (10, 2, 2))[-1]

print({
    "selected_resources_per_side": SELECTED_RESOURCES_PER_SIDE,
    "good_residual_resources_required": GOOD_RESOURCES_REQUIRED,
    "reserve_formula": "m >= 8 + max(b_L,b_R)",
    "eight_resource_case": "requires zero bad vertices on both sides",
    "ten_resource_case": "tolerates two bad vertices on each side",
    "parameter_cases_checked": len(records),
    "remaining_gap": "the asymptotic host has not been shown to bound the real bad-vertex sets",
    "evidence_level": "exact_six_resource_bad_vertex_reserve_formula",
    "status": "passed",
})

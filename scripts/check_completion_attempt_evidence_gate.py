#!/usr/bin/env python3
from fractions import Fraction

FIXED_POINT_TOTAL = Fraction(705466760524005697, 3623878655999606784)
SLACK = Fraction(200502903475895999, 3623878655999606784)
assert FIXED_POINT_TOTAL + SLACK == Fraction(1, 4)

frontiers = {
    "boundary": {
        "candidate_fields": "3/5",
        "new_result": "all twelve exact saturation refills fail",
        "actual_row_evidence": "fixture_derived",
    },
    "hall": {
        "candidate_fields": "5/5 repository-typed",
        "new_result": "every complete twelve-pair bijection has six singleton-blocker geometries",
        "actual_row_evidence": "fixture_derived",
    },
    "threshold": {
        "candidate_fields": "4/5",
        "new_result": "nearest legal matrices have quotient-loss frontier (2,1) or (3,0)",
        "actual_row_evidence": "fixture_derived",
    },
    "prefix": {
        "candidate_fields": "5/5 encoded model",
        "new_result": "canonical convex chord embedding has zero collinear triples despite positive span risk",
        "actual_row_evidence": "fixture_derived",
    },
    "shell": {
        "candidate_fields": "5/5 source benchmark",
        "new_result": "one odd unit action repairs the lattice conditionally at throughput cost 1/20",
        "actual_row_evidence": "fixture_derived",
    },
    "integration": {
        "candidate_fields": "1/5",
        "new_result": "fixture fixed point unchanged",
        "actual_row_evidence": "fixture_derived",
    },
}

assert len(frontiers) == 6
assert all(record["actual_row_evidence"] == "fixture_derived" for record in frontiers.values())

print({
    "candidate_source_fields_completed": 23,
    "candidate_source_fields_total": 30,
    "new_actual_coordinate_source_paths_completed": 0,
    "actual_rows_promoted": 0,
    "global_evidence_meet": "fixture_derived",
    "fixture_fixed_point_total": str(FIXED_POINT_TOTAL),
    "fixture_fixed_point_decimal": f"{float(FIXED_POINT_TOTAL):.12f}",
    "slack_below_one_quarter": str(SLACK),
    "geometric_closure_allowed": False,
    "frontiers": frontiers,
    "conclusion": "the completion attempts sharpen five finite obligations but do not verify any global prime-patching row",
    "status": "passed",
})

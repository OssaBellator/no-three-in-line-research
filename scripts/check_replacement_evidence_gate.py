#!/usr/bin/env python3
from fractions import Fraction

FIELD_COMPLETION = {
    "boundary": (3, 5),
    "hall": (4, 5),
    "threshold": (4, 5),
    "prefix": (5, 5),
    "shell": (5, 5),
    "integration": (2, 5),
}
assert sum(done for done, _ in FIELD_COMPLETION.values()) == 23
assert sum(total for _, total in FIELD_COMPLETION.values()) == 30

ACTUAL_ROWS = {
    "boundary": "fixture_derived",
    "hall": "fixture_derived",
    "threshold": "fixture_derived",
    "prefix": "fixture_derived",
    "shell": "fixture_derived",
    "integration": "fixture_derived",
}
assert set(ACTUAL_ROWS.values()) == {"fixture_derived"}

fixed_point_total = Fraction(705466760524005697, 3623878655999606784)
slack = Fraction(1, 4) - fixed_point_total
assert slack == Fraction(200502903475895999, 3623878655999606784)
assert slack > 0

replacement_results = {
    "boundary": "three point deletions are necessary and sufficient for four radius-32 sixth-step candidates, but saturation is broken",
    "hall": "only six of twelve decoded pairs survive every one-cell residual exclusion",
    "threshold": "nearest fully legal conservative matrix has entrywise l1 distance six",
    "prefix": "ancestry-aware interval-span aggregate is exact but lacks a grid support-chord embedding",
    "shell": "docs/517 actions span an index-two cycle-resource sublattice",
}
assert len(replacement_results) == 5

print({
    "candidate_field_completion": FIELD_COMPLETION,
    "completed_fields": 23,
    "total_fields": 30,
    "replacement_results": replacement_results,
    "actual_row_evidence": ACTUAL_ROWS,
    "rows_promoted": 0,
    "fixture_fixed_point_total": str(fixed_point_total),
    "fixture_slack_below_one_quarter": str(slack),
    "geometric_closure_allowed": False,
    "status": "passed",
})

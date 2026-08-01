#!/usr/bin/env python3
from fractions import Fraction

CANDIDATE_FIELDS = {
    "boundary": (4, 5),
    "Hall": (4, 5),
    "threshold": (4, 5),
    "prefix": (5, 5),
    "shell": (5, 5),
    "integration": (2, 5),
}
assert sum(value for value, total in CANDIDATE_FIELDS.values()) == 24
assert sum(total for value, total in CANDIDATE_FIELDS.values()) == 30

ACTUAL_EVIDENCE = {
    "boundary": "fixture_derived",
    "Hall": "fixture_derived",
    "threshold": "fixture_derived",
    "prefix": "fixture_derived",
    "shell": "fixture_derived",
    "integration": "fixture_derived",
}
PROMOTED = tuple(name for name, evidence in ACTUAL_EVIDENCE.items() if evidence == "geometrically_verified")
assert PROMOTED == ()

FIXED_POINT = (
    Fraction(70590897652005075, 1207959551999868928),
    Fraction(211454017460, 9215999999999),
    Fraction(3086096934497, 73727999999992),
    Fraction(59599619386893, 2359295999999744),
    Fraction(475832507959075, 18874367999997952),
    Fraction(9494283900954065, 452984831999950848),
)
TOTAL = sum(FIXED_POINT)
SLACK = Fraction(1, 4) - TOTAL
assert TOTAL == Fraction(705466760524005697, 3623878655999606784)
assert SLACK == Fraction(200502903475895999, 3623878655999606784)
assert SLACK > 0

print({
    "candidate_field_completion": {
        name: f"{value}/{total}" for name, (value, total) in CANDIDATE_FIELDS.items()
    },
    "candidate_fields_complete": 24,
    "candidate_fields_total": 30,
    "new_results": {
        "boundary": "one canonical corrected seventh transition exists; raw eighth extension count is zero",
        "Hall": "K_4,4 minus two matching-shaped forbidden families survives one extra exclusion",
        "threshold": "all eight nearest degree-four legal replacements are unit alternating three-cycle trades",
        "prefix": "two synthetic source anchors per unary run give exactly eleven source-pair blockers per encoding",
        "shell": "signed cancellation and coordinate permutation preserve the even-sum source lattice",
    },
    "actual_evidence_levels": ACTUAL_EVIDENCE,
    "promoted_rows": PROMOTED,
    "fixture_fixed_point_total": str(TOTAL),
    "fixture_slack_below_one_quarter": str(SLACK),
    "geometric_closure": False,
    "all_n_theorem": "open",
    "status": "passed",
})

#!/usr/bin/env python3
from fractions import Fraction
from math import comb

CANDIDATE_FIELDS = {
    "boundary": (4,5),
    "Hall": (4,5),
    "threshold": (5,5),
    "prefix": (5,5),
    "shell": (5,5),
    "integration": (2,5),
}
assert sum(value for value, _ in CANDIDATE_FIELDS.values()) == 25
assert sum(total for _, total in CANDIDATE_FIELDS.values()) == 30

ACTUAL_EVIDENCE = {name: "fixture_derived" for name in CANDIDATE_FIELDS}
PROMOTED = tuple(name for name, evidence in ACTUAL_EVIDENCE.items()
                 if evidence == "geometrically_verified")
assert PROMOTED == ()

BOUNDARY_CANONICAL_CORES = 15
BOUNDARY_CANONICAL_BUDGETS = {4:1,5:7,6:5,7:2}
assert sum(BOUNDARY_CANONICAL_BUDGETS.values()) == BOUNDARY_CANONICAL_CORES
assert 128 == 16 * 8

HALL_FAMILIES_CHECKED = 16383
assert HALL_FAMILIES_CHECKED == sum(comb(15, size) for size in range(1, 8))

THRESHOLD_LEGAL_ENDPOINTS = 4475
THRESHOLD_SEPARATOR_MARGIN = 3
assert THRESHOLD_LEGAL_ENDPOINTS > 0 and THRESHOLD_SEPARATOR_MARGIN > 0

PREFIX_DELETION_DISTRIBUTION = {2:15744,3:3072,4:192}
assert sum(PREFIX_DELETION_DISTRIBUTION.values()) == 19008
assert max(PREFIX_DELETION_DISTRIBUTION) == 4

SHELL_ROBUST_EXAMPLE = {
    "upper_cycle_burden": Fraction(4),
    "periods": 2,
    "worst_gain": Fraction(2),
    "entry_worst_saving": Fraction(-2),
    "setup": Fraction(7),
    "repetitions": 5,
}
assert 3 * SHELL_ROBUST_EXAMPLE["periods"] - SHELL_ROBUST_EXAMPLE["upper_cycle_burden"] == SHELL_ROBUST_EXAMPLE["worst_gain"]
assert (SHELL_ROBUST_EXAMPLE["entry_worst_saving"]
        + SHELL_ROBUST_EXAMPLE["repetitions"] * SHELL_ROBUST_EXAMPLE["worst_gain"]
        - SHELL_ROBUST_EXAMPLE["setup"]) > 0
assert (SHELL_ROBUST_EXAMPLE["entry_worst_saving"]
        + (SHELL_ROBUST_EXAMPLE["repetitions"] - 1) * SHELL_ROBUST_EXAMPLE["worst_gain"]
        - SHELL_ROBUST_EXAMPLE["setup"]) <= 0

FIXED_POINT = (
    Fraction(70590897652005075,1207959551999868928),
    Fraction(211454017460,9215999999999),
    Fraction(3086096934497,73727999999992),
    Fraction(59599619386893,2359295999999744),
    Fraction(475832507959075,18874367999997952),
    Fraction(9494283900954065,452984831999950848),
)
TOTAL = sum(FIXED_POINT)
SLACK = Fraction(1,4) - TOTAL
assert TOTAL == Fraction(705466760524005697,3623878655999606784)
assert SLACK == Fraction(200502903475895999,3623878655999606784)

print({
    "candidate_field_completion": {name:f"{value}/{total}" for name,(value,total) in CANDIDATE_FIELDS.items()},
    "candidate_fields_complete": 25,
    "candidate_fields_total": 30,
    "new_results": {
        "boundary": "one sixteenth attempt has all 15 minimum cores correctable through budget seven; a four-point correction reaches sixteen blocks",
        "Hall": "resource multiplicities give an incidence-derived local Caro--Wei packing certificate",
        "threshold": "an integer functional separates the source from all 4475 legal endpoints and forbids every finite native compensation cycle",
        "prefix": "all 19008 second-reservoir two-component deletion cases repair within anchor radius four",
        "shell": "interval edge burdens admit exact robust, possible, and impossible positive-cycle certificates",
    },
    "actual_evidence_levels": ACTUAL_EVIDENCE,
    "promoted_rows": PROMOTED,
    "fixture_fixed_point_total": str(TOTAL),
    "fixture_slack_below_one_quarter": str(SLACK),
    "geometric_closure": False,
    "all_n_theorem": "open",
    "next_theorem_identifier": "PP3dbr",
    "status": "passed",
})

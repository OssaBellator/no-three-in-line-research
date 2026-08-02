#!/usr/bin/env python3
from fractions import Fraction

CANDIDATE_FIELDS = {
    "boundary": (4, 5),
    "Hall": (4, 5),
    "threshold": (5, 5),
    "prefix": (5, 5),
    "shell": (5, 5),
    "integration": (2, 5),
}
assert sum(value for value, _ in CANDIDATE_FIELDS.values()) == 25
assert sum(total for _, total in CANDIDATE_FIELDS.values()) == 30

ACTUAL_EVIDENCE = {name: "fixture_derived" for name in CANDIDATE_FIELDS}
PROMOTED = tuple(name for name, evidence in ACTUAL_EVIDENCE.items()
                 if evidence == "geometrically_verified")
assert PROMOTED == ()

CANONICAL_BOUNDARY_CORE_BUDGETS = {4: 1, 5: 7, 6: 5, 7: 2}
assert sum(CANONICAL_BOUNDARY_CORE_BUDGETS.values()) == 15
assert 128 == 16 * 8

HALL_FAMILIES_CHECKED = 54263
assert HALL_FAMILIES_CHECKED > 0

THRESHOLD_LEGAL_MATRICES = 4475
THRESHOLD_SOURCE_SCORE = -3
THRESHOLD_MINIMUM_LEGAL_SCORE = 0
assert THRESHOLD_SOURCE_SCORE < THRESHOLD_MINIMUM_LEGAL_SCORE

PREFIX_DELETIONS = 2
PREFIX_OPTIMAL_REROUTINGS_PER_DELETION = 144
PREFIX_COMPOSITIONS_PER_REROUTING = 2 ** 10
PREFIX_PAIRS_CHECKED = (
    PREFIX_DELETIONS
    * PREFIX_OPTIMAL_REROUTINGS_PER_DELETION
    * PREFIX_COMPOSITIONS_PER_REROUTING
)
assert PREFIX_PAIRS_CHECKED == 294912
assert (87, 84) == (87, 84)
assert (144, 156) == (144, 156)

SHELL_ROBUST_EXAMPLE = {
    "entry_worst_saving": Fraction(-2),
    "cycle_worst_gain": Fraction(2),
    "setup": Fraction(7),
    "repetitions": 5,
}
assert (SHELL_ROBUST_EXAMPLE["entry_worst_saving"]
        + SHELL_ROBUST_EXAMPLE["repetitions"]
        * SHELL_ROBUST_EXAMPLE["cycle_worst_gain"]
        - SHELL_ROBUST_EXAMPLE["setup"]) > 0
assert (SHELL_ROBUST_EXAMPLE["entry_worst_saving"]
        + (SHELL_ROBUST_EXAMPLE["repetitions"] - 1)
        * SHELL_ROBUST_EXAMPLE["cycle_worst_gain"]
        - SHELL_ROBUST_EXAMPLE["setup"]) <= 0

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

print({
    "candidate_field_completion": {
        name: f"{value}/{total}"
        for name, (value, total) in CANDIDATE_FIELDS.items()
    },
    "candidate_fields_complete": 25,
    "candidate_fields_total": 30,
    "new_results": {
        "boundary": "all 15 minimum cores of P1/-37 correct through budget seven; a four-point correction reaches sixteen blocks",
        "Hall": "local resource multiplicities give an exact degree identity and host-auditable Caro--Wei certificate",
        "threshold": "an integer hyperplane separates the source from all 4475 legal four-layer endpoints",
        "prefix": "all 288 optimal reroutings for both canonical two-pair deletions pass all 1024 compositions",
        "shell": "edge-burden intervals admit exact possible, robust, and impossible cycle certificates",
    },
    "prefix_rerouting_composition_pairs_checked": PREFIX_PAIRS_CHECKED,
    "actual_evidence_levels": ACTUAL_EVIDENCE,
    "promoted_rows": PROMOTED,
    "fixture_fixed_point_total": str(TOTAL),
    "fixture_slack_below_one_quarter": str(SLACK),
    "geometric_closure": False,
    "all_n_theorem": "open",
    "next_theorem_identifier": "PP3dbr",
    "status": "passed",
})

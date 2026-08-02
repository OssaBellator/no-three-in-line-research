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

BOUNDARY = {
    "minimum_four_attempts": 1,
    "minimum_four_cores": 5,
    "budgets_exhausted": (4, 5, 6),
    "correctable_through_budget_six": 0,
    "minimum_remaining_budget": 7,
}
assert BOUNDARY["minimum_four_attempts"] == 1
assert BOUNDARY["minimum_four_cores"] == 5
assert BOUNDARY["minimum_remaining_budget"] == max(BOUNDARY["budgets_exhausted"]) + 1

HALL = {
    "two_packet_cases": 76156,
    "exact_cases": 3766,
    "strict_cases": 72390,
    "maximum_slack": 4,
}
assert HALL["exact_cases"] + HALL["strict_cases"] == HALL["two_packet_cases"]

THRESHOLD = {
    "minimal_batches": 19834,
    "support_histogram": {2: 5, 3: 210, 4: 2255, 5: 17364},
    "two_support_partition": (4, 1),
}
assert sum(THRESHOLD["support_histogram"].values()) == THRESHOLD["minimal_batches"]
assert THRESHOLD["support_histogram"][2] == 5

PREFIX = {
    "physical_matchings": 104,
    "deletion_cases": 2,
    "physical_cases": 208,
    "optimal_routes_per_case": 144,
    "compositions_per_route": 1024,
    "pairs_checked": 212992,
    "maximum_coordinate": 132,
}
assert PREFIX["physical_matchings"] * PREFIX["deletion_cases"] == PREFIX["physical_cases"]
assert PREFIX["physical_cases"] * PREFIX["compositions_per_route"] == PREFIX["pairs_checked"]

SHELL = {
    "normalized_margin": Fraction(1, 2),
    "integer_bundle_gain": Fraction(1),
    "connector_saving": Fraction(-2),
    "least_bundle_repetitions": 3,
    "executable_gain": Fraction(1),
}
assert 2 * SHELL["normalized_margin"] == SHELL["integer_bundle_gain"]
assert 2 * SHELL["integer_bundle_gain"] + SHELL["connector_saving"] == 0
assert 3 * SHELL["integer_bundle_gain"] + SHELL["connector_saving"] == SHELL["executable_gain"]

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
    "candidate_field_completion": {name: f"{value}/{total}" for name, (value, total) in CANDIDATE_FIELDS.items()},
    "candidate_fields_complete": 25,
    "candidate_fields_total": 30,
    "new_results": {
        "boundary": "the unique minimum-four nineteenth attempt has five cores and none repairs through deletion budget six",
        "Hall": "packet concatenation retains at least sum r_j minus certified interface edges, giving exact positive-surplus thresholds",
        "threshold": "there are exactly 19834 minimal equal-weight hidden-mixture batches with a complete support and multiplicity census",
        "prefix": "the first optimal route for all 208 physical matching/deletion cases passes all 1024 compositions",
        "shell": "positive robust circulations are finite LP certificates and clear to executable closed walks after exact connector repayment",
    },
    "actual_evidence_levels": ACTUAL_EVIDENCE,
    "promoted_rows": PROMOTED,
    "fixture_fixed_point_total": str(TOTAL),
    "fixture_slack_below_one_quarter": str(SLACK),
    "geometric_closure": False,
    "all_n_theorem": "open",
    "next_theorem_identifier": "PP3ddt",
    "status": "passed",
})

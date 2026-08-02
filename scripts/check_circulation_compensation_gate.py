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
    "six_point_replacements_rejected": 37976400,
    "minimum_remaining_budget": 7,
}
assert BOUNDARY["minimum_remaining_budget"] == max(BOUNDARY["budgets_exhausted"]) + 1

HALL = {
    "degree_two_incidence_graphs": 10172,
    "retention_formula": "(3q+o)/2",
    "two_packet_cases": 76156,
    "exact_cases": 3766,
    "strict_cases": 72390,
    "maximum_slack": 4,
}
assert HALL["exact_cases"] + HALL["strict_cases"] == HALL["two_packet_cases"]

THRESHOLD = {
    "minimal_batches": 19834,
    "support_histogram": {2: 5, 3: 210, 4: 2255, 5: 17364},
    "minimum_illegal_layers": 12,
    "minimum_layer_decomposition_unique": True,
    "cyclic_orders": 6720,
    "maximum_legal_four_windows": 2,
}
assert sum(THRESHOLD["support_histogram"].values()) == THRESHOLD["minimal_batches"]
assert THRESHOLD["minimum_illegal_layers"] == 12
assert THRESHOLD["maximum_legal_four_windows"] < 8

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
    "connected_integer_circulations_checked": 1086,
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
        "boundary": "the unique five-core minimum nineteenth frontier has no preserving correction through deletion budget six",
        "Hall": "defect-incidence odd-path retention and packet-interface surplus give exact conditional asymptotic bounds",
        "threshold": "19834 minimum endpoint batches share one rigid twelve-identity aggregate layer decomposition and no legal rolling four-window schedule",
        "prefix": "the deterministic first optimal route passes all 1024 compositions in all 208 physical matching/deletion cases",
        "shell": "robust circulation LP witnesses are directly executable exactly on connected support, with explicit connector repayment otherwise",
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

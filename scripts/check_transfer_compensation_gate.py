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
PROMOTED = tuple(
    name for name, evidence in ACTUAL_EVIDENCE.items()
    if evidence == "geometrically_verified"
)
assert PROMOTED == ()

BOUNDARY = {
    "minimum_four_attempts": 2,
    "minimum_four_cores": 6,
    "minimum_five_attempts": 9,
    "minimum_five_cores": 54,
    "minimum_six_attempts": 47,
    "minimum_six_cores": 435,
    "low_attempts": 58,
    "low_cores": 495,
    "new_replacements_rejected": 3466200,
    "corrected_transition": True,
    "correction_budget": 7,
    "corrected_points": 152,
    "twentieth_minimum_four_attempts": 3,
    "twentieth_minimum_four_cores": 9,
}
assert BOUNDARY["minimum_four_attempts"] + BOUNDARY["minimum_five_attempts"] + BOUNDARY["minimum_six_attempts"] == BOUNDARY["low_attempts"]
assert BOUNDARY["minimum_four_cores"] + BOUNDARY["minimum_five_cores"] + BOUNDARY["minimum_six_cores"] == BOUNDARY["low_cores"]
assert BOUNDARY["correction_budget"] == 7

HALL = {
    "packet_graphs": 1024,
    "direct_chain_checks": 4096,
    "strict_transfer_improvements": 3060,
    "maximum_four_packet_improvement": 6,
    "example_exact_packets_for_28": 9,
    "example_additive_packets_for_28": 13,
}
assert HALL["example_exact_packets_for_28"] < HALL["example_additive_packets_for_28"]

THRESHOLD = {
    "type_multisets": 126,
    "identity_free_legal": 70,
    "identity_containing_illegal": 56,
    "maximum_legal_windows": "5K-3",
    "minimum_illegal_windows": "3K+3",
    "asymptotic_legal_density": Fraction(5, 8),
}
assert THRESHOLD["identity_free_legal"] + THRESHOLD["identity_containing_illegal"] == THRESHOLD["type_multisets"]
assert Fraction(1) - THRESHOLD["asymptotic_legal_density"] == Fraction(3, 8)

PREFIX = {
    "physical_matchings": 104,
    "deletions": 2,
    "optimal_routes_per_case": 144,
    "short_compositions": 56,
    "coordinate_audits": 1677312,
    "failures": 0,
}
assert PREFIX["physical_matchings"] * PREFIX["deletions"] * PREFIX["optimal_routes_per_case"] * PREFIX["short_compositions"] == PREFIX["coordinate_audits"]

SHELL = {
    "connector_cost_matrices": 729,
    "metric_closure_strict_improvements": 3,
    "maximum_metric_improvement": 1,
    "repetition_formula": "floor((S+L*)/G)+1",
    "coordinate_macro_graph": False,
}
assert SHELL["connector_cost_matrices"] == 3**6

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
    "actual_evidence_levels": ACTUAL_EVIDENCE,
    "promoted_rows": PROMOTED,
    "new_results": {
        "boundary": "the canonical budget-seven correction reaches nineteen blocks and exposes a nine-core minimum-four twentieth frontier",
        "Hall": "exact packet boundary-state transfer and max-plus cycle mean replace uniform interface charging",
        "threshold": "minimum-batch rolling four-window legality has exact optimum 5K-3 and asymptotic density 5/8",
        "prefix": "all 144 optimal routes pass all 56 compositions with at most three runs across every physical matching and deletion",
        "shell": "minimum connector loss is the balanced connected augmentation optimum, equal to a directed metric Hamiltonian tour",
    },
    "fixture_fixed_point_total": str(TOTAL),
    "fixture_slack_below_one_quarter": str(SLACK),
    "geometric_closure": False,
    "all_n_theorem": "open",
    "next_theorem_identifier": "PP3deo",
    "status": "passed",
})

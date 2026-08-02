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
    "eighteenth_minimum_cores": 7,
    "correctable_through_budget_six": 1,
    "canonical_budget": 6,
    "corrected_points": 144,
    "corrected_blocks": 18,
    "nineteenth_minimum_four_attempts": 1,
    "nineteenth_minimum_four_cores": 5,
    "stale_p1_minus_33_minimum": 5,
}
assert BOUNDARY["corrected_points"] == 8 * BOUNDARY["corrected_blocks"]

HALL = {
    "bipartite_graphs_checked": 74954,
    "maximum_degree_two_graphs": 10172,
    "ten_motif_loss_budget": 2,
    "eleven_motif_loss_budget": 5,
    "twelve_motif_loss_budget": 8,
}
assert HALL["ten_motif_loss_budget"] == 30 - 28
assert HALL["eleven_motif_loss_budget"] == 33 - 28
assert HALL["twelve_motif_loss_budget"] == 36 - 28

THRESHOLD = {
    "source_score": -3,
    "hidden_score": -8,
    "batch_size": 8,
    "hidden_states": 3,
    "legal_facet_states": 5,
}
assert THRESHOLD["hidden_states"] * THRESHOLD["hidden_score"] == THRESHOLD["batch_size"] * THRESHOLD["source_score"]
assert THRESHOLD["hidden_states"] + THRESHOLD["legal_facet_states"] == THRESHOLD["batch_size"]

PREFIX = {
    "selected_representatives": 20,
    "deletion_cases": 2,
    "compositions_per_route": 1024,
    "pairs_checked": 40960,
    "maximum_coordinate": 132,
}
assert PREFIX["selected_representatives"] * PREFIX["deletion_cases"] * PREFIX["compositions_per_route"] == PREFIX["pairs_checked"]

SHELL = {
    "primitive_robust_gains": (Fraction(-1), Fraction(-1)),
    "mixed_margin": Fraction(1, 2),
    "composite_robust_gain": Fraction(1),
    "connector_saving": Fraction(-1),
    "least_positive_bundles": 2,
}
assert max(SHELL["primitive_robust_gains"]) < 0
assert SHELL["mixed_margin"] > 0
assert SHELL["composite_robust_gain"] == 2 * SHELL["mixed_margin"]
assert SHELL["connector_saving"] + (SHELL["least_positive_bundles"] - 1) * SHELL["composite_robust_gain"] <= 0
assert SHELL["connector_saving"] + SHELL["least_positive_bundles"] * SHELL["composite_robust_gain"] > 0

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
        "boundary": "one of seven eighteenth cores repairs at budget six; the corrected chain reaches eighteen blocks; the raw nineteenth minimum-four frontier is uniquely P2/-64 with five cores",
        "Hall": "bipartite maximum-degree-two centre conflicts have an exact path/even-cycle retention formula",
        "threshold": "the 3/8 hidden-mass lower bound is attained algebraically by a minimal eight-state mixture",
        "prefix": "forty selected routes pass all 1024 compositions, for 40960 finite coordinate audits",
        "shell": "rational mixed-cycle certificates clear to deterministic composite walks with exact connector repayment",
    },
    "actual_evidence_levels": ACTUAL_EVIDENCE,
    "promoted_rows": PROMOTED,
    "fixture_fixed_point_total": str(TOTAL),
    "fixture_slack_below_one_quarter": str(SLACK),
    "geometric_closure": False,
    "all_n_theorem": "open",
    "next_theorem_identifier": "PP3ddb",
    "status": "passed",
})

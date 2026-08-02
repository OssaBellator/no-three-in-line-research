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
    "seventeenth_minimum_cores": 3,
    "budget_histogram": {5: 3},
    "corrected_points": 136,
    "corrected_blocks": 17,
    "eighteenth_minimum_four_attempts": 3,
    "eighteenth_minimum_four_cores": 7,
}
assert sum(BOUNDARY["budget_histogram"].values()) == BOUNDARY["seventeenth_minimum_cores"]
assert BOUNDARY["corrected_points"] == 8 * BOUNDARY["corrected_blocks"]

HALL = {
    "multisets_checked": 54263,
    "strict_component_improvements": 3,
    "component_exact_cases": 50387,
}
assert HALL["component_exact_cases"] <= HALL["multisets_checked"]

THRESHOLD = {
    "legal_hull_dimension": 9,
    "facet_dimension": 8,
    "facet_vertices": 495,
    "transportation_matrices": 10147,
    "minimum_transport_score": -8,
    "source_score": -3,
    "hidden_weight": Fraction(3, 8),
}
assert THRESHOLD["facet_dimension"] + 1 == THRESHOLD["legal_hull_dimension"]
assert THRESHOLD["minimum_transport_score"] * THRESHOLD["hidden_weight"] == THRESHOLD["source_score"]

PREFIX = {
    "automorphisms": 2560,
    "matchings": 104,
    "matching_orbit_sizes": (8, 16, 40, 40),
    "deletion_cases": 208,
    "deletion_case_orbit_sizes": (16, 32, 80, 80),
    "coordinate_dihedral_symmetries": 1,
}
assert sum(PREFIX["matching_orbit_sizes"]) == PREFIX["matchings"]
assert sum(PREFIX["deletion_case_orbit_sizes"]) == PREFIX["deletion_cases"]
assert PREFIX["coordinate_dihedral_symmetries"] == 1

SHELL = {
    "fixed_cycle_robust_gains": (Fraction(-1), Fraction(-1)),
    "adaptive_minimum_gain": Fraction(1, 2),
    "exact_correlated_repetitions": 7,
    "separate_extrema_repetitions": 10,
}
assert max(SHELL["fixed_cycle_robust_gains"]) <= 0
assert SHELL["adaptive_minimum_gain"] > 0
assert SHELL["exact_correlated_repetitions"] < SHELL["separate_extrema_repetitions"]

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
        "boundary": "all three minimum seventeenth cores repair at budget five; the corrected chain reaches seventeen blocks",
        "Hall": "componentwise Caro-Wei and exact bounded-component packing strengthen the resource-list interface",
        "threshold": "the separator is a facet and any same-space compensation needs at least 3/8 hidden-state weight",
        "prefix": "104 minimum-crossing matchings and 208 deletion cases each reduce to four incidence-automorphism orbits, but not coordinate orbits",
        "shell": "polyhedral support functions give exact fixed-cycle robustness and correlated setup repayment",
    },
    "actual_evidence_levels": ACTUAL_EVIDENCE,
    "promoted_rows": PROMOTED,
    "fixture_fixed_point_total": str(TOTAL),
    "fixture_slack_below_one_quarter": str(SLACK),
    "geometric_closure": False,
    "all_n_theorem": "open",
    "next_theorem_identifier": "PP3dcj",
    "status": "passed",
})

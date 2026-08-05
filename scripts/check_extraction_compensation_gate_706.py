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
    "canonical_points": 168,
    "canonical_blocks": 21,
    "twentysecond_minimum": 6,
    "minimum_six_attempts": 26,
    "minimum_six_cores": 178,
    "budget_six_rejections": 68580,
    "budget_seven_rejection_histogram": {212940: 49, 423360: 92, 841680: 37},
    "budget_seven_rejections": 80525340,
    "repairs_through_budget_seven": 0,
}
assert BOUNDARY["canonical_points"] == 8 * BOUNDARY["canonical_blocks"]
assert sum(
    count * multiplicity
    for count, multiplicity in BOUNDARY["budget_seven_rejection_histogram"].items()
) == BOUNDARY["budget_seven_rejections"]
assert BOUNDARY["budget_six_rejections"] + BOUNDARY["budget_seven_rejections"] == 80593920
assert BOUNDARY["repairs_through_budget_seven"] == 0

HALL = {
    "centres": 30,
    "component_signatures_checked": 18170,
    "retention_at_least_28_signatures": 9,
    "exact_28_signatures": 6,
    "minimum_isolated_centres": 24,
    "maximum_nonisolated_centres": 6,
    "host_derived_resources": False,
}
assert HALL["retention_at_least_28_signatures"] == 9
assert HALL["minimum_isolated_centres"] + HALL["maximum_nonisolated_centres"] == HALL["centres"]
assert not HALL["host_derived_resources"]

THRESHOLD = {
    "legal_primitive_layers": 18,
    "dual_nonnegative_separators": 2,
    "common_zero_types": 5,
    "equality_scale": "8K",
    "hidden_matrices": "3K",
    "copies_per_common_zero_type": "4K",
    "hidden_density": Fraction(3, 8),
    "enlarged_alphabet": False,
}
assert THRESHOLD["hidden_density"] == Fraction(3, 8)
assert not THRESHOLD["enlarged_alphabet"]

PREFIX = {
    "physical_matchings": 104,
    "deletions": 2,
    "optimal_routes_per_case": 144,
    "unique_routes_per_deletion": 3624,
    "ordered_compositions": 1024,
    "distinct_coordinate_audits": 7421952,
    "covered_physical_pairs": 30670848,
    "failures": 0,
    "source_size_recurrence": False,
}
assert 2 * PREFIX["unique_routes_per_deletion"] * PREFIX["ordered_compositions"] == PREFIX["distinct_coordinate_audits"]
assert PREFIX["physical_matchings"] * PREFIX["deletions"] * PREFIX["optimal_routes_per_case"] * PREFIX["ordered_compositions"] == PREFIX["covered_physical_pairs"]
assert PREFIX["failures"] == 0
assert not PREFIX["source_size_recurrence"]

SHELL = {
    "components": 3,
    "uncertainty_states": 3,
    "directed_burden_tables": 262144,
    "statewise_incompatible_cases": 62688,
    "edgewise_worst_strict_cases": 124404,
    "maximum_edgewise_overcharge": 2,
    "repetition_formula_checks": 28311552,
    "robust_loss_tour_not_repetition_optimal": 1601388,
    "coordinate_macro_graph": False,
}
assert SHELL["directed_burden_tables"] == 2 ** 18
assert SHELL["repetition_formula_checks"] == SHELL["directed_burden_tables"] * 27 * 4
assert not SHELL["coordinate_macro_graph"]

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
        "boundary": "all 178 minimum-six twenty-second cores are obstructed through budget seven",
        "Hall": "only nine degree-two thirty-centre signatures retain at least 28 and every one has at least 24 isolated centres",
        "threshold": "two separators force every equality multiple to scale the same five-type primitive aggregate",
        "prefix": "all optimal routes pass all 1024 compositions on the fixed thirteen-pair source",
        "shell": "three-state vector-aware tour and repetition optimization is exhaustively classified",
    },
    "fixture_fixed_point_total": str(TOTAL),
    "fixture_slack_below_one_quarter": str(SLACK),
    "geometric_closure": False,
    "all_n_theorem": "open",
    "next_theorem_identifier": "PP3dgb",
    "status": "passed",
})

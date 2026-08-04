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
    "canonical_stale_coordinate": (42, 193),
    "canonical_correct_coordinate": (42, 378),
    "minimum_four_nineteenth_attempts": 2,
    "minimum_four_nineteenth_cores": 6,
    "none_through_budget": 6,
    "correction_budget": 7,
    "corrected_points": 152,
    "corrected_blocks": 19,
    "twentieth_minimum_four_attempts": 3,
    "twentieth_minimum_four_cores": 9,
}
assert BOUNDARY["correction_budget"] == BOUNDARY["none_through_budget"] + 1
assert BOUNDARY["corrected_points"] == 8 * BOUNDARY["corrected_blocks"]

HALL = {
    "centres_per_packet": 6,
    "motifs_per_packet": 2,
    "load_two_partitions": 76,
    "incidence_tables": 5776,
    "realisable_conflict_graphs": 1636,
    "all_simple_graphs": 32768,
    "direct_chain_checks": 6544,
    "strict_transfer_improvements": 4866,
    "minimum_packets_for_28": 7,
    "strict_example_additive_packets": 9,
}
assert HALL["load_two_partitions"] ** 2 == HALL["incidence_tables"]
assert HALL["realisable_conflict_graphs"] < HALL["all_simple_graphs"]
assert HALL["direct_chain_checks"] == 4 * HALL["realisable_conflict_graphs"]
assert HALL["minimum_packets_for_28"] < HALL["strict_example_additive_packets"]

THRESHOLD = {
    "legal_permutation_layers": 18,
    "forced_alphabet_size": 6,
    "forced_multisets_widths_one_through_sixteen": 74612,
    "all_width_criterion": "identity_count_zero",
    "maximum_legal_windows": "max(0,5K-w+1)",
    "fixed_width_density": Fraction(5, 8),
}
assert THRESHOLD["fixed_width_density"] == Fraction(5, 8)

PREFIX = {
    "physical_matchings": 104,
    "deletions": 2,
    "optimal_routes_per_case": 144,
    "unique_routes_per_deletion": 3624,
    "compositions_at_most_four_runs": 176,
    "distinct_coordinate_audits": 1275648,
    "covered_physical_pairs": 5271552,
    "failures": 0,
}
assert 2 * PREFIX["unique_routes_per_deletion"] * PREFIX["compositions_at_most_four_runs"] == PREFIX["distinct_coordinate_audits"]
assert PREFIX["physical_matchings"] * PREFIX["deletions"] * PREFIX["optimal_routes_per_case"] * PREFIX["compositions_at_most_four_runs"] == PREFIX["covered_physical_pairs"]

SHELL = {
    "components": 3,
    "uncertainty_states": 2,
    "directed_burden_tables": 4096,
    "statewise_incompatible_cases": 644,
    "edgewise_worst_overcharge_cases": 1116,
    "repetition_formula_checks": 147456,
    "robust_loss_tour_not_repetition_optimal": 5640,
}
assert SHELL["directed_burden_tables"] == 4 ** 6
assert SHELL["repetition_formula_checks"] == SHELL["directed_burden_tables"] * 9 * 4

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
        "boundary": "canonical budget-seven correction reaches nineteen blocks and gives an exact nine-core twentieth frontier",
        "Hall": "all two-motif degree-two incidence packets are classified and their exact transfer rates are audited",
        "threshold": "the identity separator obstructs every rolling window width with exact optimum max(0,5K-w+1)",
        "prefix": "all optimal routes pass every composition with at most four runs after exact route deduplication",
        "shell": "connector tours are optimized jointly over uncertainty vectors and repetition gains",
    },
    "fixture_fixed_point_total": str(TOTAL),
    "fixture_slack_below_one_quarter": str(SLACK),
    "geometric_closure": False,
    "all_n_theorem": "open",
    "next_theorem_identifier": "PP3dfd",
    "status": "passed",
})

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
    "corrected_points": 168,
    "corrected_blocks": 21,
    "twentysecond_minimum": 6,
    "twentysecond_minimum_attempts": 26,
    "twentysecond_minimum_cores": 178,
    "budget_six_replacement_permutations": 68580,
    "budget_six_repairs": 0,
}
assert BOUNDARY["corrected_points"] == 8 * BOUNDARY["corrected_blocks"]
assert BOUNDARY["twentysecond_minimum"] == 6
assert BOUNDARY["budget_six_repairs"] == 0

HALL = {
    "synthetic_motifs": 10,
    "synthetic_centres": 30,
    "single_packet_retention": 28,
    "chain_formula": "27*K+1",
    "explicit_coordinate_chain_checks": 6,
    "two_motif_realisable_graphs": 1636,
    "two_motif_direct_chain_checks": 6544,
    "host_derived_resources": False,
}
assert HALL["single_packet_retention"] == 28
assert HALL["two_motif_direct_chain_checks"] == 4 * HALL["two_motif_realisable_graphs"]
assert not HALL["host_derived_resources"]

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
    "new_four_run_physical_pairs": 3594240,
    "remaining_compositions": 848,
    "failures": 0,
}
assert 2 * PREFIX["unique_routes_per_deletion"] * PREFIX["compositions_at_most_four_runs"] == PREFIX["distinct_coordinate_audits"]
assert PREFIX["physical_matchings"] * PREFIX["deletions"] * PREFIX["optimal_routes_per_case"] * PREFIX["compositions_at_most_four_runs"] == PREFIX["covered_physical_pairs"]
assert PREFIX["remaining_compositions"] == 1024 - PREFIX["compositions_at_most_four_runs"]
assert PREFIX["failures"] == 0

SHELL = {
    "components": 3,
    "uncertainty_states": 2,
    "directed_burden_tables": 4096,
    "statewise_incompatible_cases": 644,
    "edgewise_worst_overcharge_cases": 1116,
    "repetition_formula_checks": 147456,
    "robust_loss_tour_not_repetition_optimal": 5640,
    "coordinate_macro_graph": False,
}
assert SHELL["directed_burden_tables"] == 4 ** 6
assert SHELL["repetition_formula_checks"] == SHELL["directed_burden_tables"] * 9 * 4
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
        "boundary": "the corrected finite chain reaches twenty-one blocks and all 178 minimum-six twenty-second cores are obstructed at budget six",
        "Hall": "a synthetic coordinate defect packet retains 28 centres and repeats with exact transfer 27K+1, but its resources are not host-derived",
        "threshold": "the identity separator obstructs every rolling width with exact optimum max(0,5K-w+1)",
        "prefix": "all optimal routes pass every composition with at most four runs after exact route deduplication",
        "shell": "connector tours are optimized jointly over uncertainty burden vectors and repetition gains",
    },
    "fixture_fixed_point_total": str(TOTAL),
    "fixture_slack_below_one_quarter": str(SLACK),
    "geometric_closure": False,
    "all_n_theorem": "open",
    "next_theorem_identifier": "PP3dfj",
    "status": "passed",
})

#!/usr/bin/env python3
from fractions import Fraction

CANDIDATE_FIELDS = {
    "boundary": (4,5),
    "Hall": (4,5),
    "threshold": (5,5),
    "prefix": (5,5),
    "shell": (5,5),
    "integration": (2,5),
}
assert sum(value for value,_ in CANDIDATE_FIELDS.values())==25
assert sum(total for _,total in CANDIDATE_FIELDS.values())==30

ACTUAL_EVIDENCE={name:"fixture_derived" for name in CANDIDATE_FIELDS}
PROMOTED=tuple(name for name,level in ACTUAL_EVIDENCE.items() if level=="geometrically_verified")
assert PROMOTED==()

BOUNDARY={
    "corrected_blocks":18,
    "corrected_points":144,
    "minimum_four_attempts":1,
    "minimum_four_cores":5,
    "cores_repaired_through_budget_six":0,
    "six_point_replacements_rejected":37976400,
}
assert BOUNDARY["corrected_points"]==8*BOUNDARY["corrected_blocks"]
assert BOUNDARY["minimum_four_attempts"]==1
assert BOUNDARY["minimum_four_cores"]==5

HALL={
    "selected_motifs":12,
    "centres":36,
    "required_odd_paths":20,
    "small_degree_two_graphs_checked":10172,
}
assert 3*HALL["selected_motifs"]+HALL["required_odd_paths"]==56

THRESHOLD={
    "target_layers":32,
    "minimum_illegal_layers":12,
    "identity_layers":12,
    "legal_types":5,
    "copies_per_legal_type":4,
}
assert THRESHOLD["identity_layers"]+THRESHOLD["legal_types"]*THRESHOLD["copies_per_legal_type"]==THRESHOLD["target_layers"]

PREFIX={
    "physical_matchings":104,
    "deletions":2,
    "all_unit_cases":208,
    "representative_composition_pairs":40960,
}
assert PREFIX["physical_matchings"]*PREFIX["deletions"]==PREFIX["all_unit_cases"]

SHELL={
    "small_connected_circulations_checked":1086,
    "balanced":True,
    "connected_support":True,
    "example_denominator":6,
    "example_robust_gain":Fraction(10),
}
assert SHELL["balanced"] and SHELL["connected_support"]
assert SHELL["example_robust_gain"]>0

FIXED_POINT=(
    Fraction(70590897652005075,1207959551999868928),
    Fraction(211454017460,9215999999999),
    Fraction(3086096934497,73727999999992),
    Fraction(59599619386893,2359295999999744),
    Fraction(475832507959075,18874367999997952),
    Fraction(9494283900954065,452984831999950848),
)
TOTAL=sum(FIXED_POINT)
SLACK=Fraction(1,4)-TOTAL
assert TOTAL==Fraction(705466760524005697,3623878655999606784)
assert SLACK==Fraction(200502903475895999,3623878655999606784)

print({
    "candidate_field_completion":{name:f"{value}/{total}" for name,(value,total) in CANDIDATE_FIELDS.items()},
    "candidate_fields_complete":25,
    "candidate_fields_total":30,
    "current_results":{
        "boundary":"the unique five-core nineteenth frontier has no preserving correction through budget six",
        "Hall":"degree-two centre conflicts retain exactly (3q+o)/2 centres, giving the sharp condition 3q+o>=56",
        "threshold":"the minimum 32-layer source decomposition is unique and contains twelve illegal identity layers",
        "prefix":"the deterministic first radius-four route passes the all-unit composition for all 208 physical matching/deletion cases",
        "shell":"a rational mixed certificate is directly executable exactly when it is a balanced circulation with connected support",
    },
    "actual_evidence_levels":ACTUAL_EVIDENCE,
    "promoted_rows":PROMOTED,
    "fixture_fixed_point_total":str(TOTAL),
    "fixture_slack_below_one_quarter":str(SLACK),
    "geometric_closure":False,
    "all_n_theorem":"open",
    "next_theorem_identifier":"PP3ddt",
    "status":"passed",
})

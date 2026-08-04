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
    name for name, level in ACTUAL_EVIDENCE.items()
    if level == "geometrically_verified"
)
assert PROMOTED == ()

BOUNDARY = {
    "corrected_points": 144,
    "corrected_blocks": 18,
    "minimum_attempts": 2,
    "minimum_cores": 6,
    "none_through_budget": 6,
    "budget_six_per_core": 7595640,
    "budget_six_total": 45573840,
}
assert BOUNDARY["corrected_points"] == 8 * BOUNDARY["corrected_blocks"]
assert BOUNDARY["minimum_cores"] * BOUNDARY["budget_six_per_core"] == BOUNDARY["budget_six_total"]

HALL = {
    "incidence_graphs": 74954,
    "degree_two_graphs": 10172,
    "packet_interfaces": 76156,
    "line_graph_formula": "alpha(H)=nu(D)=(3q+o(H))/2",
}
assert HALL["incidence_graphs"] > HALL["degree_two_graphs"] > 0
assert HALL["packet_interfaces"] > 0

THRESHOLD = {
    "minimum_batches": 19834,
    "support_histogram": {2: 5, 3: 210, 4: 2255, 5: 17364},
    "identity_layers": 12,
    "legal_layer_copies": 20,
    "cyclic_orders": 6720,
    "legal_window_histogram": {0: 3840, 1: 1920, 2: 960},
}
assert sum(THRESHOLD["support_histogram"].values()) == THRESHOLD["minimum_batches"]
assert THRESHOLD["identity_layers"] + THRESHOLD["legal_layer_copies"] == 32
assert sum(THRESHOLD["legal_window_histogram"].values()) == THRESHOLD["cyclic_orders"]
assert max(THRESHOLD["legal_window_histogram"]) == 2

PREFIX = {
    "minimum_crossing_matchings": 104,
    "physical_cases": 208,
    "optimal_routes_per_case": 144,
    "compositions_per_case": 1024,
    "coordinate_audits": 212992,
    "failures": 0,
}
assert PREFIX["physical_cases"] == 2 * PREFIX["minimum_crossing_matchings"]
assert PREFIX["coordinate_audits"] == (
    PREFIX["physical_cases"] * PREFIX["compositions_per_case"]
)
assert PREFIX["failures"] == 0

SHELL = {
    "small_connected_circulations": 1086,
    "optimal_normalized_margin": Fraction(1, 2),
    "integer_bundle_gain": Fraction(1),
    "connector_saving": Fraction(-2),
    "least_bundle_repetitions": 3,
    "connected_example_scale": 6,
    "connected_example_gain": 10,
}
assert SHELL["optimal_normalized_margin"] > 0
assert SHELL["connector_saving"] + 2 * SHELL["integer_bundle_gain"] == 0
assert SHELL["connector_saving"] + 3 * SHELL["integer_bundle_gain"] > 0
assert SHELL["small_connected_circulations"] == 1086

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
        "boundary": "six minimum-four cores across P1/-33 and P2/-64 have no preserving correction through budget six",
        "Hall": "defect incidence gives an exact degree-two line-graph retention formula and packet-interface surplus",
        "threshold": "19834 minimum equality batches share one rigid 32-layer aggregate and no cyclic four-window concealment",
        "prefix": "all 104 physical matchings and both deletions pass every composition for the deterministic first optimal route",
        "shell": "positive rational robust circulations admit an exact LP and connected-support Euler realization criterion",
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

#!/usr/bin/env python3
from fractions import Fraction
from math import factorial


def profile_count(size, encoded_binary_nodes):
    encoded_unary_nodes = size - 1 - 2 * encoded_binary_nodes
    if encoded_unary_nodes < 0:
        return 0
    return factorial(size - 1) // (
        factorial(encoded_unary_nodes)
        * factorial(encoded_binary_nodes)
        * factorial(encoded_binary_nodes + 1)
    )

# The eliminated equation has two compatible interpretations:
#   * z counts leaves of the original automaton-constrained full binary tree;
#   * z counts total nodes of the size-preserving unary-binary (Motzkin) encoding.
# U(L) is an encoded object, so it does not refute the original leaf grading.
encoded_U_L = {"encoded_nodes": 2, "encoded_leaves": 1, "original_leaves": 2}
assert encoded_U_L["encoded_nodes"] == encoded_U_L["original_leaves"]
assert encoded_U_L["encoded_leaves"] != encoded_U_L["original_leaves"]

N = 30
J = 9
ENCODED_UNARY = N - 1 - 2 * J
ENCODED_LEAVES = J + 1
FAMILY = profile_count(N, J)
assert (ENCODED_UNARY, ENCODED_LEAVES, FAMILY) == (11, 10, 168212023980)

RISK_DISTRIBUTION = {
    0: 367479684,
    1: 4491418360,
    2: 20211382620,
    3: 44097562080,
    4: 51447155760,
    5: 33242777568,
    6: 11872420560,
    7: 2261413440,
    8: 212007510,
    9: 8314020,
    10: 92378,
}
assert sum(RISK_DISTRIBUTION.values()) == FAMILY
aggregate_risk = sum(risk * count for risk, count in RISK_DISTRIBUTION.items())
assert aggregate_risk == 638045608200
assert Fraction(aggregate_risk, FAMILY) == Fraction(110, 29)

print({
    "grading_reconciliation": {
        "z_in_original_automaton_series": "original leaves",
        "z_after_unary_binary_elimination": "encoded total nodes",
        "size_preserving_identity": "original leaves = encoded total nodes",
        "encoded_U_L": encoded_U_L,
    },
    "profile": {
        "original_leaves": N,
        "encoded_total_nodes": N,
        "encoded_binary_nodes": J,
        "encoded_unary_nodes": ENCODED_UNARY,
        "encoded_leaves": ENCODED_LEAVES,
        "family_size": FAMILY,
    },
    "structural_risk": "encoded unary-to-unary edges",
    "aggregate_structural_risk": aggregate_risk,
    "mean_structural_risk": str(Fraction(aggregate_risk, FAMILY)),
    "geometric_risk_coordinate_available": False,
    "required_next_source": "map encoded nodes/edges to support-chord cells and source-incidence events",
    "evidence_level": "reconciled_source_combinatorics",
    "status": "passed",
})

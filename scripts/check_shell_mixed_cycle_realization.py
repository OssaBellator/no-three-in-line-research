#!/usr/bin/env python3
from fractions import Fraction
from math import floor, lcm

THREE = Fraction(3)

def saving(burdens, incidence):
    return sum(
        multiplicity * (THREE - burden)
        for burden, multiplicity in zip(burdens, incidence)
    )

def robust_gain(vertices, incidence):
    return min(saving(vertex, incidence) for vertex in vertices)

def clear_weights(weights):
    denominator = 1
    for weight in weights:
        denominator = lcm(denominator, weight.denominator)
    counts = tuple(int(weight * denominator) for weight in weights)
    common = 0
    from math import gcd
    for count in counts:
        common = gcd(common, count)
    if common > 1:
        counts = tuple(count // common for count in counts)
        denominator //= common
    return denominator, counts

def repetition_count(setup, connector_saving, bundle_gain):
    assert bundle_gain > 0
    return max(0, floor((Fraction(setup) - connector_saving) / bundle_gain) + 1)

vertices = (
    (Fraction(1), Fraction(4)),
    (Fraction(4), Fraction(1)),
)
cycles = ((1,0),(0,1))
weights = (Fraction(1,2), Fraction(1,2))
denominator, counts = clear_weights(weights)
assert denominator == 2 and counts == (1,1)
mixed_margin = min(
    sum(weight * saving(vertex, cycle) for weight, cycle in zip(weights, cycles))
    for vertex in vertices
)
assert mixed_margin == Fraction(1,2)
composite = tuple(
    sum(count * cycle[edge] for count, cycle in zip(counts, cycles))
    for edge in range(2)
)
assert composite == (1,1)
assert robust_gain(vertices, composite) == denominator * mixed_margin == 1

# Different-base example. One connector tour has saving -1 in both scenarios.
# Repeating each primitive cycle k times before completing the connector tour gives
# robust saving k-1. Strict positivity first occurs at k=2.
connector_saving = Fraction(-1)
bundle_gain = robust_gain(vertices, composite)
assert bundle_gain == 1
assert connector_saving + bundle_gain <= 0
assert connector_saving + 2 * bundle_gain > 0
assert repetition_count(0, connector_saving, bundle_gain) == 2
assert repetition_count(5, connector_saving, bundle_gain) == 7

# A three-cycle rational certificate with denominator three.
vertices_three = (
    (Fraction(1), Fraction(4), Fraction(2)),
    (Fraction(4), Fraction(1), Fraction(2)),
)
cycles_three = ((1,0,0),(0,1,0),(0,0,1))
weights_three = (Fraction(1,3), Fraction(1,3), Fraction(1,3))
denominator_three, counts_three = clear_weights(weights_three)
assert denominator_three == 3 and counts_three == (1,1,1)
margin_three = min(
    sum(weight * saving(vertex, cycle) for weight, cycle in zip(weights_three, cycles_three))
    for vertex in vertices_three
)
assert margin_three == Fraction(2,3)
composite_three = tuple(
    sum(count * cycle[edge] for count, cycle in zip(counts_three, cycles_three))
    for edge in range(3)
)
assert robust_gain(vertices_three, composite_three) == denominator_three * margin_three == 2

print({
    "rational_mixed_weights": ("1/2","1/2"),
    "cleared_cycle_counts": counts,
    "mixed_margin": "1/2",
    "fixed_composite_robust_gain": 1,
    "common_base_realization": True,
    "different_base_connector_saving": -1,
    "least_bundle_repetitions_without_setup": 2,
    "least_bundle_repetitions_with_setup_five": 7,
    "connector_repayment_formula": "max(0,floor((S-A_connector)/G_bundle)+1)",
    "three_cycle_composite_gain": 2,
    "observation_required_for_rational_mixed_certificate": False,
    "remaining_gap": "coordinate macros must supply compatible cycles, connector paths, and a certified burden polytope",
    "evidence_level": "exact_rational_mixed_cycle_realization",
    "status": "passed",
})

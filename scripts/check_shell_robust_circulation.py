#!/usr/bin/env python3
from fractions import Fraction
from math import floor

# Edges: loop at A, loop at B, A->B, B->A.
TAIL = (0, 1, 0, 1)
HEAD = (0, 1, 1, 0)
BURDEN_VERTICES = (
    (Fraction(1), Fraction(4), Fraction(4), Fraction(4)),
    (Fraction(4), Fraction(1), Fraction(4), Fraction(4)),
)


def saving(burdens, flow):
    return sum(
        amount * (Fraction(3) - burden)
        for amount, burden in zip(flow, burdens)
    )


def is_circulation(flow):
    balance = [Fraction(0), Fraction(0)]
    for amount, tail, head in zip(flow, TAIL, HEAD):
        balance[tail] -= amount
        balance[head] += amount
    return balance == [0, 0]


def robust_margin(flow):
    return min(saving(vertex, flow) for vertex in BURDEN_VERTICES)


OPTIMAL = (Fraction(1, 2), Fraction(1, 2), Fraction(0), Fraction(0))
assert is_circulation(OPTIMAL)
assert sum(OPTIMAL) == 1
assert robust_margin(OPTIMAL) == Fraction(1, 2)


def scenario_average(flow):
    return sum(saving(vertex, flow) for vertex in BURDEN_VERTICES) / 2


assert scenario_average(OPTIMAL) == Fraction(1, 2)
for denominator in range(1, 33):
    for first in range(denominator + 1):
        for second in range(denominator - first + 1):
            for third in range(denominator - first - second + 1):
                fourth = denominator - first - second - third
                flow = tuple(Fraction(value, denominator) for value in (first, second, third, fourth))
                if not is_circulation(flow):
                    continue
                assert robust_margin(flow) <= scenario_average(flow) <= Fraction(1, 2)

BUNDLE = (1, 1, 0, 0)
assert is_circulation(BUNDLE)
assert robust_margin(BUNDLE) == 1

CONNECTOR = (0, 0, 1, 1)
assert is_circulation(CONNECTOR)
assert robust_margin(CONNECTOR) == -2


def repetitions_needed(bundle_gain, connector_saving, setup=0):
    bundle_gain = Fraction(bundle_gain)
    connector_saving = Fraction(connector_saving)
    setup = Fraction(setup)
    assert bundle_gain > 0
    return max(1, floor((setup - connector_saving) / bundle_gain) + 1)


assert repetitions_needed(1, -2) == 3
assert robust_margin(tuple(2*b + c for b, c in zip(BUNDLE, CONNECTOR))) == 0
EXECUTABLE = tuple(3*b + c for b, c in zip(BUNDLE, CONNECTOR))
assert is_circulation(EXECUTABLE)
assert robust_margin(EXECUTABLE) == 1

print({
    "robust_circulation_lp": "maximize gamma subject to Bx=0, x>=0, sum x=1, gamma<=<3-b^u,x> for every uncertainty vertex u",
    "optimal_normalized_margin": str(robust_margin(OPTIMAL)),
    "optimal_flow": tuple(str(value) for value in OPTIMAL),
    "integer_bundle_gain": str(robust_margin(BUNDLE)),
    "connector_worst_saving": str(robust_margin(CONNECTOR)),
    "least_bundle_repetitions": 3,
    "executable_closed_walk_gain": str(robust_margin(EXECUTABLE)),
    "remaining_gap": "no coordinate macro graph supplies the certified edges, burden vertices, and connector tour",
    "evidence_level": "exact_robust_circulation_execution_interface",
    "status": "passed",
})

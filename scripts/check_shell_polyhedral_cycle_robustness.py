#!/usr/bin/env python3
from fractions import Fraction
from math import floor

THREE = Fraction(3)

def cycle_saving(burdens, incidence):
    return sum(
        multiplicity * (THREE - burden)
        for burden, multiplicity in zip(burdens, incidence)
    )

def robust_cycle_gain(vertices, incidence):
    return min(cycle_saving(vertex, incidence) for vertex in vertices)

def worst_cycle_burden(vertices, incidence):
    return max(
        sum(multiplicity * burden for burden, multiplicity in zip(vertex, incidence))
        for vertex in vertices
    )

def mixed_cycle_gain(vertices, cycles, weights):
    assert sum(weights) == 1
    return min(
        sum(weight * cycle_saving(vertex, cycle) for weight, cycle in zip(weights, cycles))
        for vertex in vertices
    )

def exact_repetition_count(scenarios, setup):
    setup = Fraction(setup)
    answer = 0
    for entry_saving, cycle_gain in scenarios:
        entry_saving = Fraction(entry_saving)
        cycle_gain = Fraction(cycle_gain)
        assert cycle_gain > 0
        repetitions = max(0, floor((setup - entry_saving) / cycle_gain) + 1)
        answer = max(answer, repetitions)
    return answer

vertices = (
    (Fraction(1), Fraction(4)),
    (Fraction(4), Fraction(1)),
)
cycles = ((1,0),(0,1))
assert [robust_cycle_gain(vertices, cycle) for cycle in cycles] == [-1,-1]
assert [worst_cycle_burden(vertices, cycle) for cycle in cycles] == [4,4]

# On the entire segment between the two vertices, the best revealed cycle has
# saving max(2-3t, -1+3t), minimized at t=1/2 with value 1/2.
for numerator in range(0, 101):
    t = Fraction(numerator, 100)
    first = 2 - 3*t
    second = -1 + 3*t
    assert max(first, second) >= Fraction(1,2)
assert max(2-3*Fraction(1,2), -1+3*Fraction(1,2)) == Fraction(1,2)

# The exact minimax dual uses equal cycle weights. Its expected gain is 1/2 at
# both uncertainty vertices, certifying the adaptive margin without selecting one
# fixed cycle in advance.
weights = (Fraction(1,2), Fraction(1,2))
assert mixed_cycle_gain(vertices, cycles, weights) == Fraction(1,2)
for numerator in range(0, 101):
    weight = Fraction(numerator, 100)
    candidate = mixed_cycle_gain(vertices, cycles, (weight, 1-weight))
    assert candidate <= Fraction(1,2)

correlated_scenarios = (
    (Fraction(-2), Fraction(3)),
    (Fraction(1), Fraction(1)),
)
assert exact_repetition_count(correlated_scenarios, 7) == 7
for repetitions in range(7):
    assert any(entry + repetitions*gain <= 7 for entry, gain in correlated_scenarios)
assert all(entry + 7*gain > 7 for entry, gain in correlated_scenarios)
separate_extrema_bound = max(
    0,
    floor((Fraction(7) - min(entry for entry, _ in correlated_scenarios))
          / min(gain for _, gain in correlated_scenarios)) + 1,
)
assert separate_extrema_bound == 10

triangle_vertices = (
    (Fraction(1),Fraction(2),Fraction(5)),
    (Fraction(2),Fraction(4),Fraction(1)),
    (Fraction(3),Fraction(1),Fraction(2)),
)
incidence = (1,2,0)
assert worst_cycle_burden(triangle_vertices, incidence) == max(
    sum(m*b for m,b in zip(incidence, vertex))
    for vertex in triangle_vertices
)
assert robust_cycle_gain(triangle_vertices, incidence) == (
    THREE*sum(incidence) - worst_cycle_burden(triangle_vertices, incidence)
)

print({
    "polyhedral_fixed_cycle_condition": "max_{b in U} <b,chi_C> < 3|C|",
    "vertex_reduction": True,
    "fixed_cycle_robust_gains_in_gap_example": (-1,-1),
    "revealed_state_adaptive_minimum_gain": "1/2",
    "mixed_cycle_dual_minimum_gain": "1/2",
    "mixed_cycle_weights": ("1/2","1/2"),
    "adaptive_minimax_formula": "min_b max_C g_C(b)=max_lambda min_b sum_C lambda_C g_C(b)",
    "fixed_vs_adaptive_gap": True,
    "correlated_setup_example_exact_repetitions": 7,
    "separate_extrema_bound": 10,
    "exact_correlated_repetition_formula": "max_u max(0,floor((S-A_u)/G_u)+1)",
    "remaining_gap": "no coordinate macro graph supplies a certified polyhedral burden set with a fixed reachable robust-positive cycle",
    "evidence_level": "exact_polyhedral_shell_cycle_interface",
    "status": "passed",
})

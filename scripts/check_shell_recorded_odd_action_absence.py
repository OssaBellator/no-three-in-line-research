#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

INCIDENCE = (
    (1, 1, 0),
    (0, 1, 1),
    (1, 0, 1),
)
RECORDED_ACTIONS = tuple(tuple(INCIDENCE[row][column] for row in range(3)) for column in range(3))
TARGET = (12, 10, 8)
UNIT_ODD_ACTIONS = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

def apply(actions):
    return tuple(sum(INCIDENCE[row][column] * actions[column] for column in range(3)) for row in range(3))

assert RECORDED_ACTIONS == ((1, 0, 1), (1, 1, 0), (0, 1, 1))
assert all(sum(action) % 2 == 0 for action in RECORDED_ACTIONS)

for counts in product(range(8), repeat=3):
    assert sum(apply(counts)) % 2 == 0

conditional = {}
for odd_action in UNIT_ODD_ACTIONS:
    solutions = []
    for odd_count in range(1, 9):
        for recorded_counts in product(range(13), repeat=3):
            cycle_total = tuple(
                apply(recorded_counts)[i] + odd_count * odd_action[i]
                for i in range(3)
            )
            if cycle_total == TARGET:
                solutions.append((sum(recorded_counts) + odd_count, odd_count, recorded_counts))
    assert solutions
    optimum = min(solutions)
    assert optimum[0] == 16
    assert optimum[1] == 2
    conditional[odd_action] = optimum

print({
    "recorded_source_actions": RECORDED_ACTIONS,
    "recorded_action_coordinate_sums": tuple(sum(action) for action in RECORDED_ACTIONS),
    "recorded_catalogue_contains_odd_sum_action": False,
    "recorded_integer_image": "even coordinate-sum cycle vectors",
    "minimal_conditional_unit_odd_action_solutions": conditional,
    "conditional_active_controls": 16,
    "stored_active_controls": 15,
    "throughput_penalty_per_twenty_slots": str(Fraction(1, 20)),
    "conclusion": "the recorded source catalogue contains no coset-crossing clean-macro action",
    "remaining_gap": "a source-level action outside the recorded catalogue is required to realise the conditional lattice repair",
    "evidence_level": "exact_recorded_source_catalogue_absence",
    "status": "passed",
})

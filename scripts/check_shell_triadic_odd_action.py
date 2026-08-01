#!/usr/bin/env python3
from itertools import product

RECORDED = (
    (1, 0, 1),
    (1, 1, 0),
    (0, 1, 1),
)
TARGET = (12, 10, 8)


def solve_with(action):
    best = None
    witness = None
    for action_count in range(1, 21):
        residual = tuple(TARGET[index] - action_count * action[index] for index in range(3))
        if min(residual) < 0:
            continue
        numerators = (
            residual[0] - residual[1] + residual[2],
            residual[0] + residual[1] - residual[2],
            -residual[0] + residual[1] + residual[2],
        )
        if any(value % 2 for value in numerators):
            continue
        recorded_counts = tuple(value // 2 for value in numerators)
        if min(recorded_counts) < 0:
            continue
        active = sum(recorded_counts) + action_count
        if best is None or active < best:
            best = active
            witness = (recorded_counts, action_count)
    return best, witness


for coefficients in product(range(-8, 9), repeat=3):
    vector = tuple(
        sum(coefficients[column] * RECORDED[column][row] for column in range(3))
        for row in range(3)
    )
    assert sum(vector) % 2 == 0

binary_odd_actions = tuple(vector for vector in product((0, 1), repeat=3) if sum(vector) % 2 == 1)
assert binary_odd_actions == ((0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 1, 1))

solutions = {action: solve_with(action) for action in binary_odd_actions}
assert solutions[(1, 0, 0)] == (16, ((4, 6, 4), 2))
assert solutions[(0, 1, 0)][0] == 16
assert solutions[(0, 0, 1)][0] == 16
assert solutions[(1, 1, 1)] == (12, ((2, 4, 0), 6))

triadic = (1, 1, 1)
recorded_counts, triadic_count = solutions[triadic][1]
reconstructed = tuple(
    sum(recorded_counts[column] * RECORDED[column][row] for column in range(3))
    + triadic_count * triadic[row]
    for row in range(3)
)
assert reconstructed == TARGET

print(
    {
        "recorded_columns": RECORDED,
        "graph_incidence_interpretation": "three edge-incidence columns of a triangle",
        "signed_coefficient_box_checked": [-8, 8],
        "recorded_integer_image": "even coordinate sum",
        "binary_odd_columns": binary_odd_actions,
        "unit_odd_action_minimum_active_controls": 16,
        "triadic_action": triadic,
        "triadic_target_witness": {
            "recorded_action_counts": recorded_counts,
            "triadic_action_count": triadic_count,
            "active_controls": solutions[triadic][0],
        },
        "improvement_over_recorded_fifteen_control_schedule": 3,
        "conclusion": "the smallest coordinatewise positive odd primitive is a triadic all-cycle action, not a pair-supported edge action",
        "remaining_gap": "no geometric clean-macro operation has yet been shown to realize the triadic incidence column",
        "status": "passed",
    }
)

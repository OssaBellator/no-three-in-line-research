#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

INCIDENCE = (
    (1, 1, 0),
    (0, 1, 1),
    (1, 0, 1),
)
TARGET_TOTAL = (12, 10, 8)
TARGET_RATE_TENTHS = (6, 5, 4)
UNIT_ACTIONS = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def determinant(columns):
    a, b, c = columns
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - b[0] * (a[1] * c[2] - a[2] * c[1])
        + c[0] * (a[1] * b[2] - a[2] * b[1])
    )


def inverse_image(cycle_vector):
    y1, y2, y3 = map(Fraction, cycle_vector)
    return (
        (y1 - y2 + y3) / 2,
        (y1 + y2 - y3) / 2,
        (-y1 + y2 + y3) / 2,
    )


def pareto_insert(frontier, vector, word):
    if any(all(existing[i] <= vector[i] for i in range(3)) for existing in frontier):
        return
    for existing in list(frontier):
        if all(vector[i] <= existing[i] for i in range(3)):
            del frontier[existing]
    frontier[vector] = word


def pareto_buffers(action_vectors, limits, symbols):
    scaled_actions = tuple(tuple(10 * value for value in vector) for vector in action_vectors)
    dp = {(0,) * len(limits): {(0, 0, 0): ""}}
    for total in range(sum(limits)):
        for state in tuple(key for key in dp if sum(key) == total):
            frontier = dp[state]
            current = tuple(
                sum(state[j] * scaled_actions[j][i] for j in range(len(limits)))
                for i in range(3)
            )
            for action_index in range(len(limits)):
                if state[action_index] == limits[action_index]:
                    continue
                next_state = list(state)
                next_state[action_index] += 1
                next_state = tuple(next_state)
                service = tuple(current[i] + scaled_actions[action_index][i] for i in range(3))
                deficit = tuple(
                    max(0, TARGET_RATE_TENTHS[i] * (total + 1) - service[i])
                    for i in range(3)
                )
                next_frontier = dp.setdefault(next_state, {})
                for maximum, word in frontier.items():
                    next_maximum = tuple(max(maximum[i], deficit[i]) for i in range(3))
                    pareto_insert(next_frontier, next_maximum, word + symbols[action_index])
    return dp[tuple(limits)]


source_columns = tuple(zip(*INCIDENCE))
assert determinant(source_columns) == 2
records = []
for extra in UNIT_ACTIONS:
    augmented_columns = source_columns + (extra,)
    minors = tuple(
        abs(determinant(tuple(augmented_columns[index] for index in indices)))
        for indices in combinations(range(4), 3)
    )
    assert 1 in minors

    exact_solutions = []
    for uses in range(0, 13):
        residual = tuple(TARGET_TOTAL[i] - uses * extra[i] for i in range(3))
        preimage = inverse_image(residual)
        if all(value.denominator == 1 and value >= 0 for value in preimage):
            exact_solutions.append((uses, tuple(int(value) for value in preimage)))
    assert exact_solutions[0] == (0, (5, 7, 3))
    assert exact_solutions[1][0] == 2
    uses, original_counts = exact_solutions[1]
    active_controls = sum(original_counts) + uses
    assert active_controls == 16

    limits = original_counts + (uses, 20 - active_controls)
    actions = source_columns + (extra, (0, 0, 0))
    frontier = pareto_buffers(actions, limits, "123XI")
    minimum_l1_tenths = min(sum(vector) for vector in frontier)
    assert minimum_l1_tenths == 4
    best_vector, best_word = min(
        ((vector, word) for vector, word in frontier.items() if sum(vector) == minimum_l1_tenths),
        key=lambda item: item[0],
    )
    records.append({
        "extra_cycle_action": extra,
        "gcd_witnessing_minors": minors,
        "smallest_positive_exact_use_count": uses,
        "original_action_counts": original_counts,
        "active_controls": active_controls,
        "idle_slots": 20 - active_controls,
        "minimum_cycle_buffer": tuple(str(Fraction(value, 10)) for value in best_vector),
        "witness_word": best_word,
    })

print({
    "source_lattice_index": 2,
    "minimal_nonnegative_coset_crossing_cycle_actions": UNIT_ACTIONS,
    "each_augmented_action_lattice_is_full_Z3": True,
    "parity_rule": "the even-sum target (12,10,8) uses any odd-sum added action an even number of times",
    "smallest_positive_extra_action_uses": 2,
    "source_active_controls": 15,
    "augmented_active_controls": 16,
    "throughput_cost_per_twenty_slot_period": "1/20",
    "minimum_l1_cycle_buffer_remains": "2/5",
    "conditional_records": records,
    "conclusion": "one unit cycle action repairs the lattice, but exact target service requires two uses and one extra active slot without reducing the optimal buffer",
    "remaining_gap": "no source-level clean-macro action with an odd-sum cycle vector is identified in the repository",
    "evidence_level": "exact_conditional_coset_action_completion",
    "status": "passed",
})

#!/usr/bin/env python3
"""Audit small odd shell columns and a zero-buffer all-cycle schedule."""
from functools import lru_cache
from itertools import product

A = (1, 0, 1)
B = (1, 1, 0)
C = (0, 1, 1)
IDLE = (0, 0, 0)
RECORDED = (A, B, C)
TARGET = (12, 10, 8)
PERIOD = 20


def add_scaled(coefficients, columns):
    return tuple(
        sum(coefficient * column[index] for coefficient, column in zip(coefficients, columns))
        for index in range(3)
    )

baseline = []
for coefficients in product(range(PERIOD + 1), repeat=3):
    if add_scaled(coefficients, RECORDED) == TARGET:
        baseline.append((sum(coefficients),) + coefficients)
assert min(baseline) == (15, 5, 7, 3)

records = []
for column in product(range(4), repeat=3):
    weight = sum(column)
    if not (weight and weight <= 3 and weight % 2):
        continue
    solutions = []
    for uses in range(1, PERIOD + 1):
        for coefficients in product(range(PERIOD + 1), repeat=3):
            if add_scaled(coefficients + (uses,), RECORDED + (column,)) == TARGET:
                solutions.append((sum(coefficients) + uses, uses) + coefficients)
    if solutions:
        records.append((min(solutions), column))

assert len(records) == 13
best_active = min(solution[0] for solution, _ in records)
best = [(solution, column) for solution, column in records if solution[0] == best_active]
assert best == [((12, 6, 2, 4, 0), (1, 1, 1))]
D = (1, 1, 1)

binary = ((1, 0, 0), (0, 1, 0), (0, 0, 1), D)
frontier = {}
for column in binary:
    pairs = sorted({(solution[1], solution[0]) for solution, item in records if item == column})
    # Re-enumerate all exact solutions to retain the complete use/cost frontier.
    exact_pairs = set()
    for uses in range(1, PERIOD + 1):
        for coefficients in product(range(PERIOD + 1), repeat=3):
            if add_scaled(coefficients + (uses,), RECORDED + (column,)) == TARGET:
                exact_pairs.add((uses, sum(coefficients) + uses))
    frontier[column] = tuple(
        pair for pair in sorted(exact_pairs)
        if not any(other != pair and other[0] <= pair[0] and other[1] <= pair[1] for other in exact_pairs)
    )
assert frontier[D] == ((2, 14), (4, 13), (6, 12))
assert all(min(cost for _, cost in frontier[column]) == 16 for column in binary[:3])

columns = {"A": A, "B": B, "D": D, "I": IDLE}
counts = {"A": 2, "B": 4, "D": 6, "I": 8}
order = tuple(columns)

@lru_cache(None)
def search(state, service):
    used = dict(zip(order, state))
    time = sum(used.values())
    if time == PERIOD:
        return ""
    for label in order:
        if used[label] >= counts[label]:
            continue
        next_used = used.copy()
        next_used[label] += 1
        next_service = tuple(service[i] + columns[label][i] for i in range(3))
        next_time = time + 1
        if any(PERIOD * next_service[i] < next_time * TARGET[i] for i in range(3)):
            continue
        tail = search(tuple(next_used[item] for item in order), next_service)
        if tail is not None:
            return label + tail
    return None

word = search((0, 0, 0, 0), (0, 0, 0))
assert word == "DABABBBDDDDDIIIIIIII"
cumulative = [0, 0, 0]
for time, label in enumerate(word, 1):
    for index in range(3):
        cumulative[index] += columns[label][index]
    assert all(PERIOD * cumulative[index] >= time * TARGET[index] for index in range(3))
assert tuple(cumulative) == TARGET

print({
    "binary_odd_columns": binary,
    "feasible_nonnegative_odd_columns_of_l1_at_most_three": len(records),
    "symmetric_column_frontier": frontier[D],
    "unique_minimum_active_column": D,
    "minimum_active_controls": best_active,
    "recorded_baseline_active_controls": 15,
    "zero_startup_buffer_word": word,
    "startup_buffer": (0, 0, 0),
    "active_control_saving": 3,
    "remaining_gap": "the all-cycle column (1,1,1) has no geometric clean-macro realization",
    "evidence_level": "exact_small_odd_column_zero_buffer_frontier",
    "status": "passed",
})

#!/usr/bin/env python3
"""Find the optimal small odd shell column and a zero-buffer twenty-slot schedule."""
from __future__ import annotations

from functools import lru_cache
from itertools import product

A = (1, 0, 1)
B = (1, 1, 0)
C = (0, 1, 1)
IDLE = (0, 0, 0)
TARGET = (12, 10, 8)
PERIOD = 20


def add(*vectors):
    return tuple(sum(vector[index] for vector in vectors) for index in range(3))


def scale(coefficient, vector):
    return tuple(coefficient * entry for entry in vector)

baseline = []
for a, b, c in product(range(PERIOD + 1), repeat=3):
    if add(scale(a, A), scale(b, B), scale(c, C)) == TARGET:
        baseline.append((a + b + c, a, b, c))
assert min(baseline) == (15, 5, 7, 3)

candidate_records = []
for column in product(range(4), repeat=3):
    weight = sum(column)
    if weight == 0 or weight > 3 or weight % 2 == 0:
        continue
    solutions = []
    for uses in range(1, PERIOD + 1):
        remainder = tuple(TARGET[index] - uses * column[index] for index in range(3))
        if min(remainder) < 0:
            continue
        for a, b, c in product(range(PERIOD + 1), repeat=3):
            if add(scale(a, A), scale(b, B), scale(c, C)) == remainder:
                solutions.append((a + b + c + uses, uses, a, b, c))
    if solutions:
        candidate_records.append((min(solutions), column))

best_active = min(record[0][0] for record in candidate_records)
best_columns = [(solution, column) for solution, column in candidate_records if solution[0] == best_active]
assert best_active == 12
assert best_columns == [((12, 6, 2, 4, 0), (1, 1, 1))]
D = (1, 1, 1)
COUNTS = {"A": 2, "B": 4, "D": 6, "I": 8}
TYPES = {"A": A, "B": B, "D": D, "I": IDLE}
ORDER = tuple(TYPES)

@lru_cache(None)
def zero_buffer_word(state, service):
    used = dict(zip(ORDER, state))
    time = sum(used.values())
    if time == PERIOD:
        return ""
    for label in ORDER:
        if used[label] >= COUNTS[label]:
            continue
        next_used = used.copy()
        next_used[label] += 1
        next_service = tuple(service[index] + TYPES[label][index] for index in range(3))
        next_time = time + 1
        if any(PERIOD * next_service[index] < next_time * TARGET[index] for index in range(3)):
            continue
        tail = zero_buffer_word(tuple(next_used[item] for item in ORDER), next_service)
        if tail is not None:
            return label + tail
    return None

word = zero_buffer_word(tuple(0 for _ in ORDER), (0, 0, 0))
assert word == "DABABBBDDDDDIIIIIIII"
assert {label: word.count(label) for label in ORDER} == COUNTS
cumulative = [0, 0, 0]
for time, label in enumerate(word, 1):
    for index in range(3):
        cumulative[index] += TYPES[label][index]
    assert all(PERIOD * cumulative[index] >= time * TARGET[index] for index in range(3))
assert tuple(cumulative) == TARGET

print({
    "recorded_baseline_active_controls": 15,
    "nonnegative_odd_columns_of_l1_at_most_three_with_exact_service": len(candidate_records),
    "unique_minimum_active_column": D,
    "minimum_active_controls": best_active,
    "exact_counts": {"A": 2, "B": 4, "D": 6, "idle": 8},
    "zero_startup_buffer_word": word,
    "startup_buffer": (0, 0, 0),
    "active_control_saving": 3,
    "remaining_gap": "the all-cycle odd column (1,1,1) has no geometric clean-macro realization",
    "evidence_level": "optimal_small_odd_shell_column_candidate",
    "status": "passed",
})

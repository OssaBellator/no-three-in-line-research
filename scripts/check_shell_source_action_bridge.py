#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations

ACTIONS = {
    "A": (1, 0, 0),
    "B": (0, 1, 0),
    "C": (0, 0, 1),
}
SOURCE_PERIOD = ("A", "B", "C")
SOURCE_TARGET = (Fraction(1, 3),) * 3
EXTENDED_MULTISET = ("A", "A", "B", "B", "C")
EXTENDED_TARGET = (Fraction(2, 5), Fraction(2, 5), Fraction(1, 5))


def startup_buffer(word, target):
    service = [Fraction(0)] * 3
    buffer = [Fraction(0)] * 3
    for step, label in enumerate(word, start=1):
        vector = ACTIONS[label]
        for coordinate in range(3):
            service[coordinate] += vector[coordinate]
            deficit = step * target[coordinate] - service[coordinate]
            buffer[coordinate] = max(buffer[coordinate], deficit)
    return tuple(buffer)


incidence = tuple(ACTIONS[label] for label in ("A", "B", "C"))
assert incidence == ((1, 0, 0), (0, 1, 0), (0, 0, 1))

source_phase_buffers = {}
for shift in range(3):
    word = SOURCE_PERIOD[shift:] + SOURCE_PERIOD[:shift]
    source_phase_buffers[word] = startup_buffer(word, SOURCE_TARGET)
assert set(source_phase_buffers.values()) == {
    (Fraction(0), Fraction(1, 3), Fraction(2, 3)),
    (Fraction(2, 3), Fraction(0), Fraction(1, 3)),
    (Fraction(1, 3), Fraction(2, 3), Fraction(0)),
}

words = sorted(set(permutations(EXTENDED_MULTISET)))
assert len(words) == 30
buffers = {word: startup_buffer(word, EXTENDED_TARGET) for word in words}
minimum_l1 = min(sum(buffer) for buffer in buffers.values())
optimal = tuple(word for word in words if sum(buffers[word]) == minimum_l1)
assert minimum_l1 == Fraction(6, 5)
assert len(optimal) == 10
assert min(optimal) == ("A", "B", "A", "B", "C")
assert buffers[min(optimal)] == (Fraction(0), Fraction(2, 5), Fraction(4, 5))

assert ACTIONS[SOURCE_PERIOD[0]] == incidence[0] == ACTIONS[EXTENDED_MULTISET[0]]

print(
    {
        "source_chapter_service_vectors": ACTIONS,
        "derived_incidence_matrix": incidence,
        "source_period_phase_buffers": source_phase_buffers,
        "extended_distinct_orders": len(words),
        "extended_optimal_orders": len(optimal),
        "extended_minimum_l1_buffer": str(minimum_l1),
        "lexicographic_optimum": "".join(min(optimal)),
        "lexicographic_buffer": tuple(str(value) for value in buffers[min(optimal)]),
        "action_level_source_bridge": "docs/523 unit service A equals canonical A-debt incidence e_A",
        "remaining_gap": "canonical A/B/C debts are not yet identified with coordinate-level clean-macro shell resources",
        "evidence_level": "repository_source_action_aligned",
        "status": "passed",
    }
)

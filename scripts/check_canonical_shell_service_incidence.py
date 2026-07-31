#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations

MULTISET = "AABBC"
TARGET = (Fraction(2, 5), Fraction(2, 5), Fraction(1, 5))
ACTION = {
    "A": (1, 0, 0),
    "B": (0, 1, 0),
    "C": (0, 0, 1),
}


def startup_buffer(word):
    counts = [0, 0, 0]
    maximum_deficit = [Fraction(0), Fraction(0), Fraction(0)]
    for time, symbol in enumerate(word, start=1):
        increment = ACTION[symbol]
        counts = [counts[j] + increment[j] for j in range(3)]
        deficits = [time * TARGET[j] - counts[j] for j in range(3)]
        maximum_deficit = [max(maximum_deficit[j], deficits[j]) for j in range(3)]
    return tuple(maximum_deficit)


words = tuple(sorted(set(permutations(MULTISET))))
assert len(words) == 30
buffers = {word: startup_buffer(word) for word in words}
minimum_l1 = min(sum(buffer) for buffer in buffers.values())
optimal = tuple(word for word in words if sum(buffers[word]) == minimum_l1)
assert minimum_l1 == Fraction(6, 5)
assert len(optimal) == 10
selected = min(optimal)
assert selected == tuple("ABABC")
assert buffers[selected] == (Fraction(0), Fraction(2, 5), Fraction(4, 5))

# The incidence is not chosen: each service action increments its named physical
# resource, so the source-derived component-to-resource map is the identity.
identity_incidence = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
assert tuple(ACTION[symbol] for symbol in "ABC") == identity_incidence

# Repetition remains feasible with the one-time buffer.
reserve = list(buffers[selected])
for index, symbol in enumerate(selected * 100, start=1):
    increment = ACTION[symbol]
    reserve = [reserve[j] + increment[j] - TARGET[j] for j in range(3)]
    assert all(value >= 0 for value in reserve), (index, symbol, reserve)

print({
    "source_service_multiset": MULTISET,
    "canonical_physical_resources": ["A-service debt", "B-service debt", "C-service debt"],
    "source_derived_incidence": identity_incidence,
    "orders_checked": len(words),
    "optimal_orders": len(optimal),
    "minimum_l1_buffer": str(minimum_l1),
    "selected_word": "".join(selected),
    "selected_buffer": [str(value) for value in buffers[selected]],
    "prefixes_checked": len(selected) * 100,
    "remaining_gap": "canonical service debts are not yet identified with prime-patching shell incidences",
    "evidence_level": "repository_source_derived_benchmark",
    "status": "passed",
})

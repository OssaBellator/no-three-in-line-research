#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations

MULTISET = tuple("AABBC")
TARGET = (Fraction(2, 5), Fraction(2, 5), Fraction(1, 5))
ACTIONS = {
    "A": (1, 0, 0),
    "B": (0, 1, 0),
    "C": (0, 0, 1),
}
INCIDENCE = (
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 0),
)


def determinant_3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def component_residual(letter):
    action = ACTIONS[letter]
    return tuple(Fraction(action[index]) - TARGET[index] for index in range(3))


def map_incidence(vector):
    return tuple(
        sum(Fraction(row[index]) * vector[index] for index in range(3))
        for row in INCIDENCE
    )


def physical_word(word):
    return tuple(map_incidence(component_residual(letter)) for letter in word)


def startup_buffer(increments):
    prefix = [Fraction(0)] * len(increments[0])
    minima = [Fraction(0)] * len(prefix)
    for increment in increments:
        prefix = [prefix[index] + increment[index] for index in range(len(prefix))]
        minima = [min(minima[index], prefix[index]) for index in range(len(prefix))]
    assert all(value == 0 for value in prefix)
    return tuple(-value for value in minima)


def l1(vector):
    return sum(vector)


assert determinant_3(INCIDENCE) == -2
assert all(any(value for value in map_incidence(component_residual(letter))) for letter in ACTIONS)

words = sorted(set(permutations(MULTISET)))
assert len(words) == 30
records = []
for word in words:
    increments = physical_word(word)
    assert any(any(value for value in increment) for increment in increments)
    buffer = startup_buffer(increments)
    records.append((l1(buffer), word, buffer, increments))

minimum = min(record[0] for record in records)
optimal = [record for record in records if record[0] == minimum]
assert minimum == Fraction(6, 5)
assert len(optimal) == 10
selected = min(optimal)
assert selected[1] == tuple("ABABC")
assert selected[2] == (Fraction(2, 5), Fraction(4, 5), Fraction(0))

reserve = list(selected[2])
prefixes_checked = 0
for increment in selected[3] * 100:
    reserve = [reserve[index] + increment[index] for index in range(3)]
    assert all(value >= 0 for value in reserve)
    prefixes_checked += 1

print({
    "component_word_multiset": "".join(MULTISET),
    "physical_resource_definitions": (
        "A+C service",
        "B+C service",
        "A+B service",
    ),
    "incidence_matrix": INCIDENCE,
    "incidence_determinant": determinant_3(INCIDENCE),
    "precancelled": False,
    "orders_checked": len(records),
    "minimum_physical_l1_buffer": str(minimum),
    "optimal_orders": len(optimal),
    "selected_word": "".join(selected[1]),
    "selected_buffer": tuple(str(value) for value in selected[2]),
    "prefixes_checked": prefixes_checked,
    "link_to_actual_prime_patching_shells": False,
    "evidence_level": "independently_enumerated_candidate",
    "status": "passed",
})

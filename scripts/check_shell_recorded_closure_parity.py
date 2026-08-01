#!/usr/bin/env python3
from itertools import product

RECORDED = (
    (1, 0, 1),
    (1, 1, 0),
    (0, 1, 1),
)
IDLE = (0, 0, 0)
SCALED_STARTUP_BUFFER = (2, 0, 2)  # five times the docs/517 fractional buffer.


def add(*vectors):
    return tuple(sum(vector[index] for vector in vectors) for index in range(3))


def scale(coefficient, vector):
    return tuple(coefficient * entry for entry in vector)


catalogue = RECORDED + (IDLE, SCALED_STARTUP_BUFFER)
assert all(sum(vector) % 2 == 0 for vector in catalogue)

# Exact bounded audit of the compound-control monoid. The parity proof is
# unbounded: sums and repetitions of even-sum generators remain even-sum.
bounded_closure = set()
for coefficients in product(range(9), repeat=4):
    bounded_closure.add(
        add(*(scale(coefficients[index], (RECORDED + (IDLE,))[index]) for index in range(4)))
    )

assert len(bounded_closure) == 729
assert all(sum(vector) % 2 == 0 for vector in bounded_closure)

unit_odd_actions = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
assert all(sum(vector) % 2 == 1 for vector in unit_odd_actions)
assert all(vector not in bounded_closure for vector in unit_odd_actions)

print(
    {
        "recorded_generators": RECORDED,
        "derived_operations_included": ["idle", "simultaneous composition", "repetition", "scaled startup buffer"],
        "bounded_compound_vectors_checked": len(bounded_closure),
        "integer_image_parity": "even coordinate sum",
        "odd_unit_actions_reachable": False,
        "conclusion": "no operation composed from the recorded clean-macro primitives can cross the missing lattice coset",
        "remaining_gap": "an odd-sum action must be a genuinely new source operation rather than a compound of the recorded catalogue",
        "evidence_level": "exact_recorded_source_monoid_obstruction",
        "status": "passed",
    }
)

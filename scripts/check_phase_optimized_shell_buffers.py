#!/usr/bin/env python3
from fractions import Fraction

# Three one-coordinate service actions, with target service 1/3 per coordinate.
ACTIONS = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1)),
)
TARGET = (Fraction(1, 3),) * 3


def phase_buffer(phase):
    cumulative = [Fraction(0)] * 3
    worst = [Fraction(0)] * 3
    word = ACTIONS[phase:] + ACTIONS[:phase]
    for t, action in enumerate(word, start=1):
        for j in range(3):
            cumulative[j] += action[j]
            deficit = t * TARGET[j] - cumulative[j]
            worst[j] = max(worst[j], deficit)
    return tuple(worst), word

buffers = []
for phase in range(3):
    b, word = phase_buffer(phase)
    buffers.append(b)
    # Repetition with this startup buffer is feasible at every prefix.
    cumulative = [Fraction(0)] * 3
    for t in range(1, 101):
        action = word[(t - 1) % 3]
        for j in range(3):
            cumulative[j] += action[j]
            assert b[j] + cumulative[j] >= t * TARGET[j]

assert buffers == [
    (Fraction(0), Fraction(1, 3), Fraction(2, 3)),
    (Fraction(2, 3), Fraction(0), Fraction(1, 3)),
    (Fraction(1, 3), Fraction(2, 3), Fraction(0)),
]
assert {sum(b) for b in buffers} == {Fraction(1)}
assert all(any(x > 0 for x in b) for b in buffers)

print({
    "phase_buffers": buffers,
    "minimum_L1_startup_buffer": Fraction(1),
    "zero_buffer_phase_exists": False,
    "prefixes_checked_per_phase": 100,
    "status": "passed",
})

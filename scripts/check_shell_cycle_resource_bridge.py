#!/usr/bin/env python3
from fractions import Fraction

# Rows are the three cycle inequalities from docs/517; columns are controls 1,2,3.
H = (
    (1, 1, 0),
    (0, 1, 1),
    (1, 0, 1),
)
TARGETS_20 = (Fraction(3, 5), Fraction(1, 2), Fraction(2, 5))
WORD_20 = "213121212122233IIIII"
COUNTS_20 = (5, 7, 3)


def determinant3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def matvec(matrix, vector):
    return tuple(sum(matrix[row][column] * vector[column] for column in range(3)) for row in range(3))


assert determinant3(H) == 2
source_actions = tuple(tuple(H[row][column] for row in range(3)) for column in range(3))
assert source_actions == ((1, 0, 1), (1, 1, 0), (0, 1, 1))

used = [0, 0, 0]
cycle_max = [Fraction(0), Fraction(0), Fraction(0)]
for time, symbol in enumerate(WORD_20, 1):
    if symbol != "I":
        used[int(symbol) - 1] += 1
    delivered = matvec(H, used)
    deficits = tuple(TARGETS_20[row] * time - delivered[row] for row in range(3))
    cycle_max = [max(cycle_max[row], deficits[row]) for row in range(3)]
assert tuple(cycle_max) == (Fraction(0), Fraction(0), Fraction(2, 5))
assert tuple(used) == COUNTS_20

# The startup action buffer stored in docs/517 maps to the required cycle reserve.
action_buffer = (Fraction(2, 5), Fraction(0), Fraction(0))
cycle_buffer = matvec(H, action_buffer)
assert cycle_buffer == (Fraction(2, 5), Fraction(0), Fraction(2, 5))
assert all(cycle_buffer[row] >= cycle_max[row] for row in range(3))

# The three-slot source-action period also has an exact cycle-coordinate phase table.
unit_word = (0, 1, 2)
unit_target = (Fraction(2, 3),) * 3
phase_buffers = []
for phase in range(3):
    word = unit_word[phase:] + unit_word[:phase]
    delivered = [0, 0, 0]
    maximum = [Fraction(0), Fraction(0), Fraction(0)]
    for time, action in enumerate(word, 1):
        for row in range(3):
            delivered[row] += H[row][action]
        for row in range(3):
            maximum[row] = max(maximum[row], unit_target[row] * time - delivered[row])
    phase_buffers.append(tuple(maximum))
assert tuple(phase_buffers) == (
    (Fraction(0), Fraction(2, 3), Fraction(1, 3)),
    (Fraction(1, 3), Fraction(0), Fraction(2, 3)),
    (Fraction(2, 3), Fraction(1, 3), Fraction(0)),
)

print({
    "cycle_action_incidence": H,
    "determinant": determinant3(H),
    "source_action_vectors": source_actions,
    "twenty_slot_cycle_deficits": tuple(str(value) for value in cycle_max),
    "action_buffer": tuple(str(value) for value in action_buffer),
    "mapped_cycle_buffer": tuple(str(value) for value in cycle_buffer),
    "three_slot_cycle_phase_buffers": [tuple(str(value) for value in row) for row in phase_buffers],
    "conclusion": "docs/517 and the canonical service-action model are related by one explicit full-rank incidence map",
    "remaining_gap": "the three stored cycle inequalities are not identified with actual clean-macro shell resources",
    "evidence_level": "repository_source_cycle_bridge",
    "status": "passed",
})

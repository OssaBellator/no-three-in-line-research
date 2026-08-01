#!/usr/bin/env python3
from fractions import Fraction

FRONTIERS = ("boundary", "hall", "threshold", "prefix", "shell", "integration")
ACTUAL_ROW_EVIDENCE = {frontier: "fixture_derived" for frontier in FRONTIERS}
CANDIDATE_FIELDS = {
    "boundary": (3, 5),
    "hall": (5, 5),
    "threshold": (4, 5),
    "prefix": (5, 5),
    "shell": (5, 5),
    "integration": (1, 5),
}
LATEST_RESULTS = {
    "boundary": "eight five-block paths at offset radius 32 and no six-block path",
    "hall": "twelve coordinate grid pairs and eighteen no-three-in-line matching extensions",
    "threshold": "zero geometrically legal decompositions of the aligned conservative matrix",
    "prefix": "state-terminal cell multisets cannot recover ancestry-sensitive nesting risk",
    "shell": "full-rank cycle/action incidence bridge from docs/517",
    "integration": "no direct row or coupling coefficient promoted",
}

assert sum(done for done, _ in CANDIDATE_FIELDS.values()) == 23
assert sum(total for _, total in CANDIDATE_FIELDS.values()) == 30
assert all(level == "fixture_derived" for level in ACTUAL_ROW_EVIDENCE.values())

BASE = (
    Fraction(7, 120),
    Fraction(11723, 524288),
    Fraction(1, 24),
    Fraction(1, 40),
    Fraction(1, 40),
    Fraction(1, 48),
)
C = [[Fraction(0) for _ in range(6)] for _ in range(6)]
C[0][5] = Fraction(1, 200)
C[1][0] = Fraction(1, 100)
C[2][1] = Fraction(1, 120)
C[3][2] = Fraction(1, 160)
C[4][3] = Fraction(1, 120)
C[5][4] = Fraction(1, 200)

# Solve (I-C)y=b exactly.
augmented = []
for row in range(6):
    augmented.append([
        Fraction(int(row == column)) - C[row][column]
        for column in range(6)
    ] + [BASE[row]])
for column in range(6):
    pivot = next(row for row in range(column, 6) if augmented[row][column])
    augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
    value = augmented[column][column]
    augmented[column] = [entry / value for entry in augmented[column]]
    for row in range(6):
        if row == column or not augmented[row][column]:
            continue
        factor = augmented[row][column]
        augmented[row] = [
            augmented[row][index] - factor * augmented[column][index]
            for index in range(7)
        ]
solution = tuple(augmented[row][-1] for row in range(6))
for row in range(6):
    assert solution[row] == BASE[row] + sum(C[row][column] * solution[column] for column in range(6))

total = sum(solution)
slack = Fraction(1, 4) - total
assert total == Fraction(705466760524005697, 3623878655999606784)
assert slack == Fraction(200502903475895999, 3623878655999606784)
assert slack > 0

promoted_rows = tuple(frontier for frontier, level in ACTUAL_ROW_EVIDENCE.items() if level == "geometric_verified")
assert promoted_rows == ()

print({
    "candidate_fields_complete": 23,
    "candidate_fields_total": 30,
    "latest_coordinate_results": LATEST_RESULTS,
    "actual_row_evidence": ACTUAL_ROW_EVIDENCE,
    "promoted_rows": promoted_rows,
    "fixture_fixed_point_total": str(total),
    "fixture_arithmetic_slack": str(slack),
    "geometric_closure_allowed": False,
    "status": "passed",
})

#!/usr/bin/env python3
from fractions import Fraction

FRONTIERS = ("boundary", "hall", "threshold", "prefix", "shell", "integration")
BASE = (
    Fraction(7, 120),
    Fraction(11723, 524288),
    Fraction(1, 24),
    Fraction(1, 40),
    Fraction(1, 40),
    Fraction(1, 48),
)
C = [[Fraction(0) for _ in FRONTIERS] for _ in FRONTIERS]
C[0][5] = Fraction(1, 200)
C[1][0] = Fraction(1, 100)
C[2][1] = Fraction(1, 120)
C[3][2] = Fraction(1, 160)
C[4][3] = Fraction(1, 120)
C[5][4] = Fraction(1, 200)


def solve_linear(matrix, rhs):
    n = len(rhs)
    work = [
        [Fraction(matrix[row][column]) for column in range(n)] + [Fraction(rhs[row])]
        for row in range(n)
    ]
    for column in range(n):
        pivot = next(row for row in range(column, n) if work[row][column])
        work[column], work[pivot] = work[pivot], work[column]
        value = work[column][column]
        work[column] = [entry / value for entry in work[column]]
        for row in range(n):
            if row == column or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][index] - factor * work[column][index]
                for index in range(n + 1)
            ]
    return tuple(work[row][-1] for row in range(n))


system = [
    [Fraction(int(row == column)) - C[row][column] for column in range(6)]
    for row in range(6)
]
fixed_point = solve_linear(system, BASE)
for row in range(6):
    assert fixed_point[row] == BASE[row] + sum(
        C[row][column] * fixed_point[column] for column in range(6)
    )

fixed_total = sum(fixed_point)
slack = Fraction(1, 4) - fixed_total
assert fixed_total == Fraction(705466760524005697, 3623878655999606784)
assert slack == Fraction(200502903475895999, 3623878655999606784)
assert slack > 0

candidate_fields = {
    "boundary": (3, 5),
    "hall": (5, 5),
    "threshold": (4, 5),
    "prefix": (5, 5),
    "shell": (5, 5),
    "integration": (1, 5),
}
assert sum(value[0] for value in candidate_fields.values()) == 23
assert sum(value[1] for value in candidate_fields.values()) == 30

conversion_levels = {
    "boundary": "inherited_line_state_obstruction",
    "hall": "repository_typed_complete_grid_decoder",
    "threshold": "source_matrix_partial_normal_census",
    "prefix": "automaton_decoded_risk_census",
    "shell": "repository_source_action_aligned",
    "integration": "fixture_derived",
}
actual_row_evidence = {frontier: "fixture_derived" for frontier in FRONTIERS}
assert all(level == "fixture_derived" for level in actual_row_evidence.values())

print(
    {
        "candidate_field_completion": {
            frontier: f"{done}/{total}"
            for frontier, (done, total) in candidate_fields.items()
        },
        "completed_candidate_fields": 23,
        "total_candidate_fields": 30,
        "candidate_complete_frontiers": ("hall", "prefix", "shell"),
        "conversion_levels": conversion_levels,
        "actual_global_row_evidence": actual_row_evidence,
        "actual_rows_promoted": 0,
        "exact_fixture_fixed_point": tuple(str(value) for value in fixed_point),
        "exact_fixture_total": str(fixed_total),
        "exact_fixture_slack": str(slack),
        "geometric_closure_allowed": False,
        "next_blockers": {
            "boundary": "unbounded or compressible inherited line history",
            "hall": "coordinate-level endpoint-cell identification",
            "threshold": "complete actual residual normal list",
            "prefix": "coordinate-level support-chord decoder",
            "shell": "clean-macro resource identification",
            "integration": "geometric direct rows and couplings",
        },
        "status": "passed",
    }
)

#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = ROOT / "certificates" / "prime-patching-independent-extraction-561-566.json"

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


def solve_linear(matrix, vector):
    size = len(vector)
    work = [
        [Fraction(matrix[i][j]) for j in range(size)] + [Fraction(vector[i])]
        for i in range(size)
    ]
    for column in range(size):
        pivot = next(row for row in range(column, size) if work[row][column])
        work[column], work[pivot] = work[pivot], work[column]
        value = work[column][column]
        work[column] = [entry / value for entry in work[column]]
        for row in range(size):
            if row == column or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][index] - factor * work[column][index]
                for index in range(size + 1)
            ]
    return tuple(work[index][-1] for index in range(size))


data = json.loads(CERTIFICATE.read_text())
frontiers = data["independent_extractions"]
assert set(frontiers) == {"boundary", "hall", "threshold", "prefix", "shell", "integration"}

completed = sum(entry["completed_required_fields"] for entry in frontiers.values())
total = sum(entry["total_required_fields"] for entry in frontiers.values())
assert (completed, total) == (22, 30)
assert data["global_summary"]["candidate_complete_frontiers"] == ["prefix", "shell"]
assert data["global_summary"]["actual_rows_promoted"] == 0
assert set(data["actual_global_row_evidence"].values()) == {"fixture_derived"}
assert data["global_summary"]["geometric_closure_allowed"] is False

matrix = [
    [Fraction(int(i == j)) - C[i][j] for j in range(6)]
    for i in range(6)
]
fixed_point = solve_linear(matrix, BASE)
for i in range(6):
    assert fixed_point[i] == BASE[i] + sum(C[i][j] * fixed_point[j] for j in range(6))

fixed_total = sum(fixed_point, Fraction(0))
assert fixed_total == Fraction(705466760524005697, 3623878655999606784)
slack = Fraction(1, 4) - fixed_total
assert slack == Fraction(200502903475895999, 3623878655999606784)
assert slack > 0

arithmetic_feasible = fixed_total < Fraction(1, 4)
evidence_gate = all(
    level == "geometric_verified"
    for level in data["actual_global_row_evidence"].values()
)
assert arithmetic_feasible is True
assert evidence_gate is False
assert not (arithmetic_feasible and evidence_gate)

print({
    "candidate_field_completion": f"{completed}/{total}",
    "candidate_complete_frontiers": data["global_summary"]["candidate_complete_frontiers"],
    "actual_rows_promoted": 0,
    "exact_fixed_point": [str(value) for value in fixed_point],
    "exact_fixed_total": str(fixed_total),
    "exact_arithmetic_slack": str(slack),
    "arithmetic_feasible": arithmetic_feasible,
    "geometric_evidence_gate": evidence_gate,
    "global_closure": False,
    "status": "passed",
})

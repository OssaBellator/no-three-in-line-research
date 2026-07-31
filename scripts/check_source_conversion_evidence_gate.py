#!/usr/bin/env python3
from fractions import Fraction

# Candidate extraction field counts remain separate from actual geometric rows.
FIELDS = {
    "boundary": (3, 5, "shortest bounded offset cycles obstructed globally"),
    "hall": (4, 5, "generic complete-choice-grid pair decoder; no endpoint-cell map"),
    "threshold": (4, 5, "aligned source matrix and observables; actual normal list absent"),
    "prefix": (5, 5, "dual grading and structural risk complete; geometric risk absent"),
    "shell": (5, 5, "canonical source-service incidence complete; geometric shell map absent"),
    "integration": (1, 5, "benchmark fixed point only"),
}
completed = sum(value[0] for value in FIELDS.values())
total = sum(value[1] for value in FIELDS.values())
assert (completed, total) == (22, 30)

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

# Exact fixed-point iteration over rationals converges rapidly because this is one directed cycle.
y = list(BASE)
for _ in range(20):
    y = [BASE[i] + sum(C[i][j] * y[j] for j in range(6)) for i in range(6)]
recorded_total = Fraction(705466760524005697, 3623878655999606784)
assert abs(sum(y) - recorded_total) < Fraction(1, 10**30)
assert recorded_total < Fraction(1, 4)

actual_rows = {name: "fixture_derived" for name in FIELDS}
assert all(level == "fixture_derived" for level in actual_rows.values())

print({
    "candidate_fields_completed": completed,
    "candidate_fields_total": total,
    "frontier_results": {name: result for name, (_, _, result) in FIELDS.items()},
    "actual_row_evidence": actual_rows,
    "actual_rows_promoted": 0,
    "fixture_fixed_point_total": str(recorded_total),
    "fixture_arithmetic_slack": str(Fraction(1, 4) - recorded_total),
    "geometric_closure_allowed": False,
    "status": "passed",
})

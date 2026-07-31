#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "certificates" / "prime-patching-provenance-audit-555-560.json"
data = json.loads(DATA.read_text())
frontiers = data["frontiers"]
order = ("boundary", "hall", "threshold", "prefix", "shell", "interaction")
evidence_key = {"interaction": "integration"}
record = frontiers["integration"]


def frontier_record(name):
    return frontiers[evidence_key.get(name, name)]


assert all(frontier_record(name)["evidence_level"] == "fixture_derived" for name in order)
assert all(frontier_record(name)["independent_geometric_source"] is None for name in order)

base = tuple(Fraction(value) for value in record["base_rows"])
y = tuple(Fraction(value) for value in record["supersolution"])
index = {name: i for i, name in enumerate(order)}
C = [[Fraction(0) for _ in order] for _ in order]
for edge in record["coupling_edges"]:
    C[index[edge["to"]]][index[edge["from"]]] = Fraction(edge["weight"])

for i in range(6):
    assert base[i] + sum(C[i][j] * y[j] for j in range(6)) <= y[i]
assert sum(y) == Fraction(99, 500)
assert Fraction(1, 4) - sum(y) == Fraction(13, 250)

# Solve (I-C)x=b exactly to expose the minimal arithmetic fixed point.
A = [[Fraction(int(i == j)) - C[i][j] for j in range(6)] for i in range(6)]
rhs = list(base)
for col in range(6):
    pivot = next(row for row in range(col, 6) if A[row][col])
    A[col], A[pivot] = A[pivot], A[col]
    rhs[col], rhs[pivot] = rhs[pivot], rhs[col]
    scale = A[col][col]
    A[col] = [value / scale for value in A[col]]
    rhs[col] /= scale
    for row in range(6):
        if row == col:
            continue
        factor = A[row][col]
        if factor:
            A[row] = [A[row][j] - factor * A[col][j] for j in range(6)]
            rhs[row] -= factor * rhs[col]
fixed_point = tuple(rhs)
for i in range(6):
    assert fixed_point[i] == base[i] + sum(C[i][j] * fixed_point[j] for j in range(6))
    assert fixed_point[i] <= y[i]

cycle_product = Fraction(1, 200 * 100 * 120 * 160 * 120 * 200)
assert cycle_product == Fraction(1, 9216000000000)
assert sum(fixed_point) < sum(y) < Fraction(1, 4)

# Evidence closure is stricter than arithmetic closure.
realized_rows = sum(frontier_record(name)["evidence_level"] == "geometric_verified" for name in order)
assert realized_rows == 0
assert not (realized_rows == 6)

print({
    "arithmetic_supersolution_sum": str(sum(y)),
    "arithmetic_supersolution_slack": str(Fraction(1, 4) - sum(y)),
    "minimal_fixed_point_sum": str(sum(fixed_point)),
    "minimal_fixed_point_decimal": f"{float(sum(fixed_point)):.12f}",
    "coupling_cycle_product": str(cycle_product),
    "geometrically_verified_rows": realized_rows,
    "evidence_closed": False,
    "status": "passed",
})

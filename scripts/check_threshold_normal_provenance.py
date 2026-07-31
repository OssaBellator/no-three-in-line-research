#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "certificates" / "prime-patching-provenance-audit-555-560.json"
record = json.loads(DATA.read_text())["frontiers"]["threshold"]
facets = tuple(tuple(Fraction(value) for value in row) for row in record["facet_normals"])

assert record["evidence_level"] == "fixture_derived"
assert record["independent_geometric_source"] is None
assert record["quotient_map"] is None
assert record["source_inequality_ids"] == []

# The stored common box has widths one in both quotient coordinates.
widths = (1, 1)
dual_bounds = tuple(sum(abs(coefficient) * width for coefficient, width in zip(facet, widths)) for facet in facets)
assert max(dual_bounds) == Fraction(1, 32)

# Exact factorization model: physical coordinates are (q1,q2,h), while the
# quotient keeps only q1,q2. A physical normal factors through the quotient iff
# its hidden-coordinate coefficient is zero.
Q = ((1, 0, 0), (0, 1, 0))
lifted_facets = tuple((row[0], row[1], Fraction(0)) for row in facets)
for physical in lifted_facets:
    coefficients = physical[:2]
    reconstructed = tuple(sum(coefficients[i] * Q[i][j] for i in range(2)) for j in range(3))
    assert reconstructed == physical

hidden_witness = (Fraction(0), Fraction(0), Fraction(1))
assert all(
    tuple(sum(coefficients[i] * Q[i][j] for i in range(2)) for j in range(3)) != hidden_witness
    for coefficients in [(Fraction(a), Fraction(b)) for a in range(-2, 3) for b in range(-2, 3)]
)

# A quotient discrepancy box cannot control a residual physical normal in ker(Q).
physical_increment = (0, 0, 7)
quotient_increment = tuple(sum(Q[i][j] * physical_increment[j] for j in range(3)) for i in range(2))
assert quotient_increment == (0, 0)
assert sum(hidden_witness[j] * physical_increment[j] for j in range(3)) == 7

assert len(record["required_for_promotion"]) == 5
print({
    "stored_facets": len(facets),
    "stored_dual_box_loss": str(max(dual_bounds)),
    "trivially_factorable_fixture_facets": len(lifted_facets),
    "hidden_normal_counterexample": [str(value) for value in hidden_witness],
    "source_inequality_ids_present": 0,
    "quotient_map_extracted": False,
    "status": "passed",
})

#!/usr/bin/env python3
import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "certificates" / "prime-patching-provenance-audit-555-560.json"
record = json.loads(DATA.read_text())["frontiers"]["shell"]
X, Y = tuple(tuple(tuple(step) for step in word) for word in record["component_words"])
incidence = tuple(tuple(row) for row in record["incidence_matrix"])

assert record["evidence_level"] == "fixture_derived"
assert record["independent_geometric_source"] is None
assert record["selected_phase"] == [0, 0]
assert record["slotwise_component_sum_zero"] is True

combined = tuple(tuple(X[t][j] + Y[t][j] for j in range(2)) for t in range(3))
assert combined == ((0, 0), (0, 0), (0, 0))


def map_word(matrix):
    return tuple(
        tuple(sum(row[j] * increment[j] for j in range(2)) for row in matrix)
        for increment in combined
    )

# Because cancellation happens before the physical incidence map, every matrix—
# including matrices with different dimensions and ranks—produces zero reserve.
matrices = (
    incidence,
    ((1, 2),),
    ((1, 0), (0, 1)),
    ((2, -3), (5, 7), (11, 13), (17, 19)),
)
for matrix in matrices:
    assert all(all(value == 0 for value in increment) for increment in map_word(matrix))

# A nonzero component residual distinguishes incidence matrices immediately.
witness = (1, -1)
images = {
    tuple(sum(row[j] * witness[j] for j in range(2)) for row in matrix)
    for matrix in matrices
}
assert len(images) == len(matrices)

assert len(record["required_for_promotion"]) == 5
print({
    "component_slots": len(combined),
    "slotwise_precancellation": True,
    "incidence_matrices_indistinguishable_on_fixture": len(matrices),
    "incidence_matrices_distinguished_off_fixture": len(images),
    "physical_incidence_extracted": False,
    "status": "passed",
})

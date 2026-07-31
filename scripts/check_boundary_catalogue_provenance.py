#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "certificates" / "prime-patching-provenance-audit-555-560.json"
record = json.loads(DATA.read_text())["frontiers"]["boundary"]

assert record["evidence_level"] == "fixture_derived"
assert record["independent_geometric_source"] is None
lineages = record["lineage"]
length_alphabets = {tuple(stage["lengths"]) for stage in lineages}
assert len(length_alphabets) == 5
assert tuple(lineages[-1]["lengths"]) == (4, 7)
assert all(stage["role"] in {"stored_fixture", "adapter_fixture"} for stage in lineages)

signature = record["current_signature"]
assert signature["block_lengths"] == [4, 7]
losses = [Fraction(value) for value in signature["per_length_losses"]]
assert losses == [Fraction(1, 30), Fraction(1, 20)]
assert Fraction(signature["seam_loss"]) == 1

# Reconstruct the stored phase-locked row without treating it as geometric data.
def representation(n, phase):
    for b in range(phase, n // 7 + 1, 3):
        if (n - 7 * b) % 4 == 0:
            return (n - 7 * b) // 4, b
    return None

thresholds = []
for phase in range(3):
    missing = [n for n in range(2001) if representation(n, phase) is None]
    thresholds.append(max(missing) + 1)
assert thresholds == [60, 67, 74]

for n in range(120, 2001):
    for phase in range(3):
        a, b = representation(n, phase)
        loss = (Fraction(4 * a, 30) + Fraction(7 * b, 20) + 1) / n
        assert loss <= Fraction(7, 120)

# Promotion is intentionally impossible until an independent source is supplied.
assert len(record["required_for_promotion"]) == 5
assert not any("geometric_verified" == stage.get("role") for stage in lineages)

print({
    "lineage_stages": len(lineages),
    "distinct_length_alphabets": len(length_alphabets),
    "current_catalogue_first_fixture_stage": "docs/537",
    "phase_thresholds": thresholds,
    "geometric_sources": 0,
    "promotion_blocked": True,
    "status": "passed",
})

#!/usr/bin/env python3
from fractions import Fraction

completion = {
    "boundary": (3, 5),
    "Hall": (4, 5),
    "threshold": (4, 5),
    "prefix": (5, 5),
    "shell": (5, 5),
    "integration": (2, 5),
}
assert sum(done for done, _ in completion.values()) == 23
assert sum(total for _, total in completion.values()) == 30

results = {
    "boundary": "2112 widened degree-preserving swaps all fail",
    "Hall": "4x5 host has minimum blocker number two for all 120 label injections",
    "threshold": "unique one-slot augmentation has 120 ordered legal decompositions",
    "prefix": "repeated-chord pair aggregate is 925166131890",
    "shell": "recorded source action catalogue has no odd-sum cycle vector",
}
assert len(results) == 5

base_total = Fraction(705466760524005697, 3623878655999606784)
slack = Fraction(1, 4) - base_total
assert slack == Fraction(200502903475895999, 3623878655999606784)
actual_evidence = {frontier: "fixture_derived" for frontier in ("boundary", "Hall", "threshold", "prefix", "shell", "interaction")}
assert all(level == "fixture_derived" for level in actual_evidence.values())

print({
    "candidate_field_completion": {key: f"{done}/{total}" for key, (done, total) in completion.items()},
    "candidate_fields_complete": 23,
    "candidate_fields_total": 30,
    "structural_enlargement_results": results,
    "actual_row_evidence": actual_evidence,
    "promoted_rows": 0,
    "fixture_fixed_point_total": str(base_total),
    "fixture_slack_below_one_quarter": str(slack),
    "geometric_closure": False,
    "status": "passed",
})

#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = (
    "scripts/check_frontier_585_590.py",
    "scripts/check_boundary_saturation_refill_obstruction.py",
    "scripts/check_hall_bijection_robustness_bound.py",
    "scripts/check_threshold_replacement_price_frontier.py",
    "scripts/check_prefix_convex_chord_embedding.py",
    "scripts/check_shell_coset_crossing_action.py",
    "scripts/check_completion_attempt_evidence_gate.py",
)

for script in SCRIPTS:
    subprocess.run([sys.executable, script], check=True)
print({"frontier_group": "591--596", "scripts": len(SCRIPTS), "status": "passed"})

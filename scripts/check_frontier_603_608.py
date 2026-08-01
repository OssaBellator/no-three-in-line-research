#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = (
    "scripts/check_frontier_597_602.py",
    "scripts/check_boundary_five_point_refill_obstruction.py",
    "scripts/check_hall_lifted_conditional_star.py",
    "scripts/check_threshold_augmentation_source_margin.py",
    "scripts/check_prefix_distinct_run_chord_triples.py",
    "scripts/check_shell_recorded_closure_parity.py",
    "scripts/check_source_identification_evidence_gate.py",
)

for script in SCRIPTS:
    subprocess.run([sys.executable, script], check=True)

print({"frontier_group": "603-608", "scripts": len(SCRIPTS), "status": "passed"})

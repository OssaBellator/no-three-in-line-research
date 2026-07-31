#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_frontier_555_560.py",
    "check_boundary_coordinate_seam_attempt.py",
    "check_independent_hall_microcensus.py",
    "check_threshold_source_layer_alignment.py",
    "check_node_graded_prefix_risk_dp.py",
    "check_nonprecancelled_shell_incidence.py",
    "check_independent_extraction_evidence_gate.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "561-566", "all_checks_passed": True})

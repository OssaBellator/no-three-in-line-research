#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_frontier_579_584.py",
    "check_boundary_three_point_seam_repair.py",
    "check_hall_single_exclusion_robustness.py",
    "check_nearest_legal_threshold_matrix.py",
    "check_prefix_ancestry_span_dp.py",
    "check_shell_index_two_resource_lattice.py",
    "check_replacement_evidence_gate.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "585-590", "all_checks_passed": True})

#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_marker_controller_synthesis.py",
    "check_optimal_erasure_hall_tags.py",
    "check_threshold_basis_path_traversal.py",
    "check_branch_and_bound_unequal_codes.py",
    "check_multicritical_descent_lp.py",
    "check_adaptive_interaction_truncation.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "459-464", "all_checks_passed": True})

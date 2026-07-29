#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_robust_marker_controller_synthesis.py",
    "check_error_erasure_hall_tags.py",
    "check_degenerate_threshold_basis_fan.py",
    "check_symmetry_reduced_unequal_code_dp.py",
    "check_shell_face_line_search.py",
    "check_minimum_work_interaction_dp.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "465-470", "all_checks_passed": True})

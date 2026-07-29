#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_marker_residue_correctors.py",
    "check_qary_hall_fourier_mixing.py",
    "check_prefix_balanced_threshold_schedules.py",
    "check_regular_prefix_code_generating_function.py",
    "check_buffered_shell_periodic_schedule.py",
    "check_vector_interaction_residue_frontiers.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "513-518", "all_checks_passed": True})

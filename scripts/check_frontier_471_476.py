#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_budget_coupled_robust_marker_controllers.py",
    "check_concatenated_hall_color_tags.py",
    "check_threshold_value_monodromy.py",
    "check_quotient_code_reconstruction.py",
    "check_shell_cycle_cutting_plane.py",
    "check_multioutput_interaction_pareto.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "471-476", "all_checks_passed": True})

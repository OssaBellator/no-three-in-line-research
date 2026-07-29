#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_double_oracle_marker_controllers.py",
    "check_block_list_hall_decoding.py",
    "check_threshold_inverse_design.py",
    "check_recursive_prefix_code_orbits.py",
    "check_shell_potential_compactification.py",
    "check_tree_decomposed_interaction_pareto.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "483-488", "all_checks_passed": True})

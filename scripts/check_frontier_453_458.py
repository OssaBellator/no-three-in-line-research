#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_cyclic_marker_automata.py",
    "check_erasure_resilient_hall_colors.py",
    "check_parametric_threshold_basis_regions.py",
    "check_pruned_unequal_symbol_code_dp.py",
    "check_multicritical_shell_faces.py",
    "check_interaction_automaton_truncation.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "453-458", "all_checks_passed": True})

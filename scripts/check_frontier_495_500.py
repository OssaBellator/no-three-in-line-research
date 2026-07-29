#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_balanced_binary_marker_schedules.py",
    "check_sparse_mitm_hall_syndromes.py",
    "check_parametric_threshold_projection_regions.py",
    "check_canonical_prefix_tree_augmentation.py",
    "check_multiparametric_shell_chambers.py",
    "check_pareto_transfer_matrix_power.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "495-500", "all_checks_passed": True})

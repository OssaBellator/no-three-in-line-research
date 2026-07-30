#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_mixed_length_marker_semigroups.py",
    "check_switched_hall_dobrushin.py",
    "check_cyclic_threshold_layer_discrepancy.py",
    "check_regular_prefix_entropy_profile.py",
    "check_mixed_period_shell_supercycles.py",
    "check_normal_interaction_semigroups.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "531-536", "all_checks_passed": True})

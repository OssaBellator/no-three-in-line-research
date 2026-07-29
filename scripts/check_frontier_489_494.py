#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_periodic_marker_controller_realization.py",
    "check_syndrome_hall_list_decoding.py",
    "check_nearest_threshold_design.py",
    "check_prefix_code_orbit_inventory.py",
    "check_parametric_shell_attenuation_path.py",
    "check_width_two_interaction_join_tree.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "489-494", "all_checks_passed": True})

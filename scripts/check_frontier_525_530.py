#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_multicritical_marker_minplus.py",
    "check_noncommuting_hall_transfer_products.py",
    "check_steinitz_threshold_layer_ordering.py",
    "check_regular_prefix_singularity.py",
    "check_order_optimized_shell_periods.py",
    "check_multicritical_interaction_cones.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "525-530", "all_checks_passed": True})

#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_column_generated_marker_controllers.py",
    "check_heterogeneous_concatenated_hall_tags.py",
    "check_threshold_value_fan_point_location.py",
    "check_prefix_code_burnside_orbits.py",
    "check_shell_cycle_separation_and_circulation.py",
    "check_blockwise_interaction_pareto_convolution.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "477-482", "all_checks_passed": True})

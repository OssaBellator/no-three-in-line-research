#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_apery_marker_certificates.py",
    "check_automaton_switched_hall_products.py",
    "check_threshold_cycle_concatenation.py",
    "check_regular_prefix_profile_clt.py",
    "check_shared_shell_reserves.py",
    "check_interaction_normal_fans.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "537-542", "all_checks_passed": True})

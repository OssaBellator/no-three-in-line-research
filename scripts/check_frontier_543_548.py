#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_six_frontier_parameter_ledger.py",
    "check_phase_locked_marker_semigroup.py",
    "check_optimal_slack_purchase.py",
    "check_product_synchronizer_automaton.py",
    "check_all_length_balanced_rounding.py",
    "check_end_to_end_compatibility_fixture.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "543-548", "all_checks_passed": True})

#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_realizable_stopping_symbol_chains.py",
    "check_hall_core_petal_edge_coloring.py",
    "check_threshold_lp_complementary_slackness.py",
    "check_unequal_symbol_prefix_trees.py",
    "check_exact_critical_shell_cycles.py",
    "check_condensation_resolvent_sensitivities.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "441-446", "all_checks_passed": True})

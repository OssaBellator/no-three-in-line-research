#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_acyclic_marker_automata.py",
    "check_color_coded_hall_banks.py",
    "check_threshold_lp_basis_certificates.py",
    "check_unequal_symbol_code_dp.py",
    "check_critical_cycle_stability_cones.py",
    "check_higher_order_condensation_sensitivities.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "447-452", "all_checks_passed": True})

#!/usr/bin/env python3
import subprocess
import sys

# Preserve the immediately preceding compatibility audit before running the new
# realization-adapter tranche.
subprocess.run([sys.executable, "scripts/check_frontier_543_548.py"], check=True)

SCRIPTS = [
    "check_boundary_signature_adapter.py",
    "check_hall_lumpability_adapter.py",
    "check_threshold_facet_adapter.py",
    "check_prefix_profile_risk_adapter.py",
    "check_shell_incidence_adapter.py",
    "check_coupled_frontier_supersolution.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "549-554", "all_checks_passed": True})

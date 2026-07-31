#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_frontier_549_554.py",
    "check_boundary_catalogue_provenance.py",
    "check_hall_microcensus_independence.py",
    "check_threshold_normal_provenance.py",
    "check_prefix_risk_census_provenance.py",
    "check_shell_incidence_provenance.py",
    "check_integration_evidence_closure.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "555-560", "all_checks_passed": True})

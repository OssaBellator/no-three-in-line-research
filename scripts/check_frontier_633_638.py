#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS=(
    "scripts/check_frontier_627_632.py",
    "scripts/check_boundary_eleventh_transition.py",
    "scripts/check_hall_mixed_degree_extraction.py",
    "scripts/check_threshold_c6_circuit.py",
    "scripts/check_prefix_saturated_anchor_reservoir_12.py",
    "scripts/check_shell_collateral_budget.py",
    "scripts/check_scalable_source_realization_gate.py",
)
for script in SCRIPTS:
    subprocess.run([sys.executable,script],check=True)
print({"frontier_group":"633-638","scripts":len(SCRIPTS),"status":"passed"})

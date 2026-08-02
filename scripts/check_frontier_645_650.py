#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = (
    "scripts/check_frontier_639_644.py",
    "scripts/check_boundary_thirteenth_transition.py",
    "scripts/check_hall_bad_centre_amplification.py",
    "scripts/check_threshold_distinct_transient_batch.py",
    "scripts/check_prefix_13_to_14_extension_obstruction.py",
    "scripts/check_shell_recurring_collateral.py",
    "scripts/check_uniformity_frontier_gate.py",
)

for script in SCRIPTS:
    subprocess.run([sys.executable, script], check=True)

print({"frontier_group":"645-650","scripts":len(SCRIPTS),"status":"passed"})

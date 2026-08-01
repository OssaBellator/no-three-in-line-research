#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS=(
    "scripts/check_frontier_621_626.py",
    "scripts/check_boundary_radius64_transition.py",
    "scripts/check_hall_sharp_degree_two_extraction.py",
    "scripts/check_threshold_atomic_six_cycle.py",
    "scripts/check_prefix_saturated_anchor_reservoir.py",
    "scripts/check_shell_weighted_odd_column.py",
    "scripts/check_geometric_source_realization_gate.py",
)
for script in SCRIPTS:
    subprocess.run([sys.executable,script],check=True)
print({"frontier_group":"627-632","scripts":len(SCRIPTS),"status":"passed"})

#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / "check_frontier_663_668.py")], check=True)
checks = [
    "check_boundary_seventeenth_transition.py",
    "check_hall_component_resource_packing.py",
    "check_threshold_facet_hidden_mass.py",
    "check_prefix_matching_orbits.py",
    "check_shell_polyhedral_cycle_robustness.py",
    "check_hidden_compensation_gate.py",
]
for check in checks:
    subprocess.run([sys.executable, str(HERE / check)], check=True)
print({"frontier":"669-674","checks":checks,"status":"passed"})

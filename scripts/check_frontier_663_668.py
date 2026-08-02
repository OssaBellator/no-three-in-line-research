#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run([sys.executable,str(HERE / "check_frontier_657_662.py")],check=True)
checks = [
    "check_boundary_sixteenth_transition.py",
    "check_hall_local_resource_incidence.py",
    "check_threshold_legal_convex_separation.py",
    "check_prefix_coordinate_rerouting_lift.py",
    "check_shell_interval_cycle_robustness.py",
    "check_coordinate_compensation_gate.py",
]
for check in checks:
    subprocess.run([sys.executable,str(HERE / check)],check=True)
print({"frontier":"663-668","checks":checks,"status":"passed"})

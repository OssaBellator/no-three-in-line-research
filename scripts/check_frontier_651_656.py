#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / "check_frontier_645_650.py")], check=True)
checks = [
    "check_boundary_fourteenth_transition.py",
    "check_hall_overlap_packing.py",
    "check_hall_conflict_graph_packing.py",
    "check_hall_cross_copy_conflict_packing.py",
    "check_threshold_factorized_exposure_collision.py",
    "check_threshold_sign_coherent_drift.py",
    "check_prefix_saturated_anchor_reservoir_14.py",
    "check_prefix_component_anchor_obstruction.py",
    "check_shell_heterogeneous_schedule.py",
    "check_shell_irregular_period_schedule.py",
    "check_uniform_mechanism_gate.py",
]
for check in checks:
    subprocess.run([sys.executable, str(HERE / check)], check=True)
print({"frontier":"651-656","checks":checks,"status":"passed"})

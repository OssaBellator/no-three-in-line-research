#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / "check_frontier_651_656.py")], check=True)
checks = [
    "check_boundary_fifteenth_transition.py",
    "check_hall_degree_sequence_packing.py",
    "check_hall_two_level_packing.py",
    "check_threshold_incidence_factorizations.py",
    "check_threshold_factorized_exposure_collision.py",
    "check_threshold_balanced_exposure_batch.py",
    "check_prefix_fourteen_pair_reservoir.py",
    "check_prefix_two_component_rerouting.py",
    "check_shell_repertoire_envelope.py",
    "check_shell_repertoire_cycle_mean.py",
    "check_compensating_mechanism_gate.py",
]
for check in checks:
    subprocess.run([sys.executable, str(HERE / check)], check=True)
print({"frontier":"657-662","checks":checks,"status":"passed"})

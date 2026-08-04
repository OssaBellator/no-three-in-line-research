#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / "check_frontier_669_674.py")], check=True)
checks = [
    "check_boundary_nineteenth_transition.py",
    "check_hall_degree_two_centre_components.py",
    "check_threshold_minimal_hidden_mixture.py",
    "check_prefix_orbit_representative_compositions.py",
    "check_shell_mixed_cycle_realization.py",
    "check_executable_compensation_gate.py",
]
for check in checks:
    subprocess.run([sys.executable, str(HERE / check)], check=True)
print({"frontier":"675-680","checks":checks,"status":"passed"})

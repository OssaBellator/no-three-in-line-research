#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_prefix_coded_stopping_levels.py",
    "check_hall_core_private_markers.py",
    "check_randomized_source_thresholds.py",
    "check_canonical_corridor_codes.py",
    "check_rational_shell_rate_oracle.py",
    "check_condensation_resolvent_dp.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

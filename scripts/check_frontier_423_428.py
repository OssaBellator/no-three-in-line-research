#!/usr/bin/env python3
"""Run every exact diagnostic attached to docs/423--428."""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CHECKS = [
    "check_sequential_petal_marker_trees.py",
    "check_hall_heavy_rectangles.py",
    "check_high_multiplicity_target_stripping.py",
    "check_coded_corridor_bank_schedules.py",
    "check_bounded_path_shell_potentials.py",
    "check_associative_type_elimination.py",
]

for check in CHECKS:
    path = ROOT / "scripts" / check
    subprocess.run([sys.executable, str(path)], cwd=ROOT, check=True)

print(f"all {len(CHECKS)} frontier checks passed")

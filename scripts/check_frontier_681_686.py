#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
subprocess.run([sys.executable,str(HERE/"check_frontier_675_680.py")],check=True)
checks=[
    "check_boundary_nineteenth_obstruction.py",
    "check_hall_odd_path_surplus.py",
    "check_threshold_minimal_layer_decomposition.py",
    "check_prefix_all_physical_unit_routes.py",
    "check_shell_circulation_realization.py",
    "check_rigid_compensation_gate.py",
]
for check in checks:
    subprocess.run([sys.executable,str(HERE/check)],check=True)
print({"frontier":"681-686","checks":checks,"status":"passed"})

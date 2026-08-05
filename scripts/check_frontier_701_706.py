#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run(
    [sys.executable, str(HERE / "check_frontier_693_700.py")],
    check=True,
)
checks = [
    "check_boundary_twentysecond_budget_seven_obstruction_701.py",
    "check_hall_thirty_centre_extremal_signatures_702.py",
    "check_threshold_all_equality_multiples_703.py",
    "check_prefix_all_optimal_all_compositions_704.py",
    "check_shell_three_state_connector_tours_705.py",
    "check_extraction_compensation_gate_706.py",
]
for check in checks:
    subprocess.run([sys.executable, str(HERE / check)], check=True)
print({"frontier": "701-706", "checks": checks, "status": "passed"})

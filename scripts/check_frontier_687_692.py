#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run(
    [sys.executable, str(HERE / "check_frontier_681_686.py")],
    check=True,
)

checks = [
    "check_boundary_nineteenth_low_frontier_obstruction.py",
    "check_hall_packet_transfer_matrix.py",
    "check_threshold_identity_window_density.py",
    "check_prefix_all_optimal_short_compositions.py",
    "check_shell_connector_augmentation.py",
    "check_transfer_compensation_gate.py",
]
for check in checks:
    subprocess.run([sys.executable, str(HERE / check)], check=True)

print({
    "frontier": "687-692",
    "checks": checks,
    "status": "passed",
})

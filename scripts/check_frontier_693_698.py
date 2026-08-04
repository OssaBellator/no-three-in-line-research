#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run(
    [sys.executable, str(HERE / "check_frontier_687_692.py")],
    check=True,
)
checks = [
    "check_boundary_nineteenth_transition.py",
    "check_hall_two_motif_incidence_packets.py",
    "check_threshold_all_window_widths.py",
    "check_prefix_all_optimal_four_run_compositions.py",
    "check_shell_robust_connector_tours.py",
    "check_realization_compensation_gate.py",
]
for check in checks:
    subprocess.run([sys.executable, str(HERE / check)], check=True)
print({
    "frontier": "693-698",
    "checks": checks,
    "status": "passed",
})

#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run(
    [sys.executable, str(HERE / "check_frontier_675_680.py")],
    check=True,
)

checks = [
    "check_hall_defect_incidence_line_graph.py",
    "check_hall_odd_path_surplus.py",
    "check_hall_packet_interface_surplus.py",
    "check_threshold_minimal_hidden_mixture_census.py",
    "check_threshold_minimal_layer_decomposition.py",
    "check_threshold_hidden_layer_windows.py",
    "check_prefix_all_physical_compositions.py",
    "check_shell_robust_circulation.py",
    "check_shell_circulation_realization.py",
    "check_structural_compensation_gate.py",
]
for check in checks:
    subprocess.run([sys.executable, str(HERE / check)], check=True)

print({
    "frontier": "681-686",
    "checks": checks,
    "status": "passed",
})

#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_frontier_573_578.py",
    "check_boundary_large_offset_horizon.py",
    "check_hall_coordinate_grid_extensions.py",
    "check_threshold_geometric_layer_obstruction.py",
    "check_prefix_state_only_cell_obstruction.py",
    "check_shell_cycle_resource_bridge.py",
    "check_coordinate_identification_evidence_gate.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "579-584", "all_checks_passed": True})

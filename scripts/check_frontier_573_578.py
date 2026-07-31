#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_frontier_567_572.py",
    "check_boundary_inherited_line_states.py",
    "check_hall_complete_grid_extensions.py",
    "check_threshold_source_cell_normals.py",
    "check_prefix_support_leaf_risk_decoder.py",
    "check_shell_source_action_bridge.py",
    "check_geometric_decoder_evidence_gate.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "573-578", "all_checks_passed": True})

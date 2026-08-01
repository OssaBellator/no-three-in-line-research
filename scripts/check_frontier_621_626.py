#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = (
    "scripts/check_frontier_615_620.py",
    "scripts/check_boundary_budget_seven_chain.py",
    "scripts/check_hall_three_matching_reserve_threshold.py",
    "scripts/check_threshold_two_swap_generation.py",
    "scripts/check_prefix_parabola_source_anchors.py",
    "scripts/check_shell_binary_odd_column_frontier.py",
    "scripts/check_repeated_transition_evidence_gate.py",
)
for script in SCRIPTS:
    subprocess.run([sys.executable, script], check=True)
print({"frontier_group": "621-626", "scripts": len(SCRIPTS), "status": "passed"})

#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = (
    "scripts/check_frontier_615_620.py",
    "scripts/check_boundary_eighth_corrected_transition.py",
    "scripts/check_boundary_budget_seven_chain.py",
    "scripts/check_hall_quantitative_reserve_extraction.py",
    "scripts/check_hall_three_matching_reserve_threshold.py",
    "scripts/check_threshold_two_pivot_generation.py",
    "scripts/check_prefix_retained_anchor_reservoir.py",
    "scripts/check_prefix_parabola_source_anchors.py",
    "scripts/check_shell_all_cycle_odd_column.py",
    "scripts/check_repeated_transition_source_generation_gate.py",
)

for script in SCRIPTS:
    subprocess.run([sys.executable, script], check=True)

print({"frontier_group": "621-626", "scripts": len(SCRIPTS), "status": "passed"})

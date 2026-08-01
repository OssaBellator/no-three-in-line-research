#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = (
    "scripts/check_frontier_591_596.py",
    "scripts/check_boundary_widened_swap_obstruction.py",
    "scripts/check_hall_four_by_five_host.py",
    "scripts/check_threshold_unique_five_slot_augmentation.py",
    "scripts/check_prefix_repeated_chord_pairs.py",
    "scripts/check_shell_recorded_odd_action_absence.py",
    "scripts/check_structural_enlargement_evidence_gate.py",
)

for script in SCRIPTS:
    subprocess.run([sys.executable, script], check=True)

print({"frontier_group": "597-602", "scripts": len(SCRIPTS), "status": "passed"})

#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_frontier_561_566.py",
    "check_boundary_band_offset_cycles.py",
    "check_hall_choice_grid_decoder.py",
    "check_aligned_threshold_decompositions.py",
    "check_prefix_grading_propagation.py",
    "check_canonical_shell_service_incidence.py",
    "check_source_conversion_evidence_gate.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "567-572", "all_checks_passed": True})

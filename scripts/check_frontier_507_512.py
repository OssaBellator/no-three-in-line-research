#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_quantized_marker_cycle_mixtures.py",
    "check_spectral_hall_mixing_bounds.py",
    "check_conservative_matrix_rounding.py",
    "check_regular_language_prefix_code_dp.py",
    "check_shell_chamber_quantization_stability.py",
    "check_interaction_residue_correctors.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "507-512", "all_checks_passed": True})

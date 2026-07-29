#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_eventual_marker_quasipolynomial.py",
    "check_heterogeneous_hall_fourier_products.py",
    "check_birkhoff_threshold_layers.py",
    "check_regular_prefix_shape_series.py",
    "check_phase_optimized_shell_buffers.py",
    "check_eventual_vector_interaction_frontiers.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "519-524", "all_checks_passed": True})

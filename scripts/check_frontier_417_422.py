#!/usr/bin/env python3
import subprocess
import sys

scripts = [
    "check_tensorized_petal_marker_reservoirs.py",
    "check_hall_endpoint_target_transfer.py",
    "check_residual_biclique_expansion.py",
    "check_colored_corridor_word_kernels.py",
    "check_shell_cycle_product_potential.py",
    "check_type_schur_elimination.py",
]
for script in scripts:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)
print("all_frontier_417_422_checks_passed")

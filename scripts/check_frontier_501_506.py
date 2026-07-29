#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_eulerian_marker_flow_realization.py",
    "check_walsh_hall_syndrome_convolution.py",
    "check_quantized_threshold_designs.py",
    "check_risk_decorated_prefix_signatures.py",
    "check_quantized_shell_attenuation.py",
    "check_asymptotic_interaction_cycle_rates.py",
]

for script in SCRIPTS:
    print(f"== {script} ==")
    subprocess.run([sys.executable, f"scripts/{script}"], check=True)

print({"frontier_group": "501-506", "all_checks_passed": True})

#!/usr/bin/env python3
import subprocess,sys
SCRIPTS=(
"scripts/check_frontier_633_638.py",
"scripts/check_boundary_twelfth_transition.py",
"scripts/check_hall_source_center_pruning.py",
"scripts/check_threshold_transient_cell_batch.py",
"scripts/check_prefix_saturated_anchor_reservoir_13.py",
"scripts/check_shell_amortized_collateral.py",
"scripts/check_scaling_mechanisms_gate.py",
)
for script in SCRIPTS:
    subprocess.run([sys.executable,script],check=True)
print({"frontier_group":"639-644","scripts":len(SCRIPTS),"status":"passed"})

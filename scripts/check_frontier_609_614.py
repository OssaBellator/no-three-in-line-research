#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = (
    "scripts/check_frontier_603_608.py",
    "scripts/check_boundary_six_point_corrector.py",
    "scripts/check_hall_spare_resource_lemma.py",
    "scripts/check_threshold_nonamortization_dual.py",
    "scripts/check_prefix_row_column_run_embedding.py",
    "scripts/check_shell_fixed_column_lattice.py",
    "scripts/check_source_resource_realization_evidence_gate.py",
)

for script in SCRIPTS:
    subprocess.run([sys.executable, script], check=True)

print({"frontier_group": "609-614", "scripts": len(SCRIPTS), "status": "passed"})

#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = (
    "scripts/check_frontier_609_614.py",
    "scripts/check_boundary_corrector_transition_state.py",
    "scripts/check_hall_two_matching_exclusion_lemma.py",
    "scripts/check_threshold_three_cycle_replacements.py",
    "scripts/check_prefix_source_anchor_chords.py",
    "scripts/check_shell_signed_permutation_lattice.py",
    "scripts/check_composition_source_generation_evidence_gate.py",
)

for script in SCRIPTS:
    subprocess.run([sys.executable, script], check=True)

print({"frontier_group": "615-620", "scripts": len(SCRIPTS), "status": "passed"})

#!/usr/bin/env python3
"""Run the exact diagnostics accompanying docs/405--410."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run(command: list[str], root: Path) -> None:
    print("+", " ".join(command), flush=True)
    subprocess.run(command, cwd=root, check=True)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    commands = [
        [sys.executable, "scripts/check_fixed_signature_boundary_sunflowers.py"],
        [sys.executable, "scripts/check_overlap_walk_backward_averaging.py"],
        [
            sys.executable,
            "scripts/check_direct_clean_target_hubs.py",
            "experiments/direct-clean-target-hub-example.json",
        ],
        [sys.executable, "scripts/check_support_chord_corridor_banks.py"],
        [sys.executable, "scripts/check_scale_sensitive_shell_invariants.py"],
        [sys.executable, "scripts/check_typed_load_matrix_composition.py"],
    ]
    for command in commands:
        run(command, root)
    print({"all_frontier_405_410_checks_passed": True})


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Run the complete PP3bxw--PP3byo finite audit group."""

from __future__ import annotations

import subprocess
import sys


CHECKS = [
    [sys.executable, "scripts/check_sunflower_petal_reservoir_expansion.py"],
    [sys.executable, "scripts/check_hall_endpoint_collision_localization.py"],
    [sys.executable, "scripts/check_rooted_biclique_extraction.py"],
    [sys.executable, "scripts/check_corridor_intersection_coloring.py"],
    [sys.executable, "scripts/check_telescoping_shell_potentials.py"],
    [sys.executable, "scripts/check_type_matrix_potential_resolvent.py"],
]


def main() -> None:
    for command in CHECKS:
        subprocess.run(command, check=True)
    print({"all_checks_passed": True, "checks_run": len(CHECKS)})


if __name__ == "__main__":
    main()

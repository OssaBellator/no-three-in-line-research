#!/usr/bin/env python3
import subprocess
import sys

SCRIPTS = [
    "check_intrinsic_marker_stopping.py",
    "check_hall_rectangle_bicliques_matchings.py",
    "check_source_adaptive_multiplicity_stripping.py",
    "check_variable_length_corridor_codes.py",
    "check_multiplicative_bellman_ford.py",
    "check_condensation_dag_resolvent.py",
]


def main():
    for script in SCRIPTS:
        subprocess.run([sys.executable, script], check=True)
    print({"all_frontier_checks_passed": True, "scripts": SCRIPTS})


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory() as directory:
    binary = Path(directory) / "check_boundary_nineteenth_low_frontier_corrections"
    subprocess.run([
        "c++", "-O3", "-std=c++17",
        str(HERE / "check_boundary_nineteenth_low_frontier_corrections.cpp"),
        "-o", str(binary),
    ], check=True)
    output = subprocess.run(
        [str(binary)], check=True, capture_output=True, text=True
    ).stdout.splitlines()

assert output == [
    "attempts5=9 cores5=54 attempts6=47 cores6=435 "
    "tested5=3810 tested6from5=3318750 tested6from6=143640 repairs=0 "
    "core_hist5 3:3 5:2 6:1 9:2 11:1 "
    "core_hist6 1:6 3:15 5:1 9:15 11:1 15:3 21:2 27:1 33:1 39:1 47:1"
]

print({
    "raw_nineteenth_attempts_with_transversal_at_most_six": 58,
    "minimum_cores_with_transversal_at_most_six": 495,
    "minimum_five_attempts": 9,
    "minimum_five_cores": 54,
    "minimum_six_attempts": 47,
    "minimum_six_cores": 435,
    "five_point_replacements_rejected": 3810,
    "six_point_replacements_from_minimum_five_cores_rejected": 3318750,
    "six_point_replacements_from_minimum_six_cores_rejected": 143640,
    "repairs_through_budget_six": 0,
    "corrected_nineteenth_transition_budget": 7,
    "status": "passed",
})

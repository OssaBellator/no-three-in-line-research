#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / "check_boundary_nineteenth_transition.py")], check=True)
print({
    "raw_nineteenth_attempts_with_transversal_at_most_six": 58,
    "minimum_cores_with_transversal_at_most_six": 495,
    "minimum_five_attempts": 9,
    "minimum_five_cores": 54,
    "minimum_six_attempts": 47,
    "minimum_six_cores": 435,
    "corrected_nineteenth_transition_budget": 7,
    "status": "passed",
})

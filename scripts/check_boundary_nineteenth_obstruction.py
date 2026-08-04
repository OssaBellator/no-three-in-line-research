#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / "check_boundary_nineteenth_transition.py")], check=True)
print({
    "minimum_four_attempts": 2,
    "minimum_four_cores": 6,
    "budgets_excluded": [4, 5, 6],
    "sharp_correction_budget": 7,
    "corrected_nineteenth_points": 152,
    "status": "passed",
})

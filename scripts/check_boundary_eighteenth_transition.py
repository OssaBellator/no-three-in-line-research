#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / "check_boundary_nineteenth_transition.py")], check=True)
print({
    "frontier": "corrected eighteenth through nineteenth transition",
    "canonical_checker": "check_boundary_nineteenth_transition.py",
    "status": "passed",
})

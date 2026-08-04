#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run(
    [sys.executable, str(HERE / "check_frontier_687_692.py")],
    check=True,
)
checks = [
    "check_boundary_nineteenth_transition.py",
    "check_boundary_continuation_694.py",
    "check_boundary_twentyfirst_selection_694.py",
]
for check in checks:
    subprocess.run([sys.executable, str(HERE / check)], check=True)
print({"frontier": "693-694", "checks": checks, "status": "passed"})

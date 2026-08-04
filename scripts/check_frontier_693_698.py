#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run(
    [sys.executable, str(HERE / "check_frontier_693_697.py")],
    check=True,
)
checks = [
    "check_prefix_all_optimal_four_run_compositions.py",
]
for check in checks:
    subprocess.run([sys.executable, str(HERE / check)], check=True)
print({"frontier": "693-698", "checks": checks, "status": "passed"})

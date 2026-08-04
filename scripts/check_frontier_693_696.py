#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run(
    [sys.executable, str(HERE / "check_frontier_693_695.py")],
    check=True,
)
checks = [
    "check_threshold_all_window_widths.py",
]
for check in checks:
    subprocess.run([sys.executable, str(HERE / check)], check=True)
print({"frontier": "693-696", "checks": checks, "status": "passed"})

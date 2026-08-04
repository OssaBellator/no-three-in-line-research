#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run(
    [sys.executable, str(HERE / "check_frontier_693_694.py")],
    check=True,
)
check = "check_boundary_twentysecond_budget_six_obstruction_695.py"
subprocess.run([sys.executable, str(HERE / check)], check=True)
print({"frontier": "693-695", "check": check, "status": "passed"})

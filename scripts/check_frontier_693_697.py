#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
subprocess.run(
    [sys.executable, str(HERE / "check_frontier_693_696.py")],
    check=True,
)
checks = [
    "check_hall_two_motif_incidence_packets.py",
    "check_hall_coordinate_defect_packet.py",
]
for check in checks:
    subprocess.run([sys.executable, str(HERE / check)], check=True)
print({"frontier": "693-697", "checks": checks, "status": "passed"})

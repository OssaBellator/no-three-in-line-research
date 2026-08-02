#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
source = HERE / "check_prefix_rerouting_geometry.cpp"
with tempfile.TemporaryDirectory() as directory:
    binary = Path(directory) / "check_prefix_rerouting_geometry"
    subprocess.run(["c++", "-O3", "-std=c++17", str(source), "-o", str(binary)], check=True)
    result = subprocess.run([str(binary)], check=True, capture_output=True, text=True)

assert result.stdout.splitlines() == [
    "case=0 routes=144 successful=144 hist 87:6 89:1 96:1 98:3 100:4 102:11 111:1 115:2 120:99 132:15 144:1",
    "case=1 routes=144 successful=144 hist 84:7 98:2 99:13 104:2 108:2 117:2 132:71 142:12 144:12 152:2 154:16 156:3",
]

print({
    "minimum_cross_matchings": 104,
    "canonical_matching_deletion_cases": 2,
    "optimal_reroutings_per_case": 144,
    "compositions_per_rerouting": 1024,
    "rerouting_composition_pairs_checked": 294912,
    "all_pairs_pass": True,
    "status": "passed",
})

#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile

HERE=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory() as directory:
    binary=Path(directory)/"check_boundary_nineteenth_corrections"
    subprocess.run([
        "c++","-O3","-std=c++17",
        str(HERE/"check_boundary_nineteenth_corrections.cpp"),
        "-o",str(binary),
    ],check=True)
    output=subprocess.run([str(binary)],check=True,capture_output=True,text=True).stdout.splitlines()

assert len(output)==21
for core in range(1,6):
    base=(core-1)*4
    assert output[base].startswith(f"P2/-64 core{core} ")
    assert output[base+1]=="budget 4 none tested 24"
    assert output[base+2]=="budget 5 none tested 17520"
    assert output[base+3]=="budget 6 none tested 7595280"
assert output[-1]=="summary attempts=1 cores=5 none_through_budget_6=true"

print({
    "attempt":"P2/-64",
    "minimum_cores":5,
    "budgets_checked":[4,5,6],
    "six_point_replacements_rejected":5*7595280,
    "corrected_transition":False,
    "status":"passed",
})

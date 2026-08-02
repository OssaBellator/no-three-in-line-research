#!/usr/bin/env python3
from collections import Counter
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
source = HERE / "check_prefix_orbit_representative_compositions.cpp"

with tempfile.TemporaryDirectory() as directory:
    binary = Path(directory) / source.stem
    subprocess.run(
        ["c++", "-O3", "-std=c++17", str(source), "-o", str(binary)],
        check=True,
    )
    result = subprocess.run(
        [str(binary)],
        check=True,
        capture_output=True,
        text=True,
    )

assert result.stderr.splitlines() == [
    "cases=40 compositions=1024 audits=40960",
    "deletion=0 hist 120:10 132:10",
    "deletion=1 hist 84:10 132:10",
]

records = []
for line in result.stdout.splitlines():
    fields = {
        key: int(value)
        for key, value in (
            token.split("=")
            for token in line.split()
        )
    }
    records.append(fields)

assert len(records) == 40
assert Counter(record["representative"] for record in records) == Counter({
    representative: 2 for representative in range(20)
})
assert Counter(record["deletion"] for record in records) == Counter({0:20, 1:20})
assert all(record["passed"] == 1024 for record in records)
assert Counter(
    record["maximum"]
    for record in records
    if record["deletion"] == 0
) == Counter({120:10, 132:10})
assert Counter(
    record["maximum"]
    for record in records
    if record["deletion"] == 1
) == Counter({84:10, 132:10})

print({
    "selected_representatives": 20,
    "deletion_cases": 2,
    "compositions_per_route": 1024,
    "route_composition_pairs": 40960,
    "all_pairs_pass": True,
    "deletion_0_maximum_coordinate_histogram": {120:10, 132:10},
    "deletion_1_maximum_coordinate_histogram": {84:10, 132:10},
    "status": "passed",
})

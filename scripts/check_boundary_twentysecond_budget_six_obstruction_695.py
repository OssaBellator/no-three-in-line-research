#!/usr/bin/env python3
from collections import Counter
from pathlib import Path
import runpy
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
context = runpy.run_path(str(HERE / "check_boundary_continuation_694.py"))
state = context["state21"]
block = context["block"]
s22 = context["s22"]
attempts = [attempt for attempt in s22[2] if attempt[3] == 6]

with tempfile.TemporaryDirectory() as directory:
    binary = Path(directory) / "legacy"
    subprocess.run([
        "c++", "-O3", "-std=c++17",
        str(HERE / "boundary_legacy_correction_kernel.cpp"),
        "-o", str(binary),
    ], check=True)
    jobs = []
    for attempt_index, attempt in enumerate(attempts):
        name, offset, triples, minimum, cores = attempt
        all_points = sorted(state | block(name, 84, offset))
        for core_index, core in enumerate(cores):
            jobs.append((f"a{attempt_index}c{core_index}", all_points, core))
    assert len(jobs) == 178
    input_lines = [str(len(jobs))]
    for identifier, all_points, core in jobs:
        input_lines.append(f"{identifier} {len(all_points)} 6 {len(core)}")
        input_lines.extend(f"{x} {y}" for x, y in all_points)
        input_lines.extend(f"{x} {y}" for x, y in core)
    output = subprocess.run(
        [str(binary)],
        input="\n".join(input_lines) + "\n",
        text=True,
        capture_output=True,
        check=True,
    ).stdout.splitlines()

assert len(output) == 178
tested = []
for line, job in zip(output, jobs):
    _, identifier, found, count = line.split()
    assert identifier == job[0]
    assert found == "0"
    tested.append(int(count))
assert sum(tested) == 68580
assert Counter(tested) == Counter({180: 49, 360: 92, 720: 37})
print({
    "minimum_six_attempts": 26,
    "minimum_six_cores": 178,
    "budget": 6,
    "replacement_permutation_histogram": {180: 49, 360: 92, 720: 37},
    "replacement_permutations_rejected": 68580,
    "repairs": 0,
    "status": "passed",
})

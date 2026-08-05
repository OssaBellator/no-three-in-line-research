#!/usr/bin/env python3
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
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
assert len(attempts) == 26
assert sum(len(attempt[4]) for attempt in attempts) == 178


def run_attempt(binary, attempt_index, attempt):
    name, offset, triples, minimum, cores = attempt
    all_points = sorted(state | block(name, 84, offset))
    input_lines = [str(len(cores))]
    for core_index, core in enumerate(cores):
        identifier = f"a{attempt_index}c{core_index}"
        input_lines.append(f"{identifier} {len(all_points)} 7 {len(core)}")
        input_lines.extend(f"{x} {y}" for x, y in all_points)
        input_lines.extend(f"{x} {y}" for x, y in core)
    result = subprocess.run(
        [str(binary)],
        input="\n".join(input_lines) + "\n",
        text=True,
        capture_output=True,
        check=True,
    )
    assert result.stderr == ""
    return attempt_index, result.stdout.splitlines()


with tempfile.TemporaryDirectory() as directory:
    binary = Path(directory) / "legacy"
    subprocess.run([
        "c++", "-O3", "-std=c++17",
        str(HERE / "boundary_legacy_correction_kernel.cpp"),
        "-o", str(binary),
    ], check=True)

    by_attempt = {}
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [
            executor.submit(run_attempt, binary, index, attempt)
            for index, attempt in enumerate(attempts)
        ]
        for future in as_completed(futures):
            index, lines = future.result()
            by_attempt[index] = lines

output = [line for index in range(len(attempts)) for line in by_attempt[index]]
assert len(output) == 178

tested = []
for line in output:
    marker, identifier, found, count = line.split()
    assert marker == "RES"
    assert identifier.startswith("a") and "c" in identifier
    assert found == "0"
    tested.append(int(count))

expected_histogram = Counter({212940: 49, 423360: 92, 841680: 37})
assert Counter(tested) == expected_histogram
assert sum(tested) == 80525340

print({
    "minimum_six_attempts": 26,
    "minimum_six_cores": 178,
    "budget": 7,
    "replacement_permutation_histogram": {
        212940: 49,
        423360: 92,
        841680: 37,
    },
    "replacement_permutations_rejected": 80525340,
    "combined_budget_six_and_seven_rejections": 80593920,
    "repairs": 0,
    "remaining_frontier": "minimum-seven raw attempts at budget seven, or minimum-six cores at budget eight",
    "evidence_level": "exact_minimum_six_twentysecond_budget_seven_obstruction",
    "status": "passed",
})

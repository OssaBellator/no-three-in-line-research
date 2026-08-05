#!/usr/bin/env python3
"""Exact census of the raw twenty-second minimum-seven layer at budget seven.

The canonical twenty-one-block state has 205 raw attempts whose minimum
transversal size is seven.  For every exact minimum core this checker invokes the
witness-producing row/column-preserving exact-cover kernel at deletion budget
seven.  Because the core already has size seven, there are no optional extra
deletions: each job either rejects every replacement assignment or emits one
complete repair witness.

The checker independently audits every emitted repair, computes its raw
Twenty-third spectrum, and reports all candidates.  It deliberately does not
select or promote a canonical continuation state.
"""

from __future__ import annotations

from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import combinations
from pathlib import Path
import json
import runpy
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
context = runpy.run_path(str(HERE / "check_boundary_continuation_694.py"))
state21 = context["state21"]
block = context["block"]
spectrum = context["spectrum"]
compile_kernel = context["compile"]
s22 = context["s22"]
attempts = [attempt for attempt in s22[2] if attempt[3] == 7]
assert len(attempts) == 205


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def audit_repair(all_points, core, deleted, added):
    base = set(all_points)
    deleted = set(deleted)
    added = set(added)
    assert len(core) == 7
    assert len(deleted) == len(added) == 7
    assert set(core) == deleted
    assert deleted <= base
    assert Counter(x for x, _ in deleted) == Counter(x for x, _ in added)
    assert Counter(y for _, y in deleted) == Counter(y for _, y in added)
    repaired = (base - deleted) | added
    assert len(repaired) == len(base) == 176
    assert repaired != base
    ordered = sorted(repaired)
    for a, b, c in combinations(ordered, 3):
        assert cross(a, b, c) != 0, (a, b, c)
    return ordered


def parse_point(token):
    x, y = token.split(",")
    return int(x), int(y)


def run_attempt(binary, attempt_index, attempt):
    name, offset, _triples, minimum, cores = attempt
    assert minimum == 7
    all_points = sorted(state21 | block(name, 84, offset))
    lines = [str(len(cores))]
    for core_index, core in enumerate(cores):
        identifier = f"a{attempt_index}c{core_index}"
        lines.append(f"{identifier} {len(all_points)} 7 {len(core)}")
        lines.extend(f"{x} {y}" for x, y in all_points)
        lines.extend(f"{x} {y}" for x, y in core)
    result = subprocess.run(
        [str(binary)],
        input="\n".join(lines) + "\n",
        text=True,
        capture_output=True,
        check=True,
    )
    assert result.stderr == ""
    return attempt_index, all_points, result.stdout.splitlines()


with tempfile.TemporaryDirectory() as directory:
    directory = Path(directory)
    exact = compile_kernel("boundary_exact_cover_kernel.cpp", directory)
    by_attempt = {}
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [
            executor.submit(run_attempt, exact, index, attempt)
            for index, attempt in enumerate(attempts)
        ]
        for future in as_completed(futures):
            attempt_index, all_points, lines = future.result()
            by_attempt[attempt_index] = (all_points, lines)

    tested_subsets = 0
    tested_nodes = 0
    core_count = 0
    witnesses = []
    for attempt_index, attempt in enumerate(attempts):
        name, offset, _triples, _minimum, cores = attempt
        all_points, lines = by_attempt[attempt_index]
        cursor = 0
        for core_index, core in enumerate(cores):
            fields = lines[cursor].split()
            cursor += 1
            assert fields[:2] == ["RES", f"a{attempt_index}c{core_index}"]
            found = fields[2] == "1"
            tested_subsets += int(fields[3])
            tested_nodes += int(fields[4])
            core_count += 1
            if found:
                deleted_line = lines[cursor].split()
                added_line = lines[cursor + 1].split()
                cursor += 2
                assert deleted_line[0] == "D"
                assert added_line[0] == "A"
                deleted = [parse_point(token) for token in deleted_line[1:]]
                added = [parse_point(token) for token in added_line[1:]]
                repaired = audit_repair(all_points, core, deleted, added)
                witnesses.append({
                    "attempt_index": attempt_index,
                    "core_index": core_index,
                    "attempt_name": name,
                    "offset": offset,
                    "deleted": deleted,
                    "added": added,
                    "repaired_state": repaired,
                    "exact_cover_subsets_tested_until_stop": int(fields[3]),
                    "exact_cover_nodes_tested_until_stop": int(fields[4]),
                })
        assert cursor == len(lines)

    spectrum_jobs = [
        (f"w{index}", witness["repaired_state"], 88, 6)
        for index, witness in enumerate(witnesses)
    ]
    spectrum_binary = compile_kernel("boundary_spectrum_kernel.cpp", directory)
    next_spectra = spectrum(spectrum_binary, spectrum_jobs) if spectrum_jobs else {}

for index, witness in enumerate(witnesses):
    histogram, minimum, next_attempts = next_spectra[f"w{index}"]
    assert minimum == min(histogram)
    assert sum(histogram.values()) == len(next_attempts)
    witness["raw_twenty_third_histogram"] = {
        str(k): histogram[k] for k in sorted(histogram)
    }
    witness["raw_twenty_third_minimum"] = minimum
    witness["raw_twenty_third_minimum_attempts"] = sum(
        attempt[3] == minimum for attempt in next_attempts
    )
    witness["raw_twenty_third_minimum_cores"] = sum(
        len(attempt[4]) for attempt in next_attempts if attempt[3] == minimum
    )

payload = {
    "frontier": "twenty-second raw minimum-seven layer",
    "attempts": len(attempts),
    "minimum_cores": core_count,
    "budget": 7,
    "exact_cover_subsets_tested_until_stop": tested_subsets,
    "exact_cover_nodes_tested_until_stop": tested_nodes,
    "repairs": len(witnesses),
    "witnesses": witnesses,
    "evidence_level": "exact_finite_minimum_seven_budget_seven_census",
    "status": "passed",
    "warning": (
        "A positive witness is only a finite continuation candidate. Canonical "
        "selection requires comparison of every emitted next spectrum; neither a "
        "finite repair nor an obstruction proves recurrence or the all-n theorem."
    ),
}
print(json.dumps(payload, indent=2, sort_keys=True))

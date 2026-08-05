#!/usr/bin/env python3
"""Extract and independently audit witnesses for repair-positive budget-seven jobs.

Input is the complete payload produced by
``merge_boundary_twentysecond_budget_seven_701.py``.  Only records marked
``repair_found`` are rerun.  The witness-producing exact-cover kernel emits the
seven deleted points and their row/column-preserving replacements; this driver
then checks those data independently in Python.

This script certifies individual finite repairs.  It does not select a canonical
continuation, compare raw twenty-third spectra, or prove a recurrent all-n path.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from itertools import combinations
from pathlib import Path
import runpy
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent


def parse_point(token: str) -> tuple[int, int]:
    x, y = token.split(",")
    return int(x), int(y)


def collinear(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def audit_witness(
    all_points: list[tuple[int, int]],
    deleted: list[tuple[int, int]],
    added: list[tuple[int, int]],
) -> list[tuple[int, int]]:
    assert len(deleted) == 7
    assert len(added) == 7
    assert len(set(deleted)) == 7
    assert len(set(added)) == 7
    base = set(all_points)
    assert set(deleted) <= base
    assert Counter(x for x, _ in deleted) == Counter(x for x, _ in added)
    assert Counter(y for _, y in deleted) == Counter(y for _, y in added)
    repaired = (base - set(deleted)) | set(added)
    assert len(repaired) == len(base)
    assert repaired != base
    ordered = sorted(repaired)
    for a, b, c in combinations(ordered, 3):
        assert not collinear(a, b, c), (a, b, c)
    return ordered


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("merged", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    merged = json.loads(args.merged.read_text())
    assert merged["frontier"] == "twenty-second"
    assert merged["budget"] == 7
    assert merged["total_core_jobs"] == 178
    assert merged["status"] == "passed"
    records = merged["records"]
    assert [record["global_index"] for record in records] == list(range(178))
    positive = [record for record in records if record["repair_found"]]

    context = runpy.run_path(str(HERE / "check_boundary_continuation_694.py"))
    state = context["state21"]
    block = context["block"]
    spectrum22 = context["s22"]
    attempts = [attempt for attempt in spectrum22[2] if attempt[3] == 6]

    jobs = []
    for record in positive:
        attempt = attempts[record["attempt_index"]]
        name, offset, _triples, minimum, cores = attempt
        assert minimum == 6
        assert name == record["attempt_name"]
        assert offset == record["offset"]
        core = cores[record["core_index"]]
        all_points = sorted(state | block(name, 84, offset))
        jobs.append((record, all_points, core))

    with tempfile.TemporaryDirectory() as directory:
        binary = Path(directory) / "exact-cover"
        subprocess.run([
            "c++", "-O3", "-std=c++17",
            str(HERE / "boundary_exact_cover_kernel.cpp"),
            "-o", str(binary),
        ], check=True)
        input_lines = [str(len(jobs))]
        for record, all_points, core in jobs:
            identifier = f"g{record['global_index']}"
            input_lines.append(f"{identifier} {len(all_points)} 7 {len(core)}")
            input_lines.extend(f"{x} {y}" for x, y in all_points)
            input_lines.extend(f"{x} {y}" for x, y in core)
        output = subprocess.run(
            [str(binary)],
            input="\n".join(input_lines) + "\n",
            text=True,
            capture_output=True,
            check=True,
        ).stdout.splitlines()

    cursor = 0
    witnesses = []
    for record, all_points, core in jobs:
        fields = output[cursor].split()
        cursor += 1
        assert fields[:2] == ["RES", f"g{record['global_index']}"]
        found = fields[2] == "1"
        assert found, {
            "global_index": record["global_index"],
            "legacy_reported_repair": True,
            "exact_cover_reported_repair": False,
        }
        deleted_line = output[cursor].split()
        added_line = output[cursor + 1].split()
        cursor += 2
        assert deleted_line[0] == "D"
        assert added_line[0] == "A"
        deleted = [parse_point(token) for token in deleted_line[1:]]
        added = [parse_point(token) for token in added_line[1:]]
        repaired = audit_witness(all_points, deleted, added)
        assert set(core) <= set(deleted)
        witnesses.append({
            "global_index": record["global_index"],
            "attempt_index": record["attempt_index"],
            "core_index": record["core_index"],
            "attempt_name": record["attempt_name"],
            "offset": record["offset"],
            "deleted": deleted,
            "added": added,
            "repaired_state": repaired,
            "exact_cover_subsets_tested_until_stop": int(fields[3]),
            "exact_cover_nodes_tested_until_stop": int(fields[4]),
            "audit": "passed",
        })
    assert cursor == len(output)

    payload = {
        "frontier": "twenty-second",
        "budget": 7,
        "total_core_jobs": 178,
        "legacy_positive_jobs": len(positive),
        "audited_witnesses": len(witnesses),
        "witnesses": witnesses,
        "status": "passed",
        "warning": (
            "These are finite repair witnesses only. Canonical continuation still "
            "requires complete positive-job coverage and exact next-spectrum comparison."
        ),
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()

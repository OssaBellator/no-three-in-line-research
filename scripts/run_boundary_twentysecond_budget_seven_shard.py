#!/usr/bin/env python3
"""Run an exact, resumable shard of the twenty-second budget-seven search.

This is search infrastructure, not a certificate of a completed obstruction or
repair.  A complete run requires every shard to finish and the resulting records
to cover all 178 canonical minimum-six cores exactly once.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import runpy
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard-index", type=int, required=True)
    parser.add_argument("--shard-count", type=int, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.shard_count <= 0:
        parser.error("--shard-count must be positive")
    if not 0 <= args.shard_index < args.shard_count:
        parser.error("--shard-index must lie in [0, shard-count)")
    return args


def main() -> None:
    args = parse_args()
    context = runpy.run_path(str(HERE / "check_boundary_continuation_694.py"))
    state = context["state21"]
    block = context["block"]
    attempts = [attempt for attempt in context["s22"][2] if attempt[3] == 6]

    jobs = []
    global_index = 0
    for attempt_index, attempt in enumerate(attempts):
        name, offset, _triples, minimum, cores = attempt
        assert minimum == 6
        all_points = sorted(state | block(name, 84, offset))
        for core_index, core in enumerate(cores):
            if global_index % args.shard_count == args.shard_index:
                jobs.append((global_index, attempt_index, core_index, name, offset,
                             all_points, core))
            global_index += 1
    assert global_index == 178

    with tempfile.TemporaryDirectory() as directory:
        binary = Path(directory) / "legacy"
        subprocess.run([
            "c++", "-O3", "-std=c++17",
            str(HERE / "boundary_legacy_correction_kernel.cpp"),
            "-o", str(binary),
        ], check=True)
        input_lines = [str(len(jobs))]
        for global_index, attempt_index, core_index, _name, _offset, all_points, core in jobs:
            identifier = f"g{global_index}a{attempt_index}c{core_index}"
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

    assert len(output) == len(jobs)
    records = []
    for line, job in zip(output, jobs):
        marker, identifier, found, permutations = line.split()
        assert marker == "RES"
        global_index, attempt_index, core_index, name, offset, _all_points, core = job
        assert identifier == f"g{global_index}a{attempt_index}c{core_index}"
        records.append({
            "global_core_index": global_index,
            "attempt_index": attempt_index,
            "core_index": core_index,
            "primitive": name,
            "offset": offset,
            "core": [list(point) for point in core],
            "repair_found": bool(int(found)),
            "replacement_permutations_tested": int(permutations),
        })

    payload = {
        "frontier": "canonical twenty-second minimum-six cores",
        "budget": 7,
        "shard_index": args.shard_index,
        "shard_count": args.shard_count,
        "canonical_core_count": 178,
        "records": records,
        "status": "complete-shard",
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()

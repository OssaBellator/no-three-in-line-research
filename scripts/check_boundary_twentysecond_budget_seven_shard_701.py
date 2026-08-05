#!/usr/bin/env python3
"""Run one deterministic shard of the exact twenty-second budget-seven census.

The full layer has 178 minimum-six cores.  For each core this driver asks the
legacy row/column-preserving correction kernel to add exactly one further
deletion and test every induced replacement permutation.  Shards partition the
178 core jobs by their canonical global index; concatenating shard records in
index order therefore reconstructs the unsharded census exactly.

This script is infrastructure, not a theorem certificate by itself.  A promoted
result must include every shard, verify the complete index partition, and rerun
all reported repairs with a witness-producing checker before selecting a
continuation state.
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
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.shard_count <= 0:
        raise SystemExit("--shard-count must be positive")
    if not 0 <= args.shard_index < args.shard_count:
        raise SystemExit("--shard-index must lie in [0, shard-count)")

    context = runpy.run_path(str(HERE / "check_boundary_continuation_694.py"))
    state = context["state21"]
    block = context["block"]
    spectrum22 = context["s22"]
    attempts = [attempt for attempt in spectrum22[2] if attempt[3] == 6]

    jobs = []
    global_index = 0
    for attempt_index, attempt in enumerate(attempts):
        name, offset, _triples, minimum, cores = attempt
        assert minimum == 6
        all_points = sorted(state | block(name, 84, offset))
        for core_index, core in enumerate(cores):
            if global_index % args.shard_count == args.shard_index:
                jobs.append({
                    "global_index": global_index,
                    "attempt_index": attempt_index,
                    "core_index": core_index,
                    "attempt_name": name,
                    "offset": offset,
                    "all_points": all_points,
                    "core": core,
                })
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
        for job in jobs:
            identifier = f"g{job['global_index']}"
            all_points = job["all_points"]
            core = job["core"]
            input_lines.append(f"{identifier} {len(all_points)} 7 {len(core)}")
            input_lines.extend(f"{x} {y}" for x, y in all_points)
            input_lines.extend(f"{x} {y}" for x, y in core)

        output_lines = subprocess.run(
            [str(binary)],
            input="\n".join(input_lines) + "\n",
            text=True,
            capture_output=True,
            check=True,
        ).stdout.splitlines()

    if len(output_lines) != len(jobs):
        raise AssertionError((len(output_lines), len(jobs)))

    records = []
    for line, job in zip(output_lines, jobs):
        marker, identifier, found, tested = line.split()
        assert marker == "RES"
        assert identifier == f"g{job['global_index']}"
        records.append({
            "global_index": job["global_index"],
            "attempt_index": job["attempt_index"],
            "core_index": job["core_index"],
            "attempt_name": job["attempt_name"],
            "offset": job["offset"],
            "repair_found": found == "1",
            "replacement_permutations_tested_until_stop": int(tested),
        })

    payload = {
        "frontier": "twenty-second",
        "budget": 7,
        "total_core_jobs": 178,
        "shard_index": args.shard_index,
        "shard_count": args.shard_count,
        "job_count": len(records),
        "global_indices": [record["global_index"] for record in records],
        "repairs_found": sum(record["repair_found"] for record in records),
        "replacement_permutations_tested_until_stop": sum(
            record["replacement_permutations_tested_until_stop"]
            for record in records
        ),
        "records": records,
        "status": "passed",
        "warning": (
            "Repair-positive records are existence results only; the legacy kernel "
            "stops at the first repair and does not emit its witness."
        ),
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Run the complete twenty-second budget-seven finite boundary pipeline.

This orchestrates deterministic shards, strict merging, independent witness
extraction, and exact twenty-third spectrum comparison.  It is intentionally a
finite frontier runner: successful completion does not select a canonical state
and does not establish recurrence or the all-n theorem.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard-count", type=int, default=16)
    parser.add_argument("--workdir", type=Path, required=True)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    if args.shard_count <= 0:
        raise SystemExit("--shard-count must be positive")

    workdir = args.workdir.resolve()
    shard_dir = workdir / "shards"
    shard_dir.mkdir(parents=True, exist_ok=True)

    shard_paths = []
    for shard_index in range(args.shard_count):
        path = shard_dir / f"budget-seven-{shard_index:04d}-of-{args.shard_count:04d}.json"
        shard_paths.append(path)
        if args.resume and path.exists():
            payload = json.loads(path.read_text())
            assert payload["status"] == "passed"
            assert payload["shard_index"] == shard_index
            assert payload["shard_count"] == args.shard_count
            continue
        run([
            sys.executable,
            str(HERE / "check_boundary_twentysecond_budget_seven_shard_701.py"),
            "--shard-index", str(shard_index),
            "--shard-count", str(args.shard_count),
            "--output", str(path),
        ])

    merged = workdir / "budget-seven-merged.json"
    run([
        sys.executable,
        str(HERE / "merge_boundary_twentysecond_budget_seven_701.py"),
        *map(str, shard_paths),
        "--output", str(merged),
    ])

    witnesses = workdir / "budget-seven-witnesses.json"
    run([
        sys.executable,
        str(HERE / "check_boundary_twentysecond_budget_seven_witnesses_701.py"),
        str(merged),
        "--output", str(witnesses),
    ])

    spectra = workdir / "budget-seven-next-spectra.json"
    run([
        sys.executable,
        str(HERE / "check_boundary_twentysecond_budget_seven_next_spectra_701.py"),
        str(witnesses),
        "--output", str(spectra),
    ])

    merged_payload = json.loads(merged.read_text())
    witness_payload = json.loads(witnesses.read_text())
    spectra_payload = json.loads(spectra.read_text())
    summary = {
        "frontier": "twenty-second",
        "budget": 7,
        "total_core_jobs": merged_payload["total_core_jobs"],
        "repair_positive_jobs": merged_payload["repairs_found"],
        "audited_witnesses": witness_payload["audited_witnesses"],
        "evaluated_repaired_states": spectra_payload["evaluated_repaired_states"],
        "raw_twenty_third_minimum_histogram": spectra_payload["raw_minimum_histogram"],
        "pareto_indices_by_cumulative_low_frontier": spectra_payload[
            "pareto_indices_by_cumulative_low_frontier"
        ],
        "artifacts": {
            "merged": str(merged),
            "witnesses": str(witnesses),
            "next_spectra": str(spectra),
        },
        "status": "passed",
        "warning": (
            "Finite frontier evidence only; no canonical continuation, recurrence, "
            "or all-n theorem is implied."
        ),
    }
    summary_path = workdir / "budget-seven-summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

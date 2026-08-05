#!/usr/bin/env python3
"""Run the complete resumable minimum-seven budget-seven boundary pipeline."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def valid_existing_shard(path: Path, index: int, count: int) -> bool:
    if not path.exists():
        return False
    try:
        payload = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return False
    return (
        payload.get("status") == "passed"
        and payload.get("shard_index") == index
        and payload.get("shard_count") == count
        and payload.get("frontier") == "twenty-second raw minimum-seven layer"
        and payload.get("budget") == 7
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--work-directory", type=Path, required=True)
    parser.add_argument("--shard-count", type=int, default=16)
    parser.add_argument(
        "--rerun-shards",
        action="store_true",
        help="rerun shards even when structurally valid shard JSON already exists",
    )
    args = parser.parse_args()

    if args.shard_count <= 0:
        raise SystemExit("--shard-count must be positive")

    work = args.work_directory
    shards_directory = work / "shards"
    shards_directory.mkdir(parents=True, exist_ok=True)
    shard_paths = []

    for shard_index in range(args.shard_count):
        path = shards_directory / f"minimum-seven-{shard_index:04d}.json"
        shard_paths.append(path)
        if not args.rerun_shards and valid_existing_shard(
            path, shard_index, args.shard_count
        ):
            continue
        run([
            sys.executable,
            str(HERE / "run_boundary_minimum_seven_attempt_shard_707.py"),
            "--shard-index",
            str(shard_index),
            "--shard-count",
            str(args.shard_count),
            "--output",
            str(path),
        ])

    merged = work / "minimum-seven-merged.json"
    run([
        sys.executable,
        str(HERE / "merge_boundary_minimum_seven_attempt_shards_707.py"),
        *(str(path) for path in shard_paths),
        "--output",
        str(merged),
    ])

    verified = work / "minimum-seven-verified.json"
    run([
        sys.executable,
        str(HERE / "verify_boundary_minimum_seven_merged_707.py"),
        str(merged),
        "--output",
        str(verified),
    ])

    payload = json.loads(verified.read_text())
    summary = {
        "frontier": payload["frontier"],
        "attempts": payload["attempts"],
        "minimum_cores": payload["minimum_cores"],
        "budget": payload["budget"],
        "repairs": payload["repairs"],
        "audited_witnesses": payload["audited_witnesses"],
        "merged_artifact": str(merged),
        "verified_artifact": str(verified),
        "status": "passed",
        "warning": (
            "Pipeline completion is exact finite evidence only. A positive result "
            "requires justified canonical selection; a zero-repair result closes "
            "only this specific minimum-seven budget-seven layer."
        ),
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

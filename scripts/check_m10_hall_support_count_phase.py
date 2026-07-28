#!/usr/bin/env python3
"""Resumable exact m=10 Hall profile by compatible-source count.

This orchestrates the already committed Dinic and gap-push-relabel workers. Each
worker is asked to solve one exact source count, so completed JSON rows remain
usable after interruption.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def run(command: list[str], *, cwd: Path, timeout: int | None = None) -> None:
    subprocess.run(command, cwd=cwd, check=True, timeout=timeout)


def compile_workers(root: Path, build: Path) -> tuple[Path, Path]:
    build.mkdir(parents=True, exist_ok=True)
    common = ["g++", "-O3", "-std=c++17", "-Wall", "-Wextra", "-pedantic", "-fopenmp"]
    dinic = build / "m10_hall_dinic_worker"
    push = build / "m10_hall_push_relabel_worker"
    run(common + [str(root / "scripts/check_m10_weighted_hall_mid_source_dinic_worker.cpp"), "-o", str(dinic)], cwd=root)
    run(common + [str(root / "scripts/check_m10_weighted_hall_mid_source_push_relabel_worker.cpp"), "-o", str(push)], cwd=root)
    return dinic, push


def valid_json(path: Path) -> bool:
    try:
        with path.open(encoding="utf-8") as handle:
            json.load(handle)
        return True
    except (OSError, json.JSONDecodeError):
        return False


def solve_count(binary: Path, source_count: int, output: Path,
                threads: int, timeout: int) -> bool:
    temporary = output.with_suffix(".tmp")
    environment = dict(os.environ, OMP_NUM_THREADS=str(threads))
    try:
        with temporary.open("w", encoding="utf-8") as handle:
            subprocess.run(
                [str(binary), str(source_count), str(source_count)],
                stdout=handle,
                stderr=subprocess.DEVNULL,
                env=environment,
                check=True,
                timeout=timeout,
            )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        temporary.unlink(missing_ok=True)
        return False
    if not valid_json(temporary):
        temporary.unlink(missing_ok=True)
        return False
    temporary.replace(output)
    return True


def compact_row(ledger: dict) -> list[object] | None:
    flaws = int(ledger["source_band_signed_flaws"])
    if not flaws:
        return None
    source_count = int(ledger["source_cycle_band"][0])
    charge = Fraction(ledger["source_band_worst_charge"])
    return [
        source_count,
        flaws,
        int(ledger["source_band_proper_bottlenecks"]),
        str(charge),
        str(source_count * charge),
        int(ledger["source_band_worst_subset_size"]),
        int(ledger["source_band_worst_supply"]),
        int(ledger["source_band_worst_capacity"]),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    parser.add_argument("--lo", type=int, required=True)
    parser.add_argument("--hi", type=int, required=True)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=90)
    args = parser.parse_args()

    root = args.root.resolve()
    args.cache.mkdir(parents=True, exist_ok=True)
    dinic, push = compile_workers(root, args.cache / "build")

    for source_count in range(args.lo, args.hi + 1):
        output = args.cache / f"{source_count}.json"
        if valid_json(output):
            continue
        if solve_count(push, source_count, output, args.threads, args.timeout):
            continue
        if solve_count(dinic, source_count, output, args.threads, args.timeout):
            continue
        print(f"unresolved source count: {source_count}", file=sys.stderr)

    columns = [
        "source_cycles", "signed_flaws", "proper_bottlenecks",
        "worst_charge", "max_support_normalized_charge",
        "worst_subset_size", "worst_supply", "worst_capacity",
    ]
    parts: list[list[object]] = []
    missing: list[int] = []
    for source_count in range(args.lo, args.hi + 1):
        path = args.cache / f"{source_count}.json"
        if not valid_json(path):
            missing.append(source_count)
            continue
        with path.open(encoding="utf-8") as handle:
            row = compact_row(json.load(handle))
        if row is not None:
            parts.append(row)

    result = {
        "m": 10,
        "covered_source_cycle_range": [args.lo, args.hi],
        "columns": columns,
        "parts": parts,
        "nonempty_source_counts": len(parts),
        "signed_flaws_covered": sum(int(row[1]) for row in parts),
        "all_covered_flaws_have_proper_bottlenecks": all(row[1] == row[2] for row in parts),
        "unresolved_source_counts": missing,
        "resumable_per_count_worker_orchestration": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, separators=(",", ":"))
        handle.write("\n")
    return 0 if not missing else 2


if __name__ == "__main__":
    raise SystemExit(main())

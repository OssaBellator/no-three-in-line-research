#!/usr/bin/env python3
"""Run a deterministic shard of minimum-seven attempts at budget seven.

This is an operational wrapper around the certified state reconstruction and the
witness-producing exact-cover kernel. Attempts, rather than individual cores,
are assigned by index modulo the shard count so every attempt's shared point set
is constructed once per shard.
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
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def parse_point(token: str) -> tuple[int, int]:
    x, y = token.split(",")
    return int(x), int(y)


def main() -> None:
    args = parse_args()
    if args.shard_count <= 0:
        raise SystemExit("--shard-count must be positive")
    if not 0 <= args.shard_index < args.shard_count:
        raise SystemExit("--shard-index must lie in [0, shard-count)")

    context = runpy.run_path(str(HERE / "check_boundary_continuation_694.py"))
    state = context["state21"]
    block = context["block"]
    attempts = [attempt for attempt in context["s22"][2] if attempt[3] == 7]
    assert len(attempts) == 205

    selected = [
        (attempt_index, attempt)
        for attempt_index, attempt in enumerate(attempts)
        if attempt_index % args.shard_count == args.shard_index
    ]

    records = []
    with tempfile.TemporaryDirectory() as directory:
        binary = context["compile"](
            "boundary_exact_cover_kernel.cpp", Path(directory)
        )
        for attempt_index, attempt in selected:
            name, offset, _triples, minimum, cores = attempt
            assert minimum == 7
            all_points = sorted(state | block(name, 84, offset))
            input_lines = [str(len(cores))]
            for core_index, core in enumerate(cores):
                identifier = f"a{attempt_index}c{core_index}"
                input_lines.append(
                    f"{identifier} {len(all_points)} 7 {len(core)}"
                )
                input_lines.extend(f"{x} {y}" for x, y in all_points)
                input_lines.extend(f"{x} {y}" for x, y in core)

            output = subprocess.run(
                [str(binary)],
                input="\n".join(input_lines) + "\n",
                text=True,
                capture_output=True,
                check=True,
            )
            assert output.stderr == ""
            lines = output.stdout.splitlines()
            cursor = 0
            for core_index, core in enumerate(cores):
                fields = lines[cursor].split()
                cursor += 1
                assert fields[:2] == [
                    "RES", f"a{attempt_index}c{core_index}"
                ]
                found = fields[2] == "1"
                record = {
                    "attempt_index": attempt_index,
                    "core_index": core_index,
                    "attempt_name": name,
                    "offset": offset,
                    "core": list(core),
                    "repair_found": found,
                    "exact_cover_subsets_tested_until_stop": int(fields[3]),
                    "exact_cover_nodes_tested_until_stop": int(fields[4]),
                }
                if found:
                    deleted_line = lines[cursor].split()
                    added_line = lines[cursor + 1].split()
                    cursor += 2
                    assert deleted_line[0] == "D"
                    assert added_line[0] == "A"
                    record["deleted"] = [
                        parse_point(token) for token in deleted_line[1:]
                    ]
                    record["added"] = [
                        parse_point(token) for token in added_line[1:]
                    ]
                records.append(record)
            assert cursor == len(lines)

    payload = {
        "frontier": "twenty-second raw minimum-seven layer",
        "budget": 7,
        "total_attempts": 205,
        "shard_index": args.shard_index,
        "shard_count": args.shard_count,
        "attempt_indices": [index for index, _attempt in selected],
        "core_records": len(records),
        "repairs": sum(record["repair_found"] for record in records),
        "records": records,
        "status": "passed",
        "warning": (
            "Shard witnesses are kernel output only. The complete merge must rerun "
            "independent coordinate audits and next-spectrum comparisons."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "shard_index": args.shard_index,
        "attempts": len(selected),
        "cores": len(records),
        "repairs": payload["repairs"],
        "status": "passed",
    }, sort_keys=True))


if __name__ == "__main__":
    main()

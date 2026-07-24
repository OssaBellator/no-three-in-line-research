#!/usr/bin/env python3
"""Compile and verify the exact unrestricted PX28 obstruction at base side eight."""
from __future__ import annotations

import argparse
import re
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ORIENTATIONS = ("cc", "cf", "ff")
SHARDS = 5
EXPECTED = {
    ("cc", 0): (103, 3_336_122),
    ("cc", 1): (103, 3_381_122),
    ("cc", 2): (102, 3_356_577),
    ("cc", 3): (102, 3_311_142),
    ("cc", 4): (102, 3_416_801),
    ("cf", 0): (103, 3_861_211),
    ("cf", 1): (103, 3_874_367),
    ("cf", 2): (102, 3_943_299),
    ("cf", 3): (102, 4_082_627),
    ("cf", 4): (102, 4_058_218),
    ("ff", 0): (103, 3_242_573),
    ("ff", 1): (103, 3_272_105),
    ("ff", 2): (102, 3_225_108),
    ("ff", 3): (102, 3_086_566),
    ("ff", 4): (102, 3_244_262),
}
PATTERN = re.compile(
    r"n=8 ori=(cc|cf|ff) shard=(\d)/5 roots=(\d+) "
    r"ok=0 nodes=(\d+) sec=([0-9.]+)"
)


def run_shard(binary: Path, orientation: str, shard: int) -> tuple[str, int, int, float]:
    completed = subprocess.run(
        [str(binary), "8", orientation, "shard", str(shard), str(SHARDS)],
        check=True,
        text=True,
        capture_output=True,
    )
    match = PATTERN.search(completed.stdout)
    if match is None:
        raise AssertionError((orientation, shard, completed.stdout, completed.stderr))
    parsed_orientation, parsed_shard, roots, nodes, seconds = match.groups()
    assert parsed_orientation == orientation
    assert int(parsed_shard) == shard
    expected_roots, expected_nodes = EXPECTED[(orientation, shard)]
    assert int(roots) == expected_roots, (orientation, shard, roots, expected_roots)
    assert int(nodes) == expected_nodes, (orientation, shard, nodes, expected_nodes)
    return orientation, shard, int(nodes), float(seconds)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=int, default=5)
    parser.add_argument("--orientation", choices=ORIENTATIONS)
    args = parser.parse_args()

    source = Path(__file__).with_suffix(".cpp")
    assert source.exists(), source
    orientations = (args.orientation,) if args.orientation else ORIENTATIONS

    with tempfile.TemporaryDirectory() as temporary_directory:
        binary = Path(temporary_directory) / "verify_product_unrestricted_eight"
        subprocess.run(
            ["g++", "-O3", "-march=native", "-std=c++17", str(source), "-o", str(binary)],
            check=True,
        )
        tasks = [(orientation, shard) for orientation in orientations for shard in range(SHARDS)]
        with ThreadPoolExecutor(max_workers=args.jobs) as executor:
            results = list(
                executor.map(
                    lambda item: run_shard(binary, item[0], item[1]),
                    tasks,
                )
            )

    totals: dict[str, int] = {orientation: 0 for orientation in orientations}
    for orientation, shard, nodes, seconds in sorted(results):
        totals[orientation] += nodes
        print(
            f"n=8 orientation={orientation} shard={shard}/{SHARDS}: "
            f"infeasible, nodes={nodes}, seconds={seconds:.3f}"
        )
    for orientation in orientations:
        print(f"n=8 orientation={orientation}: total shard nodes={totals[orientation]}")
    if args.orientation is None:
        assert totals == {"cc": 16_801_764, "cf": 19_819_722, "ff": 16_070_614}
        print("n=8 orientation=fc follows exactly from cf by scalar transposition")
        print("all unrestricted PX28 base-eight orientations are infeasible")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the affine-column obstruction for the side-twelve transposition class."""

from __future__ import annotations

import concurrent.futures
import os
import re
import subprocess
import tempfile
from pathlib import Path


EXPECTED = {
    "cc": (30_052_757, 215_309),
    "cf": (56_638_188, 323_178),
    "fc": (30_488_889, 259_065),
    "ff": (58_535_712, 405_180),
}
PAIR_COUNT = 2_304
CHUNK_SIZE = 96
LINE = re.compile(
    r"^NONE n=12 o=(cc|cf|fc|ff) first=(\d+) pairs=(\d+) "
    r"total=(\d+) avg=(\d+) max=(\d+)$"
)


def run_chunk(
    executable: Path,
    orientation: str,
    first_pair: int,
) -> tuple[int, int, int, int, int]:
    completed = subprocess.run(
        [
            str(executable),
            "12",
            orientation,
            str(first_pair),
            str(CHUNK_SIZE),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    output = completed.stdout.strip()
    assert not output.startswith("FOUND"), output
    match = LINE.fullmatch(output)
    assert match is not None, output
    assert match.group(1) == orientation
    return tuple(int(match.group(index)) for index in range(2, 7))


def main() -> None:
    source = Path(__file__).with_name(
        "search_product_transposition_affine_columns.cpp"
    )
    assert source.exists(), source

    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "transposition_affine_columns"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )

        workers = min(8, os.cpu_count() or 1)
        for orientation, expected in EXPECTED.items():
            starts = list(range(0, PAIR_COUNT, CHUNK_SIZE))
            with concurrent.futures.ThreadPoolExecutor(
                max_workers=workers
            ) as executor:
                rows = list(
                    executor.map(
                        lambda start: run_chunk(executable, orientation, start),
                        starts,
                    )
                )

            assert sorted(row[0] for row in rows) == starts
            assert sum(row[1] for row in rows) == PAIR_COUNT
            total_nodes = sum(row[2] for row in rows)
            maximum_nodes = max(row[4] for row in rows)
            assert (total_nodes, maximum_nodes) == expected, (
                orientation,
                total_nodes,
                maximum_nodes,
                expected,
            )
            print(
                f"NONE n=12 o={orientation} pairs={PAIR_COUNT} "
                f"total={total_nodes} avg={total_nodes // PAIR_COUNT} "
                f"max={maximum_nodes}"
            )

    print(
        "side-twelve all-transposition class: "
        "no affine T,Q geometry with arbitrary P"
    )


if __name__ == "__main__":
    main()

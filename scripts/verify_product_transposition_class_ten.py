#!/usr/bin/env python3
"""Verify the affine-column obstruction for the side-ten transposition class."""

from __future__ import annotations

import concurrent.futures
import os
import re
import subprocess
import tempfile
from pathlib import Path


EXPECTED = {
    "cc": (35_797_487, 495_008),
    "cf": (23_449_947, 183_088),
    "fc": (72_141_241, 2_818_716),
    "ff": (34_485_733, 361_408),
}
PAIR_COUNT = 1_600
CHUNK_SIZE = 100
LINE = re.compile(
    r"^NONE n=10 o=(cc|cf|fc|ff) first=(\d+) pairs=(\d+) "
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
            "10",
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
                f"NONE n=10 o={orientation} pairs={PAIR_COUNT} "
                f"total={total_nodes} avg={total_nodes // PAIR_COUNT} "
                f"max={maximum_nodes}"
            )

    print(
        "side-ten all-transposition class: "
        "no affine T,Q geometry with arbitrary P"
    )


if __name__ == "__main__":
    main()

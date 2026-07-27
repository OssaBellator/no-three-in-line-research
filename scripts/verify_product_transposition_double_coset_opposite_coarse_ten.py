#!/usr/bin/env python3
"""Verify the opposite-pair double coset in side-ten coarse-row orientations."""

from __future__ import annotations

import concurrent.futures
import os
import re
import subprocess
import tempfile
from pathlib import Path


EXPECTED = {
    "cc": (152_056_230, 337_026),
    "cf": (114_391_525, 214_783),
}
PAIR_COUNT = 8_000
CHUNK_SIZE = 100
LINE = re.compile(
    r"^NONE n=10 o=(cc|cf) distance=5 maps=200 first=(\d+) "
    r"pairs=(\d+) total=(\d+) avg=(\d+) max=(\d+)$"
)


def run_chunk(
    executable: Path,
    orientation: str,
    first_pair: int,
) -> tuple[int, int, int, int, int]:
    completed = subprocess.run(
        [
            str(executable),
            orientation,
            "5",
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
        "search_product_transposition_double_coset_ten.cpp"
    )
    assert source.exists(), source

    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "double_coset_search"
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
                f"NONE n=10 o={orientation} distance=5 maps=200 "
                f"pairs={PAIR_COUNT} total={total_nodes} "
                f"avg={total_nodes // PAIR_COUNT} max={maximum_nodes}"
            )

    print(
        "side-ten opposite-pair double coset: "
        "coarse-row orientations cc and cf are infeasible"
    )


if __name__ == "__main__":
    main()

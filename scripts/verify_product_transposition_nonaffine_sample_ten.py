#!/usr/bin/env python3
"""Replay a deterministic exact non-affine side-ten recursion sample."""

from __future__ import annotations

import concurrent.futures
import os
import subprocess
import tempfile
from pathlib import Path


EXPECTED = {
    "cc": "NONE n=10 o=cc samples=250 seed=101 draws=250 total=6379764 max=162281",
    "cf": "NONE n=10 o=cf samples=250 seed=202 draws=250 total=4982669 max=116189",
    "fc": "NONE n=10 o=fc samples=250 seed=303 draws=250 total=13423505 max=1314865",
    "ff": "NONE n=10 o=ff samples=250 seed=404 draws=250 total=6961172 max=474867",
}
SEEDS = {"cc": 101, "cf": 202, "fc": 303, "ff": 404}


def run_orientation(executable: Path, orientation: str) -> str:
    completed = subprocess.run(
        [str(executable), "10", orientation, "250", str(SEEDS[orientation])],
        check=True,
        capture_output=True,
        text=True,
    )
    output = completed.stdout.strip()
    assert not output.startswith("FOUND"), output
    assert output == EXPECTED[orientation], (
        orientation,
        output,
        EXPECTED[orientation],
    )
    return output


def main() -> None:
    source = Path(__file__).with_name(
        "search_product_transposition_nonaffine_sample.cpp"
    )
    assert source.exists(), source

    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "nonaffine_sample"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=min(4, os.cpu_count() or 1)
        ) as executor:
            outputs = list(
                executor.map(
                    lambda orientation: run_orientation(executable, orientation),
                    EXPECTED,
                )
            )

    for output in outputs:
        print(output)
    print(
        "side-ten all-transposition class: "
        "1000 deterministic non-affine geometries tested exactly; no witness"
    )


if __name__ == "__main__":
    main()

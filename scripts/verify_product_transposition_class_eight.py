#!/usr/bin/env python3
"""Verify the affine-column obstruction for the side-eight transposition class."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "cc": "NONE o=cc pairs=1024 total=5352870 avg=5227 max=49571",
    "cf": "NONE o=cf pairs=1024 total=6894433 avg=6732 max=37471",
    "fc": "NONE o=fc pairs=1024 total=9863816 avg=9632 max=206093",
    "ff": "NONE o=ff pairs=1024 total=11574689 avg=11303 max=82500",
}


def main() -> None:
    source = Path(__file__).with_suffix(".cpp")
    assert source.exists(), source

    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "transposition_class_eight"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )

        for orientation, expected in EXPECTED.items():
            completed = subprocess.run(
                [str(executable), orientation],
                check=True,
                capture_output=True,
                text=True,
            )
            output = completed.stdout.strip()
            assert output == expected, (orientation, output, expected)
            print(output)

    print(
        "side-eight all-transposition class: no affine T,Q geometry with arbitrary P"
    )


if __name__ == "__main__":
    main()

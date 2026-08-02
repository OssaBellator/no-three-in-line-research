#!/usr/bin/env python3
"""Compile and verify the exact bit-affine side-eight transposition census."""
from __future__ import annotations

import pathlib
import re
import subprocess
import tempfile

EXPECTED = {
    "cc": (2304, 29_420_820, 134_675),
    "cf": (2304, 32_968_556, 158_842),
    "fc": (2304, 69_724_372, 851_765),
    "ff": (2304, 104_925_268, 614_254),
}


def main() -> None:
    root = pathlib.Path(__file__).resolve().parents[1]
    source = root / "scripts" / "verify_product_bit_affine_transposition_eight.cpp"
    pattern = re.compile(r"NONE o=(\w\w) pairs=(\d+) total=(\d+) max=(\d+)")

    with tempfile.TemporaryDirectory() as directory:
        executable = pathlib.Path(directory) / "bit_affine_eight"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            cwd=root,
            check=True,
        )
        for orientation, expected in EXPECTED.items():
            completed = subprocess.run(
                [str(executable), orientation],
                cwd=root,
                check=True,
                text=True,
                capture_output=True,
            )
            output = completed.stdout.strip()
            match = pattern.fullmatch(output)
            assert match, output
            observed_orientation = match.group(1)
            observed = tuple(int(match.group(index)) for index in range(2, 5))
            assert observed_orientation == orientation
            assert observed == expected, (orientation, observed, expected)
            print(output)

    print("bit-affine all-transposition obstruction verified")


if __name__ == "__main__":
    main()

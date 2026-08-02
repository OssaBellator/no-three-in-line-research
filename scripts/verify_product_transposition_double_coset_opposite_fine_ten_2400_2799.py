#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 2400 through 2799 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        2400: (4_563_766, 810_889),
        2500: (6_895_140, 811_641),
        2600: (2_801_776, 263_333),
        2700: (2_448_213, 409_736),
    },
    "ff": {
        2400: (2_371_220, 145_572),
        2500: (1_939_029, 314_014),
        2600: (2_556_553, 200_371),
        2700: (1_889_038, 100_172),
    },
}
LINE = re.compile(
    r"^NONE n=10 o=(fc|ff) distance=5 maps=200 first=(\d+) "
    r"pairs=100 total=(\d+) avg=(\d+) max=(\d+)$"
)


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / "search_product_transposition_double_coset_ten.cpp"
    assert source.exists(), source

    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "double-coset-search"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )
        totals = {"fc": 0, "ff": 0}
        maxima = {"fc": 0, "ff": 0}
        for orientation in ("fc", "ff"):
            for first_pair in (2400, 2500, 2600, 2700):
                completed = subprocess.run(
                    [str(executable), orientation, "5", str(first_pair), "100"],
                    check=True,
                    capture_output=True,
                    text=True,
                )
                output = completed.stdout.strip()
                assert not output.startswith("FOUND"), output
                match = LINE.fullmatch(output)
                assert match is not None, output
                assert match.group(1) == orientation
                assert int(match.group(2)) == first_pair
                total = int(match.group(3))
                average = int(match.group(4))
                maximum = int(match.group(5))
                assert (total, maximum) == EXPECTED[orientation][first_pair]
                assert average == total // 100
                totals[orientation] += total
                maxima[orientation] = max(maxima[orientation], maximum)
                print(output)

    assert totals == {"fc": 16_708_895, "ff": 8_755_840}
    assert maxima == {"fc": 811_641, "ff": 314_014}
    print(
        "PX1095--PX1097 side-ten opposite-pair fine-row seventh prefix: "
        "fc_nodes=16708895 ff_nodes=8755840 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()

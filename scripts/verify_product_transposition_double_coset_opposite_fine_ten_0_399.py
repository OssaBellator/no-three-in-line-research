#!/usr/bin/env python3
"""Verify the first 400 opposite-pair fine-row geometries at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        0: (610_634, 18_321),
        100: (560_044, 13_716),
        200: (510_123, 16_195),
        300: (487_926, 16_500),
    },
    "ff": {
        0: (298_206, 12_723),
        100: (310_324, 9_718),
        200: (290_210, 11_044),
        300: (263_988, 14_278),
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

        totals: dict[str, int] = {"fc": 0, "ff": 0}
        maxima: dict[str, int] = {"fc": 0, "ff": 0}
        for orientation in ("fc", "ff"):
            for first_pair in (0, 100, 200, 300):
                completed = subprocess.run(
                    [
                        str(executable),
                        orientation,
                        "5",
                        str(first_pair),
                        "100",
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
                assert int(match.group(2)) == first_pair
                total = int(match.group(3))
                average = int(match.group(4))
                maximum = int(match.group(5))
                expected_total, expected_maximum = EXPECTED[orientation][first_pair]
                assert (total, maximum) == (expected_total, expected_maximum)
                assert average == total // 100
                totals[orientation] += total
                maxima[orientation] = max(maxima[orientation], maximum)
                print(output)

    assert totals == {"fc": 2_168_727, "ff": 1_162_728}
    assert maxima == {"fc": 18_321, "ff": 14_278}
    print(
        "PX1044--PX1046 side-ten opposite-pair fine-row prefix: "
        "fc_nodes=2168727 ff_nodes=1162728 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()

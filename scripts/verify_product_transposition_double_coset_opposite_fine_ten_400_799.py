#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 400 through 799 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        400: (457_877, 9_420),
        500: (393_513, 13_421),
        600: (598_764, 18_432),
        700: (457_847, 23_691),
    },
    "ff": {
        400: (290_148, 19_518),
        500: (249_269, 14_180),
        600: (383_909, 33_547),
        700: (573_022, 53_139),
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
            for first_pair in (400, 500, 600, 700):
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

    assert totals == {"fc": 1_908_001, "ff": 1_496_348}
    assert maxima == {"fc": 23_691, "ff": 53_139}
    print(
        "PX1047--PX1049 side-ten opposite-pair fine-row second prefix: "
        "fc_nodes=1908001 ff_nodes=1496348 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 3600 through 3999 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        3600: (2_528_158, 146_051),
        3700: (4_284_334, 256_437),
        3800: (2_912_136, 111_426),
        3900: (2_572_161, 149_592),
    },
    "ff": {
        3600: (3_456_168, 616_766),
        3700: (3_044_983, 280_226),
        3800: (1_943_360, 124_984),
        3900: (1_685_357, 89_347),
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
            for first_pair in (3600, 3700, 3800, 3900):
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

    assert totals == {"fc": 12_296_789, "ff": 10_129_868}
    assert maxima == {"fc": 256_437, "ff": 616_766}
    print(
        "PX1136--PX1138 side-ten opposite-pair fine-row tenth prefix: "
        "fc_nodes=12296789 ff_nodes=10129868 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()

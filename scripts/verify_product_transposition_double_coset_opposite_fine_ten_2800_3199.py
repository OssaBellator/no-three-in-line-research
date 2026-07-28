#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 2800 through 3199 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        2800: (4_794_532, 497_413),
        2900: (8_750_171, 823_382),
        3000: (8_192_818, 1_387_828),
        3100: (12_947_020, 674_754),
    },
    "ff": {
        2800: (4_522_407, 740_706),
        2900: (4_182_037, 443_114),
        3000: (2_625_942, 191_947),
        3100: (2_361_072, 296_010),
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
            for first_pair in (2800, 2900, 3000, 3100):
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

    assert totals == {"fc": 34_684_541, "ff": 13_691_458}
    assert maxima == {"fc": 1_387_828, "ff": 740_706}
    print(
        "PX1122--PX1124 side-ten opposite-pair fine-row eighth prefix: "
        "fc_nodes=34684541 ff_nodes=13691458 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()

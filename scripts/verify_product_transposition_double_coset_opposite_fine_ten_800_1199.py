#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 800 through 1199 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        800: (613_918, 30_404),
        900: (595_801, 41_699),
        1000: (1_175_010, 102_050),
        1100: (1_432_463, 68_768),
    },
    "ff": {
        800: (1_479_138, 168_049),
        900: (1_729_715, 142_919),
        1000: (2_107_202, 111_917),
        1100: (3_407_259, 396_937),
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
            for first_pair in (800, 900, 1000, 1100):
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

    assert totals == {"fc": 3_817_192, "ff": 8_723_314}
    assert maxima == {"fc": 102_050, "ff": 396_937}
    print(
        "PX1066--PX1068 side-ten opposite-pair fine-row third prefix: "
        "fc_nodes=3817192 ff_nodes=8723314 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 3200 through 3599 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        3200: (5_716_774, 319_997),
        3300: (3_825_283, 421_080),
        3400: (3_384_865, 213_636),
        3500: (3_657_273, 149_780),
    },
    "ff": {
        3200: (1_989_681, 110_191),
        3300: (2_251_035, 194_878),
        3400: (1_749_589, 213_367),
        3500: (1_620_334, 85_076),
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
            for first_pair in (3200, 3300, 3400, 3500):
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

    assert totals == {"fc": 16_584_195, "ff": 7_610_639}
    assert maxima == {"fc": 421_080, "ff": 213_367}
    print(
        "PX1133--PX1135 side-ten opposite-pair fine-row ninth prefix: "
        "fc_nodes=16584195 ff_nodes=7610639 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()

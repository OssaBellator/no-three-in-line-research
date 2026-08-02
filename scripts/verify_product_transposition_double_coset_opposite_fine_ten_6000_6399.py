#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 6000 through 6399 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        6000: (469_639, 17_824),
        6100: (547_596, 17_172),
        6200: (638_837, 23_756),
        6300: (747_433, 21_420),
    },
    "ff": {
        6000: (531_863, 17_818),
        6100: (561_966, 23_590),
        6200: (1_489_081, 76_725),
        6300: (1_387_628, 46_602),
    },
}
LINE = re.compile(
    r"^NONE n=10 o=(fc|ff) distance=5 maps=200 first=(\d+) "
    r"pairs=100 total=(\d+) avg=(\d+) max=(\d+)$"
)


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / "search_product_transposition_double_coset_ten.cpp"
    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "double-coset-search"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )
        totals = {"fc": 0, "ff": 0}
        maxima = {"fc": 0, "ff": 0}
        for orientation in ("fc", "ff"):
            for first_pair in (6000, 6100, 6200, 6300):
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
                total = int(match.group(3))
                average = int(match.group(4))
                maximum = int(match.group(5))
                assert (total, maximum) == EXPECTED[orientation][first_pair]
                assert average == total // 100
                totals[orientation] += total
                maxima[orientation] = max(maxima[orientation], maximum)
                print(output)

    assert totals == {"fc": 2_403_505, "ff": 3_970_538}
    assert maxima == {"fc": 23_756, "ff": 76_725}
    print(
        "PX1215--PX1217 side-ten opposite-pair fine-row sixteenth prefix: "
        "fc_nodes=2403505 ff_nodes=3970538 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()

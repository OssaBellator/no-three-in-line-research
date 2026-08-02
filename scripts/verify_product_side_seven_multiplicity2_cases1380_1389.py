#!/usr/bin/env python3
"""Verify the selector-aware classification of multiplicity-two cases 1380--1389."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    1380: "FINAL case=1380 signature=257,6,516,1032,2176,8224,96 top_orders=44792,40074 top_nodes=271521,212955 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=135770,102179,115148,111332 rejection_total=464429 digest=7319284530954993992 PASS",
    1381: "FINAL case=1381 signature=257,6,516,1032,2176,8224,4128 top_orders=28352,17480 top_nodes=432812,278138 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=75581,45816,73206,48449 rejection_total=243052 digest=3221066886467667313 PASS",
    1382: "FINAL case=1382 signature=257,6,516,1032,2176,8224,8256 top_orders=33060,26098 top_nodes=246894,225368 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=88331,62964,83579,72721 rejection_total=307595 digest=18396338264906931230 PASS",
    1383: "FINAL case=1383 signature=257,6,516,1032,2176,8224,12288 top_orders=18240,8240 top_nodes=403959,370790 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=45623,21047,47338,21789 rejection_total=135797 digest=9146397096454413286 PASS",
    1384: "FINAL case=1384 signature=257,6,516,1032,2176,8256,4128 top_orders=23618,18392 top_nodes=366010,279020 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=60237,44672,59371,47824 rejection_total=212104 digest=2841601550497478034 PASS",
    1385: "FINAL case=1385 signature=257,6,516,1032,2176,8256,4160 top_orders=28352,17480 top_nodes=432812,278138 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=75581,45816,73206,48449 rejection_total=243052 digest=3583209879738751821 PASS",
    1386: "FINAL case=1386 signature=257,6,516,1032,2176,12288,96 top_orders=22544,61072 top_nodes=430742,600118 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=72142,152559,54105,178817 rejection_total=457623 digest=2908957634065235222 PASS",
    1387: "FINAL case=1387 signature=257,6,516,1032,2176,12288,4160 top_orders=13300,44296 top_nodes=355935,692414 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=37465,110511,33629,111242 rejection_total=292847 digest=4688154644453038016 PASS",
    1388: "FINAL case=1388 signature=257,6,516,2064,144,96,4160 top_orders=72470,32072 top_nodes=239934,115331 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=177593,93092,204390,81175 rejection_total=556250 digest=8748161535169185449 PASS",
    1389: "FINAL case=1389 signature=257,6,516,2064,144,96,12288 top_orders=70188,13940 top_nodes=345951,114012 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=184288,39209,186641,41845 rejection_total=451983 digest=11172147241996266398 PASS",
}
FINAL_RE = re.compile(
    r"^FINAL case=(\d+).* top_orders=(\d+),(\d+) top_nodes=(\d+),(\d+) "
    r"infeasible_selectors=(\d+) constructive_selectors=(\d+) "
    r"rejection_nodes=(\d+),(\d+),(\d+),(\d+) rejection_total=(\d+) "
    r"digest=(\d+) PASS$"
)


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / "measure_product_side_seven_single_case_all_selectors.cpp"
    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "classify-case"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )
        top_orders = [0, 0]
        top_nodes = [0, 0]
        rejection_nodes = [0, 0, 0, 0]
        infeasible = constructive = 0
        for case in range(1380, 1390):
            completed = subprocess.run(
                [str(executable), str(case), "2"],
                check=True,
                capture_output=True,
                text=True,
            )
            assert "FEASIBLE " not in completed.stdout
            final = completed.stdout.strip().splitlines()[-1]
            assert final == EXPECTED[case]
            match = FINAL_RE.fullmatch(final)
            assert match is not None
            values = [int(value) for value in match.groups()]
            top_orders[0] += values[1]
            top_orders[1] += values[2]
            top_nodes[0] += values[3]
            top_nodes[1] += values[4]
            infeasible += values[5]
            constructive += values[6]
            for orientation in range(4):
                rejection_nodes[orientation] += values[7 + orientation]
            assert sum(values[7:11]) == values[11]
            print(final)

    assert top_orders == [354_916, 279_144]
    assert top_nodes == [3_526_570, 3_166_284]
    assert infeasible == 20 and constructive == 0
    assert rejection_nodes == [952_611, 717_865, 930_613, 763_643]
    assert sum(rejection_nodes) == 3_364_732
    print(
        "PX1180--PX1183 cases1380--1389: "
        "top_orders=354916,279144 top_nodes=3526570,3166284 "
        "infeasible_selectors=20 constructive_selectors=0 "
        "rejection_nodes=952611,717865,930613,763643 "
        "rejection_total=3364732 PASS"
    )


if __name__ == "__main__":
    main()

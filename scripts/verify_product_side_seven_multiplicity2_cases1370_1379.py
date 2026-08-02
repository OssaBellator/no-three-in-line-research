#!/usr/bin/env python3
"""Verify the selector-aware classification of multiplicity-two cases 1370--1379."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    1370: "FINAL case=1370 signature=257,6,516,1032,144,8224,8256 top_orders=35214,26714 top_nodes=126472,102162 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=91132,68000,91659,69159 rejection_total=319950 digest=1810215207757239972 PASS",
    1371: "FINAL case=1371 signature=257,6,516,1032,144,8224,12288 top_orders=29986,21398 top_nodes=180821,173947 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=80217,53217,77797,56907 rejection_total=268138 digest=1771273280478592961 PASS",
    1372: "FINAL case=1372 signature=257,6,516,1032,144,8256,4128 top_orders=27543,23483 top_nodes=141715,120767 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=67504,58337,69947,57539 rejection_total=253327 digest=5538187135371104426 PASS",
    1373: "FINAL case=1373 signature=257,6,516,1032,144,8256,4160 top_orders=35015,27719 top_nodes=179344,143554 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=88176,73526,91045,71701 rejection_total=324448 digest=6105991396001012831 PASS",
    1374: "FINAL case=1374 signature=257,6,516,1032,144,12288,96 top_orders=45196,42988 top_nodes=230909,207474 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=126700,106162,112564,118325 rejection_total=463751 digest=14917046920312673849 PASS",
    1375: "FINAL case=1375 signature=257,6,516,1032,144,12288,4160 top_orders=33798,54041 top_nodes=199347,294844 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=93417,139353,86921,144173 rejection_total=463864 digest=224476763019304889 PASS",
    1376: "FINAL case=1376 signature=257,6,516,1032,2176,96,4160 top_orders=65744,9188 top_nodes=351453,90236 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=170438,23966,178609,26196 rejection_total=399209 digest=16287483067216321519 PASS",
    1377: "FINAL case=1377 signature=257,6,516,1032,2176,96,12288 top_orders=52608,2864 top_nodes=596481,138502 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=127287,6348,136620,8561 rejection_total=278816 digest=2886759908069204100 PASS",
    1378: "FINAL case=1378 signature=257,6,516,1032,2176,4128,4160 top_orders=33060,26098 top_nodes=246894,225368 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=88331,62964,83579,72721 rejection_total=307595 digest=17753350937339374626 PASS",
    1379: "FINAL case=1379 signature=257,6,516,1032,2176,4128,8256 top_orders=23618,18392 top_nodes=363185,279830 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=60245,44664,59371,47823 rejection_total=212103 digest=473366611310269554 PASS",
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
        for case in range(1370, 1380):
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

    assert top_orders == [381_782, 252_885]
    assert top_nodes == [2_616_621, 1_776_684]
    assert infeasible == 20 and constructive == 0
    assert rejection_nodes == [993_447, 636_537, 988_112, 673_105]
    assert sum(rejection_nodes) == 3_291_201
    print(
        "PX1173--PX1176 cases1370--1379: "
        "top_orders=381782,252885 top_nodes=2616621,1776684 "
        "infeasible_selectors=20 constructive_selectors=0 "
        "rejection_nodes=993447,636537,988112,673105 "
        "rejection_total=3291201 PASS"
    )


if __name__ == "__main__":
    main()

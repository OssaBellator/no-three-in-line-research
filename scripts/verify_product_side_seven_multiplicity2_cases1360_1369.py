#!/usr/bin/env python3
"""Verify the selector-aware classification of multiplicity-two cases 1360--1369."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    1360: "FINAL case=1360 signature=257,6,12,2056,2176,8256,4128 top_orders=81748,86226 top_nodes=273680,277355 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=225040,220126,214159,218976 rejection_total=878301 digest=13131993118497559949 PASS",
    1361: "FINAL case=1361 signature=257,6,12,2056,2176,8256,4160 top_orders=100656,107612 top_nodes=335819,346416 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=266725,280144,284049,286782 rejection_total=1117700 digest=13006766811822709410 PASS",
    1362: "FINAL case=1362 signature=257,6,12,2056,2176,12288,96 top_orders=105120,103920 top_nodes=351515,327967 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=353482,261904,293308,326274 rejection_total=1234968 digest=10571013258278950442 PASS",
    1363: "FINAL case=1363 signature=257,6,12,2056,2176,12288,4160 top_orders=76768,224844 top_nodes=284851,729068 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=229924,584771,222804,670861 rejection_total=1708360 digest=16513937281522596800 PASS",
    1364: "FINAL case=1364 signature=257,6,516,1032,144,96,4160 top_orders=32934,10742 top_nodes=110392,42534 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=77481,27985,88910,25985 rejection_total=220361 digest=1439880033829034356 PASS",
    1365: "FINAL case=1365 signature=257,6,516,1032,144,96,12288 top_orders=39668,6192 top_nodes=198728,60186 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=97948,15134,100659,16577 rejection_total=230318 digest=1293143353359751275 PASS",
    1366: "FINAL case=1366 signature=257,6,516,1032,144,4128,4160 top_orders=35214,26714 top_nodes=126472,102162 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=91132,68000,91659,69159 rejection_total=319950 digest=13126318732264049288 PASS",
    1367: "FINAL case=1367 signature=257,6,516,1032,144,4128,8256 top_orders=27543,23483 top_nodes=141656,121242 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=67510,58340,69942,57536 rejection_total=253328 digest=9591605799865436429 PASS",
    1368: "FINAL case=1368 signature=257,6,516,1032,144,8224,96 top_orders=34522,27910 top_nodes=115712,93388 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=87797,72166,92613,68079 rejection_total=320655 digest=1589417884840706176 PASS",
    1369: "FINAL case=1369 signature=257,6,516,1032,144,8224,4128 top_orders=35015,27719 top_nodes=179344,143554 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=88176,73526,91045,71701 rejection_total=324448 digest=306096196577262883 PASS",
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
        infeasible = 0
        constructive = 0
        for case in range(1360, 1370):
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
            assert values[0] == case
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

    assert top_orders == [569_188, 645_362]
    assert top_nodes == [2_118_169, 2_243_872]
    assert infeasible == 20 and constructive == 0
    assert rejection_nodes == [1_585_215, 1_662_096, 1_549_148, 1_811_930]
    assert sum(rejection_nodes) == 6_608_389
    print(
        "PX1169--PX1172 cases1360--1369: "
        "top_orders=569188,645362 top_nodes=2118169,2243872 "
        "infeasible_selectors=20 constructive_selectors=0 "
        "rejection_nodes=1585215,1662096,1549148,1811930 "
        "rejection_total=6608389 PASS"
    )


if __name__ == "__main__":
    main()

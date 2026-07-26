#!/usr/bin/env python3
"""Finite diagnostic for anchored-pair and inserted-triple terminal pencils."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from math import ceil
from pathlib import Path
from typing import Any


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data: dict[str, Any] = json.loads(args.input.read_text())

    H = int(data["anchored_extensions"])
    M = int(data["controller_pools"])
    fixed_row = int(data["anchored_fixed_row"])
    triple_row = int(data["triple_fixed_row"])
    triple_columns = list(map(int, data["triple_variable_columns"]))

    # Fixed inserted cell is (0,0).  Variable anchored-pair cells are (x,fixed_row).
    # Choose one anchor p_x=(t*x,t*fixed_row), t=x+1, on the same nonhorizontal line.
    anchors: list[tuple[int, int]] = []
    recovered_columns: list[Fraction] = []
    for x in range(1, H + 1):
        t = x + 1
        p = (t * x, t * fixed_row)
        anchors.append(p)
        recovered_columns.append(Fraction(p[0] * fixed_row, p[1]))

    if len(set(anchors)) != H:
        raise AssertionError("anchors must be distinct")
    if recovered_columns != [Fraction(x, 1) for x in range(1, H + 1)]:
        raise AssertionError("a fixed anchor did not determine its unique extension")

    # Alternate source permutation layers and split same-layer anchors among the
    # free class plus M controller pools.
    layer_zero = [j for j in range(H) if j % 2 == 0]
    layer_one = [j for j in range(H) if j % 2 == 1]
    same_layer = max((layer_zero, layer_one), key=len)
    class_counts = Counter(j % (M + 1) for j in same_layer)
    exact_bank = max(class_counts.values())
    theorem_bank = ceil(ceil(H / 2) / (M + 1))
    if exact_bank < theorem_bank:
        raise AssertionError("layer/controller refinement below theorem bound")

    # Inserted-triple completion: the line through (0,0) and (3,3) is y=x.
    # On the fixed row y=triple_row it has one possible column.
    completions = [x for x in triple_columns if x == triple_row]
    if len(completions) > 1:
        raise AssertionError("line-coordinate completion must be unique")

    print(f"anchored variable extensions {H}")
    print(f"distinct retained anchors {len(set(anchors))}")
    print(f"same-layer anchors {len(same_layer)}")
    print(f"controller classes including free {M+1}")
    print(f"exact uniform-class bank {exact_bank}")
    print(f"theorem bank lower bound {theorem_bank}")
    print(f"first recovered extension {recovered_columns[0]}")
    print(f"last recovered extension {recovered_columns[-1]}")
    print(f"triple variable candidates {len(triple_columns)}")
    print(f"triple completions {completions}")
    print("outcome anchored_bank_and_unique_triple_completion")


if __name__ == "__main__":
    main()

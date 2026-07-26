#!/usr/bin/env python3
"""Check one-controller puncture and reserve-budget inequalities."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def load(path: str) -> dict[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    required = {
        "R",
        "gamma",
        "xi",
        "Q",
        "q",
        "star_degree",
        "foreign_cost",
        "star_entry_controller_is_centre",
        "beta",
        "punctures_per_macro",
    }
    missing = required.difference(data)
    if missing:
        raise ValueError(f"missing keys: {sorted(missing)}")
    return data


def main(path: str) -> None:
    data = load(path)
    R = int(data["R"])
    gamma = float(data["gamma"])
    xi = float(data["xi"])
    Q = int(data["Q"])
    q = int(data["q"])
    C = int(data["star_degree"])
    foreign = float(data["foreign_cost"])

    if not (R > 0 and Q >= q >= 3 and C > 0):
        raise ValueError("require R>0, Q>=q>=3, and positive star degree")
    if bool(data["star_entry_controller_is_centre"]):
        raise AssertionError(
            "a noncontroller blocker pair containing the centre cannot be controlled by it"
        )

    original_domain = int(round((gamma + xi) * R))
    punctured_domain = original_domain - 1
    half_margin_threshold = int(round((gamma + xi / 2.0) * R))
    if punctured_domain < half_margin_threshold:
        raise AssertionError("one puncture consumed more than half the reserve")

    self_bound = C * (q - 2) / (Q - 2)
    paid_change_bound = foreign + self_bound - C
    if paid_change_bound >= 0:
        raise AssertionError("stored marked paid state does not improve")

    beta = float(data["beta"])
    punctures = [int(x) for x in data["punctures_per_macro"]]
    reserve_cap = int(beta * R)
    exhausted = [i for i, count in enumerate(punctures) if count >= reserve_cap]

    print(f"original domain lower bound {original_domain}")
    print(f"post-puncture lower bound  {punctured_domain}")
    print(f"half-margin threshold       {half_margin_threshold}")
    print(f"puncture/domain ratio       {1 / R:.12g}")
    print(f"marked self-recapture bound {self_bound:.9f}")
    print(f"paid potential upper bound  {paid_change_bound:.9f}")
    print(f"reserve cap per macro       {reserve_cap}")
    print(f"exhausted macros            {exhausted}")
    print("outcome one_controller_puncture_frees_star")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_controller_puncture_star.py INSTANCE.json")
    main(sys.argv[1])

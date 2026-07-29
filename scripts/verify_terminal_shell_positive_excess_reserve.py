#!/usr/bin/env python3
"""Verify the exact positive-excess terminal-shell reserve ledger."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

TAU = {
    8: Fraction(1468416446839930521721999, 3789940340738886748063650),
    9: Fraction(
        406616023430754819367780545483294984597292560691,
        708943793924084504981546740829982708967717363200,
    ),
    10: Fraction(
        5252950050653541320261353842660696885393101,
        33843848222070502440710524758866309866934400,
    ),
}
HORIZON = {8: 3, 9: 4, 10: 5}
BUDGET = Fraction(2, 5)


def verify(data: dict) -> None:
    assert data["audited_sizes"] == [8, 9, 10]
    assert Fraction(data["common_total_positive_excess_budget"]) == BUDGET
    assert Fraction(data["terminal_uniform_upper_bound"]) == Fraction(3, 5)
    assert len(data["cases"]) == 3

    for row in data["cases"]:
        m = int(row["m"])
        tau = Fraction(row["exact_terminal_shell_factor"])
        reserve = Fraction(row["exact_terminal_positive_excess_reserve"])
        composed = Fraction(row["composed_bound_at_common_budget"])
        margin = Fraction(row["margin_below_one_at_common_budget"])

        assert tau == TAU[m]
        assert int(row["cycle_minimum_horizon"]) == HORIZON[m]
        assert reserve == 1 - tau
        assert composed == tau / (1 - BUDGET) == Fraction(5, 3) * tau
        assert margin == 1 - composed
        assert tau < Fraction(3, 5)
        assert BUDGET < reserve
        assert composed < 1

    assert data["common_positive_excess_budget_contractive_at_all_sizes"]
    assert not data["nonterminal_shell_factors_audited"]
    assert not data["asymptotic_shell_depth_bound_proved"]
    assert data["all_exact_regressions_verified"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    args = parser.parse_args()
    path = (
        args.root.resolve()
        / "experiments"
        / "terminal-shell-positive-excess-reserve-through-m10-audit.json"
    )
    verify(json.loads(path.read_text()))
    print("terminal-shell positive-excess reserve verified")
    for m in (8, 9, 10):
        value = Fraction(5, 3) * TAU[m]
        print(f"m={m} bound={value} decimal={float(value):.12f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

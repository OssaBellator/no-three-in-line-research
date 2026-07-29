#!/usr/bin/env python3
"""Verify the exact terminal-shell reserve budgets through m=10."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction
from pathlib import Path

EXPECTED = {
    8: (3, Fraction(1468416446839930521721999, 3789940340738886748063650), Fraction(8, 5)),
    9: (4, Fraction(406616023430754819367780545483294984597292560691,
                   708943793924084504981546740829982708967717363200), Fraction(6, 5)),
    10: (5, Fraction(5252950050653541320261353842660696885393101,
                    33843848222070502440710524758866309866934400), Fraction(3, 2)),
}
COMMON = Fraction(6, 5)


def verify(data: dict) -> None:
    assert data["audited_sizes"] == [8, 9, 10]
    assert Fraction(data["common_equal_prior_shell_bound"]) == COMMON
    for row in data["cases"]:
        m = int(row["m"])
        horizon, terminal, clean = EXPECTED[m]
        assert int(row["cycle_minimum_horizon"]) == horizon
        assert Fraction(row["exact_terminal_shell_factor"]) == terminal
        assert Fraction(row["exact_prior_shell_product_reserve"]) == 1 / terminal
        assert Fraction(row["clean_equal_prior_shell_bound"]) == clean

        clean_total = terminal * clean ** (horizon - 1)
        common_total = terminal * COMMON ** (horizon - 1)
        assert Fraction(row["composed_bound_at_clean_equal_factor"]) == clean_total
        assert Fraction(row["margin_below_one_at_clean_equal_factor"]) == 1 - clean_total
        assert Fraction(row["composed_bound_at_common_6_over_5"]) == common_total
        assert Fraction(row["margin_below_one_at_common_6_over_5"]) == 1 - common_total
        assert clean_total < 1 and common_total < 1

    assert data["all_clean_equal_factor_budgets_contractive"]
    assert data["common_6_over_5_budget_contractive_at_all_sizes"]
    assert not data["nonterminal_shell_factors_audited"]
    assert data["all_exact_regressions_verified"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    args = parser.parse_args()
    path = args.root.resolve() / "experiments/terminal-shell-expansion-reserve-through-m10-audit.json"
    verify(json.loads(path.read_text()))
    print("terminal shell expansion reserve verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
import json
import sys
from fractions import Fraction
from pathlib import Path


def F(text: str) -> Fraction:
    return Fraction(text)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    path = root / "experiments/terminal-shell-depth-aware-excess-through-m10-audit.json"
    data = json.loads(path.read_text())
    assert data["audited_sizes"] == [8, 9, 10]
    assert F(data["common_total_positive_excess_budget"]) == Fraction(3, 5)
    clean = {8: Fraction(6, 5), 9: Fraction(3, 5), 10: Fraction(2)}
    horizons = {8: 3, 9: 4, 10: 5}
    common = Fraction(3, 5)
    for case in data["cases"]:
        m = case["m"]
        h = case["cycle_minimum_horizon"]
        r = case["nonterminal_boundaries"]
        assert h == horizons[m] and r == h - 1
        tau = F(case["exact_terminal_shell_factor"])
        assert F(case["clean_total_excess_budget"]) == clean[m]
        clean_factor = (1 + clean[m] / r) ** r
        common_factor = (1 + common / r) ** r
        assert clean_factor == F(case["clean_am_gm_factor"])
        assert common_factor == F(case["common_am_gm_factor"])
        clean_bound = tau * clean_factor
        common_bound = tau * common_factor
        assert clean_bound == F(case["composed_bound_at_clean_budget"])
        assert common_bound == F(case["composed_bound_at_common_budget"])
        assert 1 - clean_bound == F(case["margin_below_one_at_clean_budget"])
        assert 1 - common_bound == F(case["margin_below_one_at_common_budget"])
        assert clean_bound < 1 and common_bound < 1
    assert data["all_clean_total_excess_budgets_contractive"] is True
    assert data["common_three_fifths_budget_contractive_at_all_sizes"] is True
    assert data["nonterminal_shell_factors_audited"] is False
    assert data["asymptotic_shell_depth_bound_proved"] is False
    assert data["all_exact_regressions_verified"] is True
    print("terminal shell depth-aware excess profile verified")
    print("common total positive-excess budget = 3/5")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

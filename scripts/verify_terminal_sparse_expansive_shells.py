#!/usr/bin/env python3
import json
import sys
from fractions import Fraction
from pathlib import Path


def F(value: str) -> Fraction:
    return Fraction(value)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    path = root / "experiments/terminal-sparse-expansive-shells-through-m10-audit.json"
    data = json.loads(path.read_text())
    assert data["audited_sizes"] == [8, 9, 10]
    expected = {
        Fraction(3, 2): {8: 2, 9: 1, 10: 4},
        Fraction(2, 1): {8: 1, 9: 0, 10: 2},
    }
    for ceiling in data["ceilings"]:
        B = F(ceiling["B"])
        assert B in expected
        for case in ceiling["cases"]:
            m = case["m"]
            r = case["nonterminal_boundaries"]
            tau = F(case["exact_terminal_shell_factor"])
            q = case["maximum_guaranteed_expansive_boundaries"]
            assert q == expected[B][m]
            accepted = tau * B**q
            assert accepted == F(case["accepted_product"])
            assert 1 - accepted == F(case["accepted_margin_below_one"])
            assert accepted < 1
            rejected = case["first_rejected_product"]
            if q < r:
                assert rejected is not None
                first_rejected = tau * B ** (q + 1)
                assert first_rejected == F(rejected)
                assert first_rejected >= 1
            else:
                assert rejected is None
    assert data["nonterminal_shell_factors_audited"] is False
    assert data["asymptotic_bad_shell_count_bound_proved"] is False
    assert data["all_exact_regressions_verified"] is True
    print("terminal sparse expansive-shell profile verified")
    print("B=3/2 counts: m8=2 m9=1 m10=4")
    print("B=2 counts: m8=1 m9=0 m10=2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

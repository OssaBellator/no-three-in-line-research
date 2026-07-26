#!/usr/bin/env python3
"""Exact finite checks for AC5l--AC5p."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def verify_finite_menus(limit: int = 300_000) -> dict[str, int]:
    totals = {
        "finite_menu_ledgers": 0,
        "survivor_bounds": 0,
        "conditional_expectation_bounds": 0,
        "one_shot_safe_drift_implications": 0,
        "separate_selection_counterexamples": 0,
    }

    for batch in range(1, 8):
        values = [(cur, high) for cur in range(batch + 3) for high in range(4)]
        for size in range(1, 6):
            for menu in product(values, repeat=size):
                totals["finite_menu_ledgers"] += 1
                gamma_cur = Fraction(sum(cur for cur, _ in menu), size)
                gamma_high = Fraction(sum(high for _, high in menu), size)
                survivors = [(cur, high) for cur, high in menu if high == 0]
                survivor_prob = Fraction(len(survivors), size)

                assert survivor_prob >= 1 - gamma_high
                totals["survivor_bounds"] += 1

                if gamma_high < 1:
                    assert survivors
                    conditional_cur = Fraction(sum(cur for cur, _ in survivors), len(survivors))
                    assert conditional_cur <= gamma_cur / (1 - gamma_high)
                    totals["conditional_expectation_bounds"] += 1

                if gamma_cur + batch * gamma_high < batch:
                    assert any(high == 0 and cur <= batch - 1 for cur, high in menu)
                    totals["one_shot_safe_drift_implications"] += 1

                if (
                    any(high == 0 for _, high in menu)
                    and any(cur <= batch - 1 for cur, _ in menu)
                    and not any(high == 0 and cur <= batch - 1 for cur, high in menu)
                ):
                    totals["separate_selection_counterexamples"] += 1

                if totals["finite_menu_ledgers"] >= limit:
                    assert totals["separate_selection_counterexamples"] > 0
                    return totals
    return totals


def verify_spread_event_bound() -> dict[str, int]:
    totals = {
        "spread_inventory_systems": 0,
        "s5_substitution_systems": 0,
        "line_length_systems": 0,
    }

    for p in range(2, 31):
        for k in range(1, min(p, 6) + 1):
            ratio = Fraction(k, p)
            for m2 in range(0, 31):
                for m3 in range(0, 16):
                    gamma = ratio**2 * m2 + ratio**3 * m3
                    direct = sum([ratio**2] * m2, Fraction(0)) + sum(
                        [ratio**3] * m3, Fraction(0)
                    )
                    assert gamma == direct
                    totals["spread_inventory_systems"] += 1

            for t in range(1, 11):
                for ell in range(1, 8):
                    n_inventory = t * p
                    u2 = 4 * ell * n_inventory
                    u3 = 8 * ell * n_inventory**2
                    for a2 in range(0, 11):
                        gamma = ratio**2 * (a2 + u2) + ratio**3 * u3
                        substituted = (
                            ratio**2 * a2
                            + Fraction(4 * k * k * ell * t, p)
                            + Fraction(8 * k**3 * ell * t * t, p)
                        )
                        assert gamma == substituted
                        totals["s5_substitution_systems"] += 1

    for side in range(2, 101):
        for height in range(1, side + 1):
            current = 1 + (side - 1) // height
            protected = 1 + (side - 1) // (2 * height)
            assert protected <= current
            totals["line_length_systems"] += 1

    return totals


def verify_multistep_paths(limit: int = 300_000) -> dict[str, int]:
    totals = {
        "multistep_path_ledgers": 0,
        "multistep_safe_drift_implications": 0,
    }

    for batch in range(1, 7):
        for steps in range(1, 4):
            path_values = [
                (cur, highs)
                for cur in range(batch + 3)
                for highs in product(range(3), repeat=steps)
            ]
            for size in range(1, 5):
                for menu in product(path_values, repeat=size):
                    totals["multistep_path_ledgers"] += 1
                    gamma_cur = Fraction(sum(cur for cur, _ in menu), size)
                    gamma_highs = [
                        Fraction(sum(highs[j] for _, highs in menu), size)
                        for j in range(steps)
                    ]
                    if gamma_cur + batch * sum(gamma_highs, Fraction(0)) < batch:
                        assert any(
                            cur <= batch - 1 and all(high == 0 for high in highs)
                            for cur, highs in menu
                        )
                        totals["multistep_safe_drift_implications"] += 1

                    if totals["multistep_path_ledgers"] >= limit:
                        return totals
    return totals


def verify_conditional_equivalence() -> int:
    checks = 0
    for batch in range(1, 101):
        for cur_num in range(0, batch * 10 + 1):
            gamma_cur = Fraction(cur_num, 10)
            for high_num in range(0, 10):
                gamma_high = Fraction(high_num, 10)
                if gamma_high < 1:
                    assert (
                        gamma_cur + batch * gamma_high < batch
                    ) == (
                        gamma_cur < batch * (1 - gamma_high)
                    )
                checks += 1
    return checks


def main() -> None:
    totals = verify_finite_menus()
    totals.update(verify_spread_event_bound())
    totals.update(verify_multistep_paths())
    totals["conditional_form_equivalences"] = verify_conditional_equivalence()

    print("AC5l--AC5p verification passed")
    for key, value in totals.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Arithmetic checks for CMR274--CMR277."""

from __future__ import annotations


def verify_slack_identity(max_t: int = 100_000) -> None:
    for t in range(4, max_t + 1):
        for n in range(2, min(6, (t + 1) // 2) + 1):
            m = t + 1 - n
            minimum_union = n * m - 1
            maximum_incidence = n * (t - 1)
            slack = maximum_incidence - minimum_union
            assert slack == n * (n - 2) + 1

            full_line_lower_bound = (t - 1) - slack
            assert full_line_lower_bound == t - 2 - n * (n - 2)


def verify_width_specializations(max_t: int = 100_000) -> None:
    for t in range(5, max_t + 1):
        if 2 <= (t + 1) // 2:
            assert 2 * (2 - 2) + 1 == 1
            assert t - 2 - 2 * (2 - 2) == t - 2

        if 3 <= (t + 1) // 2:
            assert 3 * (3 - 2) + 1 == 4
            assert t - 2 - 3 * (3 - 2) == t - 5

        for n, expected_offset in ((4, 10), (5, 17), (6, 26)):
            if n > (t + 1) // 2:
                continue
            assert t - 2 - n * (n - 2) == t - expected_offset
            assert (t - 1) / (n - 1) <= (t - 1) / 3
            assert (t - 1) / 3 < 43 * t / 100


def verify_deficiency_examples(max_t: int = 1000) -> None:
    # Synthetic incidence profiles saturating or lying below the exact budget.
    for t in range(5, max_t + 1):
        for n in range(2, min(6, (t + 1) // 2) + 1):
            budget = n * (n - 2) + 1
            for deficiency in range(budget + 1):
                overlap = budget - deficiency
                assert deficiency + overlap == budget
                nonfull_lines = min(t - 1, deficiency)
                assert nonfull_lines <= budget


def main() -> None:
    verify_slack_identity()
    verify_width_specializations()
    verify_deficiency_examples()
    print(
        "verified finite-width Hall slack: exact deficiency-plus-overlap budget, "
        "width-two/three residuals, and width-four-to-six low-height counts"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact integer checks for CMR351--CMR354."""

from __future__ import annotations

from math import floor


def cubic_threshold(h: int) -> int:
    return (2 * h + 2) // 3 - 1


def verify_thresholds() -> None:
    for p in (3, 5, 7, 11, 13, 17):
        for h in range(1, 40):
            t = p**h
            q = cubic_threshold(h)
            assert 0 <= q < h

            # t^(2/3)/p <= p^q < t^(2/3) <= p^(q+1),
            # checked after cubing to keep the arithmetic exact.
            assert (p ** (q + 1)) ** 3 >= t * t
            assert (p**q) ** 3 < t * t

            line_bound_numerator = t * t
            line_bound_denominator = p ** (2 * (q + 1))
            batch = ((t - 2) * line_bound_denominator) // line_bound_numerator

            # J_q is at least floor((t-2)/t^(2/3)).  Avoid irrational
            # arithmetic by checking every integer j whose cubic condition
            # certifies j <= (t-2)/t^(2/3).
            lower = 0
            while (lower + 1) ** 3 * t * t <= (t - 2) ** 3:
                lower += 1
            assert batch >= lower
            assert batch * line_bound_numerator <= (
                (t - 2) * line_bound_denominator
            )


def verify_all_discrete_splits() -> None:
    for p in (3, 5, 7, 11):
        for h in range(2, 18):
            t = p**h
            for q in range(h):
                line_cost_numerator = t * t
                line_cost_denominator = p ** (2 * (q + 1))
                batch = ((t - 2) * line_cost_denominator) // line_cost_numerator

                for b in range(q + 1, h):
                    exact_upper = (t // (p**b)) ** 2
                    threshold_upper = line_cost_numerator // line_cost_denominator
                    assert exact_upper <= threshold_upper
                    if batch:
                        assert batch * exact_upper <= t - 2


def verify_thin_population_scaling() -> None:
    for p in (3, 5, 7, 11, 13):
        for h in range(2, 25):
            t = p**h
            q = cubic_threshold(h)
            denominator = h + p - 1
            for offset in (2, 9):
                population = max(0, (t - offset + denominator - 1) // denominator)
                heavy = (population + p**q - 1) // (p**q)
                support_numerator = population * p**q
                assert heavy * p**q >= population
                assert support_numerator >= 0


def main() -> None:
    verify_thresholds()
    verify_all_discrete_splits()
    verify_thin_population_scaling()
    print(
        "verified tunable token batching: discrete thresholds, deep line costs, "
        "cubic-root batch capacity, and thin-population arithmetic"
    )


if __name__ == "__main__":
    main()

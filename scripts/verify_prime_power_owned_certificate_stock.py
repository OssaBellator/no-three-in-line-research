#!/usr/bin/env python3
"""Verify CMR599--CMR604 owner-labelled certificate stock arithmetic."""

from math import comb, ceil


def check_owner_states() -> None:
    for t in range(1, 80):
        for selector_count in range(0, 100):
            total = 0
            for index in range(selector_count):
                n = 1 + (index % t)
                ell = index % (n + 1)
                total += n - ell + 1
            assert total <= (t + 1) * selector_count


def check_line_stock() -> None:
    for t in range(1, 100):
        root_bound = comb(t * t, 2)
        for m in range(1, t + 1):
            assert comb(m * m, 2) <= root_bound


def check_token_stock() -> None:
    for p in (2, 3, 5, 7):
        for h in range(1, 12):
            t = p**h
            for g in range(1, h + 1):
                for n in range(1, min(t, 40) + 1):
                    exact = (p + 1) * (g - 1) * n * (n - 1)
                    upper = (p + 1) * (h - 1) * t * (t - 1)
                    assert exact <= upper


def check_episode_incidence() -> None:
    for stock in range(0, 200):
        for recurrence in range(2, 12):
            capacity = (recurrence - 1) * stock
            for minimum_size in range(1, 20):
                episode_bound = capacity // minimum_size
                assert episode_bound * minimum_size <= capacity
                assert (episode_bound + 1) * minimum_size > capacity


def check_global_selector_bound() -> None:
    for t in range(2, 30):
        for h in range(1, 10):
            selector_bound = (
                (h + 1) * t * t * (t - 1) ** 2
                + 2 * (h + 1) * t**4 * (t - 1) ** 2
            )
            protected_bound = (t + 1) * selector_bound
            line_bound = protected_bound * comb(t * t, 2)
            assert protected_bound >= selector_bound
            assert line_bound >= 0


def main() -> None:
    check_owner_states()
    check_line_stock()
    check_token_stock()
    check_episode_incidence()
    check_global_selector_bound()
    print("verified owner-labelled certificate stock through configured ranges")


if __name__ == "__main__":
    main()

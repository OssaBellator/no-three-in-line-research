#!/usr/bin/env python3
"""Finite checks for AC3fp--AC3fr."""

from __future__ import annotations

from itertools import product

SYMBOLS = ("J", "K", "B", "O")


def core_count(envelope_roles: int) -> int:
    return 18 * envelope_roles**3 + 5 * envelope_roles**2


def protected_count(envelope_roles: int, kinds: int, rank: int) -> int:
    return core_count(envelope_roles) + kinds * sum(
        (4 * envelope_roles) ** size for size in range(1, rank + 1)
    )


def verify_cross_words() -> tuple[int, list[tuple[str, ...]]]:
    words = [
        word
        for word in product(SYMBOLS, repeat=3)
        if "J" in word and "K" in word
    ]
    assert len(words) == 18
    assert len(set(words)) == 18
    return len(SYMBOLS) ** 3, words


def verify_core_counts() -> tuple[int, dict[int, int]]:
    expected = {
        11: 24563,
        40: 1160000,
        13: 40391,
        24: 251712,
    }
    for roles, value in expected.items():
        assert core_count(roles) == value
    return len(expected), expected


def verify_protected_counts() -> int:
    checks = 0
    for roles in range(1, 8):
        previous = core_count(roles)
        for kinds in range(0, 5):
            for rank in range(1, 5):
                value = protected_count(roles, kinds, rank)
                assert value >= core_count(roles)
                if kinds > 0:
                    assert value > core_count(roles)
                assert value >= previous or kinds == 0
                checks += 1
            previous = protected_count(roles, kinds, 4)
    return checks


def verify_weighted_label_pigeonhole() -> int:
    checks = 0
    for label_count in range(1, 9):
        for weights in product(range(4), repeat=label_count):
            total = sum(weights)
            if total == 0:
                continue
            assert label_count * max(weights) >= total
            checks += 1
    return checks


def verify_ac2d_scale() -> int:
    checks = 0
    for label_count in range(1, 9):
        for center_weight in range(1, 8):
            for overload_factor in range(2, 10):
                neighbour_weight = (overload_factor - 1) * center_weight + 1
                localized_numerator = neighbour_weight
                assert label_count * (
                    (localized_numerator + label_count - 1) // label_count
                ) >= localized_numerator
                checks += 1
    return checks


def main() -> None:
    incidence_checks, cross_words = verify_cross_words()
    core_checks, core_table = verify_core_counts()
    protected_checks = verify_protected_counts()
    weighted_checks = verify_weighted_label_pigeonhole()
    ac2d_checks = verify_ac2d_scale()

    print("AC overload role dictionary verification passed")
    print(f"  rank-three incidence words checked: {incidence_checks}")
    print(f"  cross-envelope incidence words: {len(cross_words)}")
    print(f"  core-count identities: {core_checks}")
    print(f"  core-count table: {core_table}")
    print(f"  protected-dictionary checks: {protected_checks}")
    print(f"  weighted label ledgers: {weighted_checks}")
    print(f"  AC2d localization-scale checks: {ac2d_checks}")


if __name__ == "__main__":
    main()

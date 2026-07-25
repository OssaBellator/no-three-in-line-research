#!/usr/bin/env python3
"""Finite checks for AC3fm--AC3fo."""

from __future__ import annotations

from itertools import product


def verify_words() -> tuple[int, dict[int, int]]:
    checks = 0
    counts: dict[int, int] = {}
    for crossed_count in (1, 2, 3):
        words = [
            word
            for word in product((0, 1), repeat=crossed_count)
            if any(word)
        ]
        assert len(words) == 2**crossed_count - 1
        counts[crossed_count] = len(words)
        for word in words:
            rank = sum(word)
            assert 1 <= rank <= crossed_count
            checks += 1
    assert counts == {1: 1, 2: 3, 3: 7}
    return checks, counts


def verify_weighted_ledgers() -> int:
    checks = 0
    # Twenty-one labelled bins safely dominate the three crossed-count
    # classes followed by their nonzero membership-word splits.
    for weights in product(range(3), repeat=7):
        # Reuse each seven-bin word block at three crossed counts.
        expanded = weights + weights + weights
        total = sum(expanded)
        if total == 0:
            continue
        assert 21 * max(expanded) >= total
        checks += 1
    return checks


def verify_constants() -> int:
    assert 108 * 21 == 2268
    assert 36 * 21 == 756
    return 2


def main() -> None:
    word_checks, counts = verify_words()
    weighted_checks = verify_weighted_ledgers()
    constant_checks = verify_constants()
    print("AC RI blocker rank router verification passed")
    print(f"  membership-word checks: {word_checks}")
    print(f"  crossed-count word totals: {counts}")
    print(f"  weighted ledger checks: {weighted_checks}")
    print(f"  constant checks: {constant_checks}")


if __name__ == "__main__":
    main()

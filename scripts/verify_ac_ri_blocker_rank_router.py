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
    assert sum(counts.values()) == 11
    return checks, counts


def verify_weighted_ledgers() -> int:
    checks = 0
    # Exhaust every eleven-label ledger with entries 0,1,2.
    for weights in product(range(3), repeat=11):
        total = sum(weights)
        if total == 0:
            continue
        assert 11 * max(weights) >= total
        checks += 1
    return checks


def verify_constants() -> int:
    assert 108 * 11 == 1188
    assert 36 * 11 == 396
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

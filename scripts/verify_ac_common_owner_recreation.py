#!/usr/bin/env python3
"""Finite checks for AC3nx--AC3ob."""

from __future__ import annotations

from collections import Counter
from itertools import product


def first_recreation(path: tuple[int, ...], token: int) -> int | None:
    bit = 1 << token
    for index in range(1, len(path)):
        if not (path[index - 1] & bit) and path[index] & bit:
            return index
    return None


def verify_first_recreation(counts: Counter[str]) -> None:
    for token_count in range(1, 5):
        states = tuple(range(1 << token_count))
        for token in range(token_count):
            bit = 1 << token
            for length in range(2, 7):
                for path in product(states, repeat=length):
                    if path[0] & bit or not (path[-1] & bit):
                        continue
                    index = first_recreation(path, token)
                    assert index is not None
                    assert not (path[index - 1] & bit)
                    assert path[index] & bit
                    assert all(not (state & bit) for state in path[:index])
                    counts["absent-to-present paths"] += 1


def verify_cycle_recreation(counts: Counter[str]) -> None:
    for token_count in range(1, 5):
        states = tuple(range(1 << token_count))
        for start in states:
            for token in range(token_count):
                bit = 1 << token
                if not (start & bit):
                    continue
                destroyed = start & ~bit
                for internal_length in range(0, 5):
                    for internal in product(states, repeat=internal_length):
                        path = (destroyed,) + internal + (start,)
                        index = first_recreation(path, token)
                        assert index is not None
                        counts["destroy-return cycles"] += 1


def verify_one_use_before_recreation(counts: Counter[str]) -> None:
    for token_count in range(1, 9):
        current = (1 << token_count) - 1
        used = 0
        steps = 0
        while current:
            token_bit = current & -current
            assert not (used & token_bit)
            current &= ~token_bit
            used |= token_bit
            steps += 1
            # Without recreation every used token remains absent.
            assert current & used == 0
        assert steps == token_count
        assert used.bit_count() == token_count
        counts["recreation-free epochs"] += 1


def verify_recreation_ticket_counter(counts: Counter[str]) -> None:
    for owner_stock in range(0, 8):
        for ticket_stock in range(0, 8):
            destroyed = 0
            tickets = 0
            for _ in range(owner_stock):
                old = destroyed + tickets
                destroyed += 1
                assert destroyed + tickets > old
                counts["new destruction states"] += 1
            for _ in range(ticket_stock):
                old = destroyed + tickets
                tickets += 1
                assert destroyed + tickets > old
                counts["new recreation-ticket states"] += 1
            assert destroyed <= owner_stock
            assert tickets <= ticket_stock


def main() -> None:
    counts: Counter[str] = Counter()
    verify_first_recreation(counts)
    verify_cycle_recreation(counts)
    verify_one_use_before_recreation(counts)
    verify_recreation_ticket_counter(counts)
    print("AC3nx--AC3ob common-owner recreation audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()

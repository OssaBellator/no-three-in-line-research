#!/usr/bin/env python3
"""Verify BDA3e word counts and BDA4a finite recurrence."""

from __future__ import annotations

from itertools import product
from math import gcd


RANK_PATTERNS = {
    (1,),
    (2,),
    (1, 1),
    (3,),
    (2, 1),
    (1, 1, 1),
}


def totient(q: int) -> int:
    return sum(gcd(value, q) == 1 for value in range(q))


def verify_word_count() -> None:
    for q in range(2, 13):
        alphabet = q * q * totient(q)
        exact_upper = sum(alphabet ** sum(pattern) for pattern in RANK_PATTERNS)
        padded_upper = 6 * alphabet**3
        assert exact_upper <= padded_upper
        perfect_alphabet = totient(q)
        perfect_upper = sum(
            perfect_alphabet ** sum(pattern) for pattern in RANK_PATTERNS
        )
        assert perfect_upper <= 6 * perfect_alphabet**3


def verify_deterministic_recurrence(max_size: int = 4) -> None:
    for size in range(1, max_size + 1):
        for successor in product(range(size), repeat=size):
            for start in range(size):
                trace = [start]
                for _ in range(2 * size + 1):
                    trace.append(successor[trace[-1]])

                first_seen: dict[int, int] = {}
                repeated_at = None
                for index, profile in enumerate(trace):
                    if profile in first_seen:
                        repeated_at = (first_seen[profile], index)
                        break
                    first_seen[profile] = index
                assert repeated_at is not None
                left, right = repeated_at
                period = right - left
                assert left < size
                assert 1 <= period <= size
                for index in range(left, len(trace) - period):
                    assert trace[index] == trace[index + period]


def main() -> None:
    verify_word_count()
    verify_deterministic_recurrence()
    print("BDA finite words and transition recurrence: verified")


if __name__ == "__main__":
    main()

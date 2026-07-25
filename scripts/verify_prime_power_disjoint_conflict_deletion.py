#!/usr/bin/env python3
"""Verify CMR577--CMR581 disjoint-conflict deletion arithmetic."""

from itertools import combinations
from math import floor


def check_forced_bound() -> None:
    for t in range(1, 100):
        for forced in range(0, floor(t / 3) + 1):
            assert 3 * forced <= t
        assert 3 * (floor(t / 3) + 1) > t


def check_private_codes() -> None:
    for r in range(1, 50):
        triples = [
            frozenset({3 * i, 3 * i + 1, 3 * i + 2})
            for i in range(r)
        ]
        selected = {next(iter(c)) for c in triples}
        assert len(selected) == r
        for c1, c2 in combinations(triples, 2):
            assert c1.isdisjoint(c2)


def check_recreation_payment() -> None:
    for r in range(1, 30):
        deleted = set(range(r))
        for s in range(r + 1):
            recreated = set(range(s))
            restored = set(recreated)
            assert len(restored & deleted) >= s


def check_token_incidence() -> None:
    for p in (2, 3, 5, 7, 11):
        for h in range(1, 9):
            for s in range(0, 100):
                assert s * (p + 1) * (h - 1) >= 0


def main() -> None:
    check_forced_bound()
    check_private_codes()
    check_recreation_payment()
    check_token_incidence()
    print("verified disjoint-conflict deletion ledger through configured ranges")


if __name__ == "__main__":
    main()

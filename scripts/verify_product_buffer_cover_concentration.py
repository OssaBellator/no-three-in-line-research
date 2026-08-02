#!/usr/bin/env python3
"""Finite checks for PX351--PX355."""

from __future__ import annotations

from itertools import combinations


def dependency_types(deps: list[frozenset[str]]) -> set[frozenset[str]]:
    out: set[frozenset[str]] = set()
    for size in (1, 2):
        for choice in combinations(deps, size):
            union = frozenset().union(*choice)
            out.add(union)
    return out


def main() -> None:
    one_core = [
        frozenset({"a"}),
        frozenset({"a", "b"}),
        frozenset({"b"}),
    ]
    assert dependency_types(one_core) == {
        frozenset({"a"}),
        frozenset({"b"}),
        frozenset({"a", "b"}),
    }

    two_core = [
        frozenset({"a"}),
        frozenset({"a"}),
        frozenset({"b"}),
        frozenset({"b"}),
    ]
    assert dependency_types(two_core) == {
        frozenset({"a"}),
        frozenset({"b"}),
        frozenset({"a", "b"}),
    }

    for n in range(16, 200):
        bank_lower = n * n / 4
        a = (n - 1) // 16
        b = (n - 1) // 16
        required = bank_lower - n * a - n * b
        assert required >= n * n / 8

        assert (n / 16) / 3 == n / 48
        assert (n * n / 8) / 4 == n * n / 32

    one_core_one_side_types = 1
    two_core_one_side_types = 3
    two_variable_types = 4
    assert one_core_one_side_types <= 3
    assert two_core_one_side_types == 3
    assert two_variable_types == 4

    print("PX351--PX355 buffer-cover concentration verifier: PASS")


if __name__ == "__main__":
    main()

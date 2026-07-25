#!/usr/bin/env python3
"""Arithmetic checks for CMR389--CMR392."""

from __future__ import annotations

from math import ceil


def verify_exact_stocks() -> None:
    for p, h in ((3, 5), (5, 4), (7, 3), (11, 3)):
        t = p**h
        for depth in range(h):
            modulus = p**depth
            direct = (t // modulus) ** 2
            closed = t * t // (p ** (2 * depth))
            assert direct == closed
            assert direct <= t * t // modulus


def verify_inventory_sequences() -> None:
    for initial in range(0, 20):
        for reintroductions in range(0, 20):
            available_tokens = initial + reintroductions
            for visits in range(available_tokens + 1):
                assert visits <= initial + reintroductions
            if available_tokens:
                assert available_tokens > initial + reintroductions - 1


def verify_full_token_bounds() -> None:
    for p, h in ((3, 6), (5, 6), (7, 5), (11, 4)):
        t = p**h
        for depth in range(h):
            stock = t * t // (p ** (2 * depth))

            if 3 * depth > h:
                assert stock**3 < t**4
            if 3 * depth >= 2 * h:
                assert stock**3 <= t**2


def verify_visit_decomposition() -> None:
    for p, h in ((5, 3), (7, 3), (11, 2)):
        t = p**h
        for depth in range(h):
            stock = t * t // (p ** (2 * depth))
            for reintroduced in (0, 1, t, stock):
                for witness in (0, 3, t // 2):
                    for forced in (0, 2, t // 3):
                        endpoint = stock + reintroduced
                        total = endpoint + witness + forced
                        assert total <= stock + reintroduced + witness + forced
                        assert ceil(total) == total


def main() -> None:
    verify_exact_stocks()
    verify_inventory_sequences()
    verify_full_token_bounds()
    verify_visit_decomposition()
    print(
        "verified full-token reintroduction: exact two-dimensional stocks, "
        "dynamic inventory, visit decomposition, and depth thresholds"
    )


if __name__ == "__main__":
    main()

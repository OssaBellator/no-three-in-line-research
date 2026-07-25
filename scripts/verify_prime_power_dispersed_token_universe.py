#!/usr/bin/env python3
"""Exact arithmetic checks for CMR364--CMR367."""

from __future__ import annotations


def valuation(n: int, p: int) -> int:
    assert n != 0
    value = 0
    n = abs(n)
    while n % p == 0:
        n //= p
        value += 1
    return value


def count_token_pairs(t: int, p: int, d: int, b: int, slope: int | None) -> int:
    """Count ordered row pairs on the two fixed source slices."""
    modulus = p**b
    rows = list(range(0, t, modulus))
    r = valuation(d, p)
    result = 0
    for first in rows:
        for second in rows:
            displacement = second - first
            if displacement == 0:
                continue
            depth = min(r, valuation(displacement, p))
            if depth != b:
                continue
            if b < r:
                if slope is not None:
                    continue
            else:
                reduced_d = (d // modulus) % p
                reduced_e = (displacement // modulus) % p
                observed = reduced_e * pow(reduced_d, -1, p) % p
                if observed != slope:
                    continue
            result += 1
    return result


def verify_exact_counts() -> None:
    cases = ((3, 2), (3, 3), (3, 4), (5, 2), (5, 3), (7, 2))
    for p, h in cases:
        t = p**h
        for d in range(1, min(t, 3 * p + 1)):
            r = valuation(d, p)
            for b in range(r + 1):
                size = t // (p**b)
                if b < r:
                    observed = count_token_pairs(t, p, d, b, None)
                    expected = size * (size - size // p)
                    assert observed == expected
                else:
                    for slope in range(p):
                        observed = count_token_pairs(t, p, d, b, slope)
                        if slope:
                            expected = size * size // p
                        else:
                            expected = size * (size // p - 1)
                        assert observed == expected


def verify_deep_bound() -> None:
    for p in (3, 5, 7, 11, 13):
        for h in range(2, 25):
            t = p**h
            for b in range(h):
                if p ** (2 * b) <= t:
                    continue
                size = t // (p**b)
                assert size * size <= t // p
                assert (p - 1) * size * size <= t - t // p
                assert t - t // p <= t - 2


def verify_batch_threshold() -> None:
    for p in (3, 5, 7, 11, 13, 17):
        for h in range(2, 20):
            t = p**h
            for token_count in range(1, p):
                total = token_count * (t // p)
                assert total <= t - t // p
                assert total <= t - 2


def main() -> None:
    verify_exact_counts()
    verify_deep_bound()
    verify_batch_threshold()
    print(
        "verified dispersed token universes: exact vertical/nonvertical counts, "
        "the t/p deep bound, and simultaneous p-1-token elimination"
    )


if __name__ == "__main__":
    main()

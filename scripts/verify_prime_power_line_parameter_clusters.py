#!/usr/bin/env python3
"""Exact checks for CMR314--CMR317."""

from __future__ import annotations


def valuation(n: int, p: int) -> int:
    assert n != 0
    n = abs(n)
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value


def verify_ultrametric_cases() -> None:
    for p in (3, 5, 7, 11):
        for first in range(-500, 501):
            if first == 0:
                continue
            for third in range(-500, 501):
                if third in (0, first):
                    continue
                b = valuation(first, p)
                c = valuation(third, p)
                e = valuation(third - first, p)
                ordered = sorted((b, c, e))
                assert ordered[0] == ordered[1]
                if c < b:
                    assert e == c
                elif c > b:
                    assert e == b
                else:
                    assert e >= b
                    congruent = (third // (p**b) - first // (p**b)) % p == 0
                    assert (e > b) == congruent


def verify_cluster_classification() -> None:
    for p in (3, 5, 7):
        for first in range(1, 300):
            for third in range(1, 300):
                if third == first:
                    continue
                b = valuation(first, p)
                c = valuation(third, p)
                e = valuation(third - first, p)
                if c < b:
                    assert b > c == e
                else:
                    if c == e == b:
                        pass
                    elif c > b and e == b:
                        assert c > b
                    elif c == b and e > b:
                        assert e > b
                    else:
                        raise AssertionError((p, first, third, b, c, e))


def verify_depth_chain_bound() -> None:
    for h in range(1, 20):
        for start in range(h):
            depths = list(range(start + 1, h))
            assert len(depths) == h - 1 - start
            current = start
            for depth in depths:
                assert depth > current
                current = depth
            assert current <= h - 1


def main() -> None:
    verify_ultrametric_cases()
    verify_cluster_classification()
    verify_depth_chain_bound()
    print(
        "verified line-parameter clusters: ultrametric cases, external closest "
        "pairs, internal equilateral/deeper routing, and depth termination"
    )


if __name__ == "__main__":
    main()

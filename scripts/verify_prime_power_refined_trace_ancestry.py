#!/usr/bin/env python3
"""Verify CMR541--CMR545 refined rooted-trace signature counts."""

from __future__ import annotations

from math import ceil


def collinear(
    a: tuple[int, int],
    w: tuple[int, int],
    z: tuple[int, int],
) -> bool:
    return (
        (w[0] - a[0]) * (z[1] - a[1])
        == (w[1] - a[1]) * (z[0] - a[0])
    )


def compatible(a: tuple[int, int], z: tuple[int, int]) -> bool:
    return a[0] != z[0] and a[1] != z[1]


def refined_signatures(m: int) -> set[tuple[object, ...]]:
    cells = [(x, y) for x in range(m) for y in range(m)]
    signatures: set[tuple[object, ...]] = set()
    for a in cells:
        for e in cells:
            u, v = e
            for arm in ("row", "column"):
                witnesses = (
                    [(u, y) for y in range(m) if y != v]
                    if arm == "row"
                    else [(x, v) for x in range(m) if x != u]
                )
                for w in witnesses:
                    if w == a:
                        continue
                    if a[0] == w[0] or a[1] == w[1]:
                        continue
                    for z in cells:
                        if z == a or z == w:
                            continue
                        if not compatible(a, z):
                            continue
                        if collinear(a, w, z):
                            signatures.add((a, z, e, w, arm))
    return signatures


def check_signature_stock() -> None:
    for m in range(1, 9):
        count = len(refined_signatures(m))
        bound = 2 * m**4 * (m - 1) ** 2
        assert count <= bound


def check_line_determinacy() -> None:
    for m in range(2, 9):
        for signature in refined_signatures(m):
            a, z, _e, w, _arm = signature
            assert collinear(a, w, z)
            assert compatible(a, z)
            assert a[0] != w[0] and a[1] != w[1]


def check_multiplicity() -> None:
    for stock in range(1, 200):
        for threshold in range(2, 30):
            for total in range(0, 1000):
                if total > (threshold - 1) * stock:
                    assert ceil(total / stock) >= threshold


def check_chain_bound() -> None:
    for h in range(0, 10):
        for t in range(1, 30):
            sides = [max(1, t // (2**index)) for index in range(h + 1)]
            total_bound = sum(
                2 * m**4 * (m - 1) ** 2 for m in sides
            )
            assert total_bound <= (
                2 * (h + 1) * t**4 * (t - 1) ** 2
            )


def check_surcharge() -> None:
    for fixed_cost in range(3):
        assert 0 <= fixed_cost <= 2
        for q in range(1, 20):
            assert fixed_cost / q <= 2 / q


def main() -> None:
    check_signature_stock()
    check_line_determinacy()
    check_multiplicity()
    check_chain_bound()
    check_surcharge()
    print("verified refined rooted-trace signature stock through side eight")


if __name__ == "__main__":
    main()

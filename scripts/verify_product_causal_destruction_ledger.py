#!/usr/bin/env python3
"""Finite checks for PX235--PX239.

The checks are combinatorial.  Collinear triples are represented by an arbitrary
3-uniform certificate family, because the cancellation identities use only set
inclusion.  Packet release is checked by exact permutation enumeration.
"""

from __future__ import annotations

import itertools
import random
from collections.abc import Iterable


def potential(points: Iterable[str], triples: set[tuple[str, str, str]]) -> int:
    point_set = set(points)
    return sum(set(triple) <= point_set for triple in triples)


def check_cancellation_identity(trials: int = 2000, seed: int = 235) -> None:
    rng = random.Random(seed)
    x = [f"x{i}" for i in range(4)]
    a = [f"a{i}" for i in range(4)]
    c0 = [f"c{i}" for i in range(2)]
    w = [f"w{i}" for i in range(2)]
    universe = x + a + c0 + w
    all_triples = list(itertools.combinations(universe, 3))

    for _ in range(trials):
        triples = {triple for triple in all_triples if rng.random() < 0.2}

        current = set(x + a + c0)
        y = set(x + a)
        x_set = set(x)
        xw = set(x + w)
        xaw = set(x + a + w)

        d = potential(current, triples) - potential(y, triples)
        c = potential(xaw, triples) - potential(y, triples)
        raw_delta = c - d

        gamma = potential(xaw, triples) - potential(xw, triples)
        d_star = potential(current, triples) - potential(x_set, triples)
        f_star = potential(xw, triples) - potential(x_set, triples)

        assert f_star - d_star == raw_delta - gamma

        # PX235: the old certificate shadow is exactly the old triples meeting A.
        old_shadow = {triple for triple in triples if set(triple) <= current and set(triple) & set(a)}
        assert len(old_shadow) == potential(current, triples) - potential(set(x + c0), triples)


def check_designated_credits() -> None:
    # Clean-star certificates {z, P_j, Q_j} with Q_j in A.
    order = 11
    x = [f"p{i}" for i in range(order)]
    a = [f"q{i}" for i in range(order)]
    w = ["z", "w1"]
    triples = {("z", x[i], a[i]) for i in range(order)}

    gamma = potential(set(x + a + w), triples) - potential(set(x + w), triples)
    assert gamma == order

    # Radial certificates {u, v, a_j}.
    radial_order = 9
    anchors = [f"r{i}" for i in range(radial_order)]
    radial_triples = {("u", "v", anchor) for anchor in anchors}
    radial_gamma = potential(set(anchors + ["u", "v"]), radial_triples) - potential(
        {"u", "v"}, radial_triples
    )
    assert radial_gamma == radial_order


def avoids_forbidden(perm: tuple[int, ...], forbidden: set[tuple[int, int]]) -> bool:
    return all((row, perm[row]) not in forbidden for row in range(len(perm)))


def has_two_cycle(perm: tuple[int, ...], i: int, j: int) -> bool:
    return perm[i] == j and perm[j] == i


def has_no_two_cycle(perm: tuple[int, ...]) -> bool:
    order = len(perm)
    return all(not has_two_cycle(perm, i, j) for i in range(order) for j in range(i + 1, order))


def check_packet_credit_separation(order: int = 6) -> None:
    # The current matching contains the packet two-cycle 0 <-> 1.  Its cells are
    # inherited forbidden positions, so the old defect is already absent in the
    # base allowed bank.  A different prospective transposition remains possible
    # until the packet release condition is imposed.
    current = (1, 0, 2, 3, 4, 5)
    forbidden = {(row, current[row]) for row in range(order)}

    base = [
        perm
        for perm in itertools.permutations(range(order))
        if avoids_forbidden(perm, forbidden)
    ]
    released = [perm for perm in base if has_no_two_cycle(perm)]

    assert base
    assert released

    old_packet_defect = (0, 1)
    assert has_two_cycle(current, *old_packet_defect)
    assert not any(has_two_cycle(perm, *old_packet_defect) for perm in base)

    prospective_packet_cross = (2, 3)
    assert any(has_two_cycle(perm, *prospective_packet_cross) for perm in base)
    assert not any(has_two_cycle(perm, *prospective_packet_cross) for perm in released)

    print(f"packet order: {order}")
    print(f"base allowed permutations: {len(base)}")
    print(f"released permutations: {len(released)}")


def main() -> None:
    check_cancellation_identity()
    check_designated_credits()
    check_packet_credit_separation()
    print("PX235--PX239 causal ledger checks passed")


if __name__ == "__main__":
    main()

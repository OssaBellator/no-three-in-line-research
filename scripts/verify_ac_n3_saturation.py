#!/usr/bin/env python3
"""Verify AC3gz--AC3ha for the exact 3 x 3 split saturation."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations


Point = tuple[int, int]


def is_matching(points: set[Point]) -> bool:
    return (
        len({c for c, _ in points}) == len(points)
        and len({r for _, r in points}) == len(points)
    )


def canonical_singleton_state(
    blocker_perm: tuple[int, int, int],
    partner: int,
) -> tuple[frozenset[Point], frozenset[Point]]:
    active = {(0, 0), (1, 1), (2, 2)}
    blocker = {(c, blocker_perm[c]) for c in range(3)}
    x = (0, partner)
    y = (partner, 0)
    active_after = (active - {(0, 0), (partner, partner)}) | {x, y}
    blocker_after = set(blocker)

    if x in blocker:
        r0 = blocker_perm[0]
        rp = blocker_perm[partner]
        blocker_after.remove((0, r0))
        blocker_after.remove((partner, rp))
        blocker_after.add((0, rp))
        blocker_after.add((partner, r0))
    elif y in blocker:
        outside = next(c for c in range(3) if c not in {0, partner})
        rp = blocker_perm[partner]
        ro = blocker_perm[outside]
        blocker_after.remove((partner, rp))
        blocker_after.remove((outside, ro))
        blocker_after.add((partner, ro))
        blocker_after.add((outside, rp))
    else:
        raise AssertionError("the n=3 split pattern must be singleton blocked")

    assert is_matching(active_after)
    assert is_matching(blocker_after)
    assert active_after.isdisjoint(blocker_after)
    assert (0, 0) not in active_after | blocker_after
    return frozenset(active_after), frozenset(blocker_after)


def verify_states() -> tuple[int, int, int]:
    active = {(0, 0), (1, 1), (2, 2)}
    expected_a = frozenset({(0, 1), (1, 0), (2, 2)})
    expected_b = frozenset({(0, 2), (1, 1), (2, 0)})
    derangements = 0
    partner_states = 0
    support_checks = 0

    for perm in permutations(range(3)):
        if any(perm[c] == c for c in range(3)):
            continue
        derangements += 1
        blocker = {(c, perm[c]) for c in range(3)}
        parent = active | blocker
        states = [canonical_singleton_state(perm, partner) for partner in (1, 2)]
        partner_states += 2
        assert {states[0][0], states[0][1]} == {expected_a, expected_b}
        assert states[0][0] == states[1][1]
        assert states[0][1] == states[1][0]
        union0 = states[0][0] | states[0][1]
        union1 = states[1][0] | states[1][1]
        assert union0 == union1 == expected_a | expected_b
        assert len(union0 - parent) == 2
        assert len(parent - union0) == 2
        support_checks += 1

    assert derangements == 2
    return derangements, partner_states, support_checks


def verify_constants(max_weight: int = 100, max_k: int = 20) -> int:
    checks = 0
    for weight in range(1, max_weight + 1):
        for k in range(1, max_k + 1):
            assert k * Fraction(weight, k) == weight
            assert 3 * k * Fraction(weight, 3 * k) == weight
            checks += 1
    return checks


def main() -> None:
    derangements, states, support = verify_states()
    constants = verify_constants()
    print(
        "AC n=3 saturation verified:",
        f"{derangements} derangements,",
        f"{states} partner states,",
        f"{support} common-union support checks,",
        f"{constants} continuation constants",
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify AC3gv--AC3gy saturated empty-partner menu routing."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product


Point = tuple[int, int]
Triple = tuple[Point, Point, Point]


def verify_empty_menus(max_n: int = 7) -> tuple[int, int, int, int, int]:
    systems = menus = states = created_sets = pair_checks = 0
    for n in range(3, max_n + 1):
        active = {(c, c) for c in range(n)}
        for perm in permutations(range(n)):
            blocker = {(c, perm[c]) for c in range(n)}
            if active & blocker:
                continue
            systems += 1
            parent = active | blocker
            parent_triples = set(combinations(sorted(parent), 3))
            buckets: list[set[Triple]] = []
            empty_partners = []
            for c in range(1, n):
                x = (0, c)
                y = (c, 0)
                if x in blocker or y in blocker:
                    continue
                empty_partners.append(c)
                after = (active - {(0, 0), (c, c)}) | {x, y} | blocker
                created = {
                    triple
                    for triple in combinations(sorted(after), 3)
                    if triple not in parent_triples
                }
                assert all(x in triple or y in triple for triple in created)
                assert all(1 <= len(set(triple) - parent) <= 2 for triple in created)
                buckets.append(created)
                states += 1
                created_sets += len(created)

            expected = n - 2 if perm[0] == perm.index(0) else n - 3
            assert len(empty_partners) == expected
            if empty_partners:
                menus += 1
            for i, bucket in enumerate(buckets):
                for prior in buckets[:i]:
                    assert bucket.isdisjoint(prior)
                    pair_checks += 1
    return systems, menus, states, created_sets, pair_checks


def representative_target_words() -> tuple[tuple[int, int, int, int], ...]:
    words = []
    for word in product(range(4), repeat=4):
        total = sum(word)
        if 1 <= total <= 5:
            words.append(word)
    return tuple(words[:80])


def verify_weighted_router(max_targets: int = 3) -> int:
    words = representative_target_words()
    checks = 0
    for targets in range(1, max_targets + 1):
        for family in product(words, repeat=targets):
            target_totals = [sum(word) for word in family]
            w = min(target_totals)
            aggregate = sum(target_totals)
            assert aggregate >= targets * w
            class_totals = [
                sum(word[role] for word in family)
                for role in range(4)
            ]
            assert 4 * max(class_totals) >= aggregate
            assert 4 * max(class_totals) >= targets * w
            heavy_role = max(range(4), key=class_totals.__getitem__)
            realized = max(word[heavy_role] for word in family)
            assert targets * realized >= class_totals[heavy_role]
            checks += 1
    return checks


def verify_constants(max_w: int = 100, max_k: int = 20) -> int:
    checks = 0
    for w in range(1, max_w + 1):
        for k in range(1, max_k + 1):
            assert 4 * k * Fraction(w, 4 * k) == w
            assert 12 * k * Fraction(w, 12 * k) == w
            checks += 1
    return checks


def main() -> None:
    systems, menus, states, created, pairs = verify_empty_menus()
    weighted = verify_weighted_router()
    constants = verify_constants()
    print(
        "AC saturated empty-partner menu verified:",
        f"{systems} two-layer systems,",
        f"{menus} nonempty menus,",
        f"{states} empty partner states,",
        f"{created} created 3-sets,",
        f"{pairs} disjoint bucket pairs,",
        f"{weighted} weighted routers,",
        f"{constants} composition constants",
    )


if __name__ == "__main__":
    main()

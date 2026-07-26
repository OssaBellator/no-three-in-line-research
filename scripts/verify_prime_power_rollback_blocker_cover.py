#!/usr/bin/env python3
"""Finite checks for CMR1126--CMR1133."""

import random


def greedy_cover(candidates, host):
    pending = set(candidates)
    cover = []
    while pending:
        candidate = min(pending, key=lambda state: tuple(sorted(state)))
        missing = sorted(set(candidate) - set(host))
        assert missing
        edge = missing[0]
        cover.append(edge)
        pending = {state for state in pending if edge not in state}
    return tuple(cover)


def check_greedy_cover():
    rng = random.Random(1126)
    checked = 0
    covered_states = 0
    for universe_size in range(1, 150):
        universe = set(range(universe_size))
        for _ in range(200):
            anchor_size = rng.randint(0, min(universe_size, 15))
            anchor = frozenset(rng.sample(tuple(universe), anchor_size))
            host = set(anchor)
            complement = tuple(universe - set(anchor))
            host.update(rng.sample(complement, rng.randint(0, len(complement))))
            unavailable = tuple(universe - host)
            if not unavailable:
                continue
            candidates = set()
            for _candidate in range(rng.randint(1, 120)):
                size = rng.randint(1, min(universe_size, 20))
                state = set(rng.sample(tuple(universe), size))
                state.add(rng.choice(unavailable))
                candidates.add(frozenset(state))
            cover = greedy_cover(candidates, host)
            assert len(cover) == len(set(cover))
            assert set(cover) <= set(unavailable)
            assert set(cover).isdisjoint(anchor)
            assert len(cover) <= len(unavailable) <= universe_size
            assert all(set(state) & set(cover) for state in candidates)
            covered_states += len(candidates)
            checked += 1
    return checked, covered_states


def check_bulk_redeletion():
    rng = random.Random(1130)
    checked = 0
    for universe_size in range(1, 200):
        universe = set(range(universe_size))
        for _ in range(200):
            anchor = set(rng.sample(tuple(universe), rng.randint(0, min(20, universe_size))))
            blockers = set(
                rng.sample(
                    tuple(universe - anchor),
                    rng.randint(0, min(30, len(universe - anchor))),
                )
            )
            later_host = set(anchor)
            later_host.update(rng.sample(tuple(universe - anchor), rng.randint(0, len(universe - anchor))))
            returned = blockers & later_host
            normalized = later_host - returned
            assert anchor <= normalized
            assert normalized.isdisjoint(blockers)
            checked += 1
    return checked


def check_branch_arithmetic():
    checked = 0
    for side in range(1, 500):
        owner_path = sum(2 * m * m + m + 1 for m in range(1, side + 1))
        for height in range(1, 20):
            owners = (height + 1) * (2 * side + 1) * owner_path
            blocker_stock = 2 * side * side * owners
            assert blocker_stock >= owners
            checked += 1
    return checked


def main():
    cover_cases, states = check_greedy_cover()
    print(
        "verified rollback blocker cover:",
        cover_cases,
        "covers over",
        states,
        "candidate states,",
        check_bulk_redeletion(),
        "bulk redeletions, and",
        check_branch_arithmetic(),
        "branch bounds",
    )


if __name__ == "__main__":
    main()

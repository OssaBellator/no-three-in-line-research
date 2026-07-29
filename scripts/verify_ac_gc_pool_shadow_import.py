#!/usr/bin/env python3
"""Finite audit for AC5ap--AC5at."""

from itertools import combinations, product


def pair_load(zset, allowed_pairs):
    return sum(frozenset(pair) in allowed_pairs for pair in combinations(sorted(zset), 2))


def increment_terms(old, new, allowed_pairs):
    cross = sum(
        frozenset((z, y)) in allowed_pairs
        for z in old
        for y in new
    )
    new_new = sum(
        frozenset(pair) in allowed_pairs
        for pair in combinations(sorted(new), 2)
    )
    return cross, new_new


def main():
    density_checks = 0
    monotone_checks = 0
    increment_checks = 0
    crossing_checks = 0

    for n in range(1, 9):
        p0 = set(range(n))
        for blocked_mask in range(1 << n):
            blocked = {x for x in p0 if blocked_mask >> x & 1}
            delta = len(blocked) / n if n else 0
            for keep_mask in range(1 << n):
                kept = {x for x in p0 if keep_mask >> x & 1}
                if not kept:
                    continue
                rho = len(kept) / n
                lhs = len(kept - blocked)
                rhs = len(kept) - delta * n
                assert lhs + 1e-12 >= rhs
                assert lhs + 1e-12 >= (1 - delta / rho) * len(kept)
                density_checks += 1

    universe = set(range(6))
    all_pairs = [frozenset(pair) for pair in combinations(sorted(universe), 2)]
    for relation_mask in range(1 << len(all_pairs)):
        if relation_mask > 4095:
            break
        allowed = {pair for j, pair in enumerate(all_pairs) if relation_mask >> j & 1}
        for old_mask, keep_mask, new_mask in product(range(1 << 6), repeat=3):
            old = {x for x in universe if old_mask >> x & 1}
            kept = {x for x in old if keep_mask >> x & 1}
            new = {x for x in universe - old if new_mask >> x & 1}
            assert pair_load(kept, allowed) <= pair_load(old, allowed)
            monotone_checks += 1
            cross, new_new = increment_terms(old, new, allowed)
            assert pair_load(old | new, allowed) - pair_load(old, allowed) == cross + new_new
            increment_checks += 1
            if monotone_checks > 180000:
                break
        if monotone_checks > 180000:
            break

    eta = 2
    paid_atoms = list(range(11))
    reuse = 3
    charges = []
    for atom in paid_atoms:
        charges.extend([atom] * reuse)
    max_crossings = len(charges) // (eta + 1)
    for crossing_count in range(max_crossings + 1):
        needed = crossing_count * (eta + 1)
        assert needed <= reuse * len(paid_atoms)
        crossing_checks += 1
    assert (max_crossings + 1) * (eta + 1) > reuse * len(paid_atoms)

    assert density_checks > 1000
    assert monotone_checks > 10000
    assert increment_checks == monotone_checks
    print("AC GC pool/pair-shadow import audit passed")
    print(f"  density checks: {density_checks}")
    print(f"  restriction checks: {monotone_checks}")
    print(f"  increment identities: {increment_checks}")
    print(f"  charged crossing checks: {crossing_checks}")


if __name__ == "__main__":
    main()

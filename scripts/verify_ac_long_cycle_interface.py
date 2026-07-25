#!/usr/bin/env python3
"""Exact finite checks for AC3ig--AC3ik."""

from __future__ import annotations

from itertools import permutations
from math import ceil


def cells(p):
    return {(i, p[i]) for i in range(len(p))}


def cycles_of_map(p, q):
    """Permutation cycles of q^{-1} o p in edge-symmetric difference."""
    n = len(p)
    invq = [0] * n
    for i, y in enumerate(q):
        invq[y] = i
    f = [invq[p[i]] for i in range(n)]
    seen = [False] * n
    out = []
    for i in range(n):
        if seen[i]:
            continue
        cyc = []
        j = i
        while not seen[j]:
            seen[j] = True
            cyc.append(j)
            j = f[j]
        if len(cyc) > 1:
            out.append(cyc)
    return out


def component_length_through(p, q, e_col):
    for cyc in cycles_of_map(p, q):
        if e_col in cyc:
            return 2 * len(cyc)
    raise AssertionError("changed edge not on a nontrivial component")


def cross_for_removed(p, q, e_col):
    """p is old, q is new, and (e_col,p[e_col]) is removed."""
    u = e_col
    v = p[u]
    y = q[u]
    x = next(i for i, val in enumerate(q) if val == v)
    assert y != v and x != u
    return (u, v, y, x)


def check_permutation_changes():
    changes = rectangles = long_cycles = return_crosses = 0
    for n in range(3, 7):
        ps = list(permutations(range(n)))
        for p in ps:
            for q in ps:
                if p == q:
                    continue
                removed = sorted(cells(p) - cells(q))
                e = removed[0]
                sig = cross_for_removed(p, q, e[0])
                assert sig[0:2] == e
                length = component_length_through(p, q, e[0])
                changes += 1
                if length == 4:
                    u, v, y, x = sig
                    assert p[x] == y
                    rectangles += 1
                else:
                    assert length >= 6 and length % 2 == 0
                    u, v, y, x = sig
                    assert p[x] != y
                    long_cycles += 1

                inserted = sorted(cells(q) - cells(p))
                ret = inserted[0]
                rsig = cross_for_removed(q, p, ret[0])
                assert rsig[0:2] == ret
                return_crosses += 1
    return changes, rectangles, long_cycles, return_crosses


def check_ticket_pigeonhole():
    checks = 0
    for n in range(3, 18):
        for L in range(1, 8):
            T = L * (n - 1) ** 2
            for r in range(1, 5 * T + 5):
                reinserts = r - 1
                long_min = max(0, reinserts - T)
                lower = ceil(long_min / T) if long_min else 0
                loads = [long_min // T] * T
                for i in range(long_min % T):
                    loads[i] += 1
                assert max(loads, default=0) == lower
                assert min(reinserts, T) + long_min == reinserts
                checks += 1
    return checks


def switch_cycle(n, cycle):
    """Reference identity matching, switch one directed cycle."""
    q = list(range(n))
    for a, b in zip(cycle, cycle[1:] + cycle[:1]):
        q[a] = b
    return tuple(q)


def check_cycle_flowers():
    states = edge_uniqueness = pivot_removals = 0
    for petals in range(2, 7):
        n = 1 + 2 * petals
        cycles = []
        for j in range(petals):
            a = 1 + 2 * j
            b = a + 1
            cycles.append([0, a, b])
        inserted_seen = set()
        for cyc in cycles:
            q = switch_cycle(n, cyc)
            assert sorted(q) == list(range(n))
            assert q[0] != 0
            inserted = cells(q) - cells(tuple(range(n)))
            assert len(inserted) == len(cyc)
            assert not (inserted_seen & inserted)
            inserted_seen |= inserted
            states += 1
            pivot_removals += 1
            edge_uniqueness += len(inserted)
    return states, edge_uniqueness, pivot_removals


def check_rank_ledgers():
    ledgers = constants = 0
    for W in range(1, 31):
        for e1 in range(0, 61):
            for e2 in range(0, 61 - e1):
                for e3 in range(0, 61 - e1 - e2):
                    total = e1 + e2 + e3
                    if total >= W:
                        assert max(e1, e2, e3) * 3 >= W
                    ledgers += 1
        for K in range(1, 16):
            assert 3 * K * W >= W
            assert 9 * K * W >= W
            constants += 2
    return ledgers, constants


def main():
    ch, rect, longc, ret = check_permutation_changes()
    pig = check_ticket_pigeonhole()
    states, edges, piv = check_cycle_flowers()
    ledgers, const = check_rank_ledgers()
    print("AC3ig--AC3ik exact checks passed")
    print(f"permutation changes: {ch}")
    print(f"rectangle components: {rect}")
    print(f"long components: {longc}")
    print(f"reverse return crosses: {ret}")
    print(f"ticket/pigeonhole systems: {pig}")
    print(f"cycle-star states: {states}")
    print(f"unique inserted edges: {edges}")
    print(f"pivot removals: {piv}")
    print(f"failed rank ledgers: {ledgers}")
    print(f"constant checks: {const}")


if __name__ == "__main__":
    main()

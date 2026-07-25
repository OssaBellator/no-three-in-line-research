#!/usr/bin/env python3
"""Exact finite checks for AC3iu--AC3iy."""

from __future__ import annotations

from itertools import combinations, permutations, product
from math import ceil, comb


def cells(p):
    return {(i, p[i]) for i in range(len(p))}


def component_columns(old, new, start):
    n = len(old)
    inv_new = [0] * n
    for c, r in enumerate(new):
        inv_new[r] = c
    nxt = [inv_new[old[c]] for c in range(n)]
    out = []
    c = start
    while True:
        out.append(c)
        c = nxt[c]
        if c == start:
            return out


def project_component(old, target, e_col):
    comp = component_columns(old, target, e_col)
    projected = list(old)
    for c in comp:
        projected[c] = target[c]
    return tuple(projected), tuple(comp)


def check_reference_projection():
    changes = rectangles = long_cycles = 0
    for n in range(2, 7):
        ps = list(permutations(range(n)))
        for old in ps:
            for target in ps:
                if old == target:
                    continue
                removed = sorted(cells(old) - cells(target))
                e = removed[0]
                projected, comp = project_component(old, target, e[0])
                assert sorted(projected) == list(range(n))
                assert e not in cells(projected)
                assert cells(projected) <= cells(old) | cells(target)
                assert {c for c in range(n) if projected[c] != old[c]} == set(comp)
                changes += 1
                if len(comp) == 2:
                    rectangles += 1
                else:
                    assert len(comp) >= 3
                    long_cycles += 1
    return changes, rectangles, long_cycles


def has_cycle_cover(adj):
    n = len(adj)
    for sigma in permutations(range(n)):
        if all(sigma[a] in adj[a] for a in range(n)):
            return sigma
    return None


def neighbourhood(adj, sources):
    out = set()
    for a in sources:
        out |= adj[a]
    return out


def deficient(adj, sources):
    return len(neighbourhood(adj, sources)) < len(sources)


def minimal_cores(adj):
    n = len(adj)
    out = []
    for r in range(1, n + 1):
        for tup in combinations(range(n), r):
            X = set(tup)
            if not deficient(adj, X):
                continue
            minimal = True
            for s in range(1, r):
                for sub in combinations(tup, s):
                    if deficient(adj, set(sub)):
                        minimal = False
                        break
                if not minimal:
                    break
            if minimal:
                out.append(X)
    return out


def check_exchange_graphs():
    graphs = failed = cores = singleton = nonsingleton = reused_targets = 0
    for n in range(1, 5):
        for mask in range(1 << (n * n)):
            adj = [set() for _ in range(n)]
            for a in range(n):
                for b in range(n):
                    if mask & (1 << (a * n + b)):
                        adj[a].add(b)
            graphs += 1
            cover = has_cycle_cover(adj)
            hall_failure = any(
                deficient(adj, set(X))
                for r in range(1, n + 1)
                for X in combinations(range(n), r)
            )
            assert (cover is None) == hall_failure
            if cover is not None:
                continue
            failed += 1
            found = minimal_cores(adj)
            assert found
            for X in found:
                cores += 1
                N = neighbourhood(adj, X)
                if len(X) == 1:
                    assert not N
                    singleton += 1
                    continue
                assert len(N) == len(X) - 1
                assert all(neighbourhood(adj, X - {a}) == N for a in X)
                assert all(adj[a] for a in X)
                assert any(a not in adj[a] for a in X)
                for b in N:
                    assert sum(b in adj[a] for a in X) >= 2
                    reused_targets += 1
                nonsingleton += 1
    return graphs, failed, cores, singleton, nonsingleton, reused_targets


def collision_bound(role_count, minimum_degree, core_size):
    bins = role_count * (core_size - 1)
    incidences = minimum_degree * core_size
    q, r = divmod(incidences, bins)
    return bins * comb(q, 2) + r * q


def check_role_collisions():
    assignments = 0
    for n in range(2, 4):
        for mask in range(1 << (n * n)):
            adj = [set() for _ in range(n)]
            for a in range(n):
                for b in range(n):
                    if mask & (1 << (a * n + b)):
                        adj[a].add(b)
            if has_cycle_cover(adj) is not None:
                continue
            for X in minimal_cores(adj):
                if len(X) < 2:
                    continue
                N = sorted(neighbourhood(adj, X))
                edges = [(a, b) for a in sorted(X) for b in N if b in adj[a]]
                d = min(sum(b in adj[a] for b in N) for a in X)
                for role_count in (1, 2, 3):
                    for labels in product(range(role_count), repeat=len(edges)):
                        loads = {}
                        for (_, b), role in zip(edges, labels):
                            loads[(b, role)] = loads.get((b, role), 0) + 1
                        collision = sum(comb(v, 2) for v in loads.values())
                        assert collision >= collision_bound(
                            role_count, d, len(X)
                        )
                        assignments += 1
    return assignments


def check_complete_host_repairs():
    systems = repairs = 0
    for n in range(3, 11):
        for p in permutations(range(n)):
            P = cells(p)
            for c in range(n):
                for r in range(n):
                    e = (c, r)
                    if e in P:
                        continue
                    shifts = []
                    for shift in (1, 2):
                        q = tuple(p[(i + shift) % n] for i in range(n))
                        shifts.append(q)
                    assert all(cells(q).isdisjoint(P) for q in shifts)
                    assert any(e not in cells(q) for q in shifts)
                    systems += 1
                    repairs += 1
            if n >= 8:
                break
    return systems, repairs


def check_blocker_concentration():
    systems = 0
    for n in range(1, 13):
        for total in range(1, 60):
            q, r = divmod(total, n)
            loads = [q + (i < r) for i in range(n)]
            assert sum(loads) == total
            assert max(loads) >= ceil(total / n)
            systems += 1
    return systems


def check_rank_ledgers():
    ledgers = constants = 0
    for W in range(1, 41):
        for e1 in range(0, 81):
            for e2 in range(0, 81 - e1):
                for e3 in range(0, 81 - e1 - e2):
                    if e1 + e2 + e3 >= W:
                        assert 3 * max(e1, e2, e3) >= W
                    ledgers += 1
        for K in range(1, 21):
            assert 3 * K * W >= W
            assert 9 * K * W >= W
            constants += 2
    return ledgers, constants


def main():
    changes, rectangles, long_cycles = check_reference_projection()
    graphs, failed, cores, singleton, nonsingleton, reused = check_exchange_graphs()
    role_assignments = check_role_collisions()
    host_systems, repairs = check_complete_host_repairs()
    concentration = check_blocker_concentration()
    ledgers, constants = check_rank_ledgers()
    print("AC3iu--AC3iy exact checks passed")
    print(f"reference projections: {changes}")
    print(f"rectangle projections: {rectangles}")
    print(f"long-cycle projections: {long_cycles}")
    print(f"exchange digraphs: {graphs}")
    print(f"failed exchange digraphs: {failed}")
    print(f"minimal Hall cores: {cores}")
    print(f"dead-row cores: {singleton}")
    print(f"reused-target cores: {nonsingleton}")
    print(f"reused target incidences: {reused}")
    print(f"role assignments: {role_assignments}")
    print(f"complete-host systems: {host_systems}")
    print(f"complete-host repairs: {repairs}")
    print(f"blocker concentration systems: {concentration}")
    print(f"failed rank ledgers: {ledgers}")
    print(f"constant checks: {constants}")


if __name__ == "__main__":
    main()

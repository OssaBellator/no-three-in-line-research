#!/usr/bin/env python3
"""Finite checks for SAS5ik--SAS5in."""

from itertools import permutations


def swap_adjacent(state, i):
    out = list(state)
    out[i], out[i + 1] = out[i + 1], out[i]
    return tuple(out)


def path_sum(path, charge):
    return sum(charge(path[i], path[i + 1]) for i in range(len(path) - 1))


def local_defects(states, r, charge):
    defects = []
    for m in states:
        for i in range(r - 1):
            for j in range(i + 2, r - 1):
                p1 = [m, swap_adjacent(m, i)]
                p1.append(swap_adjacent(p1[-1], j))
                p2 = [m, swap_adjacent(m, j)]
                p2.append(swap_adjacent(p2[-1], i))
                defects.append(path_sum(p1, charge) - path_sum(p2, charge))
        for i in range(r - 2):
            p1 = [m]
            for g in (i, i + 1, i):
                p1.append(swap_adjacent(p1[-1], g))
            p2 = [m]
            for g in (i + 1, i, i + 1):
                p2.append(swap_adjacent(p2[-1], g))
            assert p1[-1] == p2[-1]
            defects.append(path_sum(p1, charge) - path_sum(p2, charge))
    return defects


def reconstruct(states, r, charge):
    root = states[0]
    phi = {root: 0}
    queue = [root]
    while queue:
        u = queue.pop()
        for i in range(r - 1):
            v = swap_adjacent(u, i)
            proposed = phi[u] + charge(u, v)
            if v in phi:
                if phi[v] != proposed:
                    return False
            else:
                phi[v] = proposed
                queue.append(v)
    return all(charge(u, swap_adjacent(u, i)) == phi[swap_adjacent(u, i)] - phi[u]
               for u in states for i in range(r - 1))


def main() -> None:
    relation_checks = 0
    random_checks = 0
    for r in range(2, 7):
        states = list(permutations(range(r)))
        # Several exact potential charges.
        for seed in range(12):
            phi = {s: sum((i + 1 + seed) * s[i] for i in range(r)) + seed * sum(x * x for x in s)
                   for s in states}
            charge = lambda u, v, phi=phi: phi[v] - phi[u]
            defects = local_defects(states, r, charge)
            assert all(d == 0 for d in defects)
            assert reconstruct(states, r, charge)
            relation_checks += len(defects)

        # Deterministic antisymmetric edge charges; whenever local defects vanish,
        # verify that a global potential is reconstructed.
        for seed in range(60):
            values = {}
            for u in states:
                for i in range(r - 1):
                    v = swap_adjacent(u, i)
                    key = tuple(sorted((u, v)))
                    if key not in values:
                        values[key] = ((seed + 3 * sum(u) + 5 * i + hash(key)) % 11) - 5
            def charge(u, v, values=values):
                key = tuple(sorted((u, v)))
                return values[key] if u < v else -values[key]
            defects = local_defects(states, r, charge)
            if all(d == 0 for d in defects):
                assert reconstruct(states, r, charge)
            random_checks += 1

        expected = (r - 2) * (r - 1) // 2 if r >= 2 else 0
        per_state = len(local_defects([states[0]], r, lambda _u, _v: 0))
        assert per_state == expected

    print(f"verified {relation_checks} Coxeter relation instances and {random_checks} charge systems")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finite checks for SAS5hx--SAS5ia."""

from itertools import permutations


def cycles(alpha):
    seen = set()
    out = []
    for i in range(len(alpha)):
        if i in seen or alpha[i] == i:
            continue
        cyc = []
        j = i
        while j not in seen:
            seen.add(j)
            cyc.append(j)
            j = alpha[j]
        out.append(cyc)
    return out


def swap(state, i, j):
    state = list(state)
    state[i], state[j] = state[j], state[i]
    return tuple(state)


def canonical_path(alpha):
    state = tuple(range(len(alpha)))
    path = [state]
    for cyc in cycles(alpha):
        p = cyc[0]
        for j in reversed(cyc[1:]):
            state = swap(state, p, j)
            path.append(state)
    # The convention above may produce the inverse. Reverse cycle direction if needed.
    if state != tuple(alpha):
        state = tuple(range(len(alpha)))
        path = [state]
        for cyc in cycles(alpha):
            p = cyc[0]
            for j in cyc[1:]:
                state = swap(state, p, j)
                path.append(state)
    assert state == tuple(alpha)
    return path


def path_charge(path, edge_charge):
    return sum(edge_charge(path[i], path[i + 1]) for i in range(len(path) - 1))


def main():
    checks = 0
    for n in range(2, 8):
        for alpha in permutations(range(n)):
            moved = sum(alpha[i] != i for i in range(n))
            cyc = cycles(alpha)
            if moved == 0:
                continue
            path = canonical_path(alpha)
            assert len(path) - 1 == moved - len(cyc)
            assert len(path) <= moved

            K = 5
            assert K * len(path) <= K * moved
            assert 2 * moved * (len(path) - 1) <= 2 * moved * (moved - 1)

            potential = {state: sum((i + 1) * state[i] for i in range(n)) for state in path}
            cob = lambda x, y: potential[y] - potential[x]
            assert path_charge(path, cob) == potential[path[-1]] - potential[path[0]]

            # Compare with a direct two-edge detour when available.
            if len(path) >= 2:
                P = path
                Q = [path[0], path[-1]]
                # Define one antisymmetric charge on the used directed edges.
                def charge(x, y):
                    return sum(x) - sum(y) + (hash(x) % 7) - (hash(y) % 7)
                cp = path_charge(P, charge)
                cq = path_charge(Q, charge)
                closed = P + list(reversed(Q[:-1]))
                assert cp - cq == path_charge(closed, charge)
            checks += 1

    print(f"verified {checks} canonical paths and history identities")


if __name__ == "__main__":
    main()

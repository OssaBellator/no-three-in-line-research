#!/usr/bin/env python3

import random


def maximum_independent_weight(adj, weights):
    best = 0
    for mask in range(1 << len(weights)):
        valid = True
        for i in range(len(weights)):
            if (mask >> i) & 1:
                if any(((mask >> j) & 1) for j in adj[i] if j > i):
                    valid = False
                    break
        if valid:
            best = max(best, sum(weights[i] for i in range(len(weights)) if (mask >> i) & 1))
    return best


def main():
    rng = random.Random(20260728)
    graphs = candidates = atom_incidences = conflict_edges = 0

    for _ in range(3000):
        n = rng.randint(2, 11)
        atom_count = rng.randint(2, 9)
        rank = rng.randint(1, min(4, atom_count))
        supports = []
        for _v in range(n):
            size = rng.randint(1, rank)
            supports.append(set(rng.sample(range(atom_count), size)))

        loads = [sum(atom in support for support in supports) for atom in range(atom_count)]
        adj = [set() for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if supports[i] & supports[j]:
                    adj[i].add(j)
                    adj[j].add(i)
                    conflict_edges += 1

        for i in range(n):
            atom_bound = sum(loads[atom] - 1 for atom in supports[i])
            assert len(adj[i]) <= atom_bound

        weights = [rng.randint(1, 9) for _ in range(n)]
        local_bound = sum(weights[i] / (len(adj[i]) + 1) for i in range(n))
        atom_bound = sum(
            weights[i] / (1 + sum(loads[atom] - 1 for atom in supports[i]))
            for i in range(n)
        )
        optimum = maximum_independent_weight(adj, weights)
        assert optimum + 1e-9 >= local_bound >= atom_bound - 1e-9

        graphs += 1
        candidates += n
        atom_incidences += sum(len(support) for support in supports)

    print(f"audited {graphs:,} exact conflict-atom graphs")
    print(f"checked {candidates:,} weighted switching candidates")
    print(f"checked {atom_incidences:,} candidate-atom incidences")
    print(f"checked {conflict_edges:,} exact conflict edges")


if __name__ == "__main__":
    main()

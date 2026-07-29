from itertools import combinations
from random import Random

def brute_max_weight(n, weights, edges):
    best = 0
    edge_sets = [set(e) for e in edges]
    for mask in range(1 << n):
        chosen = {i for i in range(n) if mask >> i & 1}
        if all(len(chosen & e) <= 1 for e in edge_sets):
            best = max(best, sum(weights[i] for i in chosen))
    return best

def main() -> None:
    rng = Random(2026072815)
    systems = 3500
    candidates_total = 0
    atoms_total = 0
    hyperedges_total = 0
    higher_order = 0
    atom_hyperedge_incidence = 0
    shadow_edges_total = 0
    brute_checks = 0

    for _ in range(systems):
        n = rng.randint(1, 9)
        a_count = rng.randint(1, 6)
        weights = [rng.randint(1, 7) for _ in range(n)]
        support = [set(j for j in range(a_count) if rng.random() < 0.42) for _ in range(n)]
        for i in range(n):
            if not support[i]:
                support[i].add(rng.randrange(a_count))
        candidates_total += n
        atoms_total += a_count

        edges = []
        witnessed = []
        for a in range(a_count):
            verts = [i for i in range(n) if a in support[i]]
            for _ in range(rng.randint(0, 3)):
                if len(verts) < 2:
                    break
                k = rng.randint(2, min(4, len(verts)))
                e = tuple(sorted(rng.sample(verts, k)))
                if e not in edges:
                    edges.append(e)
                    witnessed.append((e, a))
                    hyperedges_total += 1
                    atom_hyperedge_incidence += len(e)
                    if len(e) > 2:
                        higher_order += 1

        shadow = set()
        degree = [0] * n
        load = [[0] * a_count for _ in range(n)]
        for e, a in witnessed:
            for v in e:
                load[v][a] += len(e) - 1
            for u, v in combinations(e, 2):
                shadow.add((u, v))
        shadow_edges_total += len(shadow)
        for u, v in shadow:
            degree[u] += 1
            degree[v] += 1

        for v in range(n):
            assert degree[v] <= sum(load[v][a] for a in support[v])

        max_load = max((load[v][a] for v in range(n) for a in support[v]), default=0)
        r = max(len(s) for s in support)
        total_w = sum(weights)
        optimum = brute_max_weight(n, weights, edges)
        brute_checks += 1
        assert optimum * (1 + r * max_load) >= total_w

    print("SRR witnessed hyperedge-atom audit")
    print(f"  systems: {systems}")
    print(f"  candidates: {candidates_total}")
    print(f"  exact atoms: {atoms_total}")
    print(f"  witnessed hyperedges: {hyperedges_total}")
    print(f"  higher-order hyperedges: {higher_order}")
    print(f"  candidate/atom/hyperedge incidences: {atom_hyperedge_incidence}")
    print(f"  clique-shadow edges: {shadow_edges_total}")
    print(f"  brute-force executable-weight checks: {brute_checks}")

if __name__ == "__main__":
    main()

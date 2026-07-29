#!/usr/bin/env python3
"""Exhaust small conditioned Hall graphs and shifted-quantile bounds."""

from itertools import combinations, product, permutations


def saturating_cost(adj, costs, active_b):
    a_count = len(adj)
    best = None
    for chosen in permutations(active_b, a_count):
        if all(chosen[a] in adj[a] for a in range(a_count)):
            value = sum(costs[b] for b in chosen)
            best = value if best is None else min(best, value)
    return best


def hall(adj, active_b):
    a_count = len(adj)
    active = set(active_b)
    for mask in range(1, 1 << a_count):
        xs = [a for a in range(a_count) if mask & (1 << a)]
        neigh = set().union(*(adj[a] & active for a in xs))
        if len(neigh) < len(xs):
            return False
    return True


def main():
    checked = 0
    for a_count in range(1, 4):
        for b_count in range(a_count, 6):
            all_edges = [(a, b) for a in range(a_count) for b in range(b_count)]
            for edge_bits in range(1 << len(all_edges)):
                adj = [set() for _ in range(a_count)]
                for idx, (a, b) in enumerate(all_edges):
                    if edge_bits & (1 << idx):
                        adj[a].add(b)
                if not hall(adj, range(b_count)):
                    continue
                delta = max(b_count - len(adj[a]) for a in range(a_count))
                for k in range(0, min(2, b_count - a_count) + 1):
                    for deleted in combinations(range(b_count), k):
                        active = [b for b in range(b_count) if b not in deleted]
                        if not hall(adj, active) or len(active) < a_count + delta:
                            continue
                        for costs in product(range(4), repeat=b_count):
                            opt = saturating_cost(adj, costs, active)
                            assert opt is not None
                            local = sorted(costs[b] for b in active)
                            local_bound = sum(local[i + delta] for i in range(a_count))
                            global_order = sorted(costs)
                            global_bound = sum(global_order[i + delta + k] for i in range(a_count))
                            assert opt <= local_bound
                            assert opt <= global_bound
                            checked += 1
    print(f"verified {checked} conditioned Hall-cost instances")


if __name__ == "__main__":
    main()

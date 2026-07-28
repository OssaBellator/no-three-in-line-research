from collections import deque
import random


def maxflow(n, edges, source, sink):
    adj = [[] for _ in range(n)]

    def add(u, v, cap):
        f = [v, cap, None]
        r = [u, 0, f]
        f[2] = r
        adj[u].append(f)
        adj[v].append(r)

    for u, v, cap in edges:
        add(u, v, cap)

    value = 0
    while True:
        parent = [None] * n
        pedge = [None] * n
        q = deque([source])
        parent[source] = source
        while q and parent[sink] is None:
            u = q.popleft()
            for edge in adj[u]:
                if edge[1] > 0 and parent[edge[0]] is None:
                    parent[edge[0]] = u
                    pedge[edge[0]] = edge
                    q.append(edge[0])
                    if edge[0] == sink:
                        break
        if parent[sink] is None:
            break
        aug = 10**9
        v = sink
        while v != source:
            aug = min(aug, pedge[v][1])
            v = parent[v]
        v = sink
        while v != source:
            edge = pedge[v]
            edge[1] -= aug
            edge[2][1] += aug
            v = parent[v]
        value += aug
    return value


def main():
    rng = random.Random(1502)
    systems = 6000
    totals = {
        "source_classes": 0,
        "restoration_classes": 0,
        "compatibility_arcs": 0,
        "potential_capacity": 0,
        "restoration_demand": 0,
        "paid": 0,
        "deficient_systems": 0,
        "unpaid": 0,
        "hall_subset_checks": 0,
    }
    inf = 10**6

    for _ in range(systems):
        ns = rng.randint(2, 6)
        nr = rng.randint(2, 6)
        capacity = [rng.randint(0, 8) for _ in range(ns)]
        demand = [rng.randint(0, 6) for _ in range(nr)]
        compatible = [[rng.random() < 0.5 for _ in range(ns)] for _ in range(nr)]
        for i in range(nr):
            if not any(compatible[i]):
                compatible[i][rng.randrange(ns)] = True

        n = 1 + nr + ns + 1
        source = 0
        ro = 1
        so = ro + nr
        sink = n - 1
        edges = [(source, ro + i, demand[i]) for i in range(nr)]
        edges += [(ro + i, so + j, inf) for i in range(nr) for j in range(ns) if compatible[i][j]]
        edges += [(so + j, sink, capacity[j]) for j in range(ns)]
        paid = maxflow(n, edges, source, sink)
        total = sum(demand)

        max_deficit = 0
        for mask in range(1 << nr):
            totals["hall_subset_checks"] += 1
            subset_demand = sum(demand[i] for i in range(nr) if (mask >> i) & 1)
            neighborhood = {
                j
                for i in range(nr)
                if (mask >> i) & 1
                for j in range(ns)
                if compatible[i][j]
            }
            subset_capacity = sum(capacity[j] for j in neighborhood)
            max_deficit = max(max_deficit, subset_demand - subset_capacity)
        assert total - paid == max_deficit

        totals["source_classes"] += ns
        totals["restoration_classes"] += nr
        totals["compatibility_arcs"] += sum(sum(row) for row in compatible)
        totals["potential_capacity"] += sum(capacity)
        totals["restoration_demand"] += total
        totals["paid"] += paid
        if paid < total:
            totals["deficient_systems"] += 1
            totals["unpaid"] += total - paid

    print(f"systems={systems}")
    for key, value in totals.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()

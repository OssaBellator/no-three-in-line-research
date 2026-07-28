from collections import deque
import random


def maxflow(n, edges, source, sink):
    adj = [[] for _ in range(n)]
    refs = []

    def add(u, v, cap):
        f = [v, cap, None, cap]
        r = [u, 0, f, 0]
        f[2] = r
        adj[u].append(f)
        adj[v].append(r)
        return f

    for u, v, cap in edges:
        refs.append(add(u, v, cap))

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
    return value, [edge[3] - edge[1] for edge in refs]


def main():
    rng = random.Random(1507)
    systems = 5200
    totals = {
        "epochs": 0,
        "pair_classes": 0,
        "task_classes": 0,
        "neutral_sources": 0,
        "compatibility_arcs": 0,
        "pair_demand": 0,
        "task_demand": 0,
        "neutral_deposits": 0,
        "paid": 0,
        "deficient_epochs": 0,
        "unpaid": 0,
        "hall_subset_checks": 0,
    }
    inf = 10**6

    for _ in range(systems):
        npair = rng.randint(1, 4)
        ntask = rng.randint(1, 4)
        ns = rng.randint(2, 5)
        balance = [rng.randint(1, 8) for _ in range(ns)]
        demand_count = npair + ntask
        compatible = [[rng.random() < 0.55 for _ in range(ns)] for _ in range(demand_count)]
        for i in range(demand_count):
            if not any(compatible[i]):
                compatible[i][rng.randrange(ns)] = True

        totals["pair_classes"] += npair
        totals["task_classes"] += ntask
        totals["neutral_sources"] += ns
        totals["compatibility_arcs"] += sum(sum(row) for row in compatible)

        for _epoch in range(rng.randint(1, 4)):
            totals["epochs"] += 1
            deposit = [rng.randint(0, 3) for _ in range(ns)]
            balance = [x + d for x, d in zip(balance, deposit)]
            totals["neutral_deposits"] += sum(deposit)

            pair = [rng.randint(0, 4) for _ in range(npair)]
            task = [rng.randint(0, 4) for _ in range(ntask)]
            demand = pair + task
            totals["pair_demand"] += sum(pair)
            totals["task_demand"] += sum(task)

            n = 1 + demand_count + ns + 1
            source = 0
            do = 1
            so = do + demand_count
            sink = n - 1
            edges = [(source, do + i, demand[i]) for i in range(demand_count)]
            edges += [
                (do + i, so + j, inf)
                for i in range(demand_count)
                for j in range(ns)
                if compatible[i][j]
            ]
            source_positions = []
            for j, cap in enumerate(balance):
                source_positions.append(len(edges))
                edges.append((so + j, sink, cap))

            paid, used = maxflow(n, edges, source, sink)
            total = sum(demand)
            totals["paid"] += paid

            max_deficit = 0
            for mask in range(1 << demand_count):
                totals["hall_subset_checks"] += 1
                subset_demand = sum(demand[i] for i in range(demand_count) if (mask >> i) & 1)
                neighborhood = {
                    j
                    for i in range(demand_count)
                    if (mask >> i) & 1
                    for j in range(ns)
                    if compatible[i][j]
                }
                subset_capacity = sum(balance[j] for j in neighborhood)
                max_deficit = max(max_deficit, subset_demand - subset_capacity)
            assert total - paid == max_deficit

            if paid < total:
                totals["deficient_epochs"] += 1
                totals["unpaid"] += total - paid
                break
            for j, pos in enumerate(source_positions):
                balance[j] -= used[pos]
            assert min(balance) >= 0

    print(f"systems={systems}")
    for key, value in totals.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()

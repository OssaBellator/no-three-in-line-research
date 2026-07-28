from collections import deque
import random


class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]

    def add(self, u, v, c):
        f = [v, c, None]
        r = [u, 0, f]
        f[2] = r
        self.g[u].append(f)
        self.g[v].append(r)
        return f

    def flow(self, s, t):
        total = 0
        while True:
            level = [-1] * len(self.g)
            level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for v, c, _ in self.g[u]:
                    if c and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            if level[t] < 0:
                return total
            it = [0] * len(self.g)

            def dfs(u, amount):
                if u == t:
                    return amount
                while it[u] < len(self.g[u]):
                    edge = self.g[u][it[u]]
                    v, cap, rev = edge
                    if cap and level[v] == level[u] + 1:
                        sent = dfs(v, min(amount, cap))
                        if sent:
                            edge[1] -= sent
                            rev[1] += sent
                            return sent
                    it[u] += 1
                return 0

            while True:
                sent = dfs(s, 10**9)
                if not sent:
                    break
                total += sent


def solve(capacity, demand, adjacency):
    ns, nr = len(capacity), len(demand)
    source = 0
    source_offset = 1
    restoration_offset = source_offset + ns
    sink = restoration_offset + nr
    graph = Dinic(sink + 1)
    source_edges = [graph.add(source, source_offset + i, cap) for i, cap in enumerate(capacity)]
    for i in range(ns):
        for j in range(nr):
            if adjacency[i][j]:
                graph.add(source_offset + i, restoration_offset + j, 10**6)
    for j, amount in enumerate(demand):
        graph.add(restoration_offset + j, sink, amount)
    paid = graph.flow(source, sink)
    used = [capacity[i] - source_edges[i][1] for i in range(ns)]
    return paid, used


rng = random.Random(1602)
stats = dict(systems=0, epochs=0, sources=0, restorations=0, arcs=0,
             initial=0, deposits=0, demand=0, paid=0,
             deficient_epochs=0, unpaid=0, hall_checks=0)

for _ in range(6000):
    ns, nr = rng.randint(2, 6), rng.randint(2, 6)
    capacity = [rng.randint(0, 8) for _ in range(ns)]
    adjacency = [[rng.random() < 0.48 for _ in range(nr)] for _ in range(ns)]
    stats["systems"] += 1
    stats["sources"] += ns
    stats["restorations"] += nr
    stats["arcs"] += sum(map(sum, adjacency))
    stats["initial"] += sum(capacity)
    for _ in range(rng.randint(1, 4)):
        deposit = [rng.randint(0, 3) for _ in range(ns)]
        capacity = [x + y for x, y in zip(capacity, deposit)]
        demand = [rng.randint(0, 5) for _ in range(nr)]
        stats["epochs"] += 1
        stats["deposits"] += sum(deposit)
        stats["demand"] += sum(demand)
        stats["hall_checks"] += (1 << nr) - 1
        paid, used = solve(capacity, demand, adjacency)
        stats["paid"] += paid
        if paid < sum(demand):
            stats["deficient_epochs"] += 1
            stats["unpaid"] += sum(demand) - paid
            break
        capacity = [x - y for x, y in zip(capacity, used)]
        assert min(capacity) >= 0

assert stats["paid"] + stats["unpaid"] <= stats["demand"]
print("BDA cumulative restoration-potential transport")
for key, value in stats.items():
    print(f"{key}: {value}")

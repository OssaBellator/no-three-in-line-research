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


def solve(source_capacity, collateral_capacity, demand, physical_collateral, collateral_demand):
    ns, nc, nd = len(source_capacity), len(collateral_capacity), len(demand)
    source = 0
    source_offset = 1
    collateral_in = source_offset + ns
    collateral_out = collateral_in + nc
    demand_offset = collateral_out + nc
    sink = demand_offset + nd
    graph = Dinic(sink + 1)
    for i, cap in enumerate(source_capacity):
        graph.add(source, source_offset + i, cap)
    for i in range(ns):
        for j in range(nc):
            if physical_collateral[i][j]:
                graph.add(source_offset + i, collateral_in + j, 10**6)
    for j, cap in enumerate(collateral_capacity):
        graph.add(collateral_in + j, collateral_out + j, cap)
    for j in range(nc):
        for k in range(nd):
            if collateral_demand[j][k]:
                graph.add(collateral_out + j, demand_offset + k, 10**6)
    for k, amount in enumerate(demand):
        graph.add(demand_offset + k, sink, amount)
    return graph.flow(source, sink)


def sequential(source_capacity, collateral_capacity, demand, physical_collateral, collateral_demand):
    source_capacity = source_capacity[:]
    issued = [0] * len(collateral_capacity)
    for collateral, cap in enumerate(collateral_capacity):
        for _ in range(cap):
            source = next(
                (i for i, amount in enumerate(source_capacity)
                 if amount and physical_collateral[i][collateral]),
                None,
            )
            if source is None:
                break
            source_capacity[source] -= 1
            issued[collateral] += 1
    paid = 0
    for demand_class, amount in enumerate(demand):
        for _ in range(amount):
            collateral = next(
                (j for j, value in enumerate(issued)
                 if value and collateral_demand[j][demand_class]),
                None,
            )
            if collateral is None:
                return paid
            issued[collateral] -= 1
            paid += 1
    return paid


rng = random.Random(1603)
stats = dict(systems=0, physical_sources=0, collateral_classes=0,
             demand_classes=0, physical_collateral_arcs=0,
             collateral_demand_arcs=0, source_capacity=0,
             collateral_capacity=0, demand=0, paid=0,
             deficient_systems=0, unpaid=0, sequential_witnesses=0)

for _ in range(5500):
    ns, nc, nd = rng.randint(2, 5), rng.randint(2, 5), rng.randint(2, 5)
    source_capacity = [rng.randint(0, 7) for _ in range(ns)]
    collateral_capacity = [rng.randint(0, 6) for _ in range(nc)]
    demand = [rng.randint(0, 5) for _ in range(nd)]
    physical_collateral = [[rng.random() < 0.52 for _ in range(nc)] for _ in range(ns)]
    collateral_demand = [[rng.random() < 0.48 for _ in range(nd)] for _ in range(nc)]
    paid = solve(source_capacity, collateral_capacity, demand,
                 physical_collateral, collateral_demand)
    sequential_paid = sequential(source_capacity, collateral_capacity, demand,
                                 physical_collateral, collateral_demand)
    stats["systems"] += 1
    stats["physical_sources"] += ns
    stats["collateral_classes"] += nc
    stats["demand_classes"] += nd
    stats["physical_collateral_arcs"] += sum(map(sum, physical_collateral))
    stats["collateral_demand_arcs"] += sum(map(sum, collateral_demand))
    stats["source_capacity"] += sum(source_capacity)
    stats["collateral_capacity"] += sum(collateral_capacity)
    stats["demand"] += sum(demand)
    stats["paid"] += paid
    if paid < sum(demand):
        stats["deficient_systems"] += 1
        stats["unpaid"] += sum(demand) - paid
    if paid == sum(demand) and sequential_paid < paid:
        stats["sequential_witnesses"] += 1

assert stats["paid"] + stats["unpaid"] == stats["demand"]
print("RI integrated physical-source collateral flow")
for key, value in stats.items():
    print(f"{key}: {value}")

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


def solve(demand, capacity, adjacency):
    nd, ns = len(demand), len(capacity)
    source = 0
    demand_offset = 1
    source_offset = demand_offset + nd
    sink = source_offset + ns
    graph = Dinic(sink + 1)
    for i, amount in enumerate(demand):
        graph.add(source, demand_offset + i, amount)
    for i in range(nd):
        for j in range(ns):
            if adjacency[i][j]:
                graph.add(demand_offset + i, source_offset + j, 10**6)
    for j, cap in enumerate(capacity):
        graph.add(source_offset + j, sink, cap)
    return graph.flow(source, sink)


rng = random.Random(1605)
stats = dict(systems=0, residual_classes=0, edit_classes=0,
             source_classes=0, arcs=0, residual_demand=0,
             edit_demand=0, source_capacity=0, paid=0,
             deficient_systems=0, unpaid=0,
             double_spend_witnesses=0, hall_checks=0)

for _ in range(6000):
    nr, ne, ns = rng.randint(2, 5), rng.randint(2, 5), rng.randint(2, 5)
    residual_demand = [rng.randint(0, 5) for _ in range(nr)]
    edit_demand = [rng.randint(0, 5) for _ in range(ne)]
    capacity = [rng.randint(0, 7) for _ in range(ns)]
    residual_adjacency = [[rng.random() < 0.52 for _ in range(ns)] for _ in range(nr)]
    edit_adjacency = [[rng.random() < 0.52 for _ in range(ns)] for _ in range(ne)]
    joint_paid = solve(residual_demand + edit_demand, capacity,
                       residual_adjacency + edit_adjacency)
    residual_paid = solve(residual_demand, capacity, residual_adjacency)
    edit_paid = solve(edit_demand, capacity, edit_adjacency)
    total_demand = sum(residual_demand) + sum(edit_demand)
    stats["systems"] += 1
    stats["residual_classes"] += nr
    stats["edit_classes"] += ne
    stats["source_classes"] += ns
    stats["arcs"] += sum(map(sum, residual_adjacency)) + sum(map(sum, edit_adjacency))
    stats["residual_demand"] += sum(residual_demand)
    stats["edit_demand"] += sum(edit_demand)
    stats["source_capacity"] += sum(capacity)
    stats["paid"] += joint_paid
    stats["hall_checks"] += (1 << (nr + ne)) - 1
    if joint_paid < total_demand:
        stats["deficient_systems"] += 1
        stats["unpaid"] += total_demand - joint_paid
    if (residual_paid == sum(residual_demand)
            and edit_paid == sum(edit_demand)
            and joint_paid < total_demand):
        stats["double_spend_witnesses"] += 1

assert stats["paid"] + stats["unpaid"] == stats["residual_demand"] + stats["edit_demand"]
print("OP joint residual/edit transport")
for key, value in stats.items():
    print(f"{key}: {value}")

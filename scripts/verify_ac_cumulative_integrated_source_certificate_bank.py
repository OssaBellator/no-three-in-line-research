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


def solve(source_balance, certificate_balance, demand, source_certificate, certificate_defect):
    ns, nc, nd = len(source_balance), len(certificate_balance), len(demand)
    source = 0
    source_offset = 1
    cert_in = source_offset + ns
    cert_out = cert_in + nc
    defect_offset = cert_out + nc
    sink = defect_offset + nd
    graph = Dinic(sink + 1)
    source_edges = [graph.add(source, source_offset + i, cap) for i, cap in enumerate(source_balance)]
    certificate_edges = [graph.add(cert_in + j, cert_out + j, cap) for j, cap in enumerate(certificate_balance)]
    for i in range(ns):
        for j in range(nc):
            if source_certificate[i][j]:
                graph.add(source_offset + i, cert_in + j, 10**6)
    for j in range(nc):
        for k in range(nd):
            if certificate_defect[j][k]:
                graph.add(cert_out + j, defect_offset + k, 10**6)
    for k, amount in enumerate(demand):
        graph.add(defect_offset + k, sink, amount)
    paid = graph.flow(source, sink)
    used_source = [source_balance[i] - source_edges[i][1] for i in range(ns)]
    used_certificate = [certificate_balance[j] - certificate_edges[j][1] for j in range(nc)]
    return paid, used_source, used_certificate


def greedy(source_balance, certificate_balance, demand, source_certificate, certificate_defect):
    source_balance = source_balance[:]
    certificate_balance = certificate_balance[:]
    paid = 0
    for defect, amount in enumerate(demand):
        for _ in range(amount):
            chosen = None
            for certificate in range(len(certificate_balance)):
                if not certificate_balance[certificate] or not certificate_defect[certificate][defect]:
                    continue
                for source in range(len(source_balance)):
                    if source_balance[source] and source_certificate[source][certificate]:
                        chosen = source, certificate
                        break
                if chosen:
                    break
            if chosen is None:
                return paid
            source, certificate = chosen
            source_balance[source] -= 1
            certificate_balance[certificate] -= 1
            paid += 1
    return paid


rng = random.Random(1601)
stats = dict(systems=0, epochs=0, sources=0, certificates=0, defects=0,
             source_certificate_arcs=0, certificate_defect_arcs=0,
             source_deposits=0, certificate_deposits=0, demand=0, paid=0,
             deficient_epochs=0, unpaid=0, greedy_witnesses=0)

for _ in range(5000):
    ns, nc, nd = rng.randint(2, 5), rng.randint(2, 5), rng.randint(2, 5)
    source_balance = [rng.randint(0, 5) for _ in range(ns)]
    certificate_balance = [rng.randint(0, 5) for _ in range(nc)]
    source_certificate = [[rng.random() < 0.5 for _ in range(nc)] for _ in range(ns)]
    certificate_defect = [[rng.random() < 0.5 for _ in range(nd)] for _ in range(nc)]
    stats["systems"] += 1
    stats["sources"] += ns
    stats["certificates"] += nc
    stats["defects"] += nd
    stats["source_certificate_arcs"] += sum(map(sum, source_certificate))
    stats["certificate_defect_arcs"] += sum(map(sum, certificate_defect))
    for _ in range(rng.randint(1, 3)):
        source_deposit = [rng.randint(0, 2) for _ in range(ns)]
        certificate_deposit = [rng.randint(0, 2) for _ in range(nc)]
        source_balance = [x + y for x, y in zip(source_balance, source_deposit)]
        certificate_balance = [x + y for x, y in zip(certificate_balance, certificate_deposit)]
        demand = [rng.randint(0, 4) for _ in range(nd)]
        stats["epochs"] += 1
        stats["source_deposits"] += sum(source_deposit)
        stats["certificate_deposits"] += sum(certificate_deposit)
        stats["demand"] += sum(demand)
        paid, used_source, used_certificate = solve(
            source_balance, certificate_balance, demand, source_certificate, certificate_defect
        )
        greedy_paid = greedy(
            source_balance, certificate_balance, demand, source_certificate, certificate_defect
        )
        if paid == sum(demand) and greedy_paid < paid:
            stats["greedy_witnesses"] += 1
        stats["paid"] += paid
        if paid < sum(demand):
            stats["deficient_epochs"] += 1
            stats["unpaid"] += sum(demand) - paid
            break
        source_balance = [x - y for x, y in zip(source_balance, used_source)]
        certificate_balance = [x - y for x, y in zip(certificate_balance, used_certificate)]
        assert min(source_balance + certificate_balance) >= 0

assert stats["paid"] + stats["unpaid"] <= stats["demand"]
print("AC cumulative integrated source/certificate bank")
for key, value in stats.items():
    print(f"{key}: {value}")

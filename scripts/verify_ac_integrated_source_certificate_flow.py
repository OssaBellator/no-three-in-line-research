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

    reachable = [False] * n
    q = deque([source])
    reachable[source] = True
    while q:
        u = q.popleft()
        for edge in adj[u]:
            if edge[1] > 0 and not reachable[edge[0]]:
                reachable[edge[0]] = True
                q.append(edge[0])
    return value, reachable


def main():
    rng = random.Random(1501)
    systems = 5000
    totals = {
        "sources": 0,
        "certificates": 0,
        "defects": 0,
        "source_certificate_arcs": 0,
        "certificate_defect_arcs": 0,
        "demand": 0,
        "paid": 0,
        "deficient_systems": 0,
        "unpaid": 0,
        "sequential_issue_witnesses": 0,
    }
    inf = 10**6

    for _ in range(systems):
        ns = rng.randint(2, 5)
        nc = rng.randint(2, 5)
        nd = rng.randint(2, 5)
        source_capacity = [rng.randint(1, 6) for _ in range(ns)]
        certificate_capacity = [rng.randint(1, 6) for _ in range(nc)]
        demand = [rng.randint(0, 5) for _ in range(nd)]
        sc = [[rng.random() < 0.55 for _ in range(nc)] for _ in range(ns)]
        cd = [[rng.random() < 0.55 for _ in range(nd)] for _ in range(nc)]
        for i in range(ns):
            if not any(sc[i]):
                sc[i][rng.randrange(nc)] = True
        for j in range(nc):
            if not any(cd[j]):
                cd[j][rng.randrange(nd)] = True

        n = 1 + ns + 2 * nc + nd + 1
        source = 0
        sink = n - 1
        so = 1
        ci = so + ns
        co = ci + nc
        do = co + nc
        edges = [(source, so + i, cap) for i, cap in enumerate(source_capacity)]
        edges += [(so + i, ci + j, inf) for i in range(ns) for j in range(nc) if sc[i][j]]
        edges += [(ci + j, co + j, cap) for j, cap in enumerate(certificate_capacity)]
        edges += [(co + j, do + k, inf) for j in range(nc) for k in range(nd) if cd[j][k]]
        edges += [(do + k, sink, amount) for k, amount in enumerate(demand)]

        paid, _ = maxflow(n, edges, source, sink)
        total = sum(demand)
        totals["sources"] += ns
        totals["certificates"] += nc
        totals["defects"] += nd
        totals["source_certificate_arcs"] += sum(sum(row) for row in sc)
        totals["certificate_defect_arcs"] += sum(sum(row) for row in cd)
        totals["demand"] += total
        totals["paid"] += paid
        if paid < total:
            totals["deficient_systems"] += 1
            totals["unpaid"] += total - paid

        remaining_source = source_capacity[:]
        certificate_balance = [0] * nc
        for j in range(nc):
            need = certificate_capacity[j]
            for i in range(ns):
                if sc[i][j] and need:
                    take = min(need, remaining_source[i])
                    remaining_source[i] -= take
                    certificate_balance[j] += take
                    need -= take
        sequential_paid = 0
        remaining_demand = demand[:]
        for k in range(nd):
            for j in range(nc):
                if cd[j][k] and remaining_demand[k]:
                    take = min(remaining_demand[k], certificate_balance[j])
                    remaining_demand[k] -= take
                    certificate_balance[j] -= take
                    sequential_paid += take
        if paid == total and sequential_paid < total:
            totals["sequential_issue_witnesses"] += 1

    print(f"systems={systems}")
    for key, value in totals.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()

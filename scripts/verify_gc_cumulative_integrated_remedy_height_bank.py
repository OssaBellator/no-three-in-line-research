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
    rng = random.Random(1504)
    systems = 5000
    totals = {
        "epochs": 0,
        "causes": 0,
        "remedies": 0,
        "height_sources": 0,
        "cause_remedy_arcs": 0,
        "remedy_height_arcs": 0,
        "cause_demand": 0,
        "paid": 0,
        "remedy_deposits": 0,
        "height_deposits": 0,
        "deficient_epochs": 0,
        "unpaid": 0,
    }
    inf = 10**6

    for _ in range(systems):
        nc = rng.randint(2, 5)
        nr = rng.randint(2, 5)
        nh = rng.randint(2, 5)
        remedy_balance = [rng.randint(1, 7) for _ in range(nr)]
        height_balance = [rng.randint(1, 7) for _ in range(nh)]
        cr = [[rng.random() < 0.55 for _ in range(nr)] for _ in range(nc)]
        rh = [[rng.random() < 0.55 for _ in range(nh)] for _ in range(nr)]
        for i in range(nc):
            if not any(cr[i]):
                cr[i][rng.randrange(nr)] = True
        for j in range(nr):
            if not any(rh[j]):
                rh[j][rng.randrange(nh)] = True

        totals["causes"] += nc
        totals["remedies"] += nr
        totals["height_sources"] += nh
        totals["cause_remedy_arcs"] += sum(sum(row) for row in cr)
        totals["remedy_height_arcs"] += sum(sum(row) for row in rh)

        for _epoch in range(rng.randint(1, 4)):
            totals["epochs"] += 1
            remedy_deposit = [rng.randint(0, 3) for _ in range(nr)]
            height_deposit = [rng.randint(0, 3) for _ in range(nh)]
            remedy_balance = [x + d for x, d in zip(remedy_balance, remedy_deposit)]
            height_balance = [x + d for x, d in zip(height_balance, height_deposit)]
            totals["remedy_deposits"] += sum(remedy_deposit)
            totals["height_deposits"] += sum(height_deposit)

            demand = [rng.randint(0, 4) for _ in range(nc)]
            total = sum(demand)
            totals["cause_demand"] += total
            n = 1 + nc + 2 * nr + nh + 1
            source = 0
            co = 1
            ri = co + nc
            ro = ri + nr
            ho = ro + nr
            sink = n - 1
            edges = [(source, co + i, demand[i]) for i in range(nc)]
            edges += [(co + i, ri + j, inf) for i in range(nc) for j in range(nr) if cr[i][j]]
            remedy_positions = []
            for j, cap in enumerate(remedy_balance):
                remedy_positions.append(len(edges))
                edges.append((ri + j, ro + j, cap))
            edges += [(ro + j, ho + k, inf) for j in range(nr) for k in range(nh) if rh[j][k]]
            height_positions = []
            for k, cap in enumerate(height_balance):
                height_positions.append(len(edges))
                edges.append((ho + k, sink, cap))

            paid, used = maxflow(n, edges, source, sink)
            totals["paid"] += paid
            if paid < total:
                totals["deficient_epochs"] += 1
                totals["unpaid"] += total - paid
                break
            for j, pos in enumerate(remedy_positions):
                remedy_balance[j] -= used[pos]
            for k, pos in enumerate(height_positions):
                height_balance[k] -= used[pos]
            assert min(remedy_balance + height_balance) >= 0

    print(f"systems={systems}")
    for key, value in totals.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()

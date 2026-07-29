from collections import deque
import random

class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]
    def add(self, u, v, c):
        a = [v, c, None]
        b = [u, 0, a]
        a[2] = b
        self.g[u].append(a)
        self.g[v].append(b)
        return a
    def flow(self, s, t):
        total = 0
        while True:
            level = [-1] * len(self.g)
            q = deque([s]); level[s] = 0
            while q:
                u = q.popleft()
                for e in self.g[u]:
                    if e[1] and level[e[0]] < 0:
                        level[e[0]] = level[u] + 1; q.append(e[0])
            if level[t] < 0:
                return total
            it = [0] * len(self.g)
            def dfs(u, f):
                if u == t:
                    return f
                for i in range(it[u], len(self.g[u])):
                    it[u] = i
                    e = self.g[u][i]
                    if e[1] and level[e[0]] == level[u] + 1:
                        z = dfs(e[0], min(f, e[1]))
                        if z:
                            e[1] -= z; e[2][1] += z
                            return z
                return 0
            while True:
                z = dfs(s, 10**9)
                if not z:
                    break
                total += z

def rand_nonempty_edges(rng, left, right, p=0.55):
    edges = []
    for u in range(left):
        row = [v for v in range(right) if rng.random() < p]
        if not row:
            row = [rng.randrange(right)]
        edges.extend((u, v) for v in row)
    return edges

rng = random.Random(1702)
systems = 6000
stats = dict(P=0, S=0, R=0, ps=0, sr=0, physical=0, demand=0, paid=0, unpaid=0, deficient=0, preissue=0, checks=0)

def solve(pm, sb, dem, PS, SR):
    P, S, R = len(pm), len(sb), len(dem)
    src = 0; off_p = 1; off_old = off_p + P; off_s = off_old + S; off_r = off_s + S; sink = off_r + R
    flow = Dinic(sink + 1)
    for p, x in enumerate(pm): flow.add(src, off_p + p, x)
    for s, x in enumerate(sb):
        flow.add(src, off_old + s, x); flow.add(off_old + s, off_s + s, x)
    for p, s in PS: flow.add(off_p + p, off_s + s, 10**6)
    for s, r in SR: flow.add(off_s + s, off_r + r, 10**6)
    for r, x in enumerate(dem): flow.add(off_r + r, sink, x)
    return flow.flow(src, sink)

def greedy(pm, sb, dem, PS, SR):
    issued = [0] * len(sb)
    need = [sum(dem[r] for ss, r in SR if ss == s) for s in range(len(sb))]
    for p, mass in enumerate(pm):
        options = [s for pp, s in PS if pp == p]
        if options:
            issued[max(options, key=lambda s: (need[s], -s))] += mass
    return solve([0] * len(pm), [sb[s] + issued[s] for s in range(len(sb))], dem, [], SR)

for _ in range(systems):
    P, S, R = (rng.randint(2, 5) for _ in range(3))
    pm = [rng.randint(0, 7) for _ in range(P)]
    sb = [rng.randint(0, 5) for _ in range(S)]
    dem = [rng.randint(0, 6) for _ in range(R)]
    PS = rand_nonempty_edges(rng, P, S, 0.5)
    SR = rand_nonempty_edges(rng, S, R, 0.5)
    paid = solve(pm, sb, dem, PS, SR)
    greedy_paid = greedy(pm, sb, dem, PS, SR)
    total = sum(dem)
    if paid == total and greedy_paid < total: stats['preissue'] += 1
    if paid < total: stats['deficient'] += 1
    stats['P'] += P; stats['S'] += S; stats['R'] += R
    stats['ps'] += len(PS); stats['sr'] += len(SR); stats['physical'] += sum(pm)
    stats['demand'] += total; stats['paid'] += paid; stats['unpaid'] += total - paid
    for mask in range(1, 1 << R):
        subset = [r for r in range(R) if mask >> r & 1]
        neighbors = {s for s, r in SR if r in subset}
        cap = sum(sb[s] for s in neighbors) + sum(pm[p] for p in range(P) if any((p, s) in PS for s in neighbors))
        assert sum(dem[r] for r in subset) - cap <= total - paid
        stats['checks'] += 1

assert stats['paid'] + stats['unpaid'] == stats['demand']
print('BDA17', systems, stats)

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
        n = len(self.g)
        while True:
            level = [-1] * n
            q = deque([s])
            level[s] = 0
            while q:
                u = q.popleft()
                for e in self.g[u]:
                    if e[1] and level[e[0]] < 0:
                        level[e[0]] = level[u] + 1
                        q.append(e[0])
            if level[t] < 0:
                return total
            it = [0] * n
            def dfs(u, f):
                if u == t:
                    return f
                for i in range(it[u], len(self.g[u])):
                    it[u] = i
                    e = self.g[u][i]
                    if e[1] and level[e[0]] == level[u] + 1:
                        z = dfs(e[0], min(f, e[1]))
                        if z:
                            e[1] -= z
                            e[2][1] += z
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

rng = random.Random(1701)
systems = 5000
stats = dict(P=0, S=0, C=0, D=0, ps=0, sc=0, cd=0, demand=0, paid=0, unpaid=0, deficient=0, preissue=0)

def solve(pm, sb, cc, dem, PS, SC, CD):
    P, S, C, D = len(pm), len(sb), len(cc), len(dem)
    src = 0
    off_p = 1
    off_old = off_p + P
    off_s = off_old + S
    off_ci = off_s + S
    off_co = off_ci + C
    off_d = off_co + C
    sink = off_d + D
    flow = Dinic(sink + 1)
    for p, x in enumerate(pm):
        flow.add(src, off_p + p, x)
    for s, x in enumerate(sb):
        flow.add(src, off_old + s, x)
        flow.add(off_old + s, off_s + s, x)
    for p, s in PS:
        flow.add(off_p + p, off_s + s, 10**6)
    for s, c in SC:
        flow.add(off_s + s, off_ci + c, 10**6)
    for c, x in enumerate(cc):
        flow.add(off_ci + c, off_co + c, x)
    for c, d in CD:
        flow.add(off_co + c, off_d + d, 10**6)
    for d, x in enumerate(dem):
        flow.add(off_d + d, sink, x)
    return flow.flow(src, sink)

def greedy_preissue(pm, sb, cc, dem, PS, SC, CD):
    issued = [0] * len(sb)
    downstream = [0] * len(sb)
    for s in range(len(sb)):
        reach = {d for ss, c in SC if ss == s for cc2, d in CD if cc2 == c}
        downstream[s] = sum(dem[d] for d in reach)
    for p, mass in enumerate(pm):
        options = [s for pp, s in PS if pp == p]
        if options:
            issued[max(options, key=lambda s: (downstream[s], -s))] += mass
    return solve([0] * len(pm), [sb[s] + issued[s] for s in range(len(sb))], cc, dem, [], SC, CD)

for _ in range(systems):
    P, S, C, D = (rng.randint(2, 5) for _ in range(4))
    pm = [rng.randint(0, 5) for _ in range(P)]
    sb = [rng.randint(0, 4) for _ in range(S)]
    cc = [rng.randint(1, 6) for _ in range(C)]
    dem = [rng.randint(0, 5) for _ in range(D)]
    PS = rand_nonempty_edges(rng, P, S, 0.5)
    SC = rand_nonempty_edges(rng, S, C, 0.5)
    CD = rand_nonempty_edges(rng, C, D, 0.5)
    paid = solve(pm, sb, cc, dem, PS, SC, CD)
    total = sum(dem)
    greedy = greedy_preissue(pm, sb, cc, dem, PS, SC, CD)
    assert paid <= total
    if paid == total and greedy < total:
        stats['preissue'] += 1
    if paid < total:
        stats['deficient'] += 1
    stats['P'] += P; stats['S'] += S; stats['C'] += C; stats['D'] += D
    stats['ps'] += len(PS); stats['sc'] += len(SC); stats['cd'] += len(CD)
    stats['demand'] += total; stats['paid'] += paid; stats['unpaid'] += total - paid

assert stats['paid'] + stats['unpaid'] == stats['demand']
print('AC17', systems, stats)

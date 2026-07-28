from collections import deque
import random

class Dinic:
    def __init__(self, n): self.g = [[] for _ in range(n)]
    def add(self, u, v, c):
        a = [v, c, None]; b = [u, 0, a]; a[2] = b
        self.g[u].append(a); self.g[v].append(b); return a
    def flow(self, s, t):
        ans = 0
        while True:
            level = [-1] * len(self.g); level[s] = 0; q = deque([s])
            while q:
                u = q.popleft()
                for e in self.g[u]:
                    if e[1] and level[e[0]] < 0: level[e[0]] = level[u] + 1; q.append(e[0])
            if level[t] < 0: return ans
            it = [0] * len(self.g)
            def dfs(u, f):
                if u == t: return f
                for i in range(it[u], len(self.g[u])):
                    it[u] = i; e = self.g[u][i]
                    if e[1] and level[e[0]] == level[u] + 1:
                        z = dfs(e[0], min(f, e[1]))
                        if z: e[1] -= z; e[2][1] += z; return z
                return 0
            while True:
                z = dfs(s, 10**9)
                if not z: break
                ans += z

def edges(rng, left, right, p):
    out = []
    for u in range(left):
        row = [v for v in range(right) if rng.random() < p] or [rng.randrange(right)]
        out += [(u, v) for v in row]
    return out

def solve(pm, mb, dem, PM, MD):
    P, M, D = len(pm), len(mb), len(dem)
    src = 0; op = 1; oo = op + P; om = oo + M; od = om + M; sink = od + D
    f = Dinic(sink + 1); pe = []; oe = []
    for p, x in enumerate(pm): pe.append(f.add(src, op + p, x))
    for m, x in enumerate(mb): oe.append(f.add(src, oo + m, x)); f.add(oo + m, om + m, x)
    for p, m in PM: f.add(op + p, om + m, 10**6)
    for m, d in MD: f.add(om + m, od + d, 10**6)
    for d, x in enumerate(dem): f.add(od + d, sink, x)
    paid = f.flow(src, sink)
    return paid, [x - pe[p][1] for p, x in enumerate(pm)], [x - oe[m][1] for m, x in enumerate(mb)]

rng = random.Random(1707)
stats = dict(epochs=0, P=0, M=0, D=0, pm=0, md=0, deposit=0, demand=0, paid=0, unpaid=0, deficient=0)
for _ in range(5200):
    P = rng.randint(2, 5); M = rng.randint(2, 5); D = rng.randint(1, 3) + rng.randint(1, 3)
    pm = [rng.randint(0, 5) for _ in range(P)]; mb = [rng.randint(0, 5) for _ in range(M)]
    PM = edges(rng, P, M, .5); MD = edges(rng, M, D, .55)
    stats['P'] += P; stats['M'] += M; stats['D'] += D; stats['pm'] += len(PM); stats['md'] += len(MD)
    for _ in range(rng.randint(1, 3)):
        dep = [rng.randint(0, 3) for _ in range(P)]; pm = [pm[p] + dep[p] for p in range(P)]
        dem = [rng.randint(0, 5) for _ in range(D)]
        paid, up, uo = solve(pm, mb, dem, PM, MD); total = sum(dem)
        stats['epochs'] += 1; stats['deposit'] += sum(dep); stats['demand'] += total
        stats['paid'] += paid; stats['unpaid'] += total - paid
        if paid < total: stats['deficient'] += 1; break
        pm = [pm[p] - up[p] for p in range(P)]; mb = [mb[m] - uo[m] for m in range(M)]
        assert min(pm + mb) >= 0
assert stats['paid'] + stats['unpaid'] == stats['demand']
print('SAS17', 5200, stats)

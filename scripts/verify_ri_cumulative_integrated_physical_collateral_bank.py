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

def epoch_flow(pm, cb, dem, PC, CD):
    P, C, D = len(pm), len(cb), len(dem)
    src = 0; op = 1; oo = op + P; oc = oo + C; od = oc + C; sink = od + D
    f = Dinic(sink + 1); pe = []; oe = []
    for p, x in enumerate(pm): pe.append(f.add(src, op + p, x))
    for c, x in enumerate(cb): oe.append(f.add(src, oo + c, x)); f.add(oo + c, oc + c, x)
    for p, c in PC: f.add(op + p, oc + c, 10**6)
    for c, d in CD: f.add(oc + c, od + d, 10**6)
    for d, x in enumerate(dem): f.add(od + d, sink, x)
    paid = f.flow(src, sink)
    return paid, [x - pe[p][1] for p, x in enumerate(pm)], [x - oe[c][1] for c, x in enumerate(cb)]

rng = random.Random(1703)
stats = dict(epochs=0, P=0, C=0, D=0, pc=0, cd=0, deposit=0, demand=0, paid=0, unpaid=0, deficient=0)
for _ in range(5000):
    P, C, D = (rng.randint(2, 5) for _ in range(3))
    pm = [rng.randint(0, 5) for _ in range(P)]
    cb = [rng.randint(0, 5) for _ in range(C)]
    PC = edges(rng, P, C, .5); CD = edges(rng, C, D, .55)
    stats['P'] += P; stats['C'] += C; stats['D'] += D; stats['pc'] += len(PC); stats['cd'] += len(CD)
    for _ in range(rng.randint(1, 3)):
        dep = [rng.randint(0, 3) for _ in range(P)]; pm = [pm[p] + dep[p] for p in range(P)]
        dem = [rng.randint(0, 5) for _ in range(D)]
        paid, up, uo = epoch_flow(pm, cb, dem, PC, CD); total = sum(dem)
        stats['epochs'] += 1; stats['deposit'] += sum(dep); stats['demand'] += total
        stats['paid'] += paid; stats['unpaid'] += total - paid
        if paid < total: stats['deficient'] += 1; break
        pm = [pm[p] - up[p] for p in range(P)]; cb = [cb[c] - uo[c] for c in range(C)]
        assert min(pm + cb) >= 0
assert stats['paid'] + stats['unpaid'] == stats['demand']
print('RI17', 5000, stats)

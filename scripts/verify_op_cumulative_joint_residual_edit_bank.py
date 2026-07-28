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

def edges(rng, left, right):
    out = []
    for u in range(left):
        row = [v for v in range(right) if rng.random() < .5] or [rng.randrange(right)]
        out += [(u, v) for v in row]
    return out

def solve(sb, rd, ed, SR, SE):
    S, R, E = len(sb), len(rd), len(ed)
    src = 0; os = 1; orr = os + S; oe = orr + R; sink = oe + E
    f = Dinic(sink + 1); source_edges = []
    for s, x in enumerate(sb): source_edges.append(f.add(src, os + s, x))
    for s, r in SR: f.add(os + s, orr + r, 10**6)
    for s, e in SE: f.add(os + s, oe + e, 10**6)
    for r, x in enumerate(rd): f.add(orr + r, sink, x)
    for e, x in enumerate(ed): f.add(oe + e, sink, x)
    paid = f.flow(src, sink)
    return paid, [x - source_edges[s][1] for s, x in enumerate(sb)]

rng = random.Random(1705)
stats = dict(epochs=0, S=0, R=0, E=0, sr=0, se=0, deposit=0, demand=0, paid=0, unpaid=0, deficient=0, checks=0)
for _ in range(5200):
    S = rng.randint(2, 5); R = rng.randint(2, 4); E = rng.randint(2, 4)
    sb = [rng.randint(0, 6) for _ in range(S)]
    SR = edges(rng, S, R); SE = edges(rng, S, E)
    stats['S'] += S; stats['R'] += R; stats['E'] += E; stats['sr'] += len(SR); stats['se'] += len(SE)
    for _ in range(rng.randint(1, 3)):
        dep = [rng.randint(0, 3) for _ in range(S)]; sb = [sb[s] + dep[s] for s in range(S)]
        rd = [rng.randint(0, 5) for _ in range(R)]; ed = [rng.randint(0, 5) for _ in range(E)]
        paid, used = solve(sb, rd, ed, SR, SE); total = sum(rd) + sum(ed)
        stats['epochs'] += 1; stats['deposit'] += sum(dep); stats['demand'] += total
        stats['paid'] += paid; stats['unpaid'] += total - paid
        for mask in range(1, 1 << (R + E)):
            demand = sum(rd[r] for r in range(R) if mask >> r & 1) + sum(ed[e] for e in range(E) if mask >> (R + e) & 1)
            neighbors = {s for s, r in SR if mask >> r & 1} | {s for s, e in SE if mask >> (R + e) & 1}
            assert demand - sum(sb[s] for s in neighbors) <= total - paid
            stats['checks'] += 1
        if paid < total: stats['deficient'] += 1; break
        sb = [sb[s] - used[s] for s in range(S)]
        assert min(sb) >= 0
assert stats['paid'] + stats['unpaid'] == stats['demand']
print('OP17', 5200, stats)

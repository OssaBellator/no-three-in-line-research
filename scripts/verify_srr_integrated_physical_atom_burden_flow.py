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

def solve(pm, ab, dem, PA, AB):
    P, A, B = len(pm), len(ab), len(dem)
    src = 0; op = 1; oo = op + P; oa = oo + A; ob = oa + A; sink = ob + B
    f = Dinic(sink + 1)
    for p, x in enumerate(pm): f.add(src, op + p, x)
    for a, x in enumerate(ab): f.add(src, oo + a, x); f.add(oo + a, oa + a, x)
    for p, a in PA: f.add(op + p, oa + a, 10**6)
    for a, b in AB: f.add(oa + a, ob + b, 10**6)
    for b, x in enumerate(dem): f.add(ob + b, sink, x)
    return f.flow(src, sink)

def greedy(pm, ab, dem, PA, AB):
    issued = [0] * len(ab)
    score = [sum(dem[b] for aa, b in AB if aa == a) for a in range(len(ab))]
    for p, mass in enumerate(pm):
        options = [a for pp, a in PA if pp == p]
        if options: issued[max(options, key=lambda a: (score[a], -a))] += mass
    return solve([0] * len(pm), [ab[a] + issued[a] for a in range(len(ab))], dem, [], AB)

rng = random.Random(1706)
stats = dict(P=0, A=0, B=0, pa=0, ab=0, source=0, atom=0, demand=0, paid=0, unpaid=0, deficient=0, preissue=0)
for _ in range(5500):
    P, A, B = (rng.randint(2, 5) for _ in range(3))
    pm = [rng.randint(0, 6) for _ in range(P)]; ab = [rng.randint(0, 5) for _ in range(A)]; dem = [rng.randint(0, 6) for _ in range(B)]
    PA = edges(rng, P, A, .5); AB = edges(rng, A, B, .55)
    paid = solve(pm, ab, dem, PA, AB); greedy_paid = greedy(pm, ab, dem, PA, AB); total = sum(dem)
    if paid == total and greedy_paid < total: stats['preissue'] += 1
    if paid < total: stats['deficient'] += 1
    stats['P'] += P; stats['A'] += A; stats['B'] += B; stats['pa'] += len(PA); stats['ab'] += len(AB)
    stats['source'] += sum(pm); stats['atom'] += sum(ab); stats['demand'] += total
    stats['paid'] += paid; stats['unpaid'] += total - paid
assert stats['paid'] + stats['unpaid'] == stats['demand']
print('SRR17', 5500, stats)

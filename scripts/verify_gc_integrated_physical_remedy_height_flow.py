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

def edges(rng, left, right, p=.5):
    out = []
    for u in range(left):
        row = [v for v in range(right) if rng.random() < p] or [rng.randrange(right)]
        out += [(u, v) for v in row]
    return out

def solve(pm, rb, hb, dem, PR, RH, HC):
    P, R, H, C = len(pm), len(rb), len(hb), len(dem)
    src = 0; op = 1; oor = op + P; orr = oor + R; ooh = orr + R; oh = ooh + H; oc = oh + H; sink = oc + C
    f = Dinic(sink + 1)
    for p, x in enumerate(pm): f.add(src, op + p, x)
    for r, x in enumerate(rb): f.add(src, oor + r, x); f.add(oor + r, orr + r, x)
    for h, x in enumerate(hb): f.add(src, ooh + h, x); f.add(ooh + h, oh + h, x)
    for p, r in PR: f.add(op + p, orr + r, 10**6)
    for r, h in RH: f.add(orr + r, oh + h, 10**6)
    for h, c in HC: f.add(oh + h, oc + c, 10**6)
    for c, x in enumerate(dem): f.add(oc + c, sink, x)
    return f.flow(src, sink)

def greedy(pm, rb, hb, dem, PR, RH, HC):
    issued = [0] * len(rb)
    score = [sum(dem[c] for rr, h in RH if rr == r for hh, c in HC if hh == h) for r in range(len(rb))]
    for p, mass in enumerate(pm):
        options = [r for pp, r in PR if pp == p]
        if options: issued[max(options, key=lambda r: (score[r], -r))] += mass
    return solve([0] * len(pm), [rb[r] + issued[r] for r in range(len(rb))], hb, dem, [], RH, HC)

rng = random.Random(1704)
stats = dict(P=0, R=0, H=0, C=0, pr=0, rh=0, hc=0, demand=0, paid=0, unpaid=0, deficient=0, preissue=0)
for _ in range(5000):
    P, R, H, C = (rng.randint(2, 5) for _ in range(4))
    pm = [rng.randint(0, 5) for _ in range(P)]; rb = [rng.randint(0, 4) for _ in range(R)]
    hb = [rng.randint(1, 6) for _ in range(H)]; dem = [rng.randint(0, 5) for _ in range(C)]
    PR = edges(rng, P, R); RH = edges(rng, R, H); HC = edges(rng, H, C)
    paid = solve(pm, rb, hb, dem, PR, RH, HC); greedy_paid = greedy(pm, rb, hb, dem, PR, RH, HC); total = sum(dem)
    if paid == total and greedy_paid < total: stats['preissue'] += 1
    if paid < total: stats['deficient'] += 1
    stats['P'] += P; stats['R'] += R; stats['H'] += H; stats['C'] += C
    stats['pr'] += len(PR); stats['rh'] += len(RH); stats['hc'] += len(HC)
    stats['demand'] += total; stats['paid'] += paid; stats['unpaid'] += total - paid
assert stats['paid'] + stats['unpaid'] == stats['demand']
print('GC17', 5000, stats)

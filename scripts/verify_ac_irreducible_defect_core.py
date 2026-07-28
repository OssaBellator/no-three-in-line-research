#!/usr/bin/env python3
"""Audit AC5dm--AC5dq: canonical irreducible defect cores."""
from collections import deque
import random

SEED, SYSTEMS, TYPED = 18001, 4200, False
TYPE_NAMES = ("type0", "type1")

class Flow:
    def __init__(self, n): self.g = [[] for _ in range(n)]
    def add(self, u, v, c):
        self.g[u].append([v, c, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u]) - 1])
    def run(self, s, t):
        ans = 0
        while True:
            level = [-1] * len(self.g); level[s] = 0; q = deque([s])
            while q:
                u = q.popleft()
                for v, c, _ in self.g[u]:
                    if c and level[v] < 0: level[v] = level[u] + 1; q.append(v)
            if level[t] < 0: return ans
            it = [0] * len(self.g)
            def dfs(u, f):
                if u == t: return f
                while it[u] < len(self.g[u]):
                    i = it[u]; v, c, r = self.g[u][i]
                    if c and level[v] == level[u] + 1:
                        z = dfs(v, min(f, c))
                        if z:
                            self.g[u][i][1] -= z; self.g[v][r][1] += z
                            return z
                    it[u] += 1
                return 0
            while True:
                z = dfs(s, 10**9)
                if not z: break
                ans += z

def sample(rng):
    p, m, t = rng.randint(2,5), rng.randint(2,5), rng.randint(2,6)
    pc = [rng.randint(1,6) for _ in range(p)]
    pm = [(i,j) for i in range(p) for j in range(m) if rng.random() < .48]
    for j in range(m):
        if not any(y == j for _, y in pm): pm.append((rng.randrange(p), j))
    mt = [(j,k) for j in range(m) for k in range(t) if rng.random() < .48]
    for k in range(t):
        if not any(y == k for _, y in mt): mt.append((rng.randrange(m), k))
    d = [rng.randint(1,6) for _ in range(t)]
    ty = [rng.randrange(2) for _ in range(t)] if TYPED else [0] * t
    return p, m, t, pc, pm, mt, d, ty

def capacity(a, mask):
    p,m,t,pc,pm,mt,d,_ = a
    s=0; ps=1; ms=ps+p; ts=ms+m; sink=ts+t; f=Flow(sink+1)
    for i,c in enumerate(pc): f.add(s, ps+i, c)
    for i,j in pm: f.add(ps+i, ms+j, 10**6)
    for j,k in mt: f.add(ms+j, ts+k, 10**6)
    for k,x in enumerate(d):
        if mask >> k & 1: f.add(ts+k, sink, x)
    return f.run(s, sink)

def mass(a, mask): return sum(x for i,x in enumerate(a[6]) if mask >> i & 1)

def main():
    rng = random.Random(SEED)
    z = {k:0 for k in ("checks","deficient","addresses","deficit","marginal","single","type0","type1")}
    for _ in range(SYSTEMS):
        a=sample(rng); t=a[2]; cap=[0]*(1<<t)
        for mask in range(1,1<<t): cap[mask]=capacity(a,mask); z["checks"]+=1
        bad=[]
        for mask in range(1,1<<t):
            delta=mass(a,mask)-cap[mask]
            if delta>0:
                addr=tuple(i for i in range(t) if mask>>i&1)
                bad.append((len(addr),addr,mask,delta))
        if not bad: continue
        z["deficient"]+=1; bad.sort(); _,addr,core,delta=bad[0]
        z["addresses"]+=len(addr); z["deficit"]+=delta; z["single"]+=len(addr)==1
        sub=(core-1)&core
        while sub:
            assert mass(a,sub)==cap[sub]; sub=(sub-1)&core
        for x in addr:
            marginal=cap[core]-cap[core&~(1<<x)]
            assert a[6][x]-marginal==delta
            z["marginal"]+=marginal
    print("AC5dm--AC5dq audit passed")
    print(f"systems: {SYSTEMS:,}")
    print(f"terminal-subset checks: {z['checks']:,}")
    print(f"deficient systems: {z['deficient']:,}")
    print(f"irreducible core addresses: {z['addresses']:,}")
    print(f"core deficit units: {z['deficit']:,}")
    print(f"marginal payable-capacity units: {z['marginal']:,}")
    print(f"singleton cores: {z['single']:,}")
if __name__ == "__main__": main()

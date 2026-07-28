#!/usr/bin/env python3
from collections import defaultdict, deque
import random

class Dinic:
    def __init__(self,n): self.g=[[] for _ in range(n)]
    def add(self,u,v,c):
        a=[v,c,None]; b=[u,0,a]; a[2]=b; self.g[u].append(a); self.g[v].append(b)
    def flow(self,s,t):
        ans=0
        while True:
            lv=[-1]*len(self.g); lv[s]=0; q=deque([s])
            while q:
                u=q.popleft()
                for e in self.g[u]:
                    if e[1] and lv[e[0]]<0: lv[e[0]]=lv[u]+1; q.append(e[0])
            if lv[t]<0: return ans
            it=[0]*len(self.g)
            def dfs(u,f):
                if u==t: return f
                while it[u]<len(self.g[u]):
                    e=self.g[u][it[u]]
                    if e[1] and lv[e[0]]==lv[u]+1:
                        z=dfs(e[0],min(f,e[1]))
                        if z: e[1]-=z; e[2][1]+=z; return z
                    it[u]+=1
                return 0
            while True:
                z=dfs(s,10**9)
                if not z: break
                ans+=z

def assign(dem,cap,E):
    nl,nr=len(dem),len(cap); s=nl+nr; t=s+1; D=Dinic(t+1); M={}
    for i,x in enumerate(dem): D.add(s,i,x)
    for i,j in sorted(E): D.add(i,nl+j,sum(dem)+1); M[(i,j)]=D.g[i][-1]
    for j,x in enumerate(cap): D.add(nl+j,t,x)
    f=D.flow(s,t); used=[0]*nr
    for (i,j),e in M.items(): used[j]+=e[2][1]
    return f,used

def hall(dem,cap,E):
    N=[set() for _ in dem]
    for i,j in E: N[i].add(j)
    best=0
    for mask in range(1<<len(dem)):
        ns=set(); d=0
        for i,x in enumerate(dem):
            if mask>>i&1: ns|=N[i]; d+=x
        best=max(best,d-sum(cap[j] for j in ns))
    return max(0,best)

rng=random.Random(20260731); S=defaultdict(int)
for _ in range(5500):
    nl,nr=rng.randint(1,6),rng.randint(1,6)
    E={(i,j) for i in range(nl) for j in range(nr) if rng.random()<.5}
    cap=[rng.randint(0,5) for _ in range(nr)]; initial=cap[:]; depcum=[0]*nr; usedcum=[0]*nr
    S['systems']+=1; S['left_classes']+=nl; S['source_classes']+=nr; S['arcs']+=len(E)
    for _ in range(rng.randint(1,4)):
        dep=[rng.randint(0,2) if rng.random()<.4 else 0 for _ in range(nr)]
        for j,x in enumerate(dep): cap[j]+=x; depcum[j]+=x
        dem=[rng.randint(0,4) for _ in range(nl)]
        f,used=assign(dem,cap,E); deficit=hall(dem,cap,E)
        assert sum(dem)-f==deficit
        S['epochs']+=1; S['demand_units']+=sum(dem); S['deposit_units']+=sum(dep); S['subset_checks']+=1<<nl
        if deficit:
            S['deficient_epochs']+=1; S['deficient_units']+=deficit; break
        S['paid_epochs']+=1; S['paid_units']+=f
        for j,u in enumerate(used):
            cap[j]-=u; usedcum[j]+=u; assert usedcum[j]<=initial[j]+depcum[j]
print(dict(S))
